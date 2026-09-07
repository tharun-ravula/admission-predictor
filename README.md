# 🎓 University Admission Predictor

A machine learning-powered Streamlit application that predicts university admission chances based on student profiles.

## 📋 Project Structure

```
admission-app/
├── app.py                          # Main Streamlit application (entry point)
├── model.py                        # Model training and evaluation script
├── requirements.txt                # Python dependencies
├── Admission.csv                   # Training dataset (400+ records)
├── .gitignore                      # Git ignore rules
│
├── .streamlit/
│   └── config.toml                # Streamlit configuration (theme, settings)
│
├── templates/                      # HTML page templates
│   ├── README.md                  # Templates documentation
│   ├── home_template.html         # Home page layout
│   ├── prediction_template.html   # Prediction form layout
│   ├── analytics_template.html    # Analytics dashboard layout
│   └── about_template.html        # About page layout
│
└── models/                         # Saved model artifacts
    ├── model.pkl                  # Trained Logistic Regression model
    └── scaler.pkl                 # Feature StandardScaler
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the Model
```bash
python model.py
```

Expected output:
```
Loading data...
Dataset shape: (400, 7)
...
Accuracy: 0.87xx
✅ Model trained and saved successfully!
   Location: models/model.pkl
   Location: models/scaler.pkl
```

### 3. Run the Application
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## 📊 Features

### 🏠 Home Page
- Welcome message
- Quick statistics (student count, admission rate, model accuracy)
- Overview of features and capabilities

### 🔮 Prediction Page
- Interactive form for student profile input
- Real-time admission prediction
- Probability distribution visualization
- Confidence metrics

### 📈 Analytics Page
- Comprehensive statistics dashboard
- Distribution charts (GRE, GPA)
- Admission rate by various factors
- Interactive visualizations

### ℹ️ About Page
- Project overview and details
- Model information
- Technology stack
- Feature descriptions

## 🔧 Configuration

The `.streamlit/config.toml` file contains:
- Custom theme colors (primary: #FF6B6B)
- Layout settings (wide mode)
- Logger configuration

## 📊 Dataset

**Admission.csv** contains 400 records with:
- `admit`: Target variable (0 = Not Admitted, 1 = Admitted)
- `gre`: GRE score (300-850)
- `gpa`: Grade Point Average (0-4.0)
- `ses`: Socioeconomic Status (1-3)
- `Gender_Male`: Gender encoding (0 = Female, 1 = Male)
- `Race`: Race/Ethnicity category (1-4)
- `rank`: University rank preference (1-4)

## 🤖 Model Details

- **Algorithm**: Logistic Regression
- **Scaler**: StandardScaler (mean=0, std=1)
- **Train/Test Split**: 80/20
- **Cross-validation**: Stratified split
- **Accuracy**: ~87%

### Input Processing
1. Features are standardized using StandardScaler
2. Scaled data is fed to the trained model
3. Probability predictions (0-1) are generated

## 📦 Dependencies

- `streamlit==1.28.1` - Web app framework
- `pandas==2.0.3` - Data manipulation
- `scikit-learn==1.3.1` - Machine learning
- `numpy==1.24.3` - Numerical computing
- `joblib==1.3.2` - Model serialization
- `plotly==5.17.0` - Interactive visualizations

## 🎯 Usage Examples

### Making a Prediction
1. Navigate to "Prediction" tab
2. Adjust sliders for GRE score (300-850)
3. Input GPA (0-4.0)
4. Select demographic information
5. Click "Predict Admission"
6. View results with probability metrics

### Viewing Analytics
1. Navigate to "Analytics" tab
2. View overall statistics
3. Analyze distributions and trends
4. Compare your student profile against aggregate data

## 🔐 Security & Privacy

- All processing happens locally (no cloud uploads)
- Model runs on your machine
- No personal data is stored
- No external API calls made

## 📝 Notes

- Model is trained on historical admission data
- Actual admission decisions may consider additional factors
- Use this as a supplementary decision support tool
- Retraining recommended with updated data

## 🐛 Troubleshooting

**Issue: Model not found**
```
Solution: Run 'python model.py' first to train the model
```

**Issue: Port 8501 already in use**
```
Solution: streamlit run app.py --server.port 8502
```

**Issue: Slow predictions**
```
Solution: Ensure Streamlit is running in production mode
Add: streamlit run app.py --client.showErrorDetails=false
```

## 📧 Support

For issues or questions:
1. Check the About page for detailed information
2. Review the model training output for validation metrics
3. Verify dataset format matches Admission.csv

## 📄 License

This project is provided as-is for educational purposes.

---

**Developed with ❤️ using Streamlit**
