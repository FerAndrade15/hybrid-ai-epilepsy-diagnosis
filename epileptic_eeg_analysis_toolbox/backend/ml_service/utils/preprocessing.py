"""
# File: preprocessing.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Required preprocessing steps for raw signal analysis:
- Common average reference and bipolar montage implementation
- Band-pass filtering from 1 to 100 Hz
- Notch filtering at 50/60 Hz to remove mains power noise
- Standard channel renaming
"""
# Data analysis libraries
import mne
import numpy as np
from typing import Optional, List
from config.data_config import(
    SFREQ,
    DEFAULT_L_FREQ,
    DEFAULT_H_FREQ,
    DEFAULT_NOTCH_FREQ,
    CHANNELS,
    MONOPOLAR_CHANNELS,
    BIPOLAR_MONTAGE,
)

def channel_standard_nomenclature(ch_name: str) -> Optional[str]:
    """
    Considering that various academic datasets and commercial EEG machines export signals
    with channel names that vary from the standard, this function renames channels to 
    match to the current standard (incorporing 10-20, 10-10 and 10-05 systems).
    """
    text = "".join(x if x.isalnum() or x.isspace() else " " for x in ch_name)
    tokens = text.upper().split()
    matched = [ch.split("/")[-1] for x in tokens for ch in CHANNELS if x in ch.split("/")]

    if not matched:
        return None
    
    std_name = str(matched[0]).upper()
    
    if std_name.endswith("z") or std_name.endswith("Z"):
        std_name = std_name[:-1] + "Z"
    
    return std_name

def bipolar_matrix() -> np.ndarray:
    """W (18x19): bipolar = W @ monopolar, en el orden de MONOPOLAR_CHANNELS."""
    idx = {ch: i for i, ch in enumerate(MONOPOLAR_CHANNELS)}
    W = np.zeros((len(BIPOLAR_MONTAGE["names"]), len(MONOPOLAR_CHANNELS)))
    for k, (a, c) in enumerate(zip(BIPOLAR_MONTAGE["anode"], BIPOLAR_MONTAGE["cathode"])):
        if a in idx and c in idx:
            W[k, idx[a]], W[k, idx[c]] = 1.0, -1.0
    return W

def raw_data_preproccesing(
        raw_data: mne.io.Raw, 
        l_freq: float = DEFAULT_L_FREQ, 
        h_freq: float = DEFAULT_H_FREQ, 
        notch_freq: list | float = DEFAULT_NOTCH_FREQ,
        bipolar_montage: bool = False,
        resampling_freq: int = SFREQ,
        verbose: bool = False
    ) -> mne.io.Raw:
    """
    Preprocessing pipeline for all EDF raw signals.

    Parameters
        bipolar_montage:
            False: Monopolar | True: Bipolar
    """
    log_level = "INFO" if verbose else "WARNING"
    raw = raw_data.copy()

    if not raw.preload:
        raw.load_data(verbose=log_level)

    # Rename channels according to 10-10 system nomenclature
    rename_map = {
        ch: new_name 
        for ch in raw.ch_names 
        if (new_name := channel_standard_nomenclature(ch)) is not None
    }   
    #print(">> CHANNELS: ", rename_map)

    raw.rename_channels(rename_map, on_missing="ignore")
    #print(">> CHANNELS: ", raw.ch_names)

    available_monopolar = [ch for ch in MONOPOLAR_CHANNELS if ch in raw.ch_names]
    
    #print(">> CHANNELS (MONOPOLAR): ", available_monopolar)

    if len(available_monopolar) < len(MONOPOLAR_CHANNELS):
        missing = [ch for ch in MONOPOLAR_CHANNELS if ch not in raw.ch_names]
        if verbose:
            print(f"[WARN] Canales no encontrados en este estudio: {missing}")
    
    raw.pick(available_monopolar)

    # Preserve 10-20 standard positions according to 10-10 nomenclature (10-20 extended)
    montage = mne.channels.make_standard_montage("standard_1005")
    raw.set_montage(montage, on_missing="ignore", match_case=False)
    
    # Filters
    raw.filter(l_freq=l_freq, h_freq=h_freq, verbose=log_level)
    if notch_freq is not None:
        raw.notch_filter(freqs=notch_freq, verbose=log_level)

    # Resampling
    if raw.info["sfreq"] != resampling_freq:
        raw.resample(resampling_freq, verbose=log_level)
    
    # Montage configuration
    if bipolar_montage:
        # Bipolar reference
        anodes = []
        cathodes = []
        names = []
        for name, a, c in zip(BIPOLAR_MONTAGE["names"], BIPOLAR_MONTAGE["anode"], BIPOLAR_MONTAGE["cathode"]):
            if a in raw.ch_names and c in raw.ch_names:
                anodes.append(a)
                cathodes.append(c)
                names.append(name)

        raw = mne.set_bipolar_reference(
            raw, 
            anode=anodes, 
            cathode=cathodes, 
            ch_name=names, 
            drop_refs=True, 
            copy=False, 
            verbose=log_level
        )
    else:
        # Common average reference
        raw.set_eeg_reference("average", projection=False, verbose=log_level)
    return raw

### Test for preprocessing functions
# if __name__ == "__main__":