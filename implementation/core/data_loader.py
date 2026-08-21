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

# Shared config data for EEG preprocessing
from implementation.core.data_config import ALL_MONTAGES, CORPUS_PATHS, BASE_PATH


def get_session_data(corpus_name, n_patients=None, min_sessions=None, max_sessions=None, montages=None):
    """
    Pair EDF and CSV files and extract patient and montage and saves important data from edfs:
        n_patients: Patients to analyze. None means no patient limit.
        min_sessions: minimum sessions per patient to include that patient.
        max_sessions: maximum sessions per patient to return.

    Output: List of dicts   {"edf": Path, "csv": Path, "patient": str, "montage": str, 
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
        ann = load_annotations(s["csv"])
        ann = ann.assign(
            Patient=s["patient"], 
            Session=s["session"],
            Section=s["section"],
            Montage=s["montage"],
            NoChannels=s["no_channels"],
            Duration=s["duration_s"],
        )
        if paths:
            ann = ann.assign(
                Patient=s["patient"], 
                Session=s["session"],
                Section=s["section"],
                Montage=s["montage"],
                NoChannels=s["no_channels"],
                Duration=s["duration_s"],
                EDF=s["edf"],
                CSV=s["csv"],
            )
        else:
            ann = ann.assign(
                Patient=s["patient"], 
                Session=s["session"],
                Section=s["section"],
                Montage=s["montage"],
                NoChannels=s["no_channels"],
                Duration=s["duration_s"],
            )
        frames.append(ann)
    return pd.concat(frames, ignore_index=True)

if __name__ == "__main__":

    # Data integration libraries
    from tabulate import tabulate
    from pathlib import Path

    # Data analysis libraries
    from IPython.display import display

    # Extract by patient and session
    sessions = pd.DataFrame(get_session_data("artifact", n_patients=1))

    if sessions.empty:
        print("No sessions found")
    else:
        display_df = sessions.copy()
        for col in ("edf", "csv"):
            if col in display_df:
                display_df[col] = display_df[col].map(lambda p: p.name if isinstance(p, Path) else str(p))

        print("\n== Session summary ==")
        print(tabulate(display_df, headers="keys", tablefmt="psql", showindex=False))
        print(f"\nTotal sessions: {len(display_df)}")
        print(f"Patients: {display_df['patient'].nunique()}")
        print(f"Montages: {', '.join(sorted(display_df['montage'].unique()))}\n")

        for idx, row in sessions.iterrows():
            print("=" * 60)
            print(f"Session {idx + 1}: patient={row['patient']} montage={row['montage']}")
            print(f"Loading: {row['edf'].name} / {row['csv'].name}")

            # Manual extraction 
            raw = load_raw_edf(row["edf"])
            ch_names = raw.ch_names
            ch_preview = ", ".join(ch_names[:10])
            if len(ch_names) > 10:
                ch_preview += ", ..."
            print(f">> Channels: {len(ch_names)} [{ch_preview}]")
            print(f">> Duration: {raw.times[-1]:.1f} s, Frequency: {raw.info['sfreq']} Hz")

            # Manual extraction 
            ann = load_annotations(row["csv"])
            print("Annotations head:")
            print(tabulate(ann.head(), headers="keys", tablefmt="psql", showindex=False))
            print()

    # Visualize annotations (automated general functions)
    sessions = build_annotations_index("artifact", n_patients=1)
    display(sessions)