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
# data_config.py

# Data integration libraries
import platform
from pathlib import Path

# Project paths
def find_project_root(marker):
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / marker).is_dir():
            return parent
    return current.parent
BASE_DIR = find_project_root("src")
DEBUG_DIR = BASE_DIR / "outputs" / "artifact" / "individual_tests"

# Operative system
if platform.system() == "Windows":
    BASE_DATA_DIR = Path("D:/")
else:
    BASE_DATA_DIR = Path("/mnt/d/")

# Data paths
ALL_DATA_POSSIBLE_PATHS = [
    Path("/workspace/data"),                                                    # RunPod
    BASE_DATA_DIR / "tuh_eeg",                                                  # Hard disk
    BASE_DATA_DIR / Path("Users/disenoeinnovacion/Datasets/DATA_EEG_TUH"),      # PC07 CIT-114
    Path(r"\\Cit114pc07\DATA_EEG_TUH"),                                         # Shared network
]
# Data paths
ALL_OUTPUTS_POSSIBLE_PATHS = [
    Path("/workspace/ml-outputs"),                                            # RunPod
    BASE_DATA_DIR / "ml-outputs",                                               # Hard disk
    BASE_DATA_DIR / Path("Users/disenoeinnovacion/ml-outputs"),      # PC07 CIT-114
]

BASE_PATH = None
for path in ALL_DATA_POSSIBLE_PATHS:
    if path.exists() and path.is_dir():
        BASE_PATH = path
        break
if BASE_PATH is None:
    raise FileNotFoundError("No valid data path found")

OUTPUTS_DIR = None
for path in ALL_OUTPUTS_POSSIBLE_PATHS:
    if path.exists() and path.is_dir():
        OUTPUTS_DIR = path
        break
if OUTPUTS_DIR is None:
    raise FileNotFoundError("No valid outputs path found")

# Available corpus matching the TUSZ server nomenclature as of late 2026
CORPUS_PATHS = {
    "all_corpus":   Path("tuh_eeg") / "v2.0.2",
    "artifact":     Path("tuh_eeg_artifact") / "v3.0.1",
    "epilepsy":     Path("tuh_eeg_epilepsy") / "v3.1.0",
    "seizure":      Path("tuh_eeg_seizure") / "v2.0.6",
    "events":       Path("tuh_eeg_events") / "v2.0.1",
}

## Preprocessing restrictions
SFREQ = 256                     # According to all corpus majority
NORMALIZE = True
NORMALIZE_CLIP = 20.0

# Montages registered in the TUH server nomenclature as of late 2026 + Standard montages
ALL_MONTAGES = [
    "01_tcp_ar", "02_tcp_le", "03_tcp_ar_a", "04_tcp_le_a",         # TUH Corpus
    "05_tcp_ar_b", "06_tcp_le_b", "07_tcp_ar_c", "08_tcp_le_c"      # To complete standard montages
]

# Data partitions
PARTITION_TO_SPLIT = {
    "train": "train",
    "dev": "val",
    "eval": "test",
}

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

# Channel names (10-20 and 10-10 system)
CHANNELS = [
    "FP1", "FP2", "F7", "F3", "FZ", "F4", "F8",         # Frontal 
    "C3", "CZ", "C4",                                   # Central
    "P3", "PZ", "P4",                                   # Parietal
    "O1", "OZ", "O2",                                   # Occipital
    "T3/T7", "T4/T8", "T5/P7", "T6/P8",                 # Temporal
    "AT1/T1/FT9", "AT2/T2/FT10",                        # Additional: Inferior anterotemporal electrodes
    #"A1", "A2",                                         # Additional: Ear electrodes (Reference)
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


# Windowing
WINDOW_REQUESTS_ARTIFACTS = {
    "eye":                        [ {"window_size_sec": 5, "stride_sec": 2, "artifact_umbral": 0.1},
                                    {"window_size_sec": 2, "stride_sec": 1, "artifact_umbral": 0.15},
                                   #{"window_size_sec": 1, "stride_sec": 1, "artifact_umbral": 0.3},
                                   #{"window_size_sec": 1, "stride_sec": 0.5, "artifact_umbral": 0.3},
                                   #{"window_size_sec": 0.5, "stride_sec": 0.5, "artifact_umbral": 0.6},
                                   #{"window_size_sec": 0.5, "stride_sec": 0.25, "artifact_umbral": 0.6},
                                   ],
    "muscle":                     [{"window_size_sec": 1, "stride_sec": 0.5, "artifact_umbral": 0.3},
                                   {"window_size_sec": 1, "stride_sec": 1, "artifact_umbral": 0.3},
                                   {"window_size_sec": 2, "stride_sec": 1, "artifact_umbral": 0.3},
                                   {"window_size_sec": 5, "stride_sec": 2, "artifact_umbral": 0.2},
                                   ],
    "non_physiological":          [{"window_size_sec": 0.5, "stride_sec": 0.25, "artifact_umbral": 0.2},
                                   {"window_size_sec": 1, "stride_sec": 0.5, "artifact_umbral": 0.3},
                                   {"window_size_sec": 1, "stride_sec": 1, "artifact_umbral": 0.3},
                                   {"window_size_sec": 2, "stride_sec": 1, "artifact_umbral": 0.3},
                                   ],
}

# General models configuration
## Train, validation and test proportion of the dataset
RATIOS= {"train": 0.7, "val": 0.15, "test": 0.15}

## Split version
VERSION = 1
LABEL_VERSION = 1

## Identifiers metadata and target not required for the models
KEYS = ["Patient", "Session", "Section"]

LEAKAGE_COLS = [
    "ic_index", "ic_raw_label", "ic_target_label",
    "Patient", "Session", "Section", "Start", "split",
    "is_positive", "Partition",
]

### Test of current configurations
if __name__ == "__main__":

    # Project root
    print(f"BASE_DIR: {BASE_DIR}")
    assert (BASE_DIR / "src").is_dir(), "BASE_DIR must have src/ according to file location"
    
    # Dataset root
    print(f"\nBASE_PATH: {BASE_PATH}")
    assert BASE_PATH.exists(), f"Dataset not found in current BASE_PATH."

    # Checking subdirectories
    for name, rel in CORPUS_PATHS.items():
        print(f"  corpus {name:<10} {'OK   ' if (BASE_PATH / rel).exists() else 'MISSING'} {BASE_PATH / rel}")
    assert (BASE_PATH / CORPUS_PATHS["artifact"]).exists()

    # Montage configuration
    assert len(MONOPOLAR_CHANNELS) == 19 and len(set(MONOPOLAR_CHANNELS)) == 19
    assert len(BIPOLAR_MONTAGE["names"]) == 18
    assert all(c in MONOPOLAR_CHANNELS for c in BIPOLAR_MONTAGE["anode"] + BIPOLAR_MONTAGE["cathode"])
    
    # Verification of data split ratios distribution
    assert abs(sum(RATIOS.values()) - 1) < 1e-9

    # Check corpus labeling
    assert set(WINDOW_REQUESTS_ARTIFACTS) == set(ARTIFACT_KEYWORDS)
    assert RAW_TO_TARGET["eye blink"] == "eye" and RAW_TO_TARGET["muscle artifact"] == "muscle"
    assert RAW_TO_TARGET["channel noise"] == "non_physiological"
    assert RAW_TO_TARGET["other"] == "non_physiological"
    assert RAW_TO_TARGET["heart beat"] == "non_physiological"

    # Check version and debug direction
    print(f"\nVERSION={VERSION} | DEBUG_DIR={DEBUG_DIR}")

    # File functions verification
    current_script = Path(__file__).name
    print(f"\n[OK] {current_script}")