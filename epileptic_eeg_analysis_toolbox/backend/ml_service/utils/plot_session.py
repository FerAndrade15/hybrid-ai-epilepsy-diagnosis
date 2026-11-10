import argparse
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from backend.pipelines.data_loader import load_raw_edf
from backend.ml_service.utils.preprocessing import raw_data_preproccesing
from backend.ml_service.utils.data_loader import build_annotations_index
from backend.ml_service.utils.data_config import OUTPUTS_DIR
from backend.ml_service.utils.postprocess import probs_to_events
from backend.ml_service.utils.postprocess import merge_intervals

ap = argparse.ArgumentParser()
ap.add_argument("--key", required=True)
ap.add_argument("--t0", type=float, default=0.0)
ap.add_argument("--t1", type=float, default=None)
ap.add_argument("--channels", nargs="+",
                default=["FP1", "F7", "T7", "P7", "O1", "C3"])
args = ap.parse_args()

PP = OUTPUTS_DIR / "seizure" / "pp_probs"
P, S, T = args.key.split("_")
z = np.load(PP / (args.key + ".npz"))
p, sf = z["probs"].astype(np.float32), float(z["sfreq"])

ann = build_annotations_index(
    "seizure", n_patients=None, paths=True,
    CACHE_DIR=OUTPUTS_DIR / "seizure" / "annotations")
g = ann[(ann.Patient == P) & (ann.Session == S) & (ann.Section == T)]
lab = g["label"].astype(str).str.strip().str.lower()
pos = g[lab != "bckg"]
ref = merge_intervals(zip(pos.start_time, pos.stop_time))

RAW = dict(smooth_sec=0.0, thr_on=0.5, thr_off_ratio=1.0,
           merge_gap_sec=0.0, min_dur_sec=0.0)
tuned = json.loads((PP / "postprocess_frozen.json").read_text())["postprocess"]
ev_raw = [(s, e) for s, e, _ in probs_to_events(p, sf, RAW)]
ev_tun = [(s, e) for s, e, _ in probs_to_events(p, sf, tuned)]
print("eventos crudo:", len(ev_raw), "| ajustado:", len(ev_tun),
      "| referencia:", len(ref))

raw = load_raw_edf(g.EDF.iloc[0], preloaD=True)
prep = raw_data_preproccesing(
    raw_data=raw, l_freq=1.0, h_freq=100.0, notch_freq=60.0,
    bipolar_montage=False, resampling_freq=256)
data = prep.get_data(picks=args.channels) * 1e6

dur = len(p) / sf
t0 = max(0.0, args.t0)
t1 = min(args.t1 if args.t1 else dur, dur)
i0, i1 = int(t0 * sf), int(t1 * sf)
tt = np.arange(i0, i1) / sf
d = data[:, i0:i1]
step = 2.0 * np.percentile(np.abs(d), 99)

fig, ax = plt.subplots(3, 1, figsize=(14, 9), sharex=True,
                       gridspec_kw=dict(height_ratios=[4, 2, 1.5]))
n = len(args.channels)
for k, ch in enumerate(args.channels):
    ax[0].plot(tt, d[k] - d[k].mean() + (n - 1 - k) * step,
               lw=0.5, color="k")
ax[0].set_yticks([(n - 1 - k) * step for k in range(n)])
ax[0].set_yticklabels(args.channels)
ax[0].set_title(args.key)

ax[1].plot(tt[::4], p[i0:i1:4], lw=0.8)
ax[1].axhline(tuned["thr_on"], color="r", ls="--", lw=0.8)
ax[1].axhline(0.5, color="gray", ls=":", lw=0.8)
ax[1].set_ylim(0, 1)
ax[1].set_ylabel("prob.")

rows = [("referencia", ref, "g"), ("crudo", ev_raw, "orange"),
        ("ajustado", ev_tun, "r")]
for j, (name, evs, col) in enumerate(rows):
    bars = [(s, e - s) for s, e in evs if e > t0 and s < t1]
    ax[2].broken_barh(bars, (j, 0.8), color=col)
ax[2].set_yticks([j + 0.4 for j in range(len(rows))])
ax[2].set_yticklabels([r[0] for r in rows])
ax[2].set_xlim(t0, t1)
ax[2].set_xlabel("tiempo (s)")

out = PP / ("plot_" + args.key + ".png")
fig.tight_layout()
fig.savefig(out, dpi=110)
print("[OK]", out)
