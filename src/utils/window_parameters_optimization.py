"""
# File: window_parameters_optimization.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos
"""
import numpy as np
import pandas as pd
from src.core.data_config import ARTIFACT_KEYWORDS
from src.core.data_loader import build_annotations_index

print("[INFO] Loading annotations to analyze sensitivity...")
ann = build_annotations_index("artifact", paths=True)
labs = ann["label"].astype(str)
tok = {l: set(l.lower().split("_")) for l in labs.unique()}
dur = ann.drop_duplicates(["Patient", "Session", "Section"]).set_index(["Patient", "Session", "Section"])["Duration"]

# Sensitivity tests
window_sizes = [0.5, 1.0, 1.5, 2.0]
thresholds = [0.3, 0.4, 0.5, 0.6, 0.7]

results = []

for artifact, kws in ARTIFACT_KEYWORDS.items():
    sel = ann[labs.map(lambda l: bool(tok[l] & kws))]
    
    print(f" Sensitivity analysis: {artifact.upper()}")
    
    for size in window_sizes:
        # Theorical windowing
        cov = {}
        for key, g in sel.groupby(["Patient", "Session", "Section"]):
            cur_s = cur_e = None
            merged = []
            for a, b in sorted(zip(g["start_time"], g["stop_time"])):
                if cur_e is None or a > cur_e:
                    if cur_e is not None: merged.append((cur_s, cur_e))
                    cur_s, cur_e = a, b
                else:
                    cur_e = max(cur_e, b)
            if cur_e is not None: merged.append((cur_s, cur_e))
            
            session_dur = dur.get(key, 1e9)
            for a, b in merged:
                b = min(b, session_dur)
                for k in range(int(a // size), int(np.ceil(b / size))):
                    ov = min(b, (k + 1) * size) - max(a, k * size)
                    if ov > 0:
                        cov[key + (k * size,)] = cov.get(key + (k * size,), 0.0) + ov

        for thr in thresholds:
            valid_windows = [v for v in cov.values() if (v / size) >= thr]
            n_positives = len(valid_windows)
            
            results.append({
                "artifact": artifact,
                "window_size_sec": size,
                "threshold": thr,
                "n_positive_windows": n_positives
            })

df_res = pd.DataFrame(results)
print("\nPositive windows and threshold:")
print(df_res.pivot_table(index=["artifact", "window_size_sec"], columns="threshold", values="n_positive_windows").to_string())