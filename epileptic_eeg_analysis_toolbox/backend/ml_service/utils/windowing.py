"""
# File: windowing.py
# Project: Trabajo de graduación
# Author: María Fernanda Andrade Recinos

Corpus-agnostic windowing for continuous annotations into fixed-size
sections and tags according to a given taxonomy with all the passed in data.
"""
# Data integration libraries
import numpy as np
import pandas as pd
import os,  hashlib, json
from pathlib import Path
from typing import List, Dict, Optional, Any, Tuple

# Modules required functions
from config.data_config import SFREQ, ARTIFACT_KEYWORDS, KEYS
from backend.ml_service.utils.preprocessing import channel_standard_nomenclature

# Functions if required from the ICA module application for AI
try:
    from src.core.data_config import LABEL_VERSION
except ImportError:
    pass

# -----------------------------------------------------------------------------------
# Functions for raw signal windowing and labeling according to a taxonomy
# -----------------------------------------------------------------------------------
def slice_raw_into_windows(
        raw: Any, 
        window_size_sec: float = 1.0,
        stride_sec: float = 1.0,
        start_time: float = 0.0,
        end_time: Optional[float] = None
    ) -> List[Dict[str, Any]]:
    """
    Slice a raw signal into fixed-size windows with a given stride.
    Returns metadata and signal matrix for each window.
    """
    sfreq = float(raw.info['sfreq'])
    total_duration= float(raw.times[-1])

    if end_time is None or end_time > total_duration:
        end_time = total_duration

    window_samples = int(round(window_size_sec * sfreq))
    stride_samples = int(round(stride_sec * sfreq))

    start_sample = int(round(start_time * sfreq))
    stop_sample = int(round(end_time * sfreq))

    # Complete data matrix
    data, _ = raw[:, start_sample:stop_sample]

    windows = []
    n_total_samples = data.shape[1]
    current_idx = 0

    while current_idx + window_samples <= n_total_samples:
        win_data = data[:, current_idx:current_idx + window_samples]
        t_start = round((start_sample + current_idx) / sfreq, 3)
        t_end = round((start_sample + current_idx + window_samples) / sfreq, 3)

        windows.append({
            "start": t_start,
            "end": t_end,
            "window_size": window_size_sec,
            "stride": stride_sec,
            "data": win_data,
            "channels": list(raw.ch_names),
            "sfreq": sfreq
        })
        current_idx += stride_samples
    
    return windows

# ---------------------------------------------------------------------------------
# Functions for labeling windows according to a taxonomy and annotations (TUH)
# ---------------------------------------------------------------------------------
# Process to analyze data
def split_compound_label(label:str) -> set:
    return set(str(label).lower().split("_"))

# Merge annotations for a continous range
def merge_annotated_ranges(session_group: pd.DataFrame) -> List[Tuple[float, float]]:
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

def overall_interval(intervals: List[Tuple[float, float]]) -> float:
    total, cur_s, cur_e = 0.0, None, None
    for s, e in sorted(intervals):
        if e <= s:
            continue
        if cur_e is None or s > cur_e:
            if cur_e is not None:
                total += cur_e - cur_s
            cur_s, cur_e = s, e
        else:
            cur_e = max(cur_e, e)
    if cur_e is not None:
        total += cur_e - cur_s
    return total

# Labeled windows creation
def label_windowing(
        annotations_df: pd.DataFrame, 
        window_requests: Dict[str, Any],
        target_taxonomy: Dict[str, set],
        distinguish_taxonomy: Optional[set] = None,
        exclude_tokens: Optional[set] = None,
        clean_label: Optional[str] = None,
        unreviewed_tokens: bool = False,
        umbral_artefacto: float = 0.7,
        umbral_background: float = 0.1
    ) -> pd.DataFrame:
    """
    Segmentation with taxonomy-based labeling of continuous annotations into fixed-size windows
    according to the given parameters and thresholds.
    """
    rows = []
    group_cols = [
        col for col in ["Patient", "Session", "Section", "Montage", "NoChannels", "Duration", "EDF", "Partition"]
        if col in annotations_df.columns
    ]
    window_size_sec = window_requests["window_size_sec"]
    stride_sec = window_requests["stride_sec"]
    win_start_inicial = window_requests.get("win_start", 0)
 
    for keys, session_group in annotations_df.groupby(group_cols, dropna=False):
        key_dict = dict(zip(group_cols, keys if isinstance(keys, tuple) else [keys]))
        duration = key_dict.get("Duration", session_group["stop_time"].max())
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
                **key_dict,
                "Window_size": window_size_sec, 
                "stride": stride_sec,
                "Start": win_start, 
                "end": win_end,
                "Raw_labels": raw_labels,
                "Label_spans": label_spans,
                "N_channels_annotated": channels_involved,
            }
 
            intervals  = {cat: [] for cat in target_taxonomy}
            monopolar_channels_by_cat = {cat: set() for cat in target_taxonomy}
            bipolar_channels_by_cat = {cat: set() for cat in target_taxonomy}

            for span in label_spans:
                tokens = split_compound_label(span["label"])
                interval = (span["start_in_window"], span["end_in_window"])
                for cat, keywords in target_taxonomy.items():
                    if tokens & keywords:
                        intervals[cat].append(interval)
                        matching_rows = overlapping[overlapping["label"]==span["label"]]
                        ch_names = [name.split("-") for name in matching_rows["channel"].tolist()]
                        rename_map = [
                            f"{new_name1}-{new_name2}"
                            for ch in ch_names if len(ch) == 2
                            if (new_name1 := channel_standard_nomenclature(ch[0])) is not None
                            if (new_name2 := channel_standard_nomenclature(ch[1])) is not None
                        ]
                        bipolar_channels_by_cat[cat].update(rename_map)

                        ch_names_flat = [item for sublist in ch_names for item in sublist]
                        rename_map_mono = [
                            new_name 
                            for ch in ch_names_flat 
                            if (new_name := channel_standard_nomenclature(ch)) is not None
                        ] 
                        monopolar_channels_by_cat[cat].update(rename_map_mono)
                        
            coverage = {
                cat: min(overall_interval(iv)/window_size_sec, 1.0) 
                for cat, iv in intervals.items()
            }
 
            for cat in target_taxonomy:
                row[f"coverage_{cat}"] = round(coverage[cat], 3)
                row[f"monopolar_channels_{cat}"] = sorted(monopolar_channels_by_cat[cat])
                row[f"bipolar_channels_{cat}"] = sorted(bipolar_channels_by_cat[cat])
 
            coverage_total = sum(coverage.values())
 
            if coverage_total <= umbral_background:
                row["is_clean_window"] = 1
                for cat in target_taxonomy:
                    row[cat] = 0
            elif any(v >= umbral_artefacto for v in coverage.values()):
                row["is_clean_window"] = 0
                for cat, ratio in coverage.items():
                    row[cat] = int(ratio >= umbral_artefacto)
            else:
                row["is_clean_window"] = 0
                for cat in target_taxonomy:
                    row[cat] = 0
 
            row["is_ambiguous"] = int(
                coverage_total > umbral_background and
                not any(v >= umbral_artefacto for v in coverage.values())
            )

            if row["is_clean_window"] == 1:
                margen = (umbral_background - coverage_total) / umbral_background
                row["sample_weight"] = round(float(np.clip(margen, 0.2, 1.0)), 3)
            elif any(v >= umbral_artefacto for v in coverage.values()):
                margen = (max(coverage.values()) - umbral_artefacto) / (1 - umbral_artefacto)
                row["sample_weight"] = round(float(np.clip(0.4 + 0.6 * margen, 0.4, 1.0)), 3)
            else:
                row["sample_weight"] = 0.1
 
            row["distinguish"] = int(bool(all_tokens & distinguish_taxonomy)) if distinguish_taxonomy else 0

            # Coocurrence and exclusions
            categories_hit = {g for g, kws in target_taxonomy.items() if all_tokens & kws}
            row["genuine_cooccurrence"] = int(len(categories_hit) > 1)
            categories_present = sum(row[g] for g in target_taxonomy) + row["distinguish"]
            row["weak_overlap"] = int(categories_present > 1 and not row["genuine_cooccurrence"])

            row["is_unreviewed"] = int(len(all_tokens)==0)
            if row["is_unreviewed"] and unreviewed_tokens:
                row["is_clean_window"] = 1
                row["is_unreviewed"] = 0

            row["is_excluded"] = int(bool(all_tokens & exclude_tokens)) if exclude_tokens else 0    
            if clean_label is not None:
                has_target = any(row[g] for g in target_taxonomy)
                row["is_clean_window"] = int(
                    clean_label in all_tokens and not has_target and not row["distinguish"]
                )

            rows.append(row)
            n += 1

    return pd.DataFrame(rows)

def file_keys(df, keys=KEYS):
    return set(map(tuple, df[keys].astype(str).drop_duplicates().itertuples(index=False)))

def list_data(w):
    for c in w.columns:
        if c.startswith("monopolar_channels") or c.startswith("bipolar_channels"):
            w[c] = w[c].map(lambda x: list(x) if x is not None else [])
    return w

def get_or_build_windows(   annotations_df, window, taxonomy, cache_dir, unreviewed_tokens=True,
                            artifact_umbral=0.7, background_umbral=0.1, refresh=True):
    tax = hashlib.md5(json.dumps({k: sorted(v) for k, v in sorted(taxonomy.items())}).encode()).hexdigest()[:6]
    path = Path(cache_dir) / (  f"windows_w{window['window_size_sec']}_s{window['stride_sec']}"
                                f"_ua{artifact_umbral}_ub{background_umbral}_ur{unreviewed_tokens}"
                                f"_{tax}_L{LABEL_VERSION}.parquet"
                            )
    
    if path.exists() and not refresh:
        w = pd.read_parquet(path)
        if file_keys(w) == file_keys(annotations_df):
            print(f"[INFO] Windows loaded from cache: {path.name} ({len(w)} rows)")
            return list_data(w)
        print(f"[NOTICE] {path.name} not found in current annotations")
    
    w = label_windowing(annotations_df, window, taxonomy, unreviewed_tokens=unreviewed_tokens,
                        umbral_artefacto=artifact_umbral, umbral_background=background_umbral)
    w = w.drop(columns=["Label_spans"])
    w["Raw_labels"] = w["Raw_labels"].map("|".join)
    w["EDF_path"] = w["EDF_path"].astype(str)   

    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    w.to_parquet(tmp, index=False)
    os.replace(tmp, path)

    return w

# General testing for windowing functions
if __name__ == "__main__":
    print("Module windowing.py loaded successfully.")