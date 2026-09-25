"""
# File: xgboost_model.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Reusable XGBoost modules for the AI pipeline.
"""

# File: xgboost.py

import pandas as pd
from pathlib import Path
from scipy.stats import randint, uniform

from xgboost import XGBClassifier

# Functions from modules
from src.core.data_splitter import split_features_target

# Binary RF
def build_xgb_model(scale_pos_weight=1.0, **overrides):
    """
    XGBoost base cofiguration with overrides for hiperparameters.
    """
    params = {
        "n_estimators": 200,
        "learning_rate": 0.1,
        "max_depth": 6,
        "subsample": 0.8,
        "colsample_bytree": 0.8,
        "scale_pos_weight": scale_pos_weight,
        "random_state": 42,
        "n_jobs": -1,
        "tree_method": "hist",
    }

    params.update(overrides)
    return XGBClassifier(**params)
