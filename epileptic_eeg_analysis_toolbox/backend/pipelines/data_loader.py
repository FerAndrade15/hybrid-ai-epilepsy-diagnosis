"""
# File: data_loader.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Load EDFs and annotations, preloading the full signal into memory. 
"""
# Data analysis libraries
import mne
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, Any, Optional

# Shared config data for EEG preprocessing
from config.data_config import ALL_MONTAGES # CORPUS_PATHS, BASE_PATH, PARTITION_TO_SPLIT

# ----------------------------------------------------------------------------------------
# General functions to find the project root directory and partitions
# ----------------------------------------------------------------------------------------
def find_project_root(marker):
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / marker).is_dir():
            return parent
    raise RuntimeError(f"Main folder path not found (looking for '{marker}' folder)")

def partition_from_path(edf_path, corpus_path):
    """
    Folder partition if existing.
    """
    folders = Path(edf_path).relative_to(corpus_path).parts[:-1]
    return next((p for p in folders if p in PARTITION_TO_SPLIT), "")

# ----------------------------------------------------------------------------------------
# General functions to extract data (signals and annotations)
# ----------------------------------------------------------------------------------------
def load_raw_edf(edf_path: Path | str, preloaD:bool = True) -> mne.io.Raw:
    """
    Load EDF signal: All channels, duration
    """
    edf_path = Path(edf_path)
    if not edf_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo EDF: {edf_path}")
    
    mne.set_log_level("WARNING")    # Settings to set output at request raw data
    return mne.io.read_raw_edf(edf_path, preload=preloaD, verbose="WARNING") 

def load_annotations(csv_path: Path | str) -> Optional[pd.DataFrame]:
    """
    Read csv data annotations by session:
        channel, start_time, stop_time, label
    """
    csv_path = Path(csv_path)
    if not csv_path.exists():
        return None
    try:
        df = pd.read_csv(csv_path, sep=",", comment="#")
        return df
    except Exception as e:
        print(f"[WARN] Error al leer anotaciones de {csv_path}: {e}")
        return None

# ----------------------------------------------------------------------------------------
# Funtions for EEG data analysis (for standard EDF)
# ----------------------------------------------------------------------------------------
def get_edf_metadata(edf_path:Path | str) -> Dict[str, Any]:
    """ Get esential metadata from EDF header to check compatibility and feed study data base"""
    edf_path = Path(edf_path)
    raw = load_raw_edf(edf_path, preloaD=False)

    patient_code = None
    if raw.info.get("subject_info") and raw.info["subject_info"].get("his_id"):
        patient_code = str(raw.info["subject_info"]["his_id"]).strip()

    if not patient_code:
        parts = [p for p in edf_path.stem.split("_") if len(p) == 8 and p.isalpha()]
        if parts:
            patient_code = parts[0]

    duration = raw.times[-1] if len(raw.times) > 0 else 0.0
        
    return {
        "edf_file_path": str(edf_path.resolve()),
        "patient_code": patient_code,
        "sampling_freq_hz": float(raw.info["sfreq"]),
        "no_channels": len(raw.ch_names),
        "duration_s": float(duration),
        "channels": list(raw.ch_names),
        "total_samples": int(raw.n_times)
    }

# ----------------------------------------------------------------------------------------
# Funtions for EEG data analysis and dataframe generation (for models testing)
# ----------------------------------------------------------------------------------------
def get_session_data(corpus_name, n_patients=None, min_sessions=None, max_sessions=None, montages=None):
    """
    Pair EDF and CSV files and extract patient and montage and saves important data from edfs:
        n_patients: Patients to analyze. None means no patient limit.
        min_sessions: minimum sessions per patient to include that patient.
        max_sessions: maximum sessions per patient to return.

    Output: List of dicts { "edf": Path, "csv": Path, "patient": str, "montage": str, 
                            "no_channels": int, "duration_s": float}
    """

    montages = montages or ALL_MONTAGES
    corpus_path = BASE_PATH / CORPUS_PATHS[corpus_name]
    all_sessions = []

    for edf_path in corpus_path.rglob("*.edf"):
        montage = edf_path.parent.name
        if montage not in montages:
            continue

        edf_data = mne.io.read_raw_edf(edf_path, preload=False, verbose="WARNING")

        csv_path = edf_path.with_suffix(".csv")
        if not csv_path.exists():
            continue

        document_name = edf_path.stem
        patient = next((p for p in document_name.split("_") if len(p) == 8 and p.isalpha()),None)
        session = next((p for p in document_name.split("_") if p.startswith("s") and p[1:].isdigit()), None)
        section = next((p for p in document_name.split("_") if p.startswith("t") and p[1:].isdigit()), None)
        partition = partition_from_path(edf_path, corpus_path)

        if patient is None:
            continue

        all_sessions.append({
            "edf": edf_path,
            "csv": csv_path,
            "patient": patient,
            "session": session,
            "section": section,
            "montage": montage,
            "no_channels": len(edf_data.ch_names),
            "duration_s": edf_data.times[-1] if len(edf_data.times) > 0 else np.nan,
            "partition": partition,
        })

    sessions_by_patient = {}
    patient_order = []
    for session in all_sessions:
        patient = session["patient"]
        if patient not in sessions_by_patient:
            sessions_by_patient[patient] = []
            patient_order.append(patient)
        sessions_by_patient[patient].append(session)

    filtered_sessions = []
    selected_patients = 0
    for patient in patient_order:
        if n_patients is not None and selected_patients >= n_patients:
            break

        patient_sessions = sessions_by_patient[patient]
        if min_sessions is not None and len(patient_sessions) < min_sessions:
            continue

        if max_sessions is not None:
            patient_sessions = patient_sessions[:max_sessions]

        filtered_sessions.extend(patient_sessions)
        selected_patients += 1

    return pd.DataFrame(filtered_sessions)

def build_annotations_index(corpus_name,  n_patients=None, min_sessions=None, max_sessions=None, montages=None, paths=False, refresh=False, CACHE_DIR="annotations"):
    """
    Creates the dataframe according to the annotations metadata:
    - Patient
    - Session
    - Section
    - Montage
    """
    cache_dir = CACHE_DIR
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = cache_dir / f"annotations_index_{corpus_name}.parquet"

    if cache_file.exists() and not refresh:
        ann = pd.read_parquet(cache_file)

        if n_patients is not None:
            selected_patients = ann['Patient'].drop_duplicates().head(n_patients).tolist()
            ann = ann[ann['Patient'].isin(selected_patients)]
        if max_sessions is not None:
            ann = ann.groupby('Patient').apply(
                lambda x: x[x['Session'].isin(x['Session'].drop_duplicates().head(max_sessions))]
            ).reset_index(drop=True)

        if not paths:
            ann = ann.drop(columns=["EDF", "CSV"], errors="ignore")

        return ann

    print(f"[INFO] Creating '{corpus_name}' annotations, it could take long...")
    sessions_df = get_session_data(corpus_name,  n_patients, min_sessions, max_sessions, montages)
    frames = []
    for _, s in sessions_df.iterrows():
        ann = load_annotations(s["csv"]).assign(
                                                Patient=s["patient"], 
                                                Session=s["session"],
                                                Section=s["section"],
                                                Montage=s["montage"],
                                                Partition=s["partition"],
                                                NoChannels=s["no_channels"],
                                                Duration=s["duration_s"],
                                            )
        if paths:
            ann = ann.assign(
                EDF=str(s["edf"]),
                CSV=str(s["csv"]),
            )
        frames.append(ann)

    full_ann = pd.concat(frames, ignore_index=True)
    
    full_ann.to_parquet(cache_file, index=False)
    print(f"[INFO] Index saved in: {cache_file}")

    ann_to_return = full_ann.copy()
    if n_patients is not None:
        selected_patients = ann_to_return['Patient'].drop_duplicates().head(n_patients).tolist()
        ann_to_return = ann_to_return[ann_to_return['Patient'].isin(selected_patients)]
    if max_sessions is not None:
        ann_to_return = ann_to_return.groupby('Patient').apply(
            lambda x: x[x['Session'].isin(x['Session'].drop_duplicates().head(max_sessions))]
        ).reset_index(drop=True)
        
    if not paths:
        ann_to_return = ann_to_return.drop(columns=["EDF", "CSV"], errors="ignore")
        
    return ann_to_return

# Select sessions for testing
def pick_test_session(corpus="artifact", n_patients=3, index=0, min_duration=120):
    """
    Analyze shorter session (≥ min_duration s) between patients for faster depuration.
    """
    s = get_session_data(corpus, n_patients=n_patients, max_sessions=1)
    ok = s[s["duration_s"] >= min_duration]
    return (ok if len(ok) else s).sort_values("duration_s").iloc[index]

# General load tests
if __name__ == "__main__":
    print("Module data_loader cargando correctamente")