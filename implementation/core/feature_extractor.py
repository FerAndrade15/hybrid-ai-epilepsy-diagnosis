""""
# File: features_extractor.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Agnostic functions for the extraction of diverse features:
- Temporal: RMS, variance, skewness, kurtosis, line_length, zero_crossing_rate, peak_to_peak
- Espectral: PSD, power per band, DWT, entropy
- ICA components dynamics and metadata extraction
"""
import pywt
import numpy as np
import pandas as pd
from pathlib import Path

from scipy.signal import welch, find_peaks
from scipy.stats import skew, kurtosis

from implementation.core.data_config import RAW_TO_TARGET, TUAR_Labels
from implementation.core.session_cache import get_or_compute_session
from implementation.models.ica_model import channel_contribution

def temporal_features(raw, ch_names, Mean=True, Variance=True, RMS=True,  Skewness=True, Kurtosis=True, Zero_crossing_rate=True, Hjorth=True, Line_length=True, Peak_to_peak=True):
    """
    Extraction of temporal features from a raw signal window.
    """
    eps = 1e-10 
    feats = {}

    # Statistic features 
    mean_ = np.mean(raw, axis=1) if Mean else np.full(raw.shape[0], np.nan)
    var_ = np.var(raw, axis=1) if Variance else np.full(raw.shape[0], np.nan)
    rms_ = np.sqrt(np.mean(raw**2, axis=1)) if RMS else np.full(raw.shape[0], np.nan)

    # Distribution descriptors
    skew_ = skew(raw, axis=1) if Skewness else np.full(raw.shape[0], np.nan)
    kurt_ = kurtosis(raw, axis=1) if Kurtosis else np.full(raw.shape[0], np.nan)
    
    # Complexity and temporal morphology
    d1 = np.diff(raw, axis=1)
    d2 = np.diff(raw, n=2, axis=1)
    zcr_ = np.mean(np.diff(np.sign(raw), axis=1) != 0, axis=1) if Zero_crossing_rate else np.full(raw.shape[0], np.nan)
    mobility = np.sqrt(np.var(d1, axis=1) / (np.var(raw, axis=1) + eps)) if Hjorth else np.full(raw.shape[0], np.nan)
    complexity = (np.sqrt(np.var(d2, axis=1) / (np.var(d1, axis=1) + eps)) / (mobility + eps)) if Hjorth else np.full(raw.shape[0], np.nan)
    line_len = np.sum(np.abs(np.diff(raw, axis=1)), axis=1) if Line_length else np.full(raw.shape[0], np.nan)
    p2p = (raw.max(axis=1) - raw.min(axis=1)) if Peak_to_peak else np.full(raw.shape[0], np.nan)

    for i, ch in enumerate(ch_names):
        if Mean: feats[f"{ch}_mean"] = mean_[i]
        if Variance: feats[f"{ch}_variance"] = var_[i]
        if RMS: feats[f"{ch}_rms"] = rms_[i]
        if Skewness: feats[f"{ch}_skewness"] = skew_[i]
        if Kurtosis: feats[f"{ch}_kurtosis"] = kurt_[i]
        if Zero_crossing_rate: feats[f"{ch}_zcr"] = zcr_[i]
        if Hjorth: feats[f"{ch}_hjorth_mobility"] = mobility[i]
        if Hjorth: feats[f"{ch}_hjorth_complexity"] = complexity[i]
        if Line_length: feats[f"{ch}_line_length"] = line_len[i]
        if Peak_to_peak: feats[f"{ch}_peak_to_peak"] = p2p[i]
    return feats

def frequency_features(raw, sfreq, ch_names, powerbands=True, Wavelets=True):
    """
    Extraction of frequency features from a raw signal window.
    """
    freqs, psd = welch(raw, sfreq, axis=1, nperseg=min(256, raw.shape[1]))
    feats = {}
    if powerbands:
        bands = {'delta': (0.5,4), 'theta': (4,8), 'alpha': (8,13), 'beta': (13,30), 'gamma': (30,45)}
        band_power = {}
        for name, (lo, hi) in bands.items():
            mask = (freqs >= lo) & (freqs <= hi)
            band_power[name] = psd[:, mask].mean(axis=1)
        for i, ch in enumerate(ch_names):
            for name in bands:
                feats[f"{ch}_{name}_power"] = band_power[name][i]
            feats[f"{ch}_ratio_high_low"] = band_power["gamma"][i]/(band_power["delta"][i] + 1e-10)

    if Wavelets:
        # Spectral entropy
        psd_norm = psd / (np.sum(psd, axis=1, keepdims=True) + 1e-10)
        spec_entropy = -np.sum(psd_norm * np.log2(psd_norm + 1e-10), axis=1)

        # Discrete Wavelet Transformation
        coeffs = pywt.wavedec(raw, 'db4', level=4, axis=1)
        names = ['A4', 'D4', 'D3', 'D2', 'D1']

        for i, ch in enumerate(ch_names):
            feats[f"{ch}_spectral_entropy"] = spec_entropy[i]
            for j, coef in enumerate(coeffs):
                feats[f"{ch}_dwt_energy_{names[j]}"] = np.sum(coef[i]**2)
                feats[f"{ch}_dwt_var_{names[j]}"] = np.var(coef[i])
    return feats

def components_dynamics(source_window, comp_names):
    """
    Extraction of dynamics features from ICA components, including:
    peak-to-mean ratio, peak position, number of peaks, and baseline shift.
    """
    feats = {}
    for i, name in enumerate(comp_names):
        sig = source_window[i]
        envelope = np.abs(sig)
        feats[f"{name}_peak_to_mean"] = envelope.max() / (envelope.mean() + 1e-8)
        feats[f"{name}_peak_position"] = np.argmax(envelope) / len(sig)
        threshold = envelope.mean() + 2*envelope.std()
        peaks, _ = find_peaks(envelope, height=threshold)
        feats[f"{name}_n_peaks"] = len(peaks)
        half = len(sig)//2
        feats[f"{name}_baseline_shift"] = abs(sig[:half].mean() - sig[half:].mean())
    return feats

def session_ica_metadata(comp_names, probs):
    """
    ICA components: Raw signal, category and probabilities per session
    """
    name_arr = np.array(comp_names)
    probs_arr = np.array(probs)
    target_labels = np.array([RAW_TO_TARGET.get(name, None) for name in name_arr])
    keep_idx = np.where(target_labels != None)[0]

    return{
        "raw_labels": name_arr,
        "probs": probs_arr,
        "target_labels": target_labels,
        "keep_idx": keep_idx
    }

def component_features_by_window(component_window, session_ica_metadata, mixing, ch_names, sfreq):
    """
    Returns a dataframe with a row per ICA component for the current window.
    """
    idx = session_ica_metadata["keep_idx"]
    if len(idx)==0:
        return pd.DataFrame()

    # Components windowing
    sub_signal = component_window[idx]
    provisional_names = [f"c{i}" for i in range(len(idx))]

    # Features generation
    tp_feat = temporal_features(sub_signal, provisional_names,)
    freq_feat = frequency_features(sub_signal, sfreq, provisional_names)
    dyn_feat = components_dynamics(sub_signal, provisional_names)
    contribution = channel_contribution(sub_signal, mixing[:,idx], ch_names, provisional_names)

    # Extraction of ICA session metadata
    raw_labels = session_ica_metadata["raw_labels"]
    target_labels = session_ica_metadata["target_labels"]
    probs = session_ica_metadata["probs"]

    # Data tabulation for future analysis
    rows = []
    for j, comp_idx in enumerate(idx):
        n = provisional_names[j]
        prefix = f"{n}_"

        row_data = {
            "ic_index": int(comp_idx),
            "ic_raw_label": raw_labels[comp_idx],
            "ic_target_label": target_labels[comp_idx],
            "ic_iclabel_prob": float(probs[comp_idx]),
        }

        for key, value in tp_feat.items():
            if key.startswith(prefix):
                row_data[key.replace(prefix, "ic_")] = value

        for key, value in dyn_feat.items():
            if key.startswith(prefix):
                new_key = key.replace(prefix, "ic_")
                row_data[new_key] = value

        for key, value in freq_feat.items():
            if key.startswith(prefix):
                new_key = key.replace(prefix, "ic_")
                row_data[new_key] = value

        row_data.update(contribution[n])
        rows.append(row_data)

    return pd.DataFrame(rows)

def iter_session_windows(label_windowing_df, use_ica=True, session_cache_dir="cache/sessions",ica_cache_dir="cache/ica"):
    """
    Window generator with added categories.
    """
    for (patient, session, path_edf), group in label_windowing_df.groupby(
        ["Patient", "Session", "EDF_path"]
    ):
        try:
            s = get_or_compute_session(patient, session, path_edf,
                                       cache_dir=session_cache_dir,
                                       ica_cache_dir=ica_cache_dir,
                                       use_ica=use_ica)
        except RuntimeError as e:
            print(f"[SKIP] Session {patient}_{session} discarted by ICA error {e}")
            continue

        data = s["data"]
        sfreq = s["sfreq"]
        ch_names = s["ch_names"]

        ic_components_map = None
        if use_ica:
            ic_components_map = session_ica_metadata(s["comp_names"], s["probs"])

        for row in group.itertuples():
            start = int(round(row.Start*sfreq))
            end = int(round(row.end * sfreq))

            if end > data.shape[1]:
                continue

            tuar_metadata = {f"tuar_{col}":getattr(row, col, 0) for col in TUAR_Labels if hasattr(row, col)}
            window_paquet = {
                "Patient": patient,
                "Session": session,
                "Start": row.Start,
                "End": row.end,
                "split": getattr(row,  "split", None),
                "channel_window": data[:, start:end],
                "ch_names": ch_names,
                "sfreq": sfreq,
            }
            window_paquet.update(tuar_metadata)

            if use_ica:
                window_paquet.update({
                    "component_window": s["sources_full"][:, start:end],
                    "mixing": s["mixing"],
                    "ic_map": ic_components_map,
                })

            yield window_paquet

def build_feature_dataset(label_windowing_df, use_ica=True, ica_cache_dir="cache/ica", session_cache_dir="cache/sessions"):
    """
    Returns signal + ICA features added by ICLabel cathegories.
    """    
    rows = []

    for w in iter_session_windows(label_windowing_df, use_ica, session_cache_dir, ica_cache_dir):
        channel_feats = {}
        channel_feats.update(
            temporal_features(
                w["channel_window"], w["ch_names"],
                Variance=True, Line_length=True, Peak_to_peak=True,
                Mean=False, RMS=False, Skewness=False, Kurtosis=False, 
                Zero_crossing_rate=False, Hjorth=False
                )
            )

        if use_ica:
            comp_df = component_features_by_window(
                w["component_window"],
                w["ic_map"],
                w["mixing"],
                w["ch_names"],
                w["sfreq"]
            )
            if comp_df.empty:
                continue

            add_cols = {}
            add_cols.update(channel_feats)
            add_cols["Patient"] = w["Patient"]
            add_cols["Session"] = w["Session"]
            add_cols["Start"] = w["Start"]
            add_cols["split"] = w.get("split")

            for key, value in w.items():
                if key.startswith("tuar_"):
                    add_cols[key] = value

            add_cols = pd.DataFrame([add_cols]*len(comp_df))
            comp_df.reset_index(drop=True, inplace=True)
            comp_df = pd.concat([comp_df, add_cols], axis=1)
            rows.append(comp_df)

    return pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()

def build_rf_dataset(long_df, target_artifact, negative_label="clean", features_dir="features"):
    """
    Returs the categories according to the target:
    -   "eye"
    -   "muscle"
    -   "non_physiological"
    -   "tuar_labels" (genuine_cooccurrence, weak_overlap, clean...)
    """
    # Clean ambiguous windows
    clean_df = long_df[long_df["tuar_is_ambiguous"] == 0].copy()
    subset = clean_df.copy()

    # Confirmation of positive target
    tuar_column = f"tuar_{target_artifact}"
    comp = subset["ic_target_label"] == target_artifact
    ocurrence = subset[tuar_column] == 1

    subset["is_positive"] = (subset[tuar_column] == 1).astype(int)

    output_path = Path(features_dir) / f"rf_dataset_{target_artifact}.parquet"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    subset.to_parquet(output_path, index=False)

    return subset

if __name__ == "__main__":

    # Data integration libraries / project modules
    from implementation.core.data_config import ARTIFACT_KEYWORDS, WINDOW_REQUESTS_ARTIFACTS, RATIOS, VERSION
    from implementation.core.data_loader import build_annotations_index, find_project_root
    from implementation.core.windowing import label_windowing
    from implementation.core.data_splitter import get_or_compute_split

    # Data visualization and search libraries
    from IPython.display import display

    BASE_DIR = find_project_root()
    CORPUS_OUTPUTS_DIR = BASE_DIR / "outputs" / "artifact"
    ICA_CACHE_DIR = CORPUS_OUTPUTS_DIR / "individual_tests" / "cache" / "ica"
    SESSION_CACHE_DIR = CORPUS_OUTPUTS_DIR / "individual_tests" / "cache" / "sessions"
    FEATURES_DIR = CORPUS_OUTPUTS_DIR / "individual_tests"/ "features"
    SPLIT_CACHE_DIR = CORPUS_OUTPUTS_DIR / "individual_tests" / "splits"

    for d in (FEATURES_DIR, ICA_CACHE_DIR, SPLIT_CACHE_DIR):
        d.mkdir(parents=True, exist_ok=True)

    print("Loading 25 artifact patients, 1 sessions per patient for testing...")
    database_corpus_patient = build_annotations_index("artifact", n_patients=25, max_sessions=1, paths=True)
    display(database_corpus_patient.head(5))

    print("Generating windows...")
    windowed_annotations_corpus_patient = label_windowing(
                    database_corpus_patient, WINDOW_REQUESTS_ARTIFACTS["eye"],
                    ARTIFACT_KEYWORDS, unreviewd_tokens=True,
                )
    display(windowed_annotations_corpus_patient.head(5))

    windowed_annotated_splited, assignment, report = get_or_compute_split(windowed_annotations_corpus_patient, target_taxonomy=ARTIFACT_KEYWORDS, dataset_division_dir=str(SPLIT_CACHE_DIR), ratios=RATIOS, version=VERSION)

    print("Starting features extraction from channels and ICA components...")
    featured_windows = build_feature_dataset(windowed_annotated_splited, use_ica=True, ica_cache_dir=str(ICA_CACHE_DIR), session_cache_dir=str(SESSION_CACHE_DIR))
    display(featured_windows.head(5))
    print(featured_windows.columns.tolist())

    if not featured_windows.empty:
        print("Successful features extraction")
        rf_features_dataset = build_rf_dataset(featured_windows, artefact_target="eye", features_dir=str(FEATURES_DIR))
        print(rf_features_dataset.head(5))
        print("Positive count:")
        print(rf_features_dataset["is_positive"].value_counts())
    else:
        print("Resulting empty dataset")