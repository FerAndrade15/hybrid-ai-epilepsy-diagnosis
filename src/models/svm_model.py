"""
# File: rf_model.py
# Project: Trabajo de graduación

Reusable SVM modules for the AI pipeline.
"""
# File: svm_model.py
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
 
 
# Binary SVM for imbalanced data
def build_svm_model(class_weight="balanced", **overrides):
    """
    SVM base configuration for imbalanced data, with overrides for hyperparameters.
 
    class_weight:
        - "balanced": weights classes inversely proportional to their frequency.
        - dict, e.g. {0: 1.0, 1: 5.0}: manual weights (the equivalent of
          scale_pos_weight in XGBoost).
        - None: no weighting.
 
    Overrides use the SVC parameter names directly (C, gamma, kernel, ...).
    """
    params = {
        "kernel": "rbf",
        "C": 1.0,
        "gamma": "scale",
        "class_weight": class_weight,
        "probability": True,   # enables predict_proba (slower; set False if not needed)
        "cache_size": 1000,    # MB, speeds up training on larger datasets
        "random_state": 42,
    }
 
    params.update(overrides)
 
    # SVM is sensitive to feature scale, so the scaler is part of the model.
    return Pipeline([
        ("scaler", StandardScaler()),
        ("svm", SVC(**params)),
    ])
 