"""
# File: windowing.py
# Project: Trabajo de graduación
# Author: María Fernanda Andrade Recinos

Corpus-agnostic windowing for continuous annotations into fixed-size
sections and tags according to a given taxonomy with all the passed in data.
"""
# windowing.py

# Data integration libraries
import numpy as np
import pandas as pd
import os,  hashlib, json
from pathlib import Path
from torch import utils, tensor, float32

from src.core.data_config import LABEL_VERSION, KEYS
from src.core.data_loader import load_raw_edf
from src.core.preprocessing import raw_data_preproccesing, channel_standard_nomenclature
from src.models.ica_model import get_or_compute_ica

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

def overall_interval(intv):
    total, cs, ce = 0.0, None, None
    for a, b in sorted(intv):
        if ce is None or a > ce: 
            if ce is not None: total += ce - cs
            cs, ce = a, b
        else:
            ce = max(ce, b)
    return total + (ce - cs if ce is not None else 0.0)

# Labeled windows creation
def label_windowing(annotations_df, window_requests,
                     target_taxonomy, distinguish_taxonomy=None,
                     exclude_tokens=None, clean_label=None,
                     unreviewed_tokens=False, umbral_artefacto=0.7, umbral_background=0.1):
    rows = []
    group_cols = ["Patient", "Session", "Section", "Montage", "NoChannels",
                  "Duration", "EDF", "Partition"]
    window_size_sec = window_requests["window_size_sec"]
    stride_sec = window_requests["stride_sec"]
    win_start_inicial = window_requests.get("win_start", 0)
 
    for keys, session_group in annotations_df.groupby(group_cols, dropna=False):
        patient, session, section, montage, no_channels, duration, edf, partition = keys
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
                "Patient": patient, 
                "Session": session,
                "Section": section, 
                "Montage": montage,
                "Partition": partition,
                "Window_size": window_size_sec, 
                "stride": stride_sec,
                "Start": win_start, 
                "end": win_end,
                "Raw_labels": raw_labels,
                "Label_spans": label_spans,
                "N_channels_annotated": channels_involved,
                "No_channels": no_channels,
                "Session_duration": duration,
                "EDF_path": edf,
            }
 
            row["is_clean"] = 0
            row["is_excluded_unreviewed"] = 0
 
            intervals  = {cat: [] for cat in target_taxonomy}
            monopolar_channels_by_cat = {cat: set() for cat in target_taxonomy}
            bipolar_channels_by_cat = {cat: set() for cat in target_taxonomy}

            for span in label_spans:
                tokens = split_compound_label(span["label"])
                interval = (span["end_in_window"],span["start_in_window"])
                for cat, keywords in target_taxonomy.items():
                    if tokens & keywords:
                        intervals[cat].append(interval)
                        matching_rows = overlapping[overlapping["label"]==span["label"]]
                        ch_names = [name.split("-") for name in matching_rows["channel"].tolist()]
                        rename_map = [
                            new_name1 + "-" + new_name2 
                            for ch in ch_names 
                            if len(ch) == 2
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
                cat: min(overall_interval(intervals)/window_size_sec, 1.0) 
                for cat, interval in intervals.items()
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
 
            if row["is_unreviewed"] and unreviewed_tokens:
                row["is_clean"] = 1
                row["is_unreviewed"] = 0
                row["is_excluded_unreviewed"] = 0
            elif row["is_unreviewed"] and not unreviewed_tokens:
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
        signal = raw_data_preproccesing(raw, bipolar_montage=True)
        data = signal.get_data()
        sources_full = None
        if self.use_ica:
            ica, ic_labels, probs = get_or_compute_ica(signal, patient, session, cache_dir=self.ica_cache_dir)
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
    from src.core.data_config import ARTIFACT_KEYWORDS, WINDOW_REQUESTS_ARTIFACTS
    from src.core.data_loader import build_annotations_index

    def union_len(iv):
        total, cs, ce = 0.0, None, None
        for a, b in sorted(iv):
            if ce is None or a > ce:
                if ce is not None: total += ce - cs
                cs, ce = a, b
            else:
                ce = max(ce, b)
        return total + (ce - cs if ce is not None else 0.0)

    ann = build_annotations_index("artifact", n_patients=3, max_sessions=1, paths=True)
    key = ["Patient", "Session", "Section"]
    n_sessions = ann.groupby(key).ngroups
    durations = ann.drop_duplicates(key)["Duration"]
    cats = list(ARTIFACT_KEYWORDS)

    for artifact, req in WINDOW_REQUESTS_ARTIFACTS.items():
        size, stride = req["window_size_sec"], req["stride_sec"]
        w = label_windowing(ann, req, ARTIFACT_KEYWORDS, unreviewed_tokens=True)
        print(f"\n=== {artifact}: ventana {size}s / paso {stride}s → {len(w)} ventanas ===")

        # 1) Integridad
        assert w[key].notna().all().all(), "hay Patient/Session/Section nulos"
        assert w.groupby(key).ngroups == n_sessions, "se perdieron sesiones (usa dropna=False en el groupby)"
        expected = sum(int((d - size) // stride) + 1 for d in durations)
        assert abs(len(w) - expected) <= n_sessions, (len(w), expected)

        # 2) Clases exclusivas: limpia XOR ambigua XOR artefacto
        total = w["is_clean_window"] + w["is_ambiguous"] + w[cats].max(axis=1)
        assert (total == 1).all(), w[total != 1][["Start", *cats, "is_clean_window", "is_ambiguous"]].head()
        assert w["sample_weight"].between(0.1, 1.0).all()

        # 3) Conteos
        print(w[["is_clean_window", "is_ambiguous", *cats]].sum().to_string())

        # 4) Canales mapeados en positivas
        for cat in cats:
            pos = w[w[cat] == 1]
            empty = int((pos[f"monopolar_channels_{cat}"].map(len) == 0).sum())
            print(f"  {cat}: {len(pos)} positivas, {empty} sin canales monopolares mapeados")

        # 5) Diagnóstico de cobertura: suma por canal (actual) vs unión temporal, umbral 0.7
        for cat, kws in ARTIFACT_KEYWORDS.items():
            changes = 0
            for spans in w["Label_spans"]:
                iv = [(x["start_in_window"], x["end_in_window"]) for x in spans
                      if split_compound_label(x["label"]) & kws]
                if iv:
                    summed = min(sum(e - s for s, e in iv) / size, 1.0)
                    changes += (summed >= 0.7) != (union_len(iv) / size >= 0.7)
            print(f"  {cat}: ventanas cuya etiqueta positiva cambiaría con la unión temporal: {changes}")
    print("\n[OK] windowing")