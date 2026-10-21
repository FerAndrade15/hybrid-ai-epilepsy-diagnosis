"""
# File: data_config.py
# Project: Trabajo de graduación
# Author: María Fernanda Andrade Recinos
#
# Standard configurations for EEG processing and clinical taxonomy
"""
# Required libraries
from pathlib import Path

# -----------------------------------------------------------------
# Signal parameters: Preprocessing restrictions
# -----------------------------------------------------------------
SFREQ = 256                     # According to all corpus majority
DEFAULT_L_FREQ = 1.0            # Hz (Deleting DC contribution)
DEFAULT_H_FREQ = 100.0           # Hz
DEFAULT_NOTCH_FREQ = 60.0       # Hz

KEYS = ["Patient", "Session", "Section"]

# -----------------------------------------------------------------
# Channel names: 10-20 and 10-10 system
# -----------------------------------------------------------------
CHANNELS = [
    "FP1", "FP2", "F7", "F3", "FZ", "F4", "F8",         # Frontal 
    "C3", "CZ", "C4",                                   # Central
    "P3", "PZ", "P4",                                   # Parietal
    "O1", "OZ", "O2",                                   # Occipital
    "T3/T7", "T4/T8", "T5/P7", "T6/P8",                 # Temporal
    "AT1/T1/FT9", "AT2/T2/FT10",                        # Additional: Inferior anterotemporal electrodes
    "A1", "A2",                                         # Additional: Ear electrodes (Reference)
]

BIPOLAR_MONTAGE = {
    "anode": [
        # Left Parasagittal
        'FP1', 'F3', 'C3', 'P3',
        # Right Parasagittal
        'FP2', 'F4', 'C4', 'P4',
        # Left Temporal
        'FP1', 'F7', 'T7', 'P7',
        # Right Temporal
        'FP2', 'F8', 'T8', 'P8',
        # Middle line
        'FZ', 'CZ'
    ],
    "cathode": [
        #  Left Parasagittal
        'F3', 'C3', 'P3', 'O1',
        # Parasagital Derecho
        'F4', 'C4', 'P4', 'O2',
        # Left Temporal
        'F7', 'T7', 'P7', 'O1',
        # Right Temporal
        'F8', 'T8', 'P8', 'O2',
        # Middle line
        'CZ', 'PZ'
    ],
}

BIPOLAR_MONTAGE["names"]= [f"{a}-{c}" for a, c in zip(BIPOLAR_MONTAGE["anode"], BIPOLAR_MONTAGE["cathode"])]
MONOPOLAR_CHANNELS = list(dict.fromkeys(BIPOLAR_MONTAGE["anode"] + BIPOLAR_MONTAGE["cathode"]))

# -----------------------------------------------------------------
# TUH montages to standarize data saving
# -----------------------------------------------------------------
# Montages registered in the TUH server nomenclature as of late 2026 + Standard montages
ALL_MONTAGES = [
    "01_tcp_ar", "02_tcp_le", "03_tcp_ar_a", "04_tcp_le_a",         # TUH Corpus
    "05_tcp_ar_b", "06_tcp_le_b", "07_tcp_ar_c", "08_tcp_le_c"      # To complete standard montages
]

# -----------------------------------------------------------------
# Clinical taxonomy
# -----------------------------------------------------------------
# TUAR CORPUS: Labeling and resources ---------------------------------------------------
ARTIFACT_KEYWORDS = {
    "eye": {"eyem"},
    "muscle": {"musc", "shiv", "chew"},
    "non_physiological": {"elec", "elpp"},
}
ARTIFACT_ADDITIONAL_TOKENS = {"tcsz", "cpsz", "gnsz", "fnsz"}
BACKGROUND_LABEL = "bckg"

## Windows labeling
TUAR_Labels = [
    "is_clean_window", 
    "is_ambiguous",        
    "sample_weight", 
    "eye", 
    "muscle", 
    "non_physiological", 
    "genuine_cooccurrence", 
    "weak_overlap", 
    "is_excluded"          
]

## Fixed categories mne-icalabel
ICLABEL_CATEGORIES = [
    "brain", "muscle artifact", "eye blink",
    "heart beat", "line noise", "channel noise", "other",
]

## TUAR and MNE-icLABEL
ICLABEL_TO_TARGET = {
    "eye": ["eye_blink"],
    "muscle": ["muscle_artifact"],
    "non_physiological": ["channel_noise", "other", "heart_beat"],
    "clean": ["brain"],
}

## Dict to convert ICA outputs into TUAR equivalent labels
RAW_TO_TARGET = {}
for cat in ICLABEL_CATEGORIES:
    safe = cat.replace(" ", "_")
    target = next((key for key, values in ICLABEL_TO_TARGET.items() if safe in values), None)
    RAW_TO_TARGET[cat] = target

# TUSZ CORPUS: Labeling and resources ---------------------------------------------------
# Seizure Corpus Keywords
SEIZURE_KEYWORDS = {
    "focal": {"spsz", "cpsz", "fnsz"},
    "generalized_toniclonic": {"absz", "mysz", "tnsz", "gnsz", "tcsz"},
    # tonic_clonic_unspecified = tcsz
}

SEIZURE_START_CONFIDENCE = {
    "high": {"absz", "mysz", "tnsz", "spsz", "cpsz"},
    "low":  {"fnsz", "gnsz", "tcsz"},
}

# TUEV CORPUS: Labeling and resources ---------------------------------------------------
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