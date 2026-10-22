"""Consolida bloques de data_extractor.py sin recalcular EDF.

Lee _shards y run_manifest.json; no importa el extractor ni modifica origen.
Escribe NPY secuenciales (sin memmap de salida), un bloque EDF a la vez.
Requiere Python y NumPy. El destino debe ser una carpeta nueva.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import tempfile

import numpy as np

ARRAY_FILES = {
    "windows": "windows_np.npy",
    "features_raw": "features_raw.npy",
    "features_scaled": "features_scaled.npy",
    "labels": "labels_np.npy",
}
COMMON_META = ("feature_names", "extraction_config", "label_rule", "filters")


def read_json(path):
    with Path(path).open(encoding="utf-8") as f:
        return json.load(f)


def sha256(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(
        value, sort_keys=True, allow_nan=False
    ).encode("utf-8")).hexdigest()


def write_json(path, data):
    with Path(path).open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, allow_nan=False)
        f.flush()
        os.fsync(f.fileno())


def read_npy_header(path):
    with Path(path).open("rb") as f:
        version = np.lib.format.read_magic(f)
        if version == (1, 0):
            shape, fortran, dtype = np.lib.format.read_array_header_1_0(f)
        elif version == (2, 0):
            shape, fortran, dtype = np.lib.format.read_array_header_2_0(f)
        else:
            raise ValueError(f"Version NPY no contemplada {version}: {path}")
        offset = f.tell()
    if dtype.hasobject or not shape or shape[0] <= 0:
        raise ValueError(f"NPY no numerico o vacio: {path}")
    expected_size = offset + math.prod(shape) * dtype.itemsize
    if Path(path).stat().st_size != expected_size:
        raise ValueError(f"NPY truncado o de tamano incorrecto: {path}")
    return {"shape": list(shape), "dtype": str(dtype),
            "size_bytes": expected_size}


def inventory(source):
    run = read_json(source / "run_manifest.json")
    run_hash = digest(run)
    entries, exclusions = [], []
    for identity in run["inputs"]:
        key = hashlib.sha256(identity["edf_path"].encode()).hexdigest()[:24]
        folder = source / "_shards" / key
        excluded = source / "_shards" / f"{key}.excluded.json"
        if folder.is_dir():
            done = read_json(folder / "complete.json")
            if done["identity"] != identity or done["run_digest"] != run_hash:
                raise ValueError(f"Bloque de otra corrida: {folder}")
            actual = {k: read_npy_header(folder / name)
                      for k, name in ARRAY_FILES.items()}
            if actual != done["arrays"]:
                raise ValueError(f"Bloque modificado: {folder}")
            if sha256(folder / "meta.json") != done["meta_sha256"]:
                raise ValueError(f"Metadatos modificados: {folder}")
            n = done["n_windows"]
            if any(d["shape"][0] != n for d in actual.values()):
                raise ValueError(f"Filas inconsistentes: {folder}")
            entries.append((folder, done))
        elif excluded.is_file():
            ex = read_json(excluded)
            if ex["identity"] != identity or ex["run_digest"] != run_hash:
                raise ValueError(f"Exclusion de otra corrida: {excluded}")
            exclusions.append({"edf_path": identity["edf_path"],
                               "status": "excluded", "reason": ex["reason"]})
        else:
            raise ValueError(
                f"Falta terminar un EDF: {identity['edf_path']}. "
                "Reanuda el extractor original antes de consolidar."
            )
    if not entries:
        raise ValueError("No hay bloques completos para exportar.")
    for key in ARRAY_FILES:
        reference = entries[0][1]["arrays"][key]
        for folder, done in entries:
            d = done["arrays"][key]
            if d["shape"][1:] != reference["shape"][1:] or d["dtype"] != reference["dtype"]:
                raise ValueError(f"Forma o dtype incompatible ({key}): {folder}")
    return run, entries, exclusions


def stream_array(entries, key, path):
    n_total = sum(done["n_windows"] for _, done in entries)
    desc = entries[0][1]["arrays"][key]
    dtype = np.dtype(desc["dtype"])
    shape = (n_total, *desc["shape"][1:])
    filename = ARRAY_FILES[key]
    print(f"Escribiendo {filename}: {shape}, {dtype}", flush=True)
    with path.open("wb") as f:
        np.lib.format.write_array_header_2_0(f, {
            "descr": np.lib.format.dtype_to_descr(dtype),
            "fortran_order": False, "shape": shape,
        })
        for i, (folder, done) in enumerate(entries, 1):
            # Solo un EDF en memoria; no reserva todo el NPY de salida.
            arr = np.load(folder / filename, allow_pickle=False)
            expected = done["arrays"][key]
            if list(arr.shape) != expected["shape"] or str(arr.dtype) != expected["dtype"]:
                raise ValueError(f"El bloque cambio durante la copia: {folder}")
            contiguous = np.ascontiguousarray(arr)
            raw = memoryview(contiguous).cast("B")
            chunk_size = 16 * 1024 * 1024
            for start in range(0, len(raw), chunk_size):
                chunk = raw[start:start+chunk_size]
                if f.write(chunk) != len(chunk):
                    raise OSError(f"Escritura incompleta: {path}")
            del chunk, raw, contiguous, arr
            if i % 50 == 0 or i == len(entries):
                f.flush()
                print(f"  {i}/{len(entries)} bloques copiados", flush=True)
        f.flush()
        os.fsync(f.fileno())
    read_npy_header(path)


def merged_metadata(entries, run, exclusions):
    first = read_json(entries[0][0] / "meta.json")
    result = {k: first[k] for k in COMMON_META}
    result.update(times=[], paths=[], records=[], window_metadata=[])
    for folder, done in entries:
        local = read_json(folder / "meta.json")
        if any(local[k] != result[k] for k in COMMON_META):
            raise ValueError(f"Configuracion inconsistente: {folder}")
        n = done["n_windows"]
        if any(len(local[k]) != n for k in ("times", "paths", "window_metadata")):
            raise ValueError(f"Metadatos de ventanas incompletos: {folder}")
        window_offset = len(result["times"])
        record_offset = len(result["records"])
        records = local["records"]
        if [r["record_id"] for r in records] != list(range(len(records))):
            raise ValueError(f"IDs de registro invalidos: {folder}")
        for i, w in enumerate(local["window_metadata"]):
            if w["window_id"] != i or not 0 <= w["record_id"] < len(records):
                raise ValueError(f"IDs de ventanas invalidos: {folder}")
        result["times"].extend(local["times"])
        result["paths"].extend(local["paths"])
        result["records"].extend(
            {**r, "record_id": r["record_id"] + record_offset} for r in records
        )
        result["window_metadata"].extend(
            {**w, "window_id": w["window_id"] + window_offset,
             "record_id": w["record_id"] + record_offset}
            for w in local["window_metadata"]
        )
    result["provenance"] = {
        **run,
        "selection": "todos los EDF solicitados; exclusiones explicitas por montaje",
        "selected_edfs": [item["edf_path"] for item in run["inputs"]],
        "included_edfs": [done["identity"]["edf_path"] for _, done in entries],
        "excluded_edfs": exclusions,
        "actual_coverage": "subconjunto compatible" if exclusions else "todos los EDF solicitados",
        "export_method": "consolidacion secuencial desde bloques completos",
    }
    return result


def consolidate(source_dir, output_dir, check_only=False):
    source = Path(source_dir).expanduser().resolve()
    target = Path(output_dir).expanduser().resolve()
    if source == target or source in target.parents or target in source.parents:
        raise ValueError("Elige un destino separado del directorio de origen.")
    if target.exists():
        raise FileExistsError(f"El destino debe ser una carpeta nueva: {target}")
    run, entries, exclusions = inventory(source)
    total = sum(d["n_windows"] for _, d in entries)
    positives = sum(d["n_positive"] for _, d in entries)
    data_bytes = sum(
        math.prod(d["arrays"][k]["shape"]) * np.dtype(d["arrays"][k]["dtype"]).itemsize
        for _, d in entries for k in ARRAY_FILES
    )
    metadata_bytes = sum((p / "meta.json").stat().st_size for p, _ in entries)
    # Margen para metadatos globales, cabeceras y manifiestos.
    required = data_bytes + 2 * metadata_bytes + 256 * 1024**2
    existing_parent = target.parent
    while not existing_parent.exists():
        existing_parent = existing_parent.parent
    free = shutil.disk_usage(existing_parent).free
    print(f"EDF incluidos: {len(entries)}; excluidos: {len(exclusions)}", flush=True)
    print(f"Ventanas: {total}; positivas: {positives}", flush=True)
    print(f"NPY: {data_bytes / 1024**3:.2f} GiB; "
          f"espacio requerido con margen: {required / 1024**3:.2f} GiB; "
          f"libre informado por el destino: {free / 1024**3:.2f} GiB", flush=True)
    if check_only:
        return {"n_windows": total, "n_positive": positives, "required_bytes": required}
    if free < required:
        raise OSError("Espacio insuficiente en el destino. Usa otro disco o libera espacio.")
    target.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=target.name + ".pending-", dir=target.parent))
    try:
        for key, filename in ARRAY_FILES.items():
            stream_array(entries, key, stage / filename)
        print("Consolidando metadatos...", flush=True)
        meta = merged_metadata(entries, run, exclusions)
        write_json(stage / "meta.json", meta)
        del meta
        write_json(stage / "run_manifest.json", run)
        write_json(stage / "exclusions.json", exclusions)
        write_json(stage / "dataset_complete.json", {
            "run_digest": digest(run), "n_windows": total,
            "included_records": len(entries), "n_positive": positives,
        })
        # Nunca sobrescribe un destino existente.
        if target.exists():
            raise FileExistsError(target)
        os.rename(stage, target)
    except BaseException:
        print(f"Exportacion interrumpida. Los bloques originales siguen en {source}.\n"
              f"La carpeta temporal incompleta es: {stage}", flush=True)
        raise
    print(f"LISTO. Usa esta carpeta como entrada de tu XAI: {target}", flush=True)
    return {"n_windows": total, "n_positive": positives, "output_dir": str(target)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--check-only", action="store_true",
                        help="Validar bloques y estimar espacio sin escribir el dataset.")
    args = parser.parse_args()
    consolidate(args.source_dir, args.output_dir, args.check_only)


if __name__ == "__main__":
    main()
