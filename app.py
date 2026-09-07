import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Set page config
st.set_page_config(
    page_title="Admission Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .prediction-result {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
    }
    .admitted {
        background-color: #d4edda;
        color: #155724;
    }
    .rejected {
        background-color: #f8d7da;
        color: #721c24;
    }
    </style>
""", unsafe_allow_html=True)

def load_model():
    """Load the trained model and scaler"""
    if os.path.exists('models/model.pkl'):
        model = joblib.load('models/model.pkl')
        scaler = joblib.load('models/scaler.pkl')
        return model, scaler
    return None, None

def predict_admission(model, scaler, input_data):
    """Make prediction using the model"""
    input_scaled = scaler.transform([input_data])
    probability = model.predict_proba(input_scaled)[0]
    prediction = model.predict(input_scaled)[0]
    return prediction, probability

def render_histogram(series, bins=30, label='Value'):
    """Render histogram data using string-safe labels for Streamlit compatibility."""
    if hasattr(st, 'histogram'):
        try:
            st.histogram(series, bins=bins, label=label)
            return
        except Exception:
            pass

    hist = pd.cut(series, bins=bins, include_lowest=True).value_counts().sort_index()
    hist_df = pd.DataFrame({label: [str(idx) for idx in hist.index], 'Count': hist.values})
    st.bar_chart(hist_df.set_index(label))


def render_grouped_average(df, column, target, bins=5, label='Value'):
    """Render a grouped average chart with interval labels converted to strings."""
    grouped = df.groupby(pd.cut(df[column], bins=bins, include_lowest=True))[target].mean()
    grouped_df = grouped.rename('Average').reset_index()
    grouped_df.columns = [label, 'Average']
    grouped_df[label] = grouped_df[label].astype(str)
    st.bar_chart(grouped_df.set_index(label))

# Main title
st.markdown("# 🎓 University Admission Predictor")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Configuration")
    page = st.radio("Select Page", ["Home", "Prediction", "Analytics", "About"])
    st.markdown("---")
    st.markdown("### 📊 App Info")
    st.info("This app predicts university admission chances based on student profiles.")

# Load model
model, scaler = load_model()

if page == "Home":
    st.markdown("""
    ## Welcome to the Admission Predictor System!
    
    This application helps predict the likelihood of university admission based on various factors:
    
    - **GRE Score**: Graduate Record Examination score
    - **GPA**: Cumulative Grade Point Average
    - **SES**: Socioeconomic Status
    - **Gender**: Student Gender
    - **Race**: Student Race/Ethnicity
    - **University Rank**: University ranking preference
    
    ### How to use:
    1. Navigate to the **Prediction** tab
    2. Enter student details
    3. Get instant admission prediction
    4. View detailed analytics in the **Analytics** tab
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Students", "400+", "+12%")
    with col2:
        st.metric("Avg Admission Rate", "45%", "-2%")
    with col3:
        st.metric("Model Accuracy", "87%", "+5%")

elif page == "Prediction":
    if model is None:
        st.error("⚠️ Model not found! Please train the model first.")
        st.info("Run `python model.py` to train the model.")
    else:
        st.markdown("## 🔮 Admission Prediction")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Student Profile")
            gre_score = st.slider("GRE Score", 300, 850, 600)
            gpa = st.slider("GPA", 0.0, 4.0, 3.0, step=0.01)
            ses = st.selectbox("Socioeconomic Status", [1, 2, 3], format_func=lambda x: f"Level {x}")
        
        with col2:
            st.markdown("### Demographics")
            gender = st.radio("Gender", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
            race = st.selectbox("Race/Ethnicity", [1, 2, 3, 4])
            rank = st.selectbox("University Rank Preference", [1, 2, 3, 4])
        
        # Prepare input data
        input_data = [gre_score, gpa, ses, gender, race, rank]
        
        if st.button("🎯 Predict Admission", key="predict_btn"):
            prediction, probability = predict_admission(model, scaler, input_data)
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("GRE Score", gre_score)
            with col2:
                st.metric("GPA", f"{gpa:.2f}")
            with col3:
                st.metric("SES Level", ses)
            with col4:
                st.metric("University Rank", rank)
            
            st.markdown("---")
            
            # Show prediction result
            if prediction == 1:
                st.markdown(f"""
                <div class="prediction-result admitted">
                ✅ LIKELY TO BE ADMITTED<br>
                Confidence: {probability[1]*100:.1f}%
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="prediction-result rejected">
                ❌ UNLIKELY TO BE ADMITTED<br>
                Confidence: {probability[0]*100:.1f}%
                </div>
                """, unsafe_allow_html=True)
            
            # Probability distribution
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### Prediction Probability")
                prob_data = pd.DataFrame({
                    'Status': ['Rejected', 'Admitted'],
                    'Probability': [probability[0], probability[1]]
                })
                st.bar_chart(prob_data.set_index('Status'))
            
            with col2:
                st.markdown("### Score Summary")
                st.write(f"**Not Admitted Probability:** {probability[0]:.2%}")
                st.write(f"**Admitted Probability:** {probability[1]:.2%}")

elif page == "Analytics":
    st.markdown("## 📈 Analytics Dashboard")
    
    # Load data
    df = pd.read_csv('Admission.csv')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Records", len(df))
    with col2:
        admitted = df['admit'].sum()
        st.metric("Admitted", f"{admitted} ({admitted/len(df)*100:.1f}%)")
    with col3:
        rejected = len(df) - admitted
        st.metric("Not Admitted", f"{rejected} ({rejected/len(df)*100:.1f}%)")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### GRE Score Distribution")
        render_histogram(df['gre'], bins=30, label='GRE Score')
    
    with col2:
        st.markdown("### GPA Distribution")
        render_histogram(df['gpa'], bins=30, label='GPA')
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Admission by GPA")
        render_grouped_average(df, 'gpa', 'admit', bins=5, label='GPA Range')
    
    with col2:
        st.markdown("### Admission by GRE")
        render_grouped_average(df, 'gre', 'admit', bins=5, label='GRE Range')

elif page == "About":
    st.markdown("""
    ## ℹ️ About This Application
    
    ### Project Overview
    This is a machine learning-based admission prediction system that helps predict 
    whether a student will be admitted to a university based on their academic profile.
    
    ### Features
    - Real-time admission predictions
    - Interactive student profile input
    - Comprehensive analytics dashboard
    - Probability-based decision support
    
    ### Model Information
    - **Algorithm**: Logistic Regression
    - **Features**: 6 (GRE, GPA, SES, Gender, Race, Rank)
    - **Dataset**: Historical admission records
    - **Accuracy**: ~87%
    
    ### Technologies Used
    - **Streamlit**: Frontend and UI
    - **scikit-learn**: Machine Learning
    - **pandas**: Data Processing
    - **plotly**: Visualizations
    
    ### How It Works
    1. Student data is preprocessed and scaled
    2. Model predicts admission probability
    3. Results are displayed with confidence metrics
    4. Users can compare with aggregate analytics
    
    ---
    **Developed with ❤️ using Streamlit**
    """)