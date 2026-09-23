""""
# File: split_cache.py

Functions to save and reload into cache files of heavy loading data.
"""
# split_cache.py

import json
import os
from pathlib import Path

def _save(registry_path: Path, registry: dict):
    tmp = registry_path.with_name(registry_path.stem + "_tmp.json")
    tmp.write_text(json.dumps(registry, indent=2, sort_keys=True))
    os.replace(tmp, registry_path)

def _load(registry_path: Path) -> dict:
    if registry_path.exists():
        return json.loads(registry_path.read_text())
    return {}

def _key(artifact, window, n_patients, version):
    return f"{artifact}|w{window['window_size_sec']}|s{window['stride_sec']}|ua{window['artifact_umbral']}|p{n_patients}|v{version}"

def save_selected_sw(registry_path, artifact, window, n_patients, version, selected_sw):
    registry = _load(registry_path)
    key = _key(artifact, window, n_patients, version)
    registry[key] = selected_sw
    _save(registry_path, registry)
    print(f"[INFO] sw registrado: {key} = {selected_sw}")

def load_selected_sw(registry_path, artifact, window, n_patients, version):
    registry = _load(registry_path)
    key = _key(artifact, window, n_patients, version)
    if key not in registry:
        print(f"[INFO]: Split for {key} not found")
        return None 
    return registry[key]