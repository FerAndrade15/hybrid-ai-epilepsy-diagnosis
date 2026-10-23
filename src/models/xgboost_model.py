"""
# File: xgboost_model.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Reusable XGBoost modules for the AI pipeline.
"""
# File: xgboost.py
from xgboost import XGBClassifier

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