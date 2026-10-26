from collections import OrderedDict
from types import SimpleNamespace
import numpy as np

import src.models.cnn_artifact_detector as m
Clase = m.EEGWindowDataset

def fake(patient, session, section, *a, **k):
    return {"data": np.full((18, 100), float(section[1:]))}
m.get_or_compute_session = fake

stub = SimpleNamespace(
    _session_cache=OrderedDict(),
    _estimated_session_bytes=None,
    max_cached_sessions=10,
    session_cache_dir=None,
    ica_cache_dir=None,
)

a = Clase._get_session(stub, "aaaaabbn", "s009", "t000", "x.edf")
b = Clase._get_session(stub, "aaaaabbn", "s009", "t003", "x.edf")

print("misma señal?", a is b, "| valores:", a["data"][0, 0], b["data"][0, 0])
assert a is not b and a["data"][0, 0] != b["data"][0, 0], "COLISIÓN"
print("OK: secciones distintas no se pisan")
