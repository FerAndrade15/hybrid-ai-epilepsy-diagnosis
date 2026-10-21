# Sanchez - Temporal transformer: Data extractor
# File: data_extractor.py

import json, pickle
import numpy as np
import scipy.signal as scipy_signal
from pathlib import Path

import io
import csv
import hashlib
import random
from collections import defaultdict

from src.xai.models.temporal_transformer.sanchez_transformer_network_eval import (
    _load_bipolar_signals, _iter_windows, _compute_feature_vector,
)

def apply_filters(signals_np, fs):
    """Bandpass 0.5-40 Hz + notch 60 Hz, canal por canal. signals_np: (muestras, canales)."""
    b_bp, a_bp = scipy_signal.butter(4, [0.5 / (fs / 2), 40.0 / (fs / 2)], btype='band')
    b_notch, a_notch = scipy_signal.iirnotch(60.0, Q=30, fs=fs)
    filtered = signals_np.copy()
    for ch in range(signals_np.shape[1]):
        filtered[:, ch] = scipy_signal.filtfilt(b_bp, a_bp, filtered[:, ch])
        filtered[:, ch] = scipy_signal.filtfilt(b_notch, a_notch, filtered[:, ch])
    return filtered

def parse_csv_bi(csv_bi_path):
    """Lee el .csv_bi de TUSZ y devuelve [(t_ini, t_fin), ...] solo de filas 'seiz'."""
    intervals = []
    with open(csv_bi_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    header_idx = next((i for i, l in enumerate(lines) if l.strip().startswith('channel,')), None)
    if header_idx is None:
        return []

    header = lines[header_idx].strip().split(',')
    i_start, i_stop, i_label = header.index('start_time'), header.index('stop_time'), header.index('label')

    for line in lines[header_idx + 1:]:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split(',')
        if len(parts) <= max(i_start, i_stop, i_label):
            continue
        if 'seiz' in parts[i_label].strip().lower():
            try:
                intervals.append((float(parts[i_start]), float(parts[i_stop])))
            except ValueError:
                continue
    return intervals


def label_window(t_start, t_end, seizure_intervals, min_overlap_sec=1.0):
    """1 (ictal) si la ventana se solapa >= 1 s con alguna crisis; 0 (fondo) si no."""
    for s_start, s_end in seizure_intervals:
        overlap = max(0.0, min(t_end, s_end) - max(t_start, s_start))
        if overlap >= min_overlap_sec:
            return 1
    return 0

def find_seizure_edfs(tusz_root):
    selected = []

    for edf_path in sorted(Path(tusz_root).rglob("*.edf")):
        annotation_path = edf_path.with_suffix(".csv_bi")

        if not annotation_path.exists():
            continue

        annotations = read_annotations(annotation_path)

        if any("seiz" in a["label"] for a in annotations):
            selected.append(edf_path.resolve())

    return selected

def build_dataset(
    edf_paths,
    config,
    feature_names,
    verbose=True,
    min_overlap_sec=1.0,
):
    fs_target = float(config["target_fs"])
    win_sec = float(config["window_sec"])
    hop_sec = float(config["hop_sec"])
    n_samples = int(fs_target * win_sec)

    if min_overlap_sec <= 0:
        raise ValueError("min_overlap_sec debe ser positivo.")

    windows, feats, labels = [], [], []
    times, paths = [], []

    records = []
    window_metadata = []

    for input_path in edf_paths:
        edf_path = Path(input_path).resolve()
        annotation_path = edf_path.with_suffix(".csv_bi")

        if not annotation_path.exists():
            raise FileNotFoundError(annotation_path)

        annotations = read_annotations(annotation_path)
        seizure_annotations = [
            a for a in annotations if "seiz" in a["label"]
        ]

        # Si falla la carga, detenemos la extracción para no omitir
        # registros sin que quede claro qué dataset se generó.
        signals, fs = _load_bipolar_signals(
            edf_path,
            montage=config["montage"],
            target_fs=fs_target,
        )

        fs = float(fs)

        if not np.isclose(fs, fs_target):
            raise ValueError(
                f"Frecuencia inesperada en {edf_path}: {fs}"
            )

        signals = apply_filters(signals, fs)
        record_id = len(records)

        records.append({
            "record_id": record_id,
            "edf_path": str(edf_path),
            "edf_size_bytes": edf_path.stat().st_size,
            "annotation_path": str(annotation_path),
            "annotation_sha256": file_sha256(annotation_path),
            "fs": fs,
            "n_channels": int(signals.shape[1]),
            "annotations": annotations,
        })

        for window, t0, t1 in _iter_windows(
            signals,
            fs=fs,
            window_sec=win_sec,
            hop_sec=hop_sec,
            window_samples=n_samples,
            hop_samples=int(hop_sec * fs),
        ):
            t0, t1 = float(t0), float(t1)

            if window.shape[0] != n_samples:
                raise ValueError("La ventana tiene un tamaño inesperado.")

            fd = _compute_feature_vector(window, fs=fs)

            # Evita sustituir silenciosamente una feature inexistente por 0.
            missing = [name for name in feature_names if name not in fd]
            if missing:
                raise ValueError(f"Features no encontradas: {missing}")

            feature_values = np.asarray(
                [float(fd[name]) for name in feature_names],
                dtype=np.float32,
            )

            if not (
                np.isfinite(window).all()
                and np.isfinite(feature_values).all()
            ):
                raise ValueError(
                    f"Datos no finitos en {edf_path}, intervalo {t0}-{t1}"
                )

            overlaps = []

            for annotation in seizure_annotations:
                overlap_start = max(t0, annotation["start_sec"])
                overlap_end = min(t1, annotation["end_sec"])
                overlap_sec = max(0.0, overlap_end - overlap_start)

                if overlap_sec > 0:
                    overlaps.append({
                        "annotation_id": annotation["annotation_id"],
                        "channel": annotation["channel"],
                        "label": annotation["label"],
                        "overlap_start_sec": overlap_start,
                        "overlap_end_sec": overlap_end,
                        "overlap_sec": overlap_sec,

                        # Coordenadas para superponer en la gráfica,
                        # cuyo tiempo comienza en cero en cada ventana.
                        "relative_start_sec": overlap_start - t0,
                        "relative_end_sec": overlap_end - t0,

                        "meets_label_rule": (
                            overlap_sec >= min_overlap_sec
                        ),
                    })

            # Misma regla original: basta UNA anotación con >= 1 s.
            label = int(any(
                item["meets_label_rule"] for item in overlaps
            ))

            window_id = len(windows)

            windows.append(window)
            feats.append(feature_values)
            labels.append(label)
            times.append((t0, t1))

            # Se mantiene la clave paths para tu script XAI,
            # pero ahora contiene la ruta completa.
            paths.append(str(edf_path))

            window_metadata.append({
                "window_id": window_id,
                "record_id": record_id,
                "source_file": str(edf_path),
                "annotation_file": str(annotation_path),
                "start_sec": t0,
                "end_sec": t1,
                "n_samples": int(window.shape[0]),
                "fs": fs,
                "label": label,
                "seizure_overlaps": overlaps,
            })

        if verbose:
            print(
                f"{edf_path.name}: {len(windows)} ventanas acumuladas, "
                f"{sum(labels)} positivas"
            )

    if not windows:
        raise ValueError("No se generaron ventanas.")

    return {
        "windows": np.asarray(windows, dtype=np.float32),
        "features": np.asarray(feats, dtype=np.float32),
        "labels": np.asarray(labels, dtype=np.int8),
        "times": times,
        "paths": paths,
        "records": records,
        "window_metadata": window_metadata,
        "feature_names": list(feature_names),
        "extraction_config": config,
        "label_rule": {
            "positive_label_match": "contiene 'seiz'",
            "min_overlap_sec": min_overlap_sec,
            "aggregation": "alguna anotación individual alcanza el umbral",
        },
        "filters": {
            "bandpass_hz": [0.5, 40.0],
            "bandpass_order": 4,
            "notch_hz": 60.0,
            "notch_q": 30,
            "application": "filtfilt antes de segmentar",
        },
    }

def save_dataset(ds, scaler, save_dir):
    save_dir = Path(save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)

    features_scaled = np.asarray(
        scaler.transform(ds["features"]),
        dtype=np.float32,
    )

    if not np.isfinite(features_scaled).all():
        raise ValueError("Las features escaladas contienen NaN o infinitos.")

    # Arreglos numéricos.
    np.save(save_dir / "windows_np.npy", ds["windows"])
    np.save(save_dir / "features_raw.npy", ds["features"])
    np.save(save_dir / "features_scaled.npy", features_scaled)
    np.save(save_dir / "labels_np.npy", ds["labels"])

    # Metadatos: incluye la información de cada ventana y anotación.
    metadata_keys = [
        "times",
        "paths",
        "records",
        "window_metadata",
        "feature_names",
        "extraction_config",
        "label_rule",
        "filters",
    ]

    meta = {key: ds[key] for key in metadata_keys}
    meta["provenance"] = ds.get("provenance", {})

    with open(save_dir / "meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)


def load_dataset(save_dir):
    save_dir = Path(save_dir)

    with open(save_dir / "meta.json", encoding="utf-8") as f:
        meta = json.load(f)

    # Conserva todos los metadatos del JSON.
    ds = dict(meta)

    ds.update({
        "windows": np.load(save_dir / "windows_np.npy"),
        "features": np.load(save_dir / "features_scaled.npy"),
        "labels": np.load(save_dir / "labels_np.npy"),
    })

    raw_path = save_dir / "features_raw.npy"
    if raw_path.exists():
        ds["features_raw"] = np.load(raw_path)

    return ds


def file_sha256(path):
    """Huella del contenido; permite detectar si el archivo cambió."""
    digest = hashlib.sha256()

    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(block)

    return digest.hexdigest()

def read_annotations(csv_bi_path):
    """Lee las filas de anotación conservando sus campos originales."""
    csv_bi_path = Path(csv_bi_path)

    lines = csv_bi_path.read_text(
        encoding="utf-8-sig",
        errors="strict",
    ).splitlines()

    header_idx = next(
        (
            i for i, line in enumerate(lines)
            if line.strip().startswith("channel,")
        ),
        None,
    )

    if header_idx is None:
        raise ValueError(f"No se encontró encabezado en {csv_bi_path}")

    header = [
        value.strip()
        for value in next(csv.reader([lines[header_idx]]))
    ]

    required = {"channel", "start_time", "stop_time", "label"}
    if not required.issubset(header):
        raise ValueError(f"Faltan columnas en {csv_bi_path}")

    annotations = []

    for line_number, line in enumerate(
        lines[header_idx + 1:],
        start=header_idx + 2,
    ):
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        values = next(csv.reader(io.StringIO(line)))

        if len(values) != len(header):
            raise ValueError(
                f"Fila inválida en {csv_bi_path}:{line_number}"
            )

        original = dict(zip(header, values))
        t0 = float(original["start_time"])
        t1 = float(original["stop_time"])

        if not np.isfinite([t0, t1]).all() or t1 <= t0:
            raise ValueError(
                f"Intervalo inválido en {csv_bi_path}:{line_number}"
            )

        annotations.append({
            "annotation_id": len(annotations),
            "line_number": line_number,
            "channel": original["channel"].strip(),
            "label": original["label"].strip().lower(),
            "start_sec": t0,
            "end_sec": t1,
            "original_fields": original,
        })

    return annotations


def parse_csv_bi(csv_bi_path):
    """Compatibilidad con tu función anterior."""
    return [
        (a["start_sec"], a["end_sec"])
        for a in read_annotations(csv_bi_path)
        if "seiz" in a["label"]
    ]

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    AMOUNT_PATIENTS = 20

    CONFIG_PATH = base_dir / "sanchez_transformer_config_used.json"
    SCALER_PATH = base_dir / "sanchez_transformer_feature_scaler.pkl"

    TUSZ_ROOT = Path(
        "/mnt/d/tuh_eeg/tuh_eeg_seizure/v2.0.6/edf/eval"
    )

    SAVE_DIR = base_dir / "_data"

    with open(CONFIG_PATH, encoding="utf-8") as f:
        config = json.load(f)

    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)

    edfs = find_seizure_edfs(TUSZ_ROOT)
    edfs_by_patient = defaultdict(list)
    for edf in edfs:
        patient_id = edf.parents[2].name
        edfs_by_patient[patient_id].append(edf)

    available_patients = list(edfs_by_patient.keys())
    n_patients = min(AMOUNT_PATIENTS, len(available_patients))
    sampled_patients = random.sample(available_patients, n_patients)

    selected_edfs = []
    for patient in sampled_patients:
        patient_edfs = edfs_by_patient[patient]
        selected_edfs.append(random.choice(patient_edfs))

    edfs = selected_edfs

    print("Registros seleccionados:")
    for edf in edfs:
        print(edf)

    ds = build_dataset(
        edfs,
        config,
        config["selected_features"],
        min_overlap_sec=1.0,
    )

    ds["provenance"] = {
        "config_path": str(CONFIG_PATH.resolve()),
        "config_sha256": file_sha256(CONFIG_PATH),
        "scaler_path": str(SCALER_PATH.resolve()),
        "scaler_sha256": file_sha256(SCALER_PATH),
        "dataset_root": str(TUSZ_ROOT.resolve()),
        "selection": "primeros 5 EDF ordenados con etiqueta que contiene seiz",
        "selected_edfs": [str(path.resolve()) for path in edfs],
    }

    save_dataset(ds, scaler, SAVE_DIR)

    print("Dataset guardado en:", SAVE_DIR)
    print("Señal:", ds["windows"].shape)
    print("Features:", ds["features"].shape)