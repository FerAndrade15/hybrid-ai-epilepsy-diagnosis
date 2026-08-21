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
import pandas as pd

# Shared config data for EEG preprocessing
from implementation.core.data_config import CHANNELS
from implementation.core.data_loader import get_session_data, load_raw_edf

def channel_standard_nomenclature(ch_name):
    """
    Considering that various academic datasets and commercial EEG machines export signals
    with channel names that vary from the standard, this function renames channels to 
    match the 10-20 and 10-10 systems.
    """
    text = "".join(x if x.isalnum() or x.isspace() else " " for x in ch_name)
    text = text.upper().split()
    name = [ch.split("/")[-1] for x in text for ch in CHANNELS if x in ch.split("/")]
    name = str(name[0]).capitalize() if name else None
    return name

def raw_data_preproccesing(raw_data, l_freq=1.0, h_freq=100.0, notch_freq=60.0, presaved_raw=True, verbose=False, resamplig_freq=256):
    """
    Preprocessing pipeline for all EDF raw signals.
    """
    raw = raw_data.copy()

    # Rename channels according to 10-10 system nomenclature
    rename_map = {
        ch: new_name 
        for ch in raw.ch_names 
        if (new_name := channel_standard_nomenclature(ch)) is not None
    }   
    raw.pick_channels(list(rename_map.keys()))              # Extract EEG channels
    raw.rename_channels(rename_map, on_missing="ignore")

    # Preserve 10-20 standard positions according to 10-10 nomenclature (10-20 extended)
    montage = mne.channels.make_standard_montage("standard_1005")
    raw.set_montage(montage, on_missing="ignore", match_case=False)

    ## Filtering 
    raw.filter(l_freq, h_freq, verbose="WARNING" if not verbose else None)
    raw.notch_filter(freqs=notch_freq, verbose="WARNING" if not verbose else None)

    # Resampling
    raw.resample(resamplig_freq, verbose="WARNING" if not verbose else None)

    # Common average reference
    raw.set_eeg_reference("average", verbose="WARNING" if not verbose else None)

    return raw


if __name__ == "__main__":

    # Shared config data for EEG preprocessing

    sessions = get_session_data("artifact", n_patients=1, max_sessions=1)
    if sessions.empty:
        print("No sessions found")
    else:
        for idx, row in sessions.iterrows():
            print("=" * 60)
            print(f"Session {idx + 1}: patient={row['patient']} montage={row['montage']}")
            print(f"Loading: {row['edf'].name} / {row['csv'].name}")

            # Original signal
            raw = load_raw_edf(row["edf"])
            ch_names = raw.ch_names
            ch_preview = ", ".join(ch_names[:10])
            if len(ch_names) > 10:
                ch_preview += ", ..."
            print(f">> Channels: {len(ch_names)} - {ch_preview}")

            # Procesed signal
            preprocessed_raw = raw_data_preproccesing(raw)
            ch_names = preprocessed_raw.ch_names
            ch_preview = ", ".join(ch_names[:10])
            if len(ch_names) > 10:
                ch_preview += ", ..."
            print(f">> Channels: {len(ch_names)} - {ch_preview}")

            # Visualization
            preprocessed_renamed = preprocessed_raw.copy()
            preprocessed_renamed.rename_channels(
                {ch: f"{ch}_pre" for ch in preprocessed_renamed.ch_names}
            )

            combined = raw.copy()
            combined.resample(preprocessed_raw.info['sfreq'], npad='auto')
            combined.add_channels([preprocessed_renamed], force_update_info=True)

            # Plot interleaved signals for comparison
            original_order = list(raw.ch_names)
            interleaved = []
            for ch in original_order:
                interleaved.append(ch)
                standard_name = channel_standard_nomenclature(ch)
                pre_ch = f"{standard_name}_pre" if standard_name is not None else None
                if pre_ch and pre_ch in combined.ch_names:
                    interleaved.append(pre_ch)

            combined.reorder_channels(interleaved)
            combined.plot(
                n_channels=2,
                duration=20,
                start=0,
                scalings={'eeg': 1500e-6},          # fija la altura en 1500 µV
                block=True
            )