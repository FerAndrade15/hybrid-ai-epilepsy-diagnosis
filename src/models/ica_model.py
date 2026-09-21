"""
# File: ica_model.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Reusable ICA (Independent Component Analysis) modules for the AI pipeline 
including ICALabel. Provides functions for preliminary visual exploration, 
automated artifact detection (EOG/EMG), and EEG signal denoising prior to 
model training.
"""
# File: ica_model.py

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
from src.core.data_loader import load_raw_edf, get_session_data
from src.core.preprocessing import raw_data_preproccesing

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
            comp_feats[f"ic_contrib_{ch.upper()}"] = activity[comp_idx] *  abs(mixing[ch_idx, comp_idx])
        feats[comp]= comp_feats
    return feats


### Test ICA functions
if __name__ == "__main__":
    import time
    from collections import Counter
    from src.core.data_config import DEBUG_DIR, MONOPOLAR_CHANNELS, ICLABEL_CATEGORIES, RAW_TO_TARGET
    from src.core.data_loader import pick_test_session

    row = pick_test_session()
    p, s, sec = row["patient"], row["session"], row["section"]
    print(f"Sesión: {p}_{s}_{sec} ({row['duration_s']:.0f} s)")

    signal = raw_data_preproccesing(load_raw_edf(row["edf"]), bipolar_montage=False)
    assert signal.ch_names == MONOPOLAR_CHANNELS

    t0 = time.time()
    ica, ic_labels, probs = get_or_compute_ica(signal, p, f"{s}_{sec}", DEBUG_DIR / "cache" / "ica")
    print(f"ICA + ICLabel: {time.time() - t0:.0f} s (la 2ª corrida debe ser instantánea)")

    labels, n_ic = list(ic_labels["labels"]), ica.n_components_
    print(f"Componentes: {n_ic} de {len(MONOPOLAR_CHANNELS)} canales")
    print("ICLabel :", dict(Counter(labels)))
    print("→ TUAR  :", dict(Counter(RAW_TO_TARGET[l] for l in labels)))
    assert len(labels) == len(probs) == n_ic
    assert set(labels) <= set(ICLABEL_CATEGORIES), set(labels) - set(ICLABEL_CATEGORIES)
    assert ica.ch_names == MONOPOLAR_CHANNELS

    sources = ica.get_sources(signal).get_data()
    mixing = ica.get_components()
    assert sources.shape == (n_ic, signal.n_times) and mixing.shape == (19, n_ic)

    contrib = channel_contribution(sources[:, :256], mixing, MONOPOLAR_CHANNELS, [f"c{i}" for i in range(n_ic)])
    assert len(contrib["c0"]) == 19 and "ic_contrib_FP1" in contrib["c0"]

    # Sanidad: los ICs 'eye blink' deben pesar sobre los canales frontales
    for i, l in enumerate(labels):
        if l == "eye blink":
            top = np.array(MONOPOLAR_CHANNELS)[np.argsort(-np.abs(mixing[:, i]))[:3]]
            print(f"  IC{i} eye blink (p={probs[i]:.2f}): top-3 canales = {list(top)}")
    print("[OK] ica_model")

"""

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
"""