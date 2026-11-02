"""
# File: ica_module.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Reusable ICA (Independent Component Analysis) modules for the AI pipeline 
including ICALabel and direct application of signal decomposition if required.
 
Provides functions for preliminary visual exploration, 
automated artifact detection (EOG/EMG), and EEG signal denoising prior to 
model training.
"""
# Data analysis libraries
import mne
import numpy as np
from pathlib import Path
from pickle import load, dump
from mne.preprocessing import ICA
from mne_icalabel import label_components
from mne_icalabel.iclabel import iclabel_label_components

# Data extraction functions EEG preprocessing
#from src.core.data_loader import load_raw_edf, get_session_data
#from src.core.preprocessing import raw_data_preproccesing

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


def get_or_compute_ica(raw, cache_key, cache_dir):
    cache_dir = Path(cache_dir); cache_dir.mkdir(parents=True, exist_ok=True)
    fif, meta = cache_dir / f"{cache_key}-ica.fif", cache_dir / f"{cache_key}_labels.npz"
    if fif.exists() and meta.exists():
        try:
            ica = mne.preprocessing.read_ica(fif, verbose="WARNING")
            npz = np.load(meta, allow_pickle=False)
            probs = npz["probs"]
            return ica, {"labels": [str(x) for x in npz["labels"]], "y_pred_proba": probs}, probs
        except Exception as e:
            print(f"[WARN] Caché ICA ilegible, se recalcula: {e}")
    ica, ic_labels, probs = classification_iclabel(raw)   # tu función original
    try:
        ica.save(fif, overwrite=True, verbose="WARNING")
        np.savez_compressed(meta, labels=np.array(ic_labels["labels"], dtype="U32"), probs=probs)
    except Exception as e:
        print(f"[WARN] No se pudo guardar la caché ICA: {e}")
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