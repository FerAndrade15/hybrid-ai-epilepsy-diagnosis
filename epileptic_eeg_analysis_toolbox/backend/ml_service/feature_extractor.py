""""
# File: features_extractor.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Agnostic functions for the extraction of diverse features:
- Temporal: RMS, variance, skewness, kurtosis, line_length, zero_crossing_rate, peak_to_peak
- Espectral: PSD, power per band, DWT, entropy
- ICA components dynamics and metadata extraction
"""
# Data libraries
import pywt
import numpy as np
import pandas as pd
from pathlib import Path
from typing import List, Dict, Any, Optional

# Mathematical features libraries
from scipy.signal import welch, find_peaks
from scipy.stats import skew, kurtosis

# Internal modules
from config.data_config import SFREQ, RAW_TO_TARGET, ICLABEL_CATEGORIES
from backend.ml_service.ica_module import channel_contribution

def temporal_features(
        raw: np.ndarray, 
        ch_names: List[str], 
        Mean: bool = True, 
        Variance: bool = True, 
        RMS: bool = True, 
        Skewness: bool = True, 
        Kurtosis: bool = True, 
        Zero_crossing_rate: bool = True, 
        Hjorth: bool = True, 
        Line_length: bool = True, 
        Peak_to_peak: bool = True
    ) -> Dict[str, Any]:
    """
    Extraction of temporal features from a raw signal window.
    """
    eps = 1e-10 
    feats: Dict[str, float] = {}

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

def frequency_features(
        raw: np.ndarray, 
        sfreq: float, 
        ch_names: List[str], 
        powerbands: bool = True, 
        Wavelets: bool = True
    ) -> Dict[str, float]:
    """
    Extraction of frequency features from a raw signal window.
    """
    nperseg = min(256, raw.shape[1])
    freqs, psd = welch(raw, sfreq, axis=1, nperseg=nperseg)
    feats: Dict[str, float] = {}

    if powerbands:
        bands = {
            'delta': (0.5,4.0), 
            'theta': (4.0,8.0), 
            'alpha': (8.0,13.0), 
            'beta': (13.0,30.0), 
            'gamma': (30.0,45.0)
        }
        band_power = {}
        for name, (lo, hi) in bands.items():
            mask = (freqs >= lo) & (freqs <= hi)
            band_power[name] = psd[:, mask].mean(axis=1) if np.any(mask) else np.zeros(raw.shape[0])

        for i, ch in enumerate(ch_names):
            clean_ch = str(ch).replace("EEG ", "").replace("-REF", "").strip()
            for name in bands:
                feats[f"{clean_ch}_{name}_power"] = band_power[name][i]
            feats[f"{clean_ch}_ratio_high_low"] = band_power["gamma"][i]/(band_power["delta"][i] + 1e-10)

    if Wavelets:
        # Spectral entropy
        psd_norm = psd / (np.sum(psd, axis=1, keepdims=True) + 1e-10)
        spec_entropy = -np.sum(psd_norm * np.log2(psd_norm + 1e-10), axis=1)

        # Discrete Wavelet Transformation
        coeffs = pywt.wavedec(raw, 'db4', level=4, axis=1)
        names = ['A4', 'D4', 'D3', 'D2', 'D1']

        for i, ch in enumerate(ch_names):
            clean_ch = str(ch).replace("EEG ", "").replace("-REF", "").strip()
            feats[f"{clean_ch}_spectral_entropy"] = spec_entropy[i]
            for j, coef in enumerate(coeffs):
                feats[f"{clean_ch}_dwt_energy_{names[j]}"] = np.sum(coef[i]**2)
                feats[f"{clean_ch}_dwt_var_{names[j]}"] = np.var(coef[i])
    return feats

def components_dynamics(source_window, comp_names):
    """
    Extraction of dynamics features from ICA components, including:
    peak-to-mean ratio, peak position, number of peaks, and baseline shift.
    """
    feats: Dict[str, float] = {}
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

# Models and inference functions
def extract_features_from_window_payload(
        channel_data: np.ndarray,
        ch_names: List[str],
        sfreq: float = SFREQ,
        component_data: Optional[np.ndarray] = None,
        mixing_matrix: Optional[np.ndarray] = None,
        ic_probs: Optional[List[float]] = None,    
    ) -> Dict[str, Any]:
    """
    Extracts features from a given window of EEG data, including temporal and frequency features for channels
    """
    full_vector: Dict[str, float] = {}
    full_vector.update(temporal_features(channel_data, ch_names))
    full_vector.update(frequency_features(channel_data, sfreq, ch_names))

    if component_data is not None and mixing_matrix is not None:
        n_comps = component_data.shape[0]
        comp_names = [f"IC_{i}" for i in range(n_comps)]

        # Temporal dynamics features
        full_vector.update(components_dynamics(component_data, comp_names))

        # Spacial contribution features
        spatial_contrib = channel_contribution(component_data, mixing_matrix, ch_names, comp_names)
        for comp_name, ch_dict in spatial_contrib.items():
            full_vector.update(ch_dict)

    if ic_probs is not None and len(ic_probs) > 0:
        mean_probs = np.mean(ic_probs, axis=0) if np.ndim(ic_probs) == 2 else ic_probs
        for idx, cat_name in enumerate(ICLABEL_CATEGORIES):
            if idx < len(mean_probs):
                safe_name = cat_name.replace(" ", "_")
                full_vector[f"iclabel_prob_{safe_name}"] = float(mean_probs[idx])

    return full_vector

if __name__ == "__main__":
    print("[INFO] Ejecutando feature_extractor.py como script de prueba")
    n_ch, n_samples = 19, 256
    mock_raw = np.random.randn(n_ch, n_samples)
    mock_ch = [f"EEG {ch}" for ch in ["FP1", "FP2", "F3", "F4", "C3", "C4", "P3", "P4", "O1", "O2", 
                                      "F7", "F8", "T3", "T4", "T5", "T6", "FZ", "CZ", "PZ"]]
    
    res = extract_features_from_window_payload(mock_raw, mock_ch, sfreq=256.0)
    print(f"[OK] Extracción exitosa. Vector generado con {len(res)} características.")