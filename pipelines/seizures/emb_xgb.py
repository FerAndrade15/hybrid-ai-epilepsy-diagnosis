"""Embeddings (CNN+LSTM-PSD y SeizureTransformer) -> XGBoost GPU, TUSZ.

Colocar en pipelines/seizures/emb_xgb.py y correr desde la raíz del repo:

  uv run python -u -m pipelines.seizures.emb_xgb --stage extract_cnn --limit-sessions 3   # prueba
  uv run python -u -m pipelines.seizures.emb_xgb --stage extract_cnn
  uv run python -u -m pipelines.seizures.emb_xgb --stage train --variants cnn --trials 15
  # despues, si hay tiempo:
  uv run python -u -m pipelines.seizures.emb_xgb --stage extract_tr
  uv run python -u -m pipelines.seizures.emb_xgb --stage train --variants tr concat --trials 15

Protocolo identico al de tu pipeline: mismas ventanas (predict_sessions), umbral elegido en val
y reporte con full_report / window_metrics. El XGBoost entra como una columna p_seiz mas.
"""
import argparse
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd
import torch

SPLITS = ("train", "val", "test")
SFREQ_TR, WIN_TR_S, STRIDE_TR_S = 256, 60, 30          # SeizureTransformer: 60 s @ 256 Hz
PROJECT = Path(__file__).resolve().parents[2]


# ---------------------------------------------------------------- utilidades puras (testeables)
def chunk_starts(S, win=WIN_TR_S, stride=STRIDE_TR_S):
    """Inicios (en segundos enteros) de chunks de 60 s con paso 30 s; el ultimo termina en S."""
    if S < win:
        return []
    st = list(range(0, S - win + 1, stride))
    if st[-1] != S - win:
        st.append(S - win)
    return st


def assemble_seconds(S, starts, chunk_emb, win=WIN_TR_S, stride=STRIDE_TR_S):
    """chunk_emb[k] (win, D) -> E (S, D). Cada segundo sale del chunk donde esta mas al centro."""
    D = chunk_emb[0].shape[1]
    E = np.zeros((S, D), np.float32)
    covered = 0
    for k, s in enumerate(starts):
        hi = S if k == len(starts) - 1 else s + win - (win - stride) // 2     # centro del chunk: s+45
        E[covered:hi] = chunk_emb[k][covered - s:hi - s]
        covered = hi
    return E


def window_means(E, start_s, end_s):
    """Media de E (S, D) sobre los segundos que cubre cada ventana [start_s, end_s)."""
    S = len(E)
    C = np.vstack([np.zeros((1, E.shape[1])), np.cumsum(E.astype(np.float64), 0)])
    lo = np.clip(np.floor(np.asarray(start_s) + 1e-6).astype(int), 0, S - 1)
    hi = np.clip(np.ceil(np.asarray(end_s) - 1e-6).astype(int), 1, S)
    hi = np.maximum(hi, lo + 1)
    return ((C[hi] - C[lo]) / (hi - lo)[:, None]).astype(np.float32)


def f1_threshold(y, p):
    from sklearn.metrics import precision_recall_curve
    pr, rc, th = precision_recall_curve(y, p)
    f1 = 2 * pr * rc / np.clip(pr + rc, 1e-12, None)
    return float(th[np.argmax(f1[:-1])])


def f1_at(y, p, t):
    pred = p >= t
    tp = (pred & (y == 1)).sum(); fp = (pred & (y == 0)).sum(); fn = (~pred & (y == 1)).sum()
    return 2 * tp / max(2 * tp + fp + fn, 1)


def patient_bootstrap(y, p_new, p_old, pid, t_new, t_old, n=300, seed=0):
    """IC95% de la diferencia (nuevo - CNN+LSTM) remuestreando PACIENTES."""
    from sklearn.metrics import roc_auc_score
    rng = np.random.default_rng(seed)
    ids = np.unique(pid)
    idx = {i: np.where(pid == i)[0] for i in ids}
    dA, dF = [], []
    for _ in range(n):
        s = np.concatenate([idx[i] for i in rng.choice(ids, len(ids))])
        if y[s].min() == y[s].max():
            continue
        dA.append(roc_auc_score(y[s], p_new[s]) - roc_auc_score(y[s], p_old[s]))
        dF.append(f1_at(y[s], p_new[s], t_new) - f1_at(y[s], p_old[s], t_old))
    ci = lambda v: [float(np.percentile(v, 2.5)), float(np.percentile(v, 97.5))]
    return {"d_auroc_ci95": ci(dA), "d_f1_ci95": ci(dF)}


# ---------------------------------------------------------------- indices (copiados de tu pipeline)
def build_indices(ann_dir):
    from src.core.data_config import SEIZURE_MULTILABELS, PARTITION_TO_SPLIT
    from src.core.windowing import split_compound_label
    from src.core.data_loader import build_annotations_index
    from src.utils.patient_registry import load_registry, forced_for
    ann_df = build_annotations_index("seizure", n_patients=None, paths=True, CACHE_DIR=ann_dir)
    ann_df["EDF_path"] = ann_df["EDF"]
    ann_df["is_positive"] = ann_df["label"].map(
        lambda l: int(bool(split_compound_label(str(l)) & SEIZURE_MULTILABELS)))
    forced = forced_for(load_registry(), ann_df["Patient"].unique(), source_prefix="folder:seizure")
    ann_df["split"] = ann_df["Patient"].map(forced)
    off = ann_df["Partition"].map(PARTITION_TO_SPLIT)
    # IMPORTANTE para el transformer preentrenado: si esto no es ~100 %, puede haber fuga.
    print(f"[CHECK] registro == partición oficial: {(ann_df['split'] == off).mean():.1%}")
    ann_df = ann_df[ann_df["split"].notna()].reset_index(drop=True)
    return {s: ann_df[ann_df["split"] == s].reset_index(drop=True) for s in SPLITS}


# ---------------------------------------------------------------- extraccion CNN+LSTM
def extract_cnn(args, idx, device, model_dir, emb_dir):
    from src.core.data_config import SEIZURE_MULTILABELS, SEIZURE_SESSION_CACHE
    from src.models.aitrics_cnn_lstm import build_model, predict_sessions
    taxonomy = {"seiz": SEIZURE_MULTILABELS}
    cfg = json.loads((model_dir / "config.json").read_text())
    print(f"[INFO] config.json: {cfg}")     # configs viejas pueden no traer dropout
    model = build_model(enc=cfg.get("enc", "psd"), n_out=1, hidden=cfg.get("hidden", 256),
                        n_layers=cfg.get("n_layers", 2), dropout=cfg.get("dropout", 0.1))
    model.load_state_dict(torch.load(model_dir / "best.pt", map_location=device))
    model.to(device).eval()
    buf = []
    # Entrada del clasificador = salida del LSTM por ventana: (B*Nw, hidden), en orden de ventana.
    model.classifier.register_forward_pre_hook(lambda m, inp: buf.append(inp[0].detach().float().cpu()))
    for s in SPLITS:
        buf.clear()
        t0 = time.time()
        preds = predict_sessions(model, idx[s], taxonomy, device, max_sessions=args.limit_sessions,
                                 session_cache_dir=str(SEIZURE_SESSION_CACHE))
        emb = torch.cat(buf).numpy()
        assert len(emb) == len(preds), f"{s}: {len(emb)} embeddings vs {len(preds)} ventanas"
        preds.to_parquet(emb_dir / f"preds_{s}.parquet", index=False)
        np.save(emb_dir / f"cnn_{s}.npy", emb)
        print(f"[ok] cnn/{s}: emb{emb.shape} positivos={int(preds['y_seiz'].sum())}  {time.time()-t0:.0f}s")
        old = model_dir / f"preds_{s}.parquet"
        if old.exists() and not args.limit_sessions and s != "train":
            o = pd.read_parquet(old)
            if len(o) == len(preds):
                print(f"[CHECK] {s}: max|p_seiz nuevo - guardado| = {np.abs(o['p_seiz'].values - preds['p_seiz'].values).max():.2e}")
            else:
                print(f"[WARN] {s}: tamaños distintos ({len(o)} vs {len(preds)})")


# ---------------------------------------------------------------- extraccion SeizureTransformer
def extract_tr(args, idx, device, emb_dir):
    from src.core.data_config import SEIZURE_SESSION_CACHE, MONOPOLAR_CHANNELS
    from src.models.large_eeg_u_transformer import SeizureTransformer     # ajusta si tu ruta difiere
    from src.utils.session_cache import get_or_compute_session
    torch.backends.cuda.matmul.allow_tf32 = True
    raw = torch.load(args.tr_weights, map_location="cpu", weights_only=True)
    sd = raw.get("model_state_dict", raw.get("state_dict", raw))
    model = SeizureTransformer(in_channels=sd["encoder.convs.0.weight"].shape[1], in_samples=WIN_TR_S * SFREQ_TR)
    model.load_state_dict(sd, strict=True)
    model.to(device).eval()
    store = []
    # x = salida del transformer + residual, justo antes del decoder: (B, 512, 480)
    model.decoder_d.register_forward_pre_hook(lambda m, inp: store.append(inp[0].detach()))
    cols = ["Patient", "Session", "Section", "EDF_path"]
    for s in SPLITS:
        t0, keys, arrs, n_skip = time.time(), [], [], 0
        for n_done, ((pat, ses, sec, edf), _) in enumerate(idx[s].groupby(cols, dropna=False)):
            if args.limit_sessions and n_done >= args.limit_sessions:
                break
            try:
                sess = get_or_compute_session(patient=pat, session=ses, section=sec, path_edf=edf,
                                              use_ica=False, bipolar_montage=False,
                                              cache_dir=str(SEIZURE_SESSION_CACHE))
            except ValueError as e:
                if "Missing channels" in str(e) or "Short signal" in str(e):
                    n_skip += 1
                    continue
                raise
            assert sess["sfreq"] == SFREQ_TR and sess["ch_names"] == MONOPOLAR_CHANNELS, "montaje/frecuencia inesperados"
            x = np.ascontiguousarray(sess["data"], dtype=np.float32)
            S = x.shape[1] // SFREQ_TR
            starts = chunk_starts(S)
            if not starts:
                n_skip += 1
                continue
            outs = []
            with torch.inference_mode():
                for i in range(0, len(starts), args.tr_batch):
                    batch = np.stack([x[:, a * SFREQ_TR:(a + WIN_TR_S) * SFREQ_TR] for a in starts[i:i + args.tr_batch]])
                    store.clear()
                    prob = model(torch.from_numpy(batch).to(device))                # (B, 15360)
                    z = store[0]                                                    # (B, 512, 480)
                    B, C, T = z.shape
                    z = z.reshape(B, C, WIN_TR_S, T // WIN_TR_S).mean(-1).permute(0, 2, 1)       # (B, 60, 512)
                    p = prob.reshape(B, WIN_TR_S, -1)                                              # (B, 60, 256)
                    feat = torch.cat([z, p.mean(-1, keepdim=True), p.amax(-1, keepdim=True)], -1)  # (B, 60, 514)
                    outs.extend(feat.float().cpu().numpy())
            arrs.append(assemble_seconds(S, starts, outs).astype(np.float16))
            keys.append(f"{pat}_{ses}_{sec}")
        lens = np.array([len(a) for a in arrs])
        np.savez(emb_dir / f"tr_{s}.npz", emb=np.concatenate(arrs), keys=np.array(keys), lens=lens)
        print(f"[ok] tr/{s}: {len(keys)} sesiones, {int(lens.sum())} s, omitidas={n_skip}  {time.time()-t0:.0f}s")


def tr_to_windows(preds, path):
    z = np.load(path)
    emb, keys, lens = z["emb"], z["keys"], z["lens"]
    off = dict(zip(keys, np.concatenate([[0], np.cumsum(lens)[:-1]])))
    ln = dict(zip(keys, lens))
    X = np.full((len(preds), emb.shape[1]), np.nan, np.float32)      # NaN: XGBoost lo maneja
    for k, g in preds.groupby("key", sort=False):
        if k in off:
            E = emb[off[k]:off[k] + ln[k]].astype(np.float32)
            X[g.index.values] = window_means(E, g["start_s"].values, g["end_s"].values)
    return X


# ---------------------------------------------------------------- XGBoost
def load_X(variant, split, emb_dir):
    preds = pd.read_parquet(emb_dir / f"preds_{split}.parquet")
    parts = []
    if variant in ("cnn", "concat"):
        parts.append(np.load(emb_dir / f"cnn_{split}.npy"))
    if variant in ("tr", "concat"):
        parts.append(tr_to_windows(preds, emb_dir / f"tr_{split}.npz"))
    return np.concatenate(parts, 1), preds


def train_variant(variant, args, emb_dir, device):
    import xgboost as xgb
    from sklearn.metrics import average_precision_score, roc_auc_score
    from src.core.data_config import WINDOWS_REQUESTS_SEIZURES
    from src.utils.seizure_eval import full_report, window_metrics
    data = {s: load_X(variant, s, emb_dir) for s in SPLITS}
    (Xtr, ptr), (Xv, pv), (Xte, pte) = data["train"], data["val"], data["test"]
    ytr, yv, yte = (d[1]["y_seiz"].values.astype(int) for d in (data["train"], data["val"], data["test"]))
    spw = float((ytr == 0).sum() / max((ytr == 1).sum(), 1))
    rng, best = np.random.default_rng(0), None
    for t in range(args.trials):
        prm = dict(max_depth=6, learning_rate=0.1, subsample=0.8, colsample_bytree=0.8,
                   min_child_weight=1, reg_lambda=1, gamma=0) if t == 0 else dict(
            max_depth=int(rng.choice([4, 6, 8, 10])), learning_rate=float(rng.choice([0.03, 0.05, 0.1])),
            subsample=float(rng.choice([0.6, 0.8, 1.0])), colsample_bytree=float(rng.choice([0.4, 0.6, 0.8, 1.0])),
            min_child_weight=float(rng.choice([1, 5, 20])), reg_lambda=float(rng.choice([1, 5, 20])),
            gamma=float(rng.choice([0, 0.5, 2])))
        clf = xgb.XGBClassifier(n_estimators=3000, early_stopping_rounds=50, eval_metric="aucpr",
                                tree_method="hist", device=device.type, scale_pos_weight=spw,
                                random_state=0, **prm)
        t0 = time.time()
        clf.fit(Xtr, ytr, eval_set=[(Xv, yv)], verbose=False)
        pvv = clf.predict_proba(Xv)[:, 1]
        sc = average_precision_score(yv, pvv)                          # seleccion SOLO con val
        print(f"[{variant}] trial {t:02d} val AUPRC={sc:.4f} iters={clf.best_iteration} {time.time()-t0:.0f}s", flush=True)
        if best is None or sc > best[0]:
            best = (sc, prm, clf, pvv)
    sc, prm, clf, p_val = best
    p_test = clf.predict_proba(Xte)[:, 1]
    out = emb_dir / f"xgb_{variant}"
    out.mkdir(exist_ok=True)
    clf.save_model(out / "model.json")
    pv2, pt2 = pv.copy(), pte.copy()
    pv2["p_seiz"], pt2["p_seiz"] = p_val, p_test
    pv2.to_parquet(out / "preds_val.parquet", index=False)
    pt2.to_parquet(out / "preds_test.parquet", index=False)
    report = full_report(val_preds=pv2, test_preds=pt2, margin_sec=5,
                         window_size_sec=WINDOWS_REQUESTS_SEIZURES["win_sec"],
                         shift_sec=WINDOWS_REQUESTS_SEIZURES["shift_sec"])
    report.insert(0, "variant", variant)
    report.to_csv(out / "report.csv", index=False)
    wm = window_metrics(pt2, dict(zip(report["Class"], report["Best_Threshold"])),
                        shift_sec=WINDOWS_REQUESTS_SEIZURES["shift_sec"])
    wm.insert(0, "variant", variant)
    wm.to_csv(out / "window_metrics.csv", index=False)
    # comparacion pareada contra la propia CNN+LSTM (columna p_seiz original, mismas ventanas)
    t_new, t_old = f1_threshold(yv, p_val), f1_threshold(yv, pv["p_seiz"].values)
    ci = patient_bootstrap(yte, p_test, pte["p_seiz"].values, pte["Patient"].values, t_new, t_old)
    summ = {"variant": variant, "best_params": prm, "val_auprc": sc, "scale_pos_weight": spw,
            "test_auroc_xgb": float(roc_auc_score(yte, p_test)),
            "test_auroc_cnn_lstm": float(roc_auc_score(yte, pte["p_seiz"].values)), **ci}
    json.dump(summ, open(out / "summary.json", "w"), indent=2)
    print(f"\n== {variant} ==\n{report.round(3).to_string(index=False)}\n{wm.round(3).to_string(index=False)}\n{json.dumps(summ, indent=2)}\n")


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", choices=["extract_cnn", "extract_tr", "train"], required=True)
    ap.add_argument("--variants", nargs="+", default=["cnn"], choices=["cnn", "tr", "concat"])
    ap.add_argument("--trials", type=int, default=15)
    ap.add_argument("--model-name", default=None, help="carpeta en models/, p.ej. cnn2d_lstm_psd_v6 (default: v{VERSION})")
    ap.add_argument("--limit-sessions", type=int, default=None, help="prueba rápida por split")
    ap.add_argument("--tr-batch", type=int, default=16)
    ap.add_argument("--tr-weights", default=str(PROJECT / "epileptic_eeg_analysis_toolbox" / "models_weights" / "seizure_transformer.pth"))
    args = ap.parse_args()

    from src.core.data_config import OUTPUTS_DIR, VERSION
    from src.models.aitrics_cnn_lstm import get_device
    device = get_device()
    corpus = OUTPUTS_DIR / "seizure" / "full"
    model_name = args.model_name or f"cnn2d_lstm_psd_v{VERSION}"
    emb_dir = corpus / ("emb_xgb_smoke" if args.limit_sessions else "emb_xgb") / model_name
    emb_dir.mkdir(parents=True, exist_ok=True)
    model_dir = corpus / "models" / model_name
    ann_dir = OUTPUTS_DIR / "seizure" / "annotations"
    print(f"[INFO] device={device} emb_dir={emb_dir}")

    if args.stage == "extract_cnn":
        extract_cnn(args, build_indices(ann_dir), device, model_dir, emb_dir)
    elif args.stage == "extract_tr":
        extract_tr(args, build_indices(ann_dir), device, emb_dir)
    else:
        for v in args.variants:
            train_variant(v, args, emb_dir, device)


if __name__ == "__main__":
    main()
