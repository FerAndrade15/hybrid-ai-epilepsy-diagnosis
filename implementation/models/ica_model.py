"""
# File: ica_model.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Reusable ICA (Independent Component Analysis) modules for the AI pipeline 
including ICALabel. Provides functions for preliminary visual exploration, 
automated artifact detection (EOG/EMG), and EEG signal denoising prior to 
model training.
"""

# Data analysis libraries
import numpy as np
import pandas as pd
from pathlib import Path
from pickle import load, dump
from mne.preprocessing import ICA
from mne_icalabel import label_components
from mne_icalabel.iclabel import iclabel_label_components
from IPython.display import display

# Data extraction functions EEG preprocessing
from implementation.core.data_loader import load_raw_edf, get_session_data
from implementation.core.preprocessing import raw_data_preproccesing

def explore_ica(raw, preprocessed_signal, variance_explained=0.95, random_seed=97):
    """
    Visual exploratioin of ICA without changing the signal.
    """
    print(f"Training ICA by retaining {variance_explained*100}% variance...")
    
    ica = ICA(n_components=variance_explained, 
              max_iter='auto', 
              random_state=random_seed,
              method="infomax")
    ica.fit(preprocessed_signal)

    print("Loading interactive windows...")

    # Visualization
    raw.plot(title="1. Raw signal", block=False)
    preprocessed_signal.plot(title="2. Preprocessed signal", block=False)

    ica.plot_sources(preprocessed_signal, title="3. Time series of ICA Components", block=False)
    ica.plot_components(title="4. ICA Spacial Topography")
    
    return ica

def classification_iclabel(preprocessed_signal, variance=0.99, random_seed=97):
    # Apply ICA 
    ica = ICA(n_components=variance, 
              max_iter='auto', 
              fit_params=dict(extended=True),
              random_state=random_seed,       
              method="infomax")
    
    ica.fit(preprocessed_signal)

    # Components classification
    ic_labels = label_components(preprocessed_signal, ica, method='iclabel')
    labels_pred_prob = ic_labels['y_pred_proba']
    return ica, ic_labels, labels_pred_prob


def get_or_compute_ica(signal, patient, session, cache_dir="cache/ica"):
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = cache_dir / f"{patient}_{session}_ica.pkl"

    if cache_file.exists():
        with open(cache_file, "rb") as f:
            return load(f)
    try: 
        ica, ic_labels, probs = classification_iclabel(signal)
    except RuntimeError as e:
        print(f"[WARN] ICA failed for {patient}_{session}: {e}")
        raise
    with open(cache_file, "wb") as f:
        dump((ica, ic_labels, probs), f)
    return ica, ic_labels, probs
        

def channel_contribution(sources_window, mixing, ch_names, comp_names):
    feats = {}
    activity = np.abs(sources_window).mean(axis=1)
    for comp_idx, comp in enumerate(comp_names):
        comp_feats = {}
        for ch_idx, ch in enumerate(ch_names):
            comp_feats[f"ic_contrib_{ch}"] = activity[comp_idx] *  abs(mixing[ch_idx, comp_idx])
        feats[comp]= comp_feats
    return feats

if __name__ == "__main__":
    # Definition of ammount of patients analyzed and edf path register
    sessions = pd.DataFrame(get_session_data("artifact", n_patients=1, max_sessions=1))

    # Function selection
    test = False
    
    if sessions.empty:
        print("Not sessions found.")
    else:
        for idx, row in sessions.iterrows():
            print("=" * 60)
            print(f"Loading and preprocessing EDF: {row['edf'].name}")
            
            raw = load_raw_edf(row["edf"])
            signal = raw_data_preproccesing(raw)
            if test is True:
                modelo_ica = explore_ica(raw, signal)
            else:
                classification_iclabel(signal)
            print("Inspection completed.")