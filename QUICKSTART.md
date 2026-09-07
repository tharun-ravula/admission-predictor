# 🎓 Quick Start Guide - Admission Predictor

## Step 1: Installation (2 minutes)

```bash
# Navigate to project directory
cd "c:\Users\ravul\OneDrive\Documents\Desktop\admission app documentation"

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Train the Model (1 minute)

```bash
python model.py
```

You should see output like:
```
Loading data...
Dataset shape: (400, 7)
...
Evaluating model...
Accuracy: 0.87xx
✅ Model trained and saved successfully!
   Location: models/model.pkl
   Location: models/scaler.pkl
```

## Step 3: Run the Application

```bash
streamlit run app.py
```

The browser will open automatically at `http://localhost:8501`

---

## 📊 Application Pages

### 🏠 Home
- Welcome interface
- Key statistics (400+ students, 45% admission rate, 87% accuracy)
- Feature overview

### 🔮 Prediction
- Input student profile:
  - GRE Score (300-850)
  - GPA (0.0-4.0)
  - Socioeconomic Status (1-3)
  - Gender (M/F)
  - Race/Ethnicity (1-4)
  - University Rank (1-4)
- Get instant admission prediction
- View probability distribution

### 📈 Analytics
- View dataset statistics
- Distribution charts
- Admission rate analysis
- Comparative visualizations

### ℹ️ About
- Detailed project information
- Model specifications
- Technology stack
- How it works explanation

---

## 🚀 Alternative: Using Setup Script

```bash
python setup.py
```

This script will:
1. Prompt to train model if not found
2. Start the Streamlit application

---

## 📂 Project Structure at a Glance

```
admission-app/
├── app.py                 ← Main application (RUN THIS)
├── model.py              ← Model training script
├── Admission.csv         ← Training data
├── requirements.txt      ← Dependencies
├── README.md             ← Full documentation
│
├── .streamlit/
│   └── config.toml      ← Streamlit theme settings
│
├── templates/            ← HTML page templates
│   ├── home_template.html
│   ├── prediction_template.html
│   ├── analytics_template.html
│   └── about_template.html
│
└── models/              ← Saved model artifacts
    ├── model.pkl        ← Trained model
    └── scaler.pkl       ← Feature scaler
```

---

## 🎯 Quick Commands Reference

| Command | Purpose |
|---------|---------|
| `pip install -r requirements.txt` | Install dependencies |
| `python model.py` | Train the model |
| `streamlit run app.py` | Start the web app |
| `python setup.py` | Interactive setup |

---

## ⚙️ Customization

### Change Theme Colors
Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#FF6B6B"      # Red accent
backgroundColor = "#F0F2F6"    # Light gray background
```

### Adjust Model Parameters
Edit `model.py`:
```python
classifier = LogisticRegression(
    max_iter=1000,
    random_state=42
    # Add more parameters here
)
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Model not found | Run: `python model.py` |
| Port 8501 in use | Run: `streamlit run app.py --server.port 8502` |
| Import errors | Run: `pip install -r requirements.txt --upgrade` |
| Slow app | Restart: `Ctrl+C` then `streamlit run app.py` |

---

## ✅ Verification Checklist

- [ ] Python 3.7+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Model trained (`python model.py`)
- [ ] App starts (`streamlit run app.py`)
- [ ] Can make predictions
- [ ] Analytics page shows data

---

## 📚 Next Steps

1. **Explore the app**: Test predictions with different student profiles
2. **Analyze data**: Use the Analytics tab to understand patterns
3. **Customize**: Modify the theme, add more features, retrain with new data
4. **Deploy**: Host on Streamlit Cloud (https://streamlit.io/cloud)

---

**Ready to predict? Let's go! 🚀**

For detailed documentation, see `README.md`
