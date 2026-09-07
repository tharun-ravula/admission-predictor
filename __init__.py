"""
University Admission Predictor Application

A Streamlit-based machine learning application for predicting university admission chances.

Version: 1.0
Author: ML Team
License: MIT
"""

__version__ = "1.0.0"
__author__ = "ML Team"
__description__ = "University Admission Predictor using Streamlit and scikit-learn"

from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent

# Directory paths
TEMPLATES_DIR = PROJECT_ROOT / "templates"
MODELS_DIR = PROJECT_ROOT / "models"
DATA_DIR = PROJECT_ROOT

__all__ = [
    "PROJECT_ROOT",
    "TEMPLATES_DIR", 
    "MODELS_DIR",
    "DATA_DIR",
]
