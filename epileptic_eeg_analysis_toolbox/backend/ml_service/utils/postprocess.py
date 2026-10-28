"""
# File: postprocess
# Project: Trabajo de graduación

Time analysis for events recognition to adjust model results.
"""
import numpy as np
from scipy.ndimage import uniform_filter1d, label

DEFAULT_PP = dict(smooth_sec=2.0, thr_on=0.5, thr_off_ratio=0.6,
                  merge_gap_sec=12.0, min_dur_sec=10.0)

def _runs(mask):
    d = np.diff(np.concatenate(([0], mask.astype(np.int8), [0])))
    return np.flatnonzero(d == 1), np.flatnonzero(d == -1)      # fin exclusivo

def probs_to_events(probs, sfreq, pp):
    """probs (N,) por muestra -> [(inicio_s, fin_s, confianza)]"""
    p = np.asarray(probs, dtype=np.float32).reshape(-1)
    w = max(1, int(pp["smooth_sec"] * sfreq))
    if w > 1:
        p = uniform_filter1d(p, size=w, mode="nearest")

    thr_on = pp["thr_on"]
    thr_off = thr_on * pp["thr_off_ratio"]            # histéresis: off <= on siempre
    lab, _ = label(p > thr_off)
    keep = np.unique(lab[p > thr_on]); keep = keep[keep > 0]
    starts, ends = _runs(np.isin(lab, keep))

    gap, mind = pp["merge_gap_sec"] * sfreq, pp["min_dur_sec"] * sfreq
    merged = []
    for s, e in zip(starts, ends):                    # une huecos pequeños
        if merged and s - merged[-1][1] <= gap:
            merged[-1][1] = e
        else:
            merged.append([s, e])
    return [(s / sfreq, e / sfreq, float(p[s:e].mean()))
            for s, e in merged if e - s >= mind]     # descarta cortos

def merge_intervals(iv):
    out = []
    for s, e in sorted(iv):
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return [tuple(x) for x in out]

def overlap_counts(ref, hyp):
    """OVLP: (hit, miss, falsas alarmas) en eventos."""
    ov = lambda a, b: a[1] > b[0] and a[0] < b[1]
    hit = sum(any(ov(r, h) for h in hyp) for r in ref)
    fal = sum(not any(ov(h, r) for r in ref) for h in hyp)
    return hit, len(ref) - hit, fal

def evaluate(records, pp, sfreq=256):
    hit = mis = fal = 0
    secs = 0.0
    for r in records:
        hyp = [(s, e) for s, e, _ in probs_to_events(r["probs"], sfreq, pp)]
        h, m, f = overlap_counts(r["ref"], hyp)
        hit += h; mis += m; fal += f
        secs += len(r["probs"]) / sfreq
    return dict(sens=hit / max(hit + mis, 1), fa_per_day=fal / max(secs / 86400, 1e-9),
                n_ref=hit + mis, n_fa=fal, hours=secs / 3600)