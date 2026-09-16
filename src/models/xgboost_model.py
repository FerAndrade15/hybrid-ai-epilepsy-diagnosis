"""
# File: xgboost_model.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Reusable XGBoost modules for the AI pipeline.
"""

import numpy as np
from sklearn.ensemble import xgboost
from sklearn.model_selection import cross_val_score
from mne.decoding import Vectorizer