import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

def train_model():
    """Train the admission prediction model"""
    
    # Create models directory if it doesn't exist
    os.makedirs('models', exist_ok=True)
    
    # Load data
    print("Loading data...")
    df = pd.read_csv("Admission.csv")
    print(f"Dataset shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print(f"Missing values: {df.isnull().sum().sum()}")
    
    # Data cleaning and preparation
    print("\nPreparing data...")
    X = df.drop("admit", axis=1)
    y = df["admit"]
    
    print(f"Features: {X.columns.tolist()}")
    print(f"Target distribution:\n{y.value_counts()}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale features
    print("\nScaling features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    print("Training model...")
    classifier = LogisticRegression(max_iter=1000, random_state=42)
    classifier.fit(X_train_scaled, y_train)
    
    # Evaluate model
    print("\nEvaluating model...")
    y_pred = classifier.predict(X_test_scaled)
    
    print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"\nConfusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
    print(f"\nClassification Report:\n{classification_report(y_test, y_pred)}")
    
    # Save model and scaler
    print("\nSaving model and scaler...")
    joblib.dump(classifier, 'models/model.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    
    print("[SUCCESS] Model trained and saved successfully!")
    print("   Location: models/model.pkl")
    print("   Location: models/scaler.pkl")
    
    return classifier, scaler

if __name__ == "__main__":
    train_model()

