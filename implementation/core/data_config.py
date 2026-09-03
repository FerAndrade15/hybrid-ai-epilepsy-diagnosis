""""
# File: data_config.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Shared data configuration for the data processing:
- TUH corpus paths
- Valid montages
- All corpus keyword (Artifact, event, seizures)
- Standard EEG Channel names
"""
# Data integration libraries
from pathlib import Path
import platform

def find_project_root(marker="implementation"):
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / marker).is_dir():
            return parent
    return current.parent

BASE_DIR = find_project_root()

# Operative system
if platform.system() == "Windows":
    BASE_DATA_DIR = Path("D:/")
else:
    BASE_DATA_DIR = Path("/mnt/d/")

# Current data path
BASE_PATH = BASE_DATA_DIR / "tuh_eeg"
# BASE_PATH = Path(r"\\Cit114pc07\DATA_EEG_TUH")
# BASE_PATH = Path(r"C:\Users\ferch\Documents\Various\EngineeringDesignAndInnovation")
# BASE_PATH = Path(r"D:\Users\disenoeinnovacion\Datasets\DATA_EEG_TUH")

# Available corpus matching the TUSZ server nomenclature as of late 2026
CORPUS_PATHS = {
    "all_corpus": Path("tuh_eeg") / "v2.0.2",
    "artifact":   Path("tuh_eeg_artifact") / "v3.0.1",
    "epilepsy":   Path("tuh_eeg_epilepsy") / "v3.1.0",
    "seizure":    Path("tuh_eeg_seizure") / "v2.0.6",
    "events":     Path("tuh_eeg_events") / "v2.0.1",
}

# Montages registered in the TUSZ server nomenclature as of late 2026
# + Standard montages
ALL_MONTAGES = [
    "01_tcp_ar", "02_tcp_le", "03_tcp_ar_a", "04_tcp_le_a",         # TUSZ Corpus
    "05_tcp_ar_b", "06_tcp_le_b", "07_tcp_ar_c", "08_tcp_le_c"      # To complete standard montages
]

# Artifact labeling and resources
## TUAR Corpus Keywords
ARTIFACT_KEYWORDS = {
    "eye": {"eyem"},
    "muscle": {"musc", "shiv", "chew"},
    "non_physiological": {"elec", "elpp"},
}
ARTIFACT_ADDITIONAL_TOKENS = {"tcsz", "cpsz", "gnsz", "fnsz"}
BACKGROUND_LABEL = "bckg"

## Fixed categories mne-icalabel
ICLABEL_CATEGORIES = [
    "brain", "muscle artifact", "eye blink",
    "heart beat", "line noise", "channel noise", "other",
]

## TUAR and MNE-icLABEL
ICLABEL_TO_TARGET = {
    "eye": ["eye_blink"],
    "muscle": ["muscle_artifact"],
    "non_physiological": ["channel_noise", "other"],
}

# Events Corpus Keywords
EVENT_KEYWORDS = {
    "epilepsy": {"gped", "pled"},
    "artifacts": {"artifact"},
}

# Seizure Corpus Keywords
SEIZURE_KEYWORDS = {
    "tonic_seizure": {"tcsz"},
    "complex_partial": {"cpsz"},
    "generalized_non_specific": {"gnsz"},
    "focal_non_specific": {"fnsz"},
}



# Channel names (10-20 and 10-10 system)
CHANNELS = [
    "FP1", "FP2", "F7", "F3", "FZ", "F4", "F8",         # Frontal 
    "C3", "CZ", "C4",                                   # Central
    "P3", "PZ", "P4",                                   # Parietal
    "O1", "OZ", "O2",                                   # Occipital
    "T3/T7", "T4/T8", "T5/P7", "T6/P8",                 # Temporal
    "AT1/T1/FT9", "AT2/T2/FT10",                        # Additional: Inferior anterotemporal electrodes
]

# Windowing
WINDOW_REQUESTS = {
    "rf_artifact_class":      {"window_size_sec": 1,  "stride_sec": 1},
    "xgboost_features":  {"window_size_sec": 1,  "stride_sec": 1},
    "cnn_eye":           {"window_size_sec": 20, "stride_sec": 20},
    "cnn_muscle":        {"window_size_sec": 5,  "stride_sec": 2},
    "cnn_non_phys":      {"window_size_sec": 1,  "stride_sec": 1},
}
