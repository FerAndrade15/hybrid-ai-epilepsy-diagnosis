""""
# File: session_cache.py

Functions to save and reload into cache files of heavy loading data.
"""
# session_cache.py

# Data libraries
import os
import numpy as np
from pathlib import Path

# Project modules
from src.core.data_config import MONOPOLAR_CHANNELS, BIPOLAR_MONTAGE
from src.core.data_loader import load_raw_edf
from src.core.preprocessing import raw_data_preproccesing, bipolar_matrix
from src.models.ica_model import get_or_compute_ica

ICA_KEYS = ("sources_full", "mixing", "comp_names", "probs")

def _load_mono(path_edf):
    raw = load_raw_edf(path_edf, preloaD=True)
    return raw_data_preproccesing(raw, bipolar_montage=False)     # siempre monopolar + CAR

def _save(cache_file, payload):
    tmp = cache_file.with_name(cache_file.stem + "_tmp.npz")      # escritura atómica
    np.savez_compressed(tmp, **payload)
    os.replace(tmp, cache_file)

def get_or_compute_session(patient, session, section, path_edf, cache_dir="cache/sessions",
                           ica_cache_dir="cache/ica", use_ica=True, bipolar_montage=False):
    """
    Un solo .npz por (patient, session, section) con la señal monopolar y, si alguna vez
    se pidió, la ICA. `data` sale en el montaje pedido (bipolar = W @ monopolar).
    La ICA es siempre monopolar: las filas de `mixing` siguen el orden de `ica_ch_names`.
    """
    key = f"{patient}_{session}_{section}"
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = cache_dir / f"{key}_mono.npz"

    signal = None
    if cache_file.exists():
        with np.load(cache_file) as z:        # carga perezosa: solo lee lo que pides
            payload = {k: z[k] for k in z.files if use_ica or k not in ICA_KEYS}
    else:
        signal = _load_mono(path_edf)
        payload = {"data": signal.get_data(), "sfreq": np.float64(signal.info["sfreq"])}
        _save(cache_file, payload)            # la señal se guarda siempre, con o sin ICA

    if use_ica and "sources_full" not in payload:      # archivo sin ICA (o recién creado)
        if signal is None:
            signal = _load_mono(path_edf)
        ica, ic_labels, probs = get_or_compute_ica(signal, patient, f"{session}_{section}", ica_cache_dir)
        payload.update({
            "sources_full": ica.get_sources(signal).get_data(),
            "mixing": ica.get_components(),
            "comp_names": np.array(ic_labels["labels"], dtype="U32"),
            "probs": np.asarray(probs, dtype=float),
        })
        _save(cache_file, payload)            # reescribe el mismo archivo con la ICA añadida

    mono = payload["data"]
    return {
        "data": bipolar_matrix() @ mono if bipolar_montage else mono,
        "sfreq": float(payload["sfreq"]),
        "ch_names": list(BIPOLAR_MONTAGE["names"] if bipolar_montage else MONOPOLAR_CHANNELS),
        "ica_ch_names": list(MONOPOLAR_CHANNELS),
        "sources_full": payload.get("sources_full"),
        "mixing": payload.get("mixing"),
        "comp_names": payload.get("comp_names"),
        "probs": payload.get("probs"),
    }

if __name__ == "__main__":
    import time, shutil
    from src.core.data_config import DEBUG_DIR, ICLABEL_CATEGORIES
    from src.core.data_loader import pick_test_session

    row = pick_test_session()
    p, s, sec, edf = row["patient"], row["session"], row["section"], row["edf"]
    print(f"Sesión: {p}_{s}_{sec} ({row['duration_s']:.0f} s)")

    test_dir = DEBUG_DIR / "cache" / "sessions_smoke"
    ica_dir = DEBUG_DIR / "cache" / "ica"              # se conserva: la ICA es lo lento
    shutil.rmtree(test_dir, ignore_errors=True)
    kw = dict(cache_dir=test_dir, ica_cache_dir=ica_dir)
    f = test_dir / f"{p}_{s}_{sec}_mono.npz"

    # 1) CNN primero: bipolar, sin ICA
    t0 = time.time()
    a = get_or_compute_session(p, s, sec, edf, use_ica=False, bipolar_montage=True, **kw)
    print(f"1ª llamada sin ICA: {time.time() - t0:.1f} s")
    assert f.exists() and a["data"].shape[0] == 18 and a["ch_names"] == BIPOLAR_MONTAGE["names"]
    assert a["sources_full"] is None
    with np.load(f) as z:
        assert set(z.files) == {"data", "sfreq"}, z.files

    # 2) Segunda llamada: debe salir de caché
    t0 = time.time()
    a2 = get_or_compute_session(p, s, sec, edf, use_ica=False, bipolar_montage=True, **kw)
    print(f"2ª llamada (caché): {time.time() - t0:.2f} s")
    assert np.array_equal(a["data"], a2["data"])

    # 3) RF después: pide ICA y se añade al MISMO archivo
    t0 = time.time()
    b = get_or_compute_session(p, s, sec, edf, use_ica=True, bipolar_montage=False, **kw)
    print(f"Añadir ICA: {time.time() - t0:.0f} s")
    n_ic, T = b["mixing"].shape[1], b["data"].shape[1]
    assert b["data"].shape[0] == 19 and b["mixing"].shape[0] == 19
    assert b["sources_full"].shape == (n_ic, T)
    assert len(b["comp_names"]) == len(b["probs"]) == n_ic
    assert set(b["comp_names"]) <= set(ICLABEL_CATEGORIES)
    assert ((b["probs"] >= 0) & (b["probs"] <= 1)).all()
    with np.load(f) as z:
        print("Claves en el .npz:", sorted(z.files))

    # 4) Consistencia bipolar <-> monopolar y alineación de la ICA
    c = get_or_compute_session(p, s, sec, edf, use_ica=True, bipolar_montage=True, **kw)
    assert np.allclose(c["data"], bipolar_matrix() @ b["data"])
    assert np.allclose(c["data"], a["data"])
    ica, _, _ = get_or_compute_ica(None, p, f"{s}_{sec}", ica_dir)   # ya está en caché
    assert ica.ch_names == MONOPOLAR_CHANNELS, "filas de mixing desalineadas con ica_ch_names"

    # 5) Con ICA en el archivo, use_ica=False no debe devolverla
    d = get_or_compute_session(p, s, sec, edf, use_ica=False, bipolar_montage=True, **kw)
    assert d["sources_full"] is None
    print("[OK] session_cache")