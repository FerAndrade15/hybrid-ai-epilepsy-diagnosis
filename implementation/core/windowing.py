"""
# File: windowing.py
# Project: Trabajo de graduación
# Author: María Fernanda Andrade Recinos

Corpus-agnostic windowing for continuous annotations into fixed-size
sections and tags according to a given taxonomy with all the passed in data.
"""
# File: windowing.py

# Data integration libraries
import mne
import numpy as np
import pandas as pd
from torch import utils, tensor, float32

from implementation.core.data_loader import load_raw_edf
from implementation.core.preprocessing import raw_data_preproccesing
from implementation.models.ica_model import get_or_compute_ica

# Process to analyze data
def split_compound_label(label):
    return set(label.lower().split("_"))

# Merge annotations for a continous range
def merge_annotated_ranges(session_group):
    """
    Merge time intervals to get a continous session according to the annotations
    """
    intervals = sorted(
        zip(session_group["start_time"], session_group["stop_time"])
    )
    merged = []
    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    return merged

# Labeled windows creation
def label_windowing(annotations_df, window_requests,
                     target_taxonomy, distinguish_taxonomy=None,
                     exclude_tokens=None, clean_label=None,
                     unreviewd_tokens=False, umbral_artefacto=0.7, umbral_background=0.1):
    rows = []
    group_cols = ["Patient", "Session", "Section", "Montage", "NoChannels",
                  "Duration", "EDF"]
    window_size_sec = window_requests["window_size_sec"]
    stride_sec = window_requests["stride_sec"]
    win_start_inicial = window_requests.get("win_start", 0)
 
    for keys, session_group in annotations_df.groupby(group_cols):
        patient, session, section, montage, no_channels, duration, edf = keys
        n = 0

        while (win_start_inicial + n * stride_sec + window_size_sec) <= duration:
            win_start = win_start_inicial + n * stride_sec
            win_end = win_start + window_size_sec
 
            overlapping = session_group[
                (session_group["start_time"] < win_end) &
                (session_group["stop_time"] > win_start)
            ]
 
            raw_labels = list(overlapping["label"].unique())
            channels_involved = overlapping["channel"].nunique()
 
            label_spans = [
                {
                    "label": r.label,
                    "start_in_window": round(max(r.start_time, win_start) - win_start, 3),
                    "end_in_window": round(min(r.stop_time, win_end) - win_start, 3),
                }
                for r in overlapping.itertuples()
            ]
 
            all_tokens = set()
            for lbl in raw_labels:
                all_tokens |= split_compound_label(lbl)
 
            row = {
                "Patient": patient, "Session": session,
                "Section": section, "Montage": montage,
                "Window_size": window_size_sec, "stride": stride_sec,
                "Start": win_start, "end": win_end,
                "Raw_labels": raw_labels,
                "Label_spans": label_spans,
                "N_channels_annotated": channels_involved,
                "No_channels": no_channels,
                "Session_duration": duration,
                "EDF_path": edf,
            }
 
            row["is_clean"] = 0
            row["is_excluded_unreviewed"] = 0
 
            cobertura = {cat: 0.0 for cat in target_taxonomy}
            for span in label_spans:
                tokens = split_compound_label(span["label"])
                duracion = span["end_in_window"] - span["start_in_window"]
                for cat, keywords in target_taxonomy.items():
                    if tokens & keywords:
                        cobertura[cat] += duracion
            cobertura = {cat: min(v / window_size_sec, 1.0) for cat, v in cobertura.items()}
 
            for cat in target_taxonomy:
                row[f"coverage_{cat}"] = round(cobertura[cat], 3)
 
            cobertura_total = sum(cobertura.values())
 
            if cobertura_total <= umbral_background:
                row["is_clean_window"] = 1
                for cat in target_taxonomy:
                    row[cat] = 0
            elif any(v >= umbral_artefacto for v in cobertura.values()):
                row["is_clean_window"] = 0
                for cat, ratio in cobertura.items():
                    row[cat] = int(ratio >= umbral_artefacto)
            else:
                row["is_clean_window"] = 0
                for cat in target_taxonomy:
                    row[cat] = 0
 
            row["is_ambiguous"] = int(
                cobertura_total > umbral_background and
                not any(v >= umbral_artefacto for v in cobertura.values())
            )

            if row["is_clean_window"] == 1:
                margen = (umbral_background - cobertura_total) / umbral_background
                row["sample_weight"] = round(float(np.clip(margen, 0.2, 1.0)), 3)
            elif any(v >= umbral_artefacto for v in cobertura.values()):
                margen = (max(cobertura.values()) - umbral_artefacto) / (1 - umbral_artefacto)
                row["sample_weight"] = round(float(np.clip(0.4 + 0.6 * margen, 0.4, 1.0)), 3)
            else:
                row["sample_weight"] = 0.1
 
            row["distinguish"] = int(bool(all_tokens & distinguish_taxonomy)) if distinguish_taxonomy else 0
 
            genuine_cooccurrence = False
            for lbl in raw_labels:
                tokens = split_compound_label(lbl)
                categories_hit = {g for g, kws in target_taxonomy.items() if tokens & kws}
                if len(categories_hit) > 1:
                    genuine_cooccurrence = True
                    break
 
            row["genuine_cooccurrence"] = int(genuine_cooccurrence)
            categories_present = sum(row[g] for g in target_taxonomy) + row["distinguish"]
            row["weak_overlap"] = int(categories_present > 1 and not genuine_cooccurrence)
 
            row["is_unreviewed"] = int(len(all_tokens) == 0)
 
            if row["is_unreviewed"] and unreviewd_tokens:
                row["is_clean"] = 1
                row["is_unreviewed"] = 0
                row["is_excluded_unreviewed"] = 0
            elif row["is_unreviewed"] and not unreviewd_tokens:
                row["is_clean"] = 0
                row["is_unreviewed"] = 1
                row["is_excluded_unreviewed"] = 1
 
            row["is_excluded"] = int(bool(all_tokens & exclude_tokens)) if exclude_tokens else 0

            if clean_label is not None:
                has_target = any(row[g] for g in target_taxonomy)
                row["is_clean"] = int(
                    clean_label in all_tokens and not has_target and not row["distinguish"]
                )
 
            rows.append(row)
            n += 1
 
    return pd.DataFrame(rows)

# EEG signal windows creation (Dataset)
class eeg_window_dataset(utils.data.Dataset):
    def __init__(self, label_windowing_df, use_ica=True, ica_cache_dir="cache/ica"):
        self.df = label_windowing_df.reset_index(drop=True)
        self.use_ica = use_ica
        self.ica_cache_dir = ica_cache_dir
        self._cached_session = None                 # Loaded (patient, session)
        self._cache = {}

    def __len__(self):
        return len(self.df)

    def _load_session(self, patient, session, path_edf):
        key = (patient, session)
        if self._cached_session == key:
            return self._cache
        raw = load_raw_edf(path_edf, preloaD=True)
        signal = raw_data_preproccesing(raw)
        data = signal.get_data()
        sources_full = None
        if self.use_ica:
            ica, ic_labels, probs = get_or_compute_ica(signal, patient, session, self.ica_cache_dir)
            sources_full = ica.get_sources(signal).get_data()
        self._cache = {
            "data": data, 
            "sources_full": sources_full, 
            "sfreq": signal.info["sfreq"],
            "ch_names": signal.ch_names, }
        self._cached_session = key
        return self._cache

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        s = self._load_session(row.Patient, row.Session, row.EDF_path)
        start = int(round(row.Start * s["sfreq"]))
        end = int(round(row.end * s["sfreq"]))
        channel_window = tensor(s["data"][:, start:end], dtype=float32)
        return channel_window, tensor(row.is_clean_window, dtype=float32)

if __name__ == "__main__":
    from implementation.core.data_config import ARTIFACT_KEYWORDS, ARTIFACT_ADDITIONAL_TOKENS, BACKGROUND_LABEL, WINDOW_REQUESTS
    from implementation.core.data_loader import build_annotations_index
    
    database_corpus_patient = build_annotations_index("artifact", n_patients=5, max_sessions=1, paths=True)
    windowed_annotations_corpus_patient = label_windowing(database_corpus_patient, 
                                                          WINDOW_REQUESTS["rf_artifact_class"], 
                                                          ARTIFACT_KEYWORDS, 
                                                          unreviewd_tokens=True)

    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 120)  
    pd.set_option("display.expand_frame_repr", True)
    pd.set_option("display.max_colwidth", 25)
    print(windowed_annotations_corpus_patient.head(50))
    print(windowed_annotations_corpus_patient.shape)

    # Probar el Dataset
    dataset = eeg_window_dataset(windowed_annotations_corpus_patient, use_ica=False)
    print(f"Dataset length: {len(dataset)}")


    # Verification of cache function
    channel_window, target = dataset[0]
    print(f"channel_window shape: {channel_window.shape}, dtype: {channel_window.dtype}")
    print(f"target: {target}")
    
    ch_names = dataset._cache["ch_names"]
    sfreq = dataset._cache["sfreq"]

    data = channel_window.numpy()

    info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types="eeg")
    raw_window = mne.io.RawArray(data, info)

    raw_window.plot(scalings="auto", title=f"Ventana idx=0, target={target.item()}", block=True)

    #    print(f"Segunda ventana, misma sesión (debería reusar cache): {channel_window_2.shape}")
