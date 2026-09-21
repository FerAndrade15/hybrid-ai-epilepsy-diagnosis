"""
# File: data_loader.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Load EDFs and annotations, preloading the full signal into memory. 
"""
# data_loader.py

# Data analysis libraries
import mne
import pandas as pd
import numpy as np
from pathlib import Path

# Shared config data for EEG preprocessing
from src.core.data_config import ALL_MONTAGES, CORPUS_PATHS, BASE_PATH, PARTITION_TO_SPLIT

# General function to find the project root directory
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

# Funtions for EEG data analysis and dataframe generation
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

def load_raw_edf(edf_path, preloaD=True):
    """
    Load EDF signal: All channels, duration
    """
    mne.set_log_level("WARNING")    # Settings to set output at request raw data
    return mne.io.read_raw_edf(edf_path, preload=preloaD, verbose="WARNING") 

def load_annotations(csv_path):
    """
    Read csv data annotations by session:
        channel, start_time, stop_time, label
    """
    return pd.read_csv(csv_path, sep=",", comment="#")

def build_annotations_index(corpus_name,  n_patients=None, min_sessions=None, max_sessions=None, montages=None, paths=False):
    """
    Creates the dataframe according to the annotations metadata:
    - Patient
    - Session
    - Section
    - Montage
    """
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
                EDF=s["edf"],
                CSV=s["csv"],
            )
        frames.append(ann)
    return pd.concat(frames, ignore_index=True)

# Select sessions for testing
def pick_test_session(corpus="artifact", n_patients=3, index=0, min_duration=120):
    """
    Analyze shorter session (≥ min_duration s) between patients for faster depuration.
    """
    s = get_session_data(corpus, n_patients=n_patients, max_sessions=1)
    ok = s[s["duration_s"] >= min_duration]
    return (ok if len(ok) else s).sort_values("duration_s").iloc[index]

### Test of loading functions
if __name__ == "__main__":
    # Library imports
    import time
    from IPython.display import display
    
    # Start of timer
    t0 = time.time()

    # Corpus selected
    data_corpus = list(CORPUS_PATHS.keys())[1]
    print(f"Currently selected corpus: {data_corpus}\n")

    # Extraction of patients sessions
    sessions = get_session_data(data_corpus, n_patients=3, max_sessions=1)
    print(f"get_session_data: {time.time() - t0:.0f} s (reading all EDF headers...)")
    print(sessions.drop(columns=["edf", "csv"]).to_string())
    assert not sessions.empty and sessions["patient"].nunique() == 3
    assert sessions[["patient", "session", "section"]].notna().all().all(), "Patient, session and section not parsed"
    assert all(p.exists() for p in sessions["csv"])

    # Annotations 
    ann = build_annotations_index("artifact", n_patients=3, max_sessions=1, paths=True)
    need = {"channel", "start_time", "stop_time", "label", "Patient", "Session", "Section",
            "Montage", "NoChannels", "Duration", "EDF", "CSV"}
    assert need <= set(ann.columns), need - set(ann.columns)
    assert (ann["stop_time"] > ann["start_time"]).all()
    out = (ann["stop_time"] > ann["Duration"] + 1).sum()
    print(f"Annotations out of EDF duration: {out}")
    print("\nLabels:\n", ann["label"].value_counts().to_string())
    display(ann)

    # Analyze selected sessions
    row = pick_test_session()
    raw = load_raw_edf(row["edf"])
    print(f"\nTesting session {row['patient']}_{row['session']}_{row['section']}: "
          f"{len(raw.ch_names)} channels, {raw.info['sfreq']} Hz, {row['duration_s']:.0f} s")

    # File functions verification
    current_script = Path(__file__).name
    print(f"\n[OK] {current_script}")
