#!/usr/bin/env python
"""
Setup script for University Admission Predictor

This script helps initialize and run the application.
"""

import subprocess
import sys
import os
from pathlib import Path

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("✅ Dependencies installed successfully!")

def train_model():
    """Train the ML model"""
    print("\n🤖 Training model...")
    subprocess.check_call([sys.executable, "model.py"])
    print("✅ Model training complete!")

def run_app():
    """Run the Streamlit application"""
    print("\n🚀 Starting Streamlit app...")
    subprocess.call(["streamlit", "run", "app.py"])

def main():
    """Main setup flow"""
    print("""
    ╔════════════════════════════════════════╗
    ║  University Admission Predictor Setup  ║
    ╚════════════════════════════════════════╝
    """)
    
    # Check if models directory exists and has trained model
    models_dir = Path("models")
    model_exists = (models_dir / "model.pkl").exists()
    
    if not model_exists:
        print("⚠️  No trained model found!")
        response = input("Would you like to train the model now? (y/n): ").lower()
        if response == 'y':
            train_model()
    
    # Run the app
    run_app()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Application stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
