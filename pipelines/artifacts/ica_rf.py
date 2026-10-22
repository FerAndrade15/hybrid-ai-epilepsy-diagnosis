"""
# File: ica_cnn_rf.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

End-to-end pipeline for 'artifact' corpus, process:
Windowing -> split -> features (ICA+ICLabel agregado) -> 
Hiperparameter optimization (Grid Search y Honey Badger) -> 
Training of multi-output RF -> validation -> saves work.
"""
# file: ica_cnn_rf.py (pipeline)

# Data managment libraries
import pandas as pd
from pathlib import Path

# Utils libraries
from scipy.stats import randint

# Data integration libraries / project modules
from src.core.windowing import get_or_build_windows
from src.core.data_loader import build_annotations_index, find_project_root
from src.core.data_config import ARTIFACT_KEYWORDS, WINDOW_REQUESTS_ARTIFACTS, RATIOS, VERSION, LEAKAGE_COLS, OUTPUTS_DIR, NORMALIZE, COMPARISON
from src.core.data_splitter import get_or_compute_labeled_split, split_balance_report, drop_inconsistent_channel_columns
from src.core.feature_extractor import build_ml_dataset, get_or_build_features
from src.models.rf_model import build_rf_model
from src.models.ml_models import train_binary_model
from src.utils.split_cache import load_selected_sw, save_selected_sw
from src.utils.patient_registry import load_registry, forced_for

# Data visualization and search libraries
from IPython.display import display
