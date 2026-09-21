# pipelines/artifacts/check_coverage.py: diagnóstico de una sola vez, no modifica nada
from src.core.data_config import ARTIFACT_KEYWORDS, WINDOW_REQUESTS_ARTIFACTS
from src.core.data_loader import build_annotations_index, find_project_root
from src.core.windowing import get_or_build_windows

UMBRAL = 0.7                                                  # umbral_artefacto de label_windowing
WINDOWS_DIR = find_project_root("src") / "outputs" / "artifact" / "windows"

def union_len(iv):
    total, cs, ce = 0.0, None, None
    for a, b in sorted(iv):
        if ce is None or a > ce:
            if ce is not None: total += ce - cs
            cs, ce = a, b
        else:
            ce = max(ce, b)
    return total + (ce - cs if ce is not None else 0.0)

ann = build_annotations_index("artifact", paths=True)         # lento: abre los headers de los EDF
labs = ann["label"].astype(str)
tok = {l: set(l.lower().split("_")) for l in labs.unique()}

for artifact, req in WINDOW_REQUESTS_ARTIFACTS.items():
    size, stride = req["window_size_sec"], req["stride_sec"]
    if stride != size:
        print(f"[SKIP] {artifact}: ventanas solapadas, la cota no aplica")
        continue
    windowed = get_or_build_windows(ann, req, ARTIFACT_KEYWORDS, WINDOWS_DIR)
    kws = ARTIFACT_KEYWORDS[artifact]
    sel = ann[labs.map(lambda l: bool(tok[l] & kws))]
    secs = sum(union_len(zip(g["start_time"], g["stop_time"]))
               for _, g in sel.groupby(["Patient", "Session", "Section"]))
    bound = secs / (UMBRAL * size)
    actual = int(windowed[artifact].sum())
    print(f"{artifact}: unión {secs:,.0f} s | tope {bound:,.0f} | actuales {actual:,} | actuales/tope = {actual / bound:.2f}")