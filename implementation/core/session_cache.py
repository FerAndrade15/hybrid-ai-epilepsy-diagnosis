""""
# File: session_cache.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Functions for saving the data extracted for each session and reusing it without reloading continuously.

"""
# session_cache.py

import numpy as np
from pathlib import Path

from implementation.core.data_loader import load_raw_edf
from implementation.core.preprocessing import raw_data_preproccesing
from implementation.models.ica_model import get_or_compute_ica

def get_or_compute_session(patient, session, path_edf, cache_dir="cache/sessions",
                           ica_cache_dir="cache/ica", use_ica=True):
    """
    Load EDF, preprocessing and ICA once per session.
    Save as .npz the results for future executions of the models.
    """
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = cache_dir/f"{patient}_{session}.npz"

    if cache_file.exists():
        npz = np.load(cache_file, allow_pickle=True)
        return{
            "data": npz["data"],
            "sources_full": npz["sources_full"] if use_ica else None,
            "mixing": npz["mixing"] if use_ica else None,
            "comp_names": npz["comp_names"] if use_ica else None,
            "probs": npz["probs"] if use_ica else None,
            "sfreq": float(npz["sfreq"]),
            "ch_names": list(npz["ch_names"]),
        }

    raw = load_raw_edf(path_edf, preloaD=True)
    signal = raw_data_preproccesing(raw)
    data = signal.get_data()
    sfreq = signal.info["sfreq"]
    ch_names = signal.ch_names

    payload = {
        "data": data, 
        "sfreq": sfreq,
        "ch_names": np.array(ch_names, dtype=object),
    }

    if use_ica:
        ica, ic_labels, probs = get_or_compute_ica(signal, patient, session, ica_cache_dir)
        payload.update({
            "sources_full": ica.get_sources(signal).get_data(),
            "mixing": ica.get_components(),
            "comp_names": np.array(ic_labels["labels"], dtype=object),
            "probs": probs,
        })

    np.savez_compressed(cache_file, **payload)

    return{
        "data": data,
        "sources_full": payload.get("sources_full"),
        "mixing": payload.get("mixing"),
        "comp_names": payload.get("comp_names"),
        "probs": payload.get("probs"),
        "sfreq": sfreq,
        "ch_names": ch_names,
    }