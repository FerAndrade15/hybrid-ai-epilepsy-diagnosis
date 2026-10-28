"""
# File: tune_postprocess.py
# Project: Trabajo de graduación
"""
import argparse, json, numpy as np, pandas as pd, optuna
from src.core.data_config import OUTPUTS_DIR
from src.core.data_loader import build_annotations_index
from backend.ml_service.utils.postprocess import evaluate, merge_intervals, DEFAULT_PP

ap = argparse.ArgumentParser()
ap.add_argument("--trials", type=int, default=300)
ap.add_argument("--max-fa-day", type=float, default=10.0)
ap.add_argument("--eval-test", action="store_true", help="evalúa en test con los parámetros congelados")
args = ap.parse_args()

PP_DIR = OUTPUTS_DIR / "seizure" / "pp_probs"
OUT_JSON = PP_DIR / "postprocess_frozen.json"
sess = pd.read_csv(PP_DIR / "sessions.csv")
ann = build_annotations_index("seizure", n_patients=None, paths=True,
                              CACHE_DIR=OUTPUTS_DIR / "seizure" / "annotations")

def build_records(split):
    recs = []
    ann_g = {k: g for k, g in ann.groupby(["Patient", "Session", "Section"])}
    for r in sess[sess.split == split].itertuples():
        z = np.load(PP_DIR / f"{r.Patient}_{r.Session}_{r.Section}.npz")
        g = ann_g[(r.Patient, r.Session, r.Section)]
        g = g[g["is_positive"] == 1]                         # ajusta nombres si difieren
        ref = merge_intervals(zip(g["start_time"], g["stop_time"]))
        recs.append(dict(probs=z["probs"].astype(np.float32), sfreq=float(z["sfreq"]),
                         ref=ref, patient=r.Patient))
    return recs

def objective_value(m):
    pen = max(0.0, m["fa_per_day"] - args.max_fa_day) / args.max_fa_day
    return m["sens"] - pen - 1e-4 * m["fa_per_day"]          # desempate: menos FA

def report(tag, recs, pp):
    m = evaluate(recs, pp, recs[0]["sfreq"])
    print(f"[{tag}] sens={m['sens']:.3f} FA/día={m['fa_per_day']:.1f} "
          f"eventos={m['n_ref']} horas={m['hours']:.1f}")
    return m

if not args.eval_test:
    val = build_records("val")
    raw_pp = dict(smooth_sec=0.0, thr_on=0.5, thr_off_ratio=1.0, merge_gap_sec=0.0, min_dur_sec=0.0)
    report("val baseline crudo", val, raw_pp)

    def objective(trial):
        pp = dict(smooth_sec=trial.suggest_float("smooth_sec", 0.0, 5.0),
                  thr_on=trial.suggest_float("thr_on", 0.3, 0.95),
                  thr_off_ratio=trial.suggest_float("thr_off_ratio", 0.3, 1.0),
                  merge_gap_sec=trial.suggest_float("merge_gap_sec", 0.0, 30.0),
                  min_dur_sec=trial.suggest_float("min_dur_sec", 0.0, 30.0))
        return objective_value(evaluate(val, pp, val[0]["sfreq"]))

    study = optuna.create_study(direction="maximize", sampler=optuna.samplers.TPESampler(seed=42))
    study.optimize(objective, n_trials=args.trials)
    best = study.best_params
    m_val = report("val ajustado", val, best)

    # estabilidad: perturba ±20% cada parámetro y mira cuánto cae el objetivo
    drops = []
    for k in best:
        for f in (0.8, 1.2):
            q = dict(best); q[k] = best[k] * f
            drops.append(objective_value(evaluate(val, q, val[0]["sfreq"])))
    print(f"[estabilidad] objetivo óptimo={study.best_value:.3f} | peor con ±20%={min(drops):.3f}")

    OUT_JSON.write_text(json.dumps(dict(postprocess=best, val=m_val,
                                        max_fa_day=args.max_fa_day, test=None), indent=2))
    print("[OK] congelado en", OUT_JSON)

    from epileptic_eeg_analysis_toolbox.backend.ml_service.models_registry import PP_DIR
    
    PP_DIR.mkdir(parents=True, exist_ok=True)
    (PP_DIR / f"{args.model_key}.json").write_text(json.dumps(
        dict(postprocess=best, tuned_on="val", n_val_sessions=len(val),
            max_fa_day=args.max_fa_day, val=m_val), indent=2))

else:
    cfg = json.loads(OUT_JSON.read_text())
    if cfg["test"] is not None:
        raise SystemExit("Test ya evaluado con estos parámetros. Re-ajusta en val antes de repetir.")
    test = build_records("test")
    report("test crudo", test, dict(smooth_sec=0.0, thr_on=0.5, thr_off_ratio=1.0,
                                    merge_gap_sec=0.0, min_dur_sec=0.0))
    cfg["test"] = report("test congelado", test, cfg["postprocess"])
    OUT_JSON.write_text(json.dumps(cfg, indent=2))