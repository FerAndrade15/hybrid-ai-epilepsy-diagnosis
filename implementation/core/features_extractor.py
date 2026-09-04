""""
# File: features_extractor.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Agnostic functions for the extraction of diverse features:
- Temporal: RMS, variance, skewness, kurtosis, line_length, zero_crossing_rate, peak_to_peak
- Espectral: PSD, power per band, DWT, entropy

"""
import pywt
import numpy as np
import pandas as pd

from scipy.signal import welch, find_peaks
from scipy.stats import skew, kurtosis

from implementation.core.data_config import RAW_TO_TARGET, TUAR_Labels
from implementation.core.session_cache import get_or_compute_session
from implementation.core.preprocessing import load_raw_edf, raw_data_preproccesing
from implementation.models.ica_model import get_or_compute_ica, channel_contribution

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

def iter_session_windows(label_windowing_df, use_ica=True, ica_cache_dir="cache/ica"):
    """
    Window generator with added categories.
    """
    for (patient, session, path_edf), group in label_windowing_df.groupby(
        ["Patient", "Session", "EDF_path"]
    ):
        try:
            s = get_or_compute_session(patient, session, path_edf,
                                       cache_dir=session_cache_dir,)
        raw = load_raw_edf(path_edf, preloaD=True)
        signal = raw_data_preproccesing(raw)
        sfreq = signal.info["sfreq"]
        ch_names = signal.ch_names
        data = signal.get_data()

        if use_ica:
            try: 
                ica, ic_labels, probs = get_or_compute_ica(signal, patient, session, ica_cache_dir)
                comp_names = ic_labels["labels"]
                mixing = ica.get_components()
                sources_full = ica.get_sources(signal).get_data()
            except RuntimeError as e:
                del raw, signal, data
                print(f"[SKIP] Session {patient}_{session} discarded by ICA error {e}")
                continue

        # General ICA components characteristics
        ic_components_map = session_ica_metadata(comp_names, probs)

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
                "channel_window": data[:, start:end],
                "component_window": sources_full[:, start:end],
                "ch_names": ch_names,
                "mixing": mixing,
                "ic_map": ic_components_map,
                "sfreq": sfreq,
            }
            window_paquet.update(tuar_metadata)

            yield window_paquet
        del raw, signal, data, ica, sources_full
        

def build_feature_dataset(label_windowing_df, use_ica=True, ica_cache_dir="cache/ica"):
    """
    Returns signal + ICA features added by ICLabel cathegories.
    """        
    rows = []

    for w in iter_session_windows(label_windowing_df, use_ica, ica_cache_dir):
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

            for key, value in w.items():
                if key.startswith("tuar_"):
                    add_cols[key] = value

            add_cols = pd.DataFrame([add_cols]*len(comp_df))
            comp_df.reset_index(drop=True, inplace=True)
            comp_df = pd.concat([comp_df, add_cols], axis=1)
            rows.append(comp_df)

    return pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()

def build_rf_dataset(long_df, artefact_target, negative_label="clean"):
    """
    Returs the categories according to the target:
    -   "eye"
    -   "muscle"
    -   "non_physiological"
    -   "brain"
    """
    # Clean ambiguous windows
    clean_df = long_df[long_df["tuar_is_ambiguous"]==0].copy()
    subset = clean_df.copy()

    # Confirmation of positive target
    tuar_column = f"tuar_{artefact_target}"
    comp = subset["ic_target_label"] == artefact_target
    ocurrence = subset[tuar_column] == 1

    subset["is_positive"] = (comp & ocurrence).astype(int)
    return subset

if __name__ == "__main__":

    from implementation.core.data_loader import build_annotations_index
    from implementation.core.data_config import ARTIFACT_KEYWORDS, WINDOW_REQUESTS
    from implementation.core.windowing import label_windowing
    from IPython.display import display
    from pathlib import Path

    # Location of project path to prevent rupture due to cmd running
    def find_project_root(marker="implementation"):
        current = Path(__file__).resolve()
        for parent in current.parents:
            if (parent / marker).is_dir():
                return parent
        raise RuntimeError(f"Main folder path not found (looking for '{marker}' folder)")

    BASE_DIR = find_project_root()
    CORPUS_OUTPUTS_DIR = BASE_DIR / "outputs" / "artifact"
    ICA_CACHE_DIR = CORPUS_OUTPUTS_DIR / "features_extractor_test" / "cache"
    FEATURES_DIR = CORPUS_OUTPUTS_DIR / "features_extractor_test"/ "features"
    for d in (FEATURES_DIR, ICA_CACHE_DIR):
        d.mkdir(parents=True, exist_ok=True)

    print("Loading 2 artifact session for testing...")
    database_corpus_patient = build_annotations_index("artifact", n_patients=1, max_sessions=2, paths=True)
    display(database_corpus_patient.head(5))

    print("Generating windows...")
    windowed_df = label_windowing(
                    database_corpus_patient, WINDOW_REQUESTS["rf_artifact_class"],
                    ARTIFACT_KEYWORDS, unreviewd_tokens=True,
                )
    display(windowed_df.head(5))

    print("Starting features extraction from channels and ICA components...")

    featured_windows = build_feature_dataset(windowed_df, use_ica=True, ica_cache_dir=str(ICA_CACHE_DIR))
    display(featured_windows.head(5))
    print(featured_windows.columns.tolist())

    if not featured_windows.empty:
        print("Successful features extraction")
        rf_features_dataset = build_rf_dataset(featured_windows, artefact_target="eye")
        print(rf_features_dataset.head(5))
        print("Positive count:")
        print(rf_features_dataset["is_positive"].value_counts())
    else:
        print("Resulting empty dataset")