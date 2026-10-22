"""Extraccion XAI de TUSZ, con bloques por EDF y reanudacion.

Reemplaza src/xai/models/temporal_transformer/_data/data_extractor.py.
Ejecutar desde la raiz del repositorio con python -m y el mismo modulo.

Conserva filtros, features y regla original: una anotacion seiz debe
solaparse al menos min_overlap_sec con la ventana para marcarla positiva.
Una etiqueta 0 NO implica ausencia total de actividad ictal ni de artefactos.
No modifica ni vuelve a entrenar el modelo o su scaler.

Cada EDF se guarda en _shards/ antes de continuar. Al final se exportan los
mismos cuatro NPY y meta.json, sin acumular todo el corpus en RAM.
Usar una sola instancia de este extractor por directorio de salida.
"""

import argparse
import csv
import hashlib
import inspect
import io
import json
import os
import pickle
import shutil
import tempfile
from pathlib import Path

import numpy as np
import scipy
import scipy.signal as scipy_signal
from fastapi import HTTPException

from src.xai.models.temporal_transformer.sanchez_transformer_network_eval import (
    _load_bipolar_signals, _iter_windows, _compute_feature_vector,
)

PIPELINE_VERSION = "xai-edf-shards-v1"
ARRAY_FILES = {
    "windows": "windows_np.npy",
    "features_raw": "features_raw.npy",
    "features_scaled": "features_scaled.npy",
    "labels": "labels_np.npy",
}
META_KEYS = (
    "times", "paths", "records", "window_metadata", "feature_names",
    "extraction_config", "label_rule", "filters",
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


def label_window(t_start, t_end, seizure_intervals, min_overlap_sec=1.0):
    """1 (ictal) si la ventana se solapa >= 1 s con alguna crisis; 0 (fondo) si no."""
    for s_start, s_end in seizure_intervals:
        overlap = max(0.0, min(t_end, s_end) - max(t_start, s_start))
        if overlap >= min_overlap_sec:
            return 1
    return 0


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

    if min_overlap_sec > win_sec:
        raise ValueError("min_overlap_sec no puede superar window_sec.")
    if win_sec <= 0 or hop_sec <= 0 or fs_target <= 120:
        raise ValueError(
            "window_sec y hop_sec deben ser positivos; target_fs debe ser > 120 "
            "para conservar el notch original de 60 Hz."
        )
    if int(hop_sec * fs_target) < 1 or n_samples < 1:
        raise ValueError("La ventana o el paso no alcanzan una muestra.")
    if not feature_names or len(feature_names) != len(set(feature_names)):
        raise ValueError("selected_features debe ser una lista no vacia sin duplicados.")

    windows, feats, labels = [], [], []
    times, paths = [], []

    records = []
    window_metadata = []

    for input_path in edf_paths:
        edf_path = Path(input_path).resolve()
        if verbose:
            print(f"Procesando: {edf_path}", flush=True)
        annotation_path = edf_path.with_suffix(".csv_bi")

        if not annotation_path.exists():
            raise FileNotFoundError(annotation_path)

        annotations = read_annotations(annotation_path)
        if not annotations:
            raise ValueError(f"Anotaciones vacias: {annotation_path}")
        unexpected = {a["label"] for a in annotations} - {"seiz", "bckg"}
        if unexpected:
            raise ValueError(f"Etiquetas inesperadas en csv_bi: {unexpected}")
        seizure_annotations = [
            a for a in annotations if a["label"] == "seiz"
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
            "positive_label_match": "seiz",
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
    """Compatibilidad con consumidores anteriores."""
    return [
        (a["start_sec"], a["end_sec"])
        for a in read_annotations(csv_bi_path)
        if a["label"] == "seiz"
    ]


def find_seizure_edfs(tusz_root):
    """Compatibilidad: main usa TODOS los EDF, no esta seleccion."""
    return [
        p.resolve() for p in sorted(Path(tusz_root).rglob("*.edf"))
        if p.with_suffix(".csv_bi").is_file()
        and parse_csv_bi(p.with_suffix(".csv_bi"))
    ]


def write_json(path, value):
    """Escribe JSON con reemplazo atomico en el mismo sistema de archivos."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(value, f, ensure_ascii=False, indent=2, allow_nan=False)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def json_digest(value):
    encoded = json.dumps(value, sort_keys=True, allow_nan=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def dataset_metadata(ds):
    meta = {key: ds[key] for key in META_KEYS}
    meta["provenance"] = ds.get("provenance", {})
    return meta


def save_dataset(ds, scaler, save_dir):
    """Guarda un bloque. El coordinador lo publica por rename de directorio."""
    save_dir = Path(save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)
    raw_features = np.asarray(
        ds.get("features_raw", ds["features"]), dtype=np.float32
    )
    scaled = np.asarray(scaler.transform(raw_features), dtype=np.float32)
    if scaled.shape != raw_features.shape or not np.isfinite(scaled).all():
        raise ValueError("Features escaladas invalidas o con dimensiones distintas.")
    arrays = {
        "windows": np.asarray(ds["windows"], dtype=np.float32),
        "features_raw": raw_features,
        "features_scaled": scaled,
        "labels": np.asarray(ds["labels"], dtype=np.int8),
    }
    n = len(arrays["labels"])
    if any(len(a) != n for a in arrays.values()):
        raise ValueError("Cantidad de ventanas, features y etiquetas inconsistente.")
    for key, filename in ARRAY_FILES.items():
        np.save(save_dir / filename, arrays[key], allow_pickle=False)
    write_json(save_dir / "meta.json", dataset_metadata(ds))


def load_dataset(save_dir, mmap_mode=None):
    """Contrato anterior: features escaladas; features_raw conserva las crudas.

    mmap_mode='r' permite leer los NPY sin cargarlos completos en RAM.
    """
    save_dir = Path(save_dir)
    if (save_dir / "_shards").exists():
        marker_path = save_dir / "dataset_complete.json"
        if not marker_path.exists():
            raise RuntimeError("Exportacion incompleta. Reejecuta el extractor.")
        marker = json.loads(marker_path.read_text(encoding="utf-8"))
        run = json.loads((save_dir / "run_manifest.json").read_text(encoding="utf-8"))
        if marker["run_digest"] != json_digest(run):
            raise RuntimeError("La exportacion corresponde a otra seleccion de EDF.")
    with (save_dir / "meta.json").open(encoding="utf-8") as f:
        ds = json.load(f)
    for key, filename in ARRAY_FILES.items():
        output_key = "features" if key == "features_scaled" else key
        if key == "features_raw" and not (save_dir / filename).exists():
            continue  # Compatibilidad con datasets antiguos.
        ds[output_key] = np.load(
            save_dir / filename, mmap_mode=mmap_mode, allow_pickle=False
        )
    return ds


def file_identity(edf_path):
    """El EDF se identifica por ruta, tamano y mtime; su CSV por SHA-256."""
    edf_path = Path(edf_path).resolve()
    stat = edf_path.stat()
    ann = edf_path.with_suffix(".csv_bi")
    return {
        "edf_path": str(edf_path),
        "edf_size_bytes": stat.st_size,
        "edf_mtime_ns": stat.st_mtime_ns,
        "annotation_path": str(ann),
        "annotation_sha256": file_sha256(ann),
    }


def shard_description(shard_dir):
    description = {}
    for key, filename in ARRAY_FILES.items():
        path = Path(shard_dir) / filename
        arr = np.load(path, mmap_mode="r", allow_pickle=False)
        description[key] = {
            "shape": list(arr.shape), "dtype": str(arr.dtype),
            "size_bytes": path.stat().st_size,
        }
        del arr
    return description


def validate_shard(shard_dir, identity, run_digest):
    """No reutiliza un bloque de otra entrada o un bloque incompleto."""
    marker = Path(shard_dir) / "complete.json"
    if not marker.exists():
        raise RuntimeError(f"Bloque sin marca de finalizacion: {shard_dir}")
    data = json.loads(marker.read_text(encoding="utf-8"))
    if data["identity"] != identity or data["run_digest"] != run_digest:
        raise RuntimeError(f"Bloque incompatible: {shard_dir}. Usa otro --save-dir.")
    if data["arrays"] != shard_description(shard_dir):
        raise RuntimeError(f"Bloque incompleto o modificado: {shard_dir}")
    if data["meta_sha256"] != file_sha256(Path(shard_dir) / "meta.json"):
        raise RuntimeError(f"Metadatos modificados: {shard_dir}")
    return data


def is_missing_electrodes(exc):
    return (
        isinstance(exc, HTTPException)
        and exc.status_code == 400
        and isinstance(exc.detail, str)
        and exc.detail.startswith("El EDF no contiene los electrodos requeridos")
    )


def export_dataset(shards, save_dir, run, outcomes):
    """Concatena por bloques con memmap; no copia todo el EEG a la RAM.

    Se preservan los nombres y las claves consumidas por los scripts XAI.
    Los metadatos JSON se acumulan en RAM; las senales se copian por EDF.
    """
    save_dir = Path(save_dir)
    if not shards:
        raise ValueError("Ningun EDF produjo ventanas; revisa exclusions.json.")
    marker_path = save_dir / "dataset_complete.json"
    marker_path.unlink(missing_ok=True)
    stage = save_dir / "_export_pending"
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir()

    metas = []
    descriptions = []
    for shard in shards:
        with (shard / "meta.json").open(encoding="utf-8") as f:
            metas.append(json.load(f))
        descriptions.append(shard_description(shard))
    total = sum(d["labels"]["shape"][0] for d in descriptions)
    for key, filename in ARRAY_FILES.items():
        first = descriptions[0][key]
        tail = first["shape"][1:]
        for desc in descriptions:
            if desc[key]["shape"][1:] != tail or desc[key]["dtype"] != first["dtype"]:
                raise ValueError(f"Dimensiones o dtype incompatibles para {key}.")
        dest = np.lib.format.open_memmap(
            stage / filename, mode="w+", dtype=first["dtype"],
            shape=(total, *tail),
        )
        offset = 0
        for shard, desc in zip(shards, descriptions):
            arr = np.load(shard / filename, mmap_mode="r", allow_pickle=False)
            n = desc[key]["shape"][0]
            dest[offset:offset+n] = arr
            offset += n
            del arr
        dest.flush()
        del dest

    meta = {k: metas[0][k] for k in (
        "feature_names", "extraction_config", "label_rule", "filters"
    )}
    meta.update(times=[], paths=[], records=[], window_metadata=[])
    for local in metas:
        window_offset = len(meta["times"])
        record_offset = len(meta["records"])
        meta["times"].extend(local["times"])
        meta["paths"].extend(local["paths"])
        for record in local["records"]:
            item = dict(record)
            item["record_id"] += record_offset
            meta["records"].append(item)
        for window in local["window_metadata"]:
            item = dict(window)
            item["window_id"] += window_offset
            item["record_id"] += record_offset
            meta["window_metadata"].append(item)
    meta["provenance"] = {
        **run,
        "selection": "todos los EDF solicitados; exclusiones explicitas por montaje",
        "selected_edfs": [item["edf_path"] for item in run["inputs"]],
        "included_edfs": [o["edf_path"] for o in outcomes if o["status"] == "complete"],
        "excluded_edfs": [o for o in outcomes if o["status"] == "excluded"],
        "actual_coverage": "subconjunto compatible" if any(
            o["status"] == "excluded" for o in outcomes
        ) else "todos los EDF solicitados",
    }
    write_json(stage / "meta.json", meta)
    # El lector nuevo rechaza una exportacion interrumpida sin marca final.
    # No ejecutar lectores antiguos a la vez que este exportador.
    for filename in [*ARRAY_FILES.values(), "meta.json"]:
        os.replace(stage / filename, save_dir / filename)
    stage.rmdir()
    write_json(marker_path, {
        "run_digest": json_digest(run), "n_windows": total,
        "included_records": len(shards),
    })
    print(f"Dataset final guardado: {save_dir}", flush=True)
    print(f"Ventanas: {total}; EDF incluidos: {len(shards)}", flush=True)


def run_extraction(edfs, config, scaler, save_dir, run, min_overlap_sec=1.0,
                   skip_missing_electrodes=True, export=True):
    save_dir = Path(save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)
    cache = save_dir / "_shards"
    cache.mkdir(exist_ok=True)
    manifest = save_dir / "run_manifest.json"
    if manifest.exists():
        old_run = json.loads(manifest.read_text(encoding="utf-8"))
        if old_run != run:
            raise RuntimeError(
                "Cambian entradas, configuracion, scaler o codigo. "
                "Conserva estos resultados y utiliza otro --save-dir."
            )
    else:
        # No mezcla checkpoints de una corrida sin manifiesto.
        if any(cache.iterdir()):
            raise RuntimeError("Hay bloques sin manifiesto. Utiliza otro --save-dir.")
        write_json(manifest, run)
    run_digest = json_digest(run)
    shards, outcomes = [], []
    total_windows = total_positive = 0

    for index, (edf, identity) in enumerate(zip(edfs, run["inputs"]), start=1):
        edf = Path(edf).resolve()
        key = hashlib.sha256(str(edf).encode()).hexdigest()[:24]
        shard = cache / key
        excluded_path = cache / f"{key}.excluded.json"
        print(f"[{index}/{len(edfs)}] {edf}", flush=True)
        # Detecta modificaciones ocurridas despues del inventario inicial.
        if file_identity(edf) != identity:
            raise RuntimeError(f"La entrada cambio durante la corrida: {edf}")
        if shard.exists():
            done = validate_shard(shard, identity, run_digest)
            print("  Bloque completo: reutilizado.", flush=True)
        elif excluded_path.exists():
            excluded = json.loads(excluded_path.read_text(encoding="utf-8"))
            if excluded["identity"] != identity or excluded["run_digest"] != run_digest:
                raise RuntimeError(f"Exclusion incompatible: {edf}")
            if not skip_missing_electrodes:
                raise RuntimeError(f"EDF incompatible: {excluded['reason']}")
            outcomes.append({"edf_path": str(edf), "status": "excluded",
                             "reason": excluded["reason"]})
            write_json(save_dir / "exclusions.json", [
                o for o in outcomes if o["status"] == "excluded"
            ])
            print(f"  Exclusion registrada: {excluded['reason']}", flush=True)
            continue
        else:
            try:
                ds = build_dataset(
                    [edf], config, config["selected_features"],
                    min_overlap_sec=min_overlap_sec,
                )
            except HTTPException as exc:
                if not skip_missing_electrodes or not is_missing_electrodes(exc):
                    raise
                exclusion = {
                    "identity": identity, "run_digest": run_digest,
                    "reason": exc.detail,
                }
                write_json(excluded_path, exclusion)
                outcomes.append({"edf_path": str(edf), "status": "excluded",
                                 "reason": exc.detail})
                write_json(save_dir / "exclusions.json", [
                    o for o in outcomes if o["status"] == "excluded"
                ])
                print(f"  Excluido por montaje: {exc.detail}", flush=True)
                continue
            if file_identity(edf) != identity:
                raise RuntimeError(f"La entrada cambio durante la extraccion: {edf}")
            pending = cache / f"{key}.pending"
            if pending.exists():
                shutil.rmtree(pending)
            pending.mkdir()
            ds["provenance"] = {"input": identity, "run_digest": run_digest}
            save_dataset(ds, scaler, pending)
            done = {
                "identity": identity, "run_digest": run_digest,
                "n_windows": int(len(ds["labels"])),
                "n_positive": int(np.sum(ds["labels"])),
                "arrays": shard_description(pending),
                "meta_sha256": file_sha256(pending / "meta.json"),
            }
            write_json(pending / "complete.json", done)
            os.replace(pending, shard)
            del ds
        shards.append(shard)
        total_windows += done["n_windows"]
        total_positive += done["n_positive"]
        outcomes.append({"edf_path": str(edf), "status": "complete",
                         "n_windows": done["n_windows"],
                         "n_positive": done["n_positive"]})
        write_json(save_dir / "progress.json", {
            "n_windows": total_windows, "n_positive": total_positive,
            "records": outcomes,
        })
        print(f"  Guardado: {total_windows} ventanas acumuladas, "
              f"{total_positive} positivas", flush=True)

    write_json(save_dir / "exclusions.json", [
        o for o in outcomes if o["status"] == "excluded"
    ])
    if export:
        marker = save_dir / "dataset_complete.json"
        expected = {"run_digest": run_digest, "n_windows": total_windows,
                    "included_records": len(shards)}
        if marker.exists() and json.loads(marker.read_text(encoding="utf-8")) == expected:
            if all((save_dir / f).is_file() for f in [*ARRAY_FILES.values(), "meta.json"]):
                print("La exportacion final ya esta completa.", flush=True)
                return outcomes
        print("Consolidando bloques a los NPY finales...", flush=True)
        export_dataset(shards, save_dir, run, outcomes)
    return outcomes


def main():
    base_dir = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tusz-root", type=Path, default=Path(
        "/mnt/d/tuh_eeg/tuh_eeg_seizure/v2.0.6/edf/eval"
    ))
    parser.add_argument("--config", type=Path,
                        default=base_dir / "sanchez_transformer_config_used.json")
    parser.add_argument("--scaler", type=Path,
                        default=base_dir / "sanchez_transformer_feature_scaler.pkl")
    parser.add_argument("--save-dir", type=Path, default=base_dir / "_data")
    parser.add_argument("--min-overlap-sec", type=float, default=1.0)
    parser.add_argument("--strict-montage", action="store_true",
                        help="Detenerse ante electrodos ausentes; por defecto registra y excluye.")
    parser.add_argument("--no-export", action="store_true",
                        help="Guardar solo bloques; al reejecutar sin esta opcion se consolidan.")
    args = parser.parse_args()
    if not args.tusz_root.is_dir():
        raise FileNotFoundError(args.tusz_root)
    with args.config.open(encoding="utf-8") as f:
        config = json.load(f)
    fs = float(config["target_fs"])
    win = float(config["window_sec"])
    hop = float(config["hop_sec"])
    if not np.isfinite([fs, win, hop, args.min_overlap_sec]).all():
        raise ValueError("Configuracion temporal no finita.")
    if fs <= 120 or win <= 0 or hop <= 0 or not 0 < args.min_overlap_sec <= win:
        raise ValueError("Revisa target_fs (>120), ventana, paso y umbral de solapamiento.")
    with args.scaler.open("rb") as f:
        scaler = pickle.load(f)
    if getattr(scaler, "n_features_in_", len(config["selected_features"])) != len(config["selected_features"]):
        raise ValueError("El numero de features del scaler no coincide con la configuracion.")
    edfs = sorted(p.resolve() for p in args.tusz_root.rglob("*.edf"))
    if not edfs:
        raise ValueError(f"No se encontraron EDF en {args.tusz_root}")
    missing = [p for p in edfs if not p.with_suffix(".csv_bi").is_file()]
    if missing:
        raise FileNotFoundError(f"{len(missing)} EDF sin csv_bi. Primero: {missing[0]}")
    print(f"Inventariando anotaciones de {len(edfs)} EDF...", flush=True)
    helper_source = inspect.getsourcefile(_load_bipolar_signals)
    if helper_source is None:
        raise RuntimeError("No se pudo identificar el codigo del cargador.")
    run = {
        "pipeline_version": PIPELINE_VERSION,
        "config_path": str(args.config.resolve()),
        "config_sha256": file_sha256(args.config),
        "extraction_config": config,
        "scaler_path": str(args.scaler.resolve()),
        "scaler_sha256": file_sha256(args.scaler),
        "extractor_sha256": file_sha256(__file__),
        "helper_sha256": file_sha256(helper_source),
        "numpy_version": np.__version__, "scipy_version": scipy.__version__,
        "dataset_root": str(args.tusz_root.resolve()),
        "min_overlap_sec": args.min_overlap_sec,
        "skip_missing_electrodes": not args.strict_montage,
        "inputs": [file_identity(p) for p in edfs],
    }
    # Bloqueo POSIX: WSL/Linux/RunPod. Se libera tambien al terminar con error.
    # Se comprueba antes de escribir; impide dos extractores en el mismo destino.
    import fcntl
    args.save_dir.mkdir(parents=True, exist_ok=True)
    with (args.save_dir / ".extractor.lock").open("a") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise RuntimeError("Ya hay otro extractor usando este --save-dir.") from exc
        run_extraction(
            edfs, config, scaler, args.save_dir, run,
            min_overlap_sec=args.min_overlap_sec,
            skip_missing_electrodes=not args.strict_montage,
            export=not args.no_export,
        )


if __name__ == "__main__":
    main()
