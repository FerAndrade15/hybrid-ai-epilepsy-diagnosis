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
# prerprocessing.py

# Data analysis libraries
import mne
import numpy as np

# Shared config data for EEG preprocessing
from src.core.data_config import CHANNELS, BIPOLAR_MONTAGE, MONOPOLAR_CHANNELS
from src.core.data_loader import get_session_data, load_raw_edf

def channel_standard_nomenclature(ch_name):
    """
    Considering that various academic datasets and commercial EEG machines export signals
    with channel names that vary from the standard, this function renames channels to 
    match to the current standard (incorporing 10-20, 10-10 and 10-05 systems).
    """
    text = "".join(x if x.isalnum() or x.isspace() else " " for x in ch_name)
    text = text.upper().split()
    name = [ch.split("/")[-1] for x in text for ch in CHANNELS if x in ch.split("/")]
    name = str(name[0]).upper() if name else None
    return name

def bipolar_matrix():
    """W (18x19): bipolar = W @ monopolar, en el orden de MONOPOLAR_CHANNELS."""
    idx = {ch: i for i, ch in enumerate(MONOPOLAR_CHANNELS)}
    W = np.zeros((len(BIPOLAR_MONTAGE["names"]), len(MONOPOLAR_CHANNELS)))
    for k, (a, c) in enumerate(zip(BIPOLAR_MONTAGE["anode"], BIPOLAR_MONTAGE["cathode"])):
        W[k, idx[a]], W[k, idx[c]] = 1.0, -1.0
    return W

def raw_data_preproccesing(raw_data, l_freq=1.0, h_freq=100.0, notch_freq=[50.0, 60.0], bipolar_montage=False, verbose=False, resamplig_freq=256):
    """
    Preprocessing pipeline for all EDF raw signals.

    Parameters
        bipolar_montage:
            False: Monopolar | True: Bipolar
    """
    raw = raw_data.copy()

    # Rename channels according to 10-10 system nomenclature
    rename_map = {
        ch: new_name 
        for ch in raw.ch_names 
        if (new_name := channel_standard_nomenclature(ch)) is not None
    }   

    raw.pick(list(rename_map.keys()))              # Extract EEG channels
    raw.rename_channels(rename_map, on_missing="ignore")
    missing = [c for c in MONOPOLAR_CHANNELS if c not in raw.ch_names]
    if missing:
        raise ValueError(f"Missing channels according to current configuration: \n{missing}")
    
    raw.pick(MONOPOLAR_CHANNELS)

    # Preserve 10-20 standard positions according to 10-10 nomenclature (10-20 extended)
    montage = mne.channels.make_standard_montage("standard_1005")
    raw.set_montage(montage, on_missing="ignore", match_case=False)

    ## Filtering 
    raw.filter(l_freq, h_freq, verbose="WARNING" if not verbose else None)
    if notch_freq is not None:
        raw.notch_filter(freqs=notch_freq, verbose="WARNING" if not verbose else None)

    # Resampling
    raw.resample(resamplig_freq, verbose="WARNING" if not verbose else None)

    # Montage configuration
    if bipolar_montage:
        # Bipolar reference
        raw = mne.set_bipolar_reference(raw, 
                                  anode=BIPOLAR_MONTAGE["anode"], 
                                  cathode=BIPOLAR_MONTAGE["cathode"],
                                  ch_name=BIPOLAR_MONTAGE["names"],
                                  drop_refs=True)
    else:
        # Common average reference
        raw.set_eeg_reference("average", verbose="WARNING" if not verbose else None)
    return raw

### Test for preprocessing functions
if __name__ == "__main__":
    import time
    from src.core.data_loader import get_session_data

    # 1) Nomenclatura
    cases = {"T3": "T7", "T5": "P7", "T4": "T8", "T6": "P8", "EEG FP1-REF": "FP1",
             "EEG CZ-LE": "CZ", "EEG T1-REF": "FT9", "EEG A1-REF": None}
    for raw_name, expected in cases.items():
        got = channel_standard_nomenclature(raw_name)
        assert got == expected, (raw_name, got, expected)
    assert all(channel_standard_nomenclature(c) == c for c in MONOPOLAR_CHANNELS)
    print("[OK] nomenclatura")

    # 2) Matriz bipolar
    W = bipolar_matrix()
    assert W.shape == (18, 19)
    assert (W.sum(axis=1) == 0).all() and (np.abs(W).sum(axis=1) == 2).all()
    print("[OK] bipolar_matrix")

    # 3) Sesiones reales: ¿cuántas tienen los 19 canales?
    sessions = get_session_data("artifact", n_patients=10, max_sessions=1)
    ok = 0
    for _, row in sessions.iterrows():
        raw = load_raw_edf(row["edf"])
        try:
            t0 = time.time()
            mono = raw_data_preproccesing(raw, bipolar_montage=False)
        except ValueError as e:
            print(f"[FALLA] {row['edf'].name} ({row['montage']}): {e}")
            continue
        ok += 1
        m = mono.get_data()
        assert mono.ch_names == MONOPOLAR_CHANNELS, "orden de canales distinto al de MONOPOLAR_CHANNELS"
        assert mono.info["sfreq"] == 256
        assert np.abs(m.mean(axis=0)).max() < 1e-12, "el CAR no quedó aplicado"

        # 4) Equivalencia: bipolar de MNE == W @ monopolar
        bip = raw_data_preproccesing(raw, bipolar_montage=True)
        assert bip.ch_names == BIPOLAR_MONTAGE["names"], bip.ch_names
        diff = np.abs(bip.get_data() - W @ m).max()
        print(f"[OK] {row['edf'].name} ({row['montage']}): mono {m.shape}, "
              f"máx|MNE bipolar − W@mono| = {diff:.1e} V, {time.time() - t0:.0f} s")
        assert diff < 1e-10
    print(f"\n{ok}/{len(sessions)} sesiones con montaje válido")
    assert ok > 0
