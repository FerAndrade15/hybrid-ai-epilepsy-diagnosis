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

from implementation.core.data_config import ICLABEL_CATEGORIES, ICLABEL_TO_TARGET
from implementation.core.preprocessing import load_raw_edf, raw_data_preproccesing
from implementation.models.ica_model import get_or_compute_ica, channel_contribution

def temporal_features(raw, ch_names, Mean=True, Variance=True, RMS=True,  Skewness=True, Kurtosis=True, Zero_crossing_rate=True, Hjorth=True, Line_length=True, Peak_to_peak=True):
    #
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
        feats[f"{ch}_mean"] = mean_[i]
        feats[f"{ch}_variance"] = var_[i]
        feats[f"{ch}_rms"] = rms_[i]
        feats[f"{ch}_skewness"] = skew_[i]
        feats[f"{ch}_kurtosis"] = kurt_[i]
        feats[f"{ch}_zcr"] = zcr_[i]
        feats[f"{ch}_hjorth_mobility"] = mobility[i]
        feats[f"{ch}_hjorth_complexity"] = complexity[i]
        feats[f"{ch}_line_length"] = line_len[i]
        feats[f"{ch}_peak_to_peak"] = p2p[i]

    return feats

def frequency_features(raw, sfreq, ch_names, powerbands=True, Wavelets=True):
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

def _ica_metadata_by_session(source_window, comp_names, probs, ICLABEL_CATEGORIES):
    """
    Index and probabilities per cathegory calculated and saved per session.
    """
    feats = {}
    name_arr = np.array(comp_names)
    probs_arr = np.array(probs)
    label_arr = np.array()
    for cat in ICLABEL_CATEGORIES:
        safe = cat.replace(" ", "_")
        equivalent = next((key for key, values in ICLABEL_TO_TARGET.items() if safe in values), None)
        idx = np.where(name_arr==cat)[0]

        if equivalent != None:
            sub_signal = source_window[idx]




def _aggregate_by_iclabel_category(source_window, comp_names, mixing, ch_names, probs):
    """
    Adds statistics values per ICLabel category, fixed column agnostiv of ICs number.
    """
    feats = {}
    name_arr = np.array(comp_names)
    probs_arr = np.array(probs)
    print("\n\t Componentes", name_arr)
    print("\n\t Probabilities", probs_arr)

    for cat in ICLABEL_CATEGORIES:
        safe = cat.replace(" ", "_")
        equivalent = next((key for key, values in ICLABEL_TO_TARGET.items() if safe in values), None)
        idx = np.where(name_arr == cat)[0]
        feats[f"n_ic_{safe}"] = len(idx)

        if len(idx) == 0:
            feats[f"{safe}_max_iclabel_prob"] = 0.0
            feats[f"{safe}_line_length_max"] = 0.0
            feats[f"{safe}_peak_to_mean_max"] = 0.0
            feats[f"{safe}_baseline_shift_max"] = 0.0
            feats[f"{safe}_contribution_mean"] = 0.0
            continue
            
        sub_signal = source_window[idx]
        dummy_names = [f"c{i}" for i in range(len(idx))]

        if equivalent != None:
            print("SAFE", safe, "EQUIV", equivalent, "IDX", idx, "FEATS", feats)
            print("SUBSIGNAL", sub_signal, "DUMMY", dummy_names)

        t = temporal_features(sub_signal, dummy_names)
        dyn = components_dynamics(sub_signal, dummy_names)
        contrib = channel_contribution(sub_signal, mixing[:, idx], ch_names, dummy_names)

        feats[f"{safe}_max_iclabel_prob"] = float(probs_arr[idx].max())
        feats[f"{safe}_line_length_max"] = max(t[f"{n}_line_length"] for n in dummy_names)
        feats[f"{safe}_peak_to_mean_max"] = max(dyn[f"{n}_peak_to_mean"] for n in dummy_names)
        feats[f"{safe}_baseline_shift_max"] = max(dyn[f"{n}_baseline_shift"] for n in dummy_names)
        feats[f"{safe}_contribution_mean"] = float(np.mean(list(contrib.values())))

    return feats


def iter_session_windows(label_windowing_df, use_ica=True, ica_cache_dir="cache/ica"):
    """
    Window generator with added categories.
    """
    for (patient, session, path_edf), group in label_windowing_df.groupby(
        ["Patient", "Session", "EDF_path"]
    ):
        raw = load_raw_edf(path_edf, preloaD=True)
        signal = raw_data_preproccesing(raw)
        sfreq = signal.info["sfreq"]
        ch_names = signal.ch_names
        data = signal.get_data()

        comp_names = mixing = sources_full = probs = None
        if use_ica:
            try: 
                ica, ic_labels, probs = get_or_compute_ica(signal, patient, session, ica_cache_dir)
                comp_names = ic_labels["labels"]
                mixing = ica.get_components()
                sources_full = ica.get_sources(signal).get_data()
            except RuntimeError as e:
                print(f"[SKIP] Session {patient}_{session} discarded by ICA error {e}")
                continue

        for row in group.itertuples():
            start = int(round(row.Start * sfreq))
            end = int(round(row.end * sfreq))

            yield {
                "Patient": patient, "Session": session, 
                "Start": row.Start, "End": row.end,
                "channel_window": data[:, start:end],
                "component_window": sources_full[:, start:end] if use_ica else None,
                "ch_names": ch_names, "comp_names": comp_names,
                "mixing": mixing, "probs": probs, "sfreq": sfreq,
            }

        del raw, signal, data
        if use_ica:
            del ica, sources_full


def build_feature_dataset(label_windowing_df, use_ica=True, ica_cache_dir="cache/ica"):
    """
    Returns signal + ICA features added by ICLabel cathegories.
    """
    rows = []
    for w in iter_session_windows(label_windowing_df, use_ica, ica_cache_dir):
        feats = {}
        feats.update(temporal_features(w["channel_window"], w["ch_names"]))
        feats.update(frequency_features(w["channel_window"], w["sfreq"], w["ch_names"]))
        if use_ica:
            feats.update(_aggregate_by_iclabel_category(
                w["component_window"], w["comp_names"], w["mixing"], w["ch_names"], w["probs"]
            ))

        feats["Patient"] = w["Patient"]; feats["Session"] = w["Session"]
        feats["Start"] = w["Start"]
        rows.append(feats)

    return pd.DataFrame(rows)

if __name__ == "__main__":

    from implementation.core.data_loader import build_annotations_index
    from implementation.core.data_config import ICLABEL_CATEGORIES, ARTIFACT_KEYWORDS, WINDOW_REQUESTS
    from implementation.core.windowing import label_windowing
    from IPython.display import display
    from pathlib import Path

    # Location of project path to prevent rupture due to cmd running
    def find_project_root(marker="implementation"):
        current = Path(__file__).resolve()
        for parent in current.parents:
            if (parent / marker).is_dir():
                return parent
        raise RuntimeError(f"No se encontró la raíz del proyecto (buscando carpeta '{marker}')")

    BASE_DIR = find_project_root()
    CORPUS_OUTPUTS_DIR = BASE_DIR / "outputs" / "artifact"
    ICA_CACHE_DIR = CORPUS_OUTPUTS_DIR / "features_extractor_test" / "cache"
    FEATURES_DIR = CORPUS_OUTPUTS_DIR / "features_extractor_test"/ "features"
    for d in (FEATURES_DIR, ICA_CACHE_DIR):
        d.mkdir(parents=True, exist_ok=True)

    database_corpus_patient = build_annotations_index("artifact", n_patients=1, max_sessions=1, paths=True)
    windowed_df = label_windowing(
                    database_corpus_patient, WINDOW_REQUESTS["rf_artifact_class"],
                    ARTIFACT_KEYWORDS, unreviewd_tokens=True,
                )
    display(windowed_df)

    # ICA 
    windows = build_feature_dataset(windowed_df, use_ica=True, ica_cache_dir=str(ICA_CACHE_DIR))
    display(windows)

    print("ICA Inspection")
    print(windows.columns.tolist())
    """
    probs = windows[["probs"]]
    print(f"Patient/Session: {windows[['Patient']]} / {windows[['Session']]}")
    print(f"N componentes ICA: {len(comp_names)}")
    print(f"Labels crudos devueltos por mne-icalabel: {comp_names}")
    print(f"Probabilidades (max por componente): {[round(float(p), 3) for p in probs]}")

    # ICLABELS
    labels_encontrados = set(comp_names)
    labels_esperados = set(ICLABEL_CATEGORIES)
    print(f"\nCategorías esperadas (data_config.py): {labels_esperados}")
    print(f"Categorías encontradas en esta sesión:   {labels_encontrados}")
    inesperadas = labels_encontrados - labels_esperados
    if inesperadas:
        print(f"\n[WARNING] Labels NOT recognized by ICLABEL_CATEGORIES: {inesperadas}")
        print("\t\t\t-> _aggregate_by_iclabel_category ignore")
        print("\t\t\t   (columns in 0).")
    else:
        print("\n[OK] All coincident with ICLABEL_CATEGORIES.")

    print("\n Components by cathegory")
    for cat in ICLABEL_CATEGORIES:
        n = sum(1 for c in comp_names if c == cat)
        print(f"  {cat:20s}: {n}")

    print("\n Features")
    feats = {}
    feats.update(temporal_features(first_window["channel_window"], first_window["ch_names"]))
    feats.update(frequency_features(
        first_window["channel_window"], first_window["sfreq"], first_window["ch_names"]
    ))
    feats.update(_aggregate_by_iclabel_category(
        first_window["component_window"], first_window["comp_names"],
        first_window["mixing"], first_window["ch_names"], first_window["probs"]
    ))

    feats_df = pd.DataFrame([feats])
    print(f"N features generados: {feats_df.shape[1]}")

    iclabel_cols = [c for c in feats_df.columns if any(
        c.startswith(f"{cat.replace(' ', '_')}_") or c.startswith("n_ic_")
        for cat in ICLABEL_CATEGORIES
    )]
    display(feats_df[iclabel_cols].T)

    print("\n Channel features")
    normal_cols = [c for c in feats_df.columns if c not in iclabel_cols]
    print(f"N features normales: {len(normal_cols)}")
    display(feats_df[normal_cols].T.head(15))
    """