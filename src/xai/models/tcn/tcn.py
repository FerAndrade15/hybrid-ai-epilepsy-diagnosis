#!/usr/bin/env python
"""
Implementación de TCN, Hybrid and Trasnformer CON DATOS REALES (TUH)

Propósito del código
  1. Construye un subconjunto pequeño de datos reales (ventanas EDF -> features) y mide el costo de CPU por registro.
  2. Entrena N épocas con tu `_train_one_epoch` tal cual (baseline "como está hoy") y mide tiempo por época.
  3. Micro-benchmark de velocidad: batch_size, bf16 (autocast) y num_workers. Mide también cuánto espera la GPU por datos.
  4. Extrapola a tu entrenamiento completo (--full-records) para decidir cuántas épocas caben.
  5. Pruebas de sanidad: overfit de un mini-lote, determinismo en eval, independencia de batch, dependencia de señal/features.
  6. Evalúa AUC/AP sobre validación (OJO: tras una prueba corta NO es una medida de calidad, solo detecta fallos groseros).
  7. XAI: Integrated Gradients (con delta de completitud), oclusión, deleción top vs azar; mide tiempo por ventana.

Uso (desde la raíz del repo, donde existe `src/`):
    python smoke_real_data.py --cfg cfg.json --model tcn
    python smoke_real_data.py --cfg cfg.json --model tcn --train-root /ruta/edf/train --val-root /ruta/edf/dev
"""

from __future__ import annotations
 
import argparse
import contextlib
import copy
import importlib
import json
import sys
import time
from pathlib import Path
 
import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, Subset
 
sys.path.insert(0, str(next((p for p in [Path.cwd(), *Path(__file__).resolve().parents] if (p / "src").is_dir()), Path.cwd())))
 
RESULTS: list[tuple[str, str, str]] = []  # (nombre, estado, detalle)
REPORT: dict = {}
 
 
def verdict(name: str, status: str, detail: str = "") -> None:
    RESULTS.append((name, status, detail))
    print(f"  [{status}] {name}" + (f" — {detail}" if detail else ""))
 
 
def sync(device: torch.device) -> None:
    if device.type == "cuda":
        torch.cuda.synchronize()
 
 
def win_labels(y) -> np.ndarray:
    y = np.asarray(y)
    return (y.reshape(len(y), -1).max(axis=1) > 0.5).astype(np.float32)
 
 
def stratified_idx(labels: np.ndarray, max_n: int, rng: np.random.Generator) -> np.ndarray:
    n = len(labels)
    if n <= max_n:
        return np.arange(n)
    pos = np.where(labels > 0.5)[0]
    neg = np.where(labels <= 0.5)[0]
    n_pos = min(len(pos), max_n // 2)
    n_neg = min(len(neg), max_n - n_pos)
    sel = np.concatenate([rng.choice(pos, n_pos, replace=False) if n_pos else pos[:0],
                          rng.choice(neg, n_neg, replace=False) if n_neg else neg[:0]])
    return np.sort(sel)
 
 
def rank_corr(a: np.ndarray, b: np.ndarray) -> float:
    if len(a) < 3 or np.std(a) == 0 or np.std(b) == 0:
        return float("nan")
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    return float(np.corrcoef(ra, rb)[0, 1])
 
 
 
# --------------------------------------------------------------------------------------
# Compatibilidad con TUSZ v2.0.x: anotaciones "X.csv_bi" (el código de Sánchez busca "X_bi.csv")
# --------------------------------------------------------------------------------------
def patch_annotation_names(ds, balanced_pool: bool = False) -> None:
    """Parcha en memoria el módulo dataset (no modifica archivos): acepta `.csv_bi` y `_bi.csv`.
    balanced_pool=True (smoke): el descubrimiento devuelve un pool con positivos Y negativos, para que las cuotas
    de registros positivos/negativos puedan cumplirse (si no, los primeros N registros alfabéticos suelen ser todos fondo)."""
    orig_read = ds.read_intervals
 
    def read_intervals(csv_path):
        p = Path(csv_path)
        if not p.exists() and p.name.endswith("_bi.csv"):
            alt = p.with_name(p.name[: -len("_bi.csv")] + ".csv_bi")
            if alt.exists():
                p = alt
        return orig_read(p)
 
    def discover_records(base_dir, *, max_records, max_per_patient, include_background_only=False, montage=None):
        base_dir = Path(base_dir)
        if not base_dir.exists() or max_records <= 0:
            return []
        files = sorted(set(base_dir.rglob("*.csv_bi")) | set(base_dir.rglob("*_bi.csv")))
        files = [f for f in files if ds._matches_montage_filter(f, montage)]
        need = max_records
        pos, neg, seen = [], [], set()
        counts = {"pos": {}, "neg": {}}
        for ann in files:
            has_seizure = bool(read_intervals(ann))
            if not has_seizure and not include_background_only:
                continue
            name = ann.name
            stem = name[: -len(".csv_bi")] if name.endswith(".csv_bi") else name[: -len("_bi.csv")]
            edf = next((ann.with_name(stem + ext) for ext in (".edf", ".edf.gz")
                        if ann.with_name(stem + ext).exists()), None)
            if edf is None or not ds._matches_montage_filter(edf, montage):
                continue
            key = str(edf.resolve())
            pid = edf.stem.split("_")[0]
            bucket = "pos" if (balanced_pool and has_seizure) else "neg" if balanced_pool else "pos"
            if key in seen or (max_per_patient > 0 and counts[bucket].get(pid, 0) >= max_per_patient):
                continue
            (pos if bucket == "pos" else neg).append(edf)
            seen.add(key)
            counts[bucket][pid] = counts[bucket].get(pid, 0) + 1
            if balanced_pool:
                if len(pos) >= need and len(neg) >= need:
                    break
            elif len(pos) >= max_records:
                break
        return pos + neg
 
    def discover_records_multi(base_dirs, *, max_records, max_per_patient, include_background_only=False, montage=None):
        collected, seen, split_counts = [], set(), {}
        for base_dir in base_dirs:
            if not balanced_pool and len(collected) >= max_records:
                break
            for path in discover_records(base_dir, max_records=max_records, max_per_patient=max_per_patient,
                                         include_background_only=include_background_only, montage=montage):
                key = str(path.resolve())
                if key in seen:
                    continue
                parts = path.parts
                split_name = parts[parts.index("edf") + 1] if "edf" in parts and parts.index("edf") + 1 < len(parts) else "unknown"
                collected.append(path)
                seen.add(key)
                split_counts[split_name] = split_counts.get(split_name, 0) + 1
                if not balanced_pool and len(collected) >= max_records:
                    break
        return collected, split_counts
 
    ds.read_intervals = read_intervals
    ds.discover_records = discover_records
    ds.discover_records_multi = discover_records_multi
 
 
# --------------------------------------------------------------------------------------
# 1) Datos
# --------------------------------------------------------------------------------------
def build_bundle(ds, cfg, records, preprocess_settings, prefix, workdir):
    thr = int(float(cfg.dataset_auto_memmap_threshold_mb) * 1024 * 1024)
    return ds.build_windows_dataset(
        records,
        condition=cfg.condition,
        montage=cfg.montage,
        include_features=cfg.include_features,
        time_step_labels=cfg.time_step_labels,
        feature_subset=cfg.selected_features or None,
        window_sec=cfg.window_sec,
        hop_sec=cfg.hop_sec,
        eps=cfg.epsilon,
        target_fs=cfg.target_fs,
        preprocess_settings=preprocess_settings,
        include_background_only=cfg.include_background_only_records,
        sampling_strategy=cfg.sampling_strategy,
        sampling_seed=cfg.seed,
        tfrecord_export=None,
        storage_mode=cfg.dataset_storage,
        memmap_dir=str(Path(workdir) / "memmap"),
        memmap_prefix=prefix,
        auto_memmap_threshold_bytes=thr,
        feature_worker_processes=cfg.feature_worker_processes,
        feature_worker_chunk_size=cfg.feature_worker_chunk_size,
        feature_parallel_min_windows=cfg.feature_parallel_min_windows,
        force_memmap_after_build=cfg.dataset_force_memmap_after_build,
    )
 
 
 
# --------------------------------------------------------------------------------------
# Datos residentes en GPU (sin DataLoader / workers / pin_memory)
# --------------------------------------------------------------------------------------
_GPU_CACHE: dict = {}
 
 
def _unwrap(dataset):
    """WindowDataset o Subset(WindowDataset) -> (base, indices|None)."""
    if isinstance(dataset, Subset):
        return dataset.dataset, np.asarray(dataset.indices, dtype=np.int64)
    return dataset, None
 
 
def _copy_to_gpu(arr, idx, device, dtype, chunk=1024):
    n = len(idx) if idx is not None else arr.shape[0]
    out = torch.empty((n,) + tuple(arr.shape[1:]), dtype=dtype, device=device)
    for i in range(0, n, chunk):
        if idx is None:
            block = arr[i:i + chunk]
        else:
            block = arr[idx[i:i + chunk]]
        out[i:i + chunk] = torch.from_numpy(np.ascontiguousarray(block, dtype=np.float32)).to(device=device, dtype=dtype)
    return out
 
 
class GPULoader:
    """Reemplazo de DataLoader: los datos viven en la GPU y los lotes se arman allí.
    Entrega ((seq, feat), labels) o (seq, labels), igual que WindowDataset+DataLoader."""
 
    def __init__(self, dataset, batch_size=1, shuffle=False, drop_last=False, *, device, store_dtype, budget_gb, **_ignored):
        base, idx = _unwrap(dataset)
        key = (id(base), None if idx is None else (len(idx), int(idx[0]), int(idx[-1])), str(store_dtype))
        self.device = device
        self.dataset = dataset  # el pipeline lee dataloader.dataset.labels
        if key not in _GPU_CACHE:
            n = len(idx) if idx is not None else int(base.sequences.shape[0])
            per = int(np.prod(base.sequences.shape[1:])) * torch.empty((), dtype=store_dtype).element_size()
            need = n * per / 2**30
            free = torch.cuda.mem_get_info()[0] / 2**30
            if need > budget_gb or need > free - 4.0:
                raise MemoryError(f"{need:.1f} GB > presupuesto {budget_gb:.1f} GB / libre {free:.1f} GB")
            t0 = time.perf_counter()
            X = _copy_to_gpu(base.sequences, idx, device, store_dtype)
            labels = np.asarray(base.labels, dtype=np.float32)
            y = torch.from_numpy(labels if idx is None else labels[idx]).to(device)
            F = None
            if base.features is not None:
                F = _copy_to_gpu(base.features, idx, device, torch.float32)
            _GPU_CACHE[key] = (X, y, F)
            print(f"    [gpu-data] {n} ventanas -> GPU ({need:.1f} GB, {time.perf_counter() - t0:.0f}s)")
        self.X, self.y, self.F = _GPU_CACHE[key]
        self.n = self.X.shape[0]
        self.batch_size, self.shuffle, self.drop_last = batch_size, shuffle, drop_last
 
    def __len__(self):
        return self.n // self.batch_size if self.drop_last else -(-self.n // self.batch_size)
 
    def __iter__(self):
        order = torch.randperm(self.n, device=self.device) if self.shuffle else torch.arange(self.n, device=self.device)
        for i in range(0, self.n, self.batch_size):
            ix = order[i:i + self.batch_size]
            if self.drop_last and ix.numel() < self.batch_size:
                break
            seq = self.X[ix].float()
            if self.F is not None:
                yield (seq, self.F[ix]), self.y[ix]
            else:
                yield seq, self.y[ix]
 
 
def install_gpu_loader(pl, device, store_dtype, budget_gb):
    """Sustituye pl.DataLoader (usado por train_full_dataset / evaluate_dataset). Si no cabe, cae al DataLoader normal."""
    original = pl.DataLoader
 
    def factory(dataset, *a, **kw):
        try:
            return GPULoader(dataset, *a, device=device, store_dtype=store_dtype, budget_gb=budget_gb, **kw)
        except MemoryError as exc:
            print(f"    [gpu-data] no cabe ({exc}); se usa DataLoader normal para este conjunto")
            return original(dataset, *a, **kw)
    pl.DataLoader = factory
    print(f"  [gpu-data] activado (almacenamiento {store_dtype}, presupuesto {budget_gb:.0f} GB por conjunto)")
 
# --------------------------------------------------------------------------------------
# 3) Benchmark de velocidad
# --------------------------------------------------------------------------------------
def bench_variant(pl, model, dataset, *, bs, amp, workers, n_batches, device, loss_computer, label, gpu_data=False, store_dtype=torch.float32, budget_gb=14.0):
    m = copy.deepcopy(model).to(device)
    m.train()
    opt = torch.optim.AdamW(m.parameters(), lr=1e-4)
    bs = min(bs, len(dataset))
    if gpu_data:
        loader = GPULoader(dataset, batch_size=bs, shuffle=True, drop_last=len(dataset) >= bs,
                           device=device, store_dtype=store_dtype, budget_gb=budget_gb)
    else:
        loader = DataLoader(dataset, batch_size=bs, shuffle=True, drop_last=len(dataset) >= bs,
                            num_workers=workers, pin_memory=device.type == "cuda",
                            persistent_workers=workers > 0)
    warmup, done = 3, 0
    t_total = t_wait = 0.0
    if device.type == "cuda":
        torch.cuda.reset_peak_memory_stats()
    t_start = None
    while done < warmup + n_batches:
        it = iter(loader)
        while done < warmup + n_batches:
            t0 = time.perf_counter()
            try:
                batch = next(it)
            except StopIteration:
                break
            wait = time.perf_counter() - t0
            seq, feat, labels = pl._prepare_batch(batch, device)
            opt.zero_grad(set_to_none=True)
            with torch.autocast(device.type, dtype=torch.bfloat16, enabled=amp and device.type == "cuda"):
                logits, aux = pl._forward_model(m, seq, feat)
            logits = logits.float().view_as(labels)
            loss = loss_computer(logits, labels, weights=None)
            extra = pl._accumulate_aux_losses(aux)
            if extra is not None:
                loss = loss + extra.float()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(m.parameters(), 1.0)
            opt.step()
            done += 1
            if done == warmup:
                sync(device)
                t_start = time.perf_counter()
                t_wait = 0.0
            elif done > warmup:
                t_wait += wait
    sync(device)
    t_total = time.perf_counter() - t_start
    wps = bs * n_batches / t_total
    mem = torch.cuda.max_memory_allocated() / 2**30 if device.type == "cuda" else 0.0
    print(f"    {label:<28} {wps:8.1f} ventanas/s | espera datos {100 * t_wait / t_total:4.0f}% | pico GPU {mem:4.1f} GB")
    del m, opt, loader
    return {"label": label, "bs": bs, "amp": amp, "workers": workers, "gpu_data": gpu_data, "windows_per_s": wps,
            "data_wait_pct": 100 * t_wait / t_total, "peak_gb": mem}
 
 
# --------------------------------------------------------------------------------------
# 6) XAI
# --------------------------------------------------------------------------------------
def scalar_out(pl, model, x, feat):
    logits, _ = pl._forward_model(model, x, feat)
    return logits.reshape(x.size(0), -1).mean(dim=1)
 
 
def integrated_gradients(pl, model, x, feat, n_steps, chunk=16):
    """x: (1,T,C). Baseline = ceros (la señal ya viene normalizada por canal). feat se mantiene fija."""
    model.eval()
    base = torch.zeros_like(x)
    alphas = torch.linspace(0, 1, n_steps + 1, device=x.device)
    xs = base + alphas.view(-1, 1, 1) * (x - base)
    has_lstm = any(isinstance(mod, nn.LSTM) for mod in model.modules())
    ctx = torch.backends.cudnn.flags(enabled=False) if has_lstm else contextlib.nullcontext()
    grads, outs = [], []
    with ctx:
        for i in range(0, xs.size(0), chunk):
            xc = xs[i:i + chunk].clone().requires_grad_(True)
            fc = feat.expand(xc.size(0), -1) if feat is not None else None
            out = scalar_out(pl, model, xc, fc)
            g = torch.autograd.grad(out.sum(), xc)[0]
            grads.append(g.detach())
            outs.append(out.detach())
    grads = torch.cat(grads)
    outs = torch.cat(outs)
    avg_grad = ((grads[:-1] + grads[1:]) / 2).mean(dim=0, keepdim=True)
    attr = (x - base) * avg_grad
    delta = float(outs[-1] - outs[0])
    err = abs(float(attr.sum()) - delta)
    rel = err / max(abs(delta), 1e-6)
    return attr.detach(), float(outs[-1]), rel
 
 
@torch.no_grad()
def occlusion(pl, model, x, feat, seg=256, stride=128, chunk=32):
    model.eval()
    T = x.size(1)
    starts = list(range(0, max(1, T - seg + 1), stride))
    xs = x.expand(len(starts), -1, -1).clone()
    for k, s in enumerate(starts):
        xs[k, s:s + seg, :] = 0.0
    outs = []
    for i in range(0, len(starts), chunk):
        fc = feat.expand(min(chunk, len(starts) - i), -1) if feat is not None else None
        outs.append(scalar_out(pl, model, xs[i:i + chunk], fc))
    outs = torch.cat(outs)
    base = scalar_out(pl, model, x, feat)
    return (base - outs).cpu().numpy(), starts, seg
 
 
@torch.no_grad()
def deletion_drop(pl, model, x, feat, mask_idx):
    x2 = x.clone()
    x2[:, mask_idx, :] = 0.0
    return float((scalar_out(pl, model, x, feat) - scalar_out(pl, model, x2, feat)).item())
 
 
# --------------------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cfg", default="cfg.json")
    ap.add_argument("--model", default=None, choices=[None, "tcn", "hybrid", "transformer"])
    ap.add_argument("--pkg", default="src.xai.models.temporal_transformer",
                    help="paquete donde viven sanchez_transformer_{dataset,pipeline,utils}.py")
    ap.add_argument("--train-root", default=None)
    ap.add_argument("--val-root", default=None)
    ap.add_argument("--eval-root", default=None, help="carpeta edf/eval para la evaluación final (modo real)")
    ap.add_argument("--train-records", type=int, default=12)
    ap.add_argument("--val-records", type=int, default=4)
    ap.add_argument("--real", action="store_true",
                    help="entrenamiento REAL: corre tu pipeline completo (pl.main) con el cfg, sin recortar registros ni épocas. "
                         "Sin esta bandera = modo SMOKE (subconjunto pequeño + benchmark + pruebas de sanidad + XAI)")
    ap.add_argument("--epochs", type=int, default=None, help="smoke: 2 por defecto; real: usa el del cfg salvo que lo indiques")
    ap.add_argument("--max-train-windows", type=int, default=3000)
    ap.add_argument("--max-val-windows", type=int, default=1500)
    ap.add_argument("--bench-batches", type=int, default=25)
    ap.add_argument("--full-records", type=int, default=150, help="registros de tu entrenamiento completo, para extrapolar")
    ap.add_argument("--xai-windows", type=int, default=6)
    ap.add_argument("--ig-steps", type=int, default=32)
    ap.add_argument("--gpu-data", action="store_true",
                    help="real: mantiene las ventanas en la GPU (sin DataLoader). smoke: lo agrega al benchmark siempre")
    ap.add_argument("--gpu-data-dtype", default="fp32", choices=["fp32", "fp16"],
                    help="dtype de almacenamiento en GPU (fp16 = mitad de memoria; se convierte a fp32 al armar el lote)")
    ap.add_argument("--gpu-data-gb", type=float, default=14.0, help="tope de GB de GPU por conjunto de datos")
    ap.add_argument("--workdir", default="runs/smoke")
    ap.add_argument("--seed", type=int, default=13)
    ap.add_argument("--skip-bench", action="store_true")
    ap.add_argument("--skip-xai", action="store_true")
    args = ap.parse_args()
 
    ds = importlib.import_module(f"{args.pkg}.sanchez_transformer_dataset")
    pl = importlib.import_module(f"{args.pkg}.sanchez_transformer_pipeline")
    ut = importlib.import_module(f"{args.pkg}.sanchez_transformer_utils")
    from sklearn.preprocessing import StandardScaler
 
    workdir = Path(args.workdir)
    workdir.mkdir(parents=True, exist_ok=True)
    torch.manual_seed(args.seed)
    rng = np.random.default_rng(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Dispositivo: {device}" + (f" ({torch.cuda.get_device_name(0)})" if device.type == "cuda" else ""))
    if device.type != "cuda":
        print("  ⚠️ Sin GPU: los tiempos NO sirven para decidir nada.")
 
    # ---------------- Config ----------------
    cfg = copy.deepcopy(ut.load_config(args.cfg))
    if args.model:
        cfg.model = args.model
    if args.real:
        if args.epochs is not None:
            cfg.epochs = args.epochs
    else:
        cfg.jit_compile = False
        cfg.epochs = args.epochs if args.epochs is not None else 2
        cfg.max_records_train = args.train_records
        cfg.max_records_val = args.val_records
        for split, n in (("train", args.train_records), ("val", args.val_records)):
            if hasattr(cfg, f"max_records_{split}_positive"):
                setattr(cfg, f"max_records_{split}_positive", n // 2)
                setattr(cfg, f"max_records_{split}_negative", n - n // 2)
    if args.train_root:
        cfg.train_roots = [Path(args.train_root)]
    if args.val_root:
        cfg.val_roots = [Path(args.val_root)]
    if args.eval_root:
        cfg.eval_roots = [Path(args.eval_root)]
    cfg.dataset_memmap_dir = str(workdir / "memmap")
    has_quotas = any(getattr(cfg, f"max_records_{sp}_{k}", None)
                     for sp in ("train", "val", "eval") for k in ("positive", "negative"))
    patch_annotation_names(ds, balanced_pool=(not args.real) or has_quotas)
    if args.real:
        cfg.output_dir = workdir / "real"
        cfg_path = workdir / "cfg_real_effective.json"
        cfg_path.write_text(json.dumps(ut.config_to_dict(cfg), indent=2, default=str), encoding="utf-8")
        print(f"MODO REAL: modelo={cfg.model} épocas={cfg.epochs} registros train={cfg.max_records_train} "
              f"val={cfg.max_records_val} | cfg efectivo: {cfg_path}")
        if args.gpu_data and device.type == "cuda":
            install_gpu_loader(pl, device, torch.float16 if args.gpu_data_dtype == "fp16" else torch.float32,
                               args.gpu_data_gb)
        return pl.main([str(cfg_path)])
    pre = ut.resolve_preprocess_settings(cfg)
    print(f"Modelo={cfg.model} | window={cfg.window_sec}s hop={cfg.hop_sec}s fs={cfg.target_fs} | "
          f"batch_size cfg={cfg.batch_size} | loss={cfg.loss_type}")
 
    # ---------------- 1) Datos reales ----------------
    print("\n[1] Datos reales")
    t0 = time.perf_counter()
    tr_records, _ = ds.collect_records_for_split(cfg, "train")
    tr_bundle = build_bundle(ds, cfg, tr_records, pre, "smoke_train", workdir)
    t_build_tr = time.perf_counter() - t0
    n_tr_all = int(tr_bundle.labels.shape[0])
    per_rec_s = t_build_tr / max(1, len(tr_records))
    wins_per_rec = n_tr_all / max(1, len(tr_records))
    print(f"  train: {len(tr_records)} registros -> {n_tr_all} ventanas | CPU {t_build_tr:.0f}s ({per_rec_s:.1f}s/registro)")
    REPORT["build"] = {"records": len(tr_records), "windows": n_tr_all, "seconds": t_build_tr,
                       "s_per_record": per_rec_s, "windows_per_record": wins_per_rec}
    verdict("construcción de dataset", "PASS" if n_tr_all > 0 else "FAIL",
            f"{per_rec_s:.1f}s/registro (primera vez; luego queda en caché) -> {args.full_records} registros ≈ "
            f"{per_rec_s * args.full_records / 60:.0f} min de CPU")
 
    va_records, _ = ds.collect_records_for_split(cfg, "val")
    va_bundle = build_bundle(ds, cfg, va_records, pre, "smoke_val", workdir) if va_records else None
    if va_bundle is None or va_bundle.labels.shape[0] == 0:
        print("  ⚠️ sin validación propia; se separa por paciente desde train (solo para esta prueba).")
        pats = np.unique(tr_bundle.patients)
        rng.shuffle(pats)
        held = set(pats[: max(1, len(pats) // 4)])
        mask = np.isin(tr_bundle.patients, list(held))
        va_idx_all, tr_idx_all = np.where(mask)[0], np.where(~mask)[0]
        va_bundle = tr_bundle
    else:
        tr_idx_all = np.arange(n_tr_all)
        va_idx_all = np.arange(va_bundle.labels.shape[0])
 
    ytr_all = win_labels(tr_bundle.labels)
    yva_all = win_labels(va_bundle.labels)
    tr_idx = tr_idx_all[stratified_idx(ytr_all[tr_idx_all], args.max_train_windows, rng)]
    va_idx = va_idx_all[stratified_idx(yva_all[va_idx_all], args.max_val_windows, rng)]
    print(f"  usadas: train {len(tr_idx)} (pos {int(ytr_all[tr_idx].sum())}) | val {len(va_idx)} (pos {int(yva_all[va_idx].sum())})")
    print(f"  forma de ventana: {tuple(tr_bundle.sequences.shape[1:])} | features: "
          f"{None if tr_bundle.features is None else tr_bundle.features.shape[1]}")
 
    # Features escaladas (como el pipeline: scaler ajustado en train)
    scaler, tr_feat, va_feat = None, None, None
    if tr_bundle.features is not None:
        scaler = StandardScaler().fit(np.asarray(tr_bundle.features)[tr_idx_all])
        tr_feat = scaler.transform(np.asarray(tr_bundle.features)).astype(np.float32)
        va_feat = scaler.transform(np.asarray(va_bundle.features)).astype(np.float32)
 
    tr_ds = Subset(ds.WindowDataset(tr_bundle.sequences, tr_bundle.labels, features=tr_feat,
                                    label_mode=tr_bundle.label_mode), tr_idx.tolist())
    va_ds = Subset(ds.WindowDataset(va_bundle.sequences, va_bundle.labels, features=va_feat,
                                    label_mode=va_bundle.label_mode), va_idx.tolist())
    n_pos_va = int(yva_all[va_idx].sum())
    n_neg_va = len(va_idx) - n_pos_va
 
    # ---------------- Modelo ----------------
    input_shape = tuple(tr_bundle.sequences.shape[1:])
    feat_dim = tr_bundle.features.shape[1] if tr_bundle.features is not None else None
    tparams = pl._transformer_params_from_config(cfg) if cfg.model == "transformer" else None
    model = pl.make_model(model_type=cfg.model, input_shape=input_shape, feat_dim=feat_dim,
                          num_filters=cfg.num_filters, kernel_size=cfg.kernel_size, dropout_rate=cfg.dropout,
                          rnn_units=cfg.rnn_units, time_step=cfg.time_step_labels,
                          transformer_params=tparams).to(device)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"  parámetros: {n_params / 1e6:.2f} M")
    loss_computer = pl.create_loss_factory(cfg)()
    opt = pl.create_optimizer(cfg, model)
 
    # ---------------- 2) Épocas reales (código tal cual) ----------------
    print("\n[2] Entrenamiento con tu `_train_one_epoch` (baseline actual)")
    loader = DataLoader(tr_ds, batch_size=cfg.batch_size, shuffle=True)
    epoch_times, losses = [], []
    for ep in range(cfg.epochs):
        sync(device)
        t0 = time.perf_counter()
        loss = pl._train_one_epoch(model, loader, opt, loss_computer, device=device, log_interval=None)
        sync(device)
        epoch_times.append(time.perf_counter() - t0)
        losses.append(loss)
        print(f"  época {ep + 1}: {epoch_times[-1]:.1f}s | loss {loss:.4f}")
    sec_per_window = min(epoch_times) / len(tr_ds)
    full_windows = wins_per_rec * args.full_records
    est_epoch_min = sec_per_window * full_windows / 60
    print(f"  ≈ {1 / sec_per_window:.0f} ventanas/s -> época completa ({args.full_records} registros ≈ "
          f"{int(full_windows)} ventanas) ≈ {est_epoch_min * 60:.0f} s ({est_epoch_min:.1f} min) con la config actual")
    REPORT["baseline"] = {"epoch_times": epoch_times, "losses": losses, "est_full_epoch_min": est_epoch_min}
    verdict("loss finita", "PASS" if np.all(np.isfinite(losses)) else "FAIL", f"losses={['%.4f' % l for l in losses]}")
 
    # ---------------- 3) Benchmark ----------------
    if not args.skip_bench:
        print("\n[3] Micro-benchmark (sobre una copia del modelo; ventanas/s)")
        variants = [
            (f"bs={cfg.batch_size} fp32 w0 (actual)", cfg.batch_size, False, 0),
            ("bs=32 fp32 w0", 32, False, 0),
            ("bs=32 bf16 w0", 32, True, 0),
            ("bs=32 bf16 w4", 32, True, 4),
            ("bs=64 bf16 w4", 64, True, 4),
            ("bs=32 bf16 gpu-data", 32, True, 0),
            ("bs=64 bf16 gpu-data", 64, True, 0),
        ]
        sdt = torch.float16 if args.gpu_data_dtype == "fp16" else torch.float32
        bench = []
        for label, bs, amp, w in variants:
            try:
                bench.append(bench_variant(pl, model, tr_ds, bs=bs, amp=amp, workers=w,
                                           n_batches=args.bench_batches, device=device,
                                           loss_computer=loss_computer, label=label,
                                           gpu_data="gpu-data" in label, store_dtype=sdt,
                                           budget_gb=args.gpu_data_gb))
            except (RuntimeError, MemoryError) as exc:  # OOM u otros
                print(f"    {label:<28} FALLÓ: {str(exc)[:80]}")
                if device.type == "cuda":
                    torch.cuda.empty_cache()
        REPORT["bench"] = bench
        if bench:
            best = max(bench, key=lambda b: b["windows_per_s"])
            est = full_windows / best["windows_per_s"] / 60
            print(f"  mejor: {best['label']} -> época completa ≈ {est * 60:.0f} s (vs {est_epoch_min * 60:.0f} s actual)")
            if cfg.model == "transformer":
                print("  ⚠️ Transformer + bf16: RoPE calcula las posiciones en el dtype de q; en bf16 los índices > 256 "
                      "pierden precisión. Si usas autocast, calcula RoPE en fp32 antes de cambiarlo.")
            verdict("benchmark de velocidad", "PASS", f"mejor {best['windows_per_s']:.0f} ventanas/s; "
                    f"época completa ≈ {est * 60:.0f} s")
 
    # ---------------- 5) Sanidad ----------------
    print("\n[5] Pruebas de sanidad")
    # (a) Overfit de mini-lote balanceado
    ytr_sub = ytr_all[tr_idx]
    pos_i = np.where(ytr_sub > 0.5)[0][:16]
    neg_i = np.where(ytr_sub <= 0.5)[0][:16]
    if len(pos_i) >= 2 and len(neg_i) >= 2:
        sel = np.concatenate([pos_i, neg_i]).tolist()
        batch = next(iter(DataLoader(Subset(tr_ds, sel), batch_size=len(sel))))
        seq, feat, labels = pl._prepare_batch(batch, device)
        m = copy.deepcopy(model).to(device)
        m.train()
        o = torch.optim.AdamW(m.parameters(), lr=1e-3)
        hist = []
        for _ in range(100):
            o.zero_grad(set_to_none=True)
            lg, aux = pl._forward_model(m, seq, feat)
            ls = loss_computer(lg.view_as(labels), labels, weights=None)
            ls.backward()
            torch.nn.utils.clip_grad_norm_(m.parameters(), 1.0)
            o.step()
            hist.append(float(ls.detach()))
        a, b = float(np.mean(hist[:5])), float(np.mean(hist[-5:]))
        verdict("overfit de mini-lote", "PASS" if b < 0.5 * a else "FAIL",
                f"loss {a:.3f} -> {b:.3f} en 100 pasos (si no baja: bug de gradientes/etiquetas/features)")
        del m, o
    else:
        verdict("overfit de mini-lote", "WARN", "no hay ≥2 positivos y ≥2 negativos en el subconjunto de train")
 
    # (b) Determinismo y independencia de batch en eval
    model.eval()
    vb = next(iter(DataLoader(va_ds, batch_size=min(8, len(va_ds)))))
    vseq, vfeat, _ = pl._prepare_batch(vb, device)
    with torch.no_grad():
        o1, _ = pl._forward_model(model, vseq, vfeat)
        o2, _ = pl._forward_model(model, vseq, vfeat)
        single, _ = pl._forward_model(model, vseq[:1], vfeat[:1] if vfeat is not None else None)
        zero_sig, _ = pl._forward_model(model, torch.zeros_like(vseq), vfeat)
        zero_feat = None
        if vfeat is not None:
            zero_feat, _ = pl._forward_model(model, vseq, torch.zeros_like(vfeat))
    d_det = float((o1 - o2).abs().max())
    d_batch = float((o1[:1] - single).abs().max())
    verdict("determinismo en eval", "PASS" if d_det < 1e-5 else "FAIL", f"dif máx {d_det:.2e}")
    verdict("independencia de batch", "PASS" if d_batch < 1e-3 else "WARN", f"dif máx {d_batch:.2e}")
    sig_dep = float((o1 - zero_sig).abs().mean())
    msg = f"|Δlogit| al anular la señal = {sig_dep:.4f}"
    if zero_feat is not None:
        feat_dep = float((o1 - zero_feat).abs().mean())
        msg += f" | al anular las features = {feat_dep:.4f}"
        REPORT["feat_dependence"] = feat_dep
    REPORT["signal_dependence"] = sig_dep
    verdict("dependencia de señal/features (informativo)", "INFO", msg + " — si la señal importa ~0, el XAI sobre señal no dirá nada")
 
    # ---------------- 4/6) Evaluación ----------------
    print("\n[6] Evaluación en validación (tras prueba corta: solo detecta fallos groseros)")
    probs = pl._collect_predictions(model, DataLoader(va_ds, batch_size=64), device)
    sc = probs.reshape(len(probs), -1).mean(axis=1)
    yv = yva_all[va_idx]
    auc = pl.safe_roc_auc(yv, sc)
    ap_ = pl.safe_average_precision(yv, sc)
    print(f"  val: {n_pos_va} pos / {n_neg_va} neg | AUC={auc:.3f} AP={ap_:.3f} (AP base ≈ {n_pos_va / max(1, len(yv)):.3f}) | "
          f"prob min/med/max = {sc.min():.3f}/{np.median(sc):.3f}/{sc.max():.3f}")
    REPORT["val"] = {"auc": float(auc), "ap": float(ap_), "n_pos": n_pos_va, "n_neg": n_neg_va}
    if n_pos_va == 0 or n_neg_va == 0:
        verdict("métricas de validación", "WARN", "falta una clase en val; sube --val-records")
    else:
        verdict("métricas de validación", "PASS" if auc >= 0.55 else "WARN",
                f"AUC={auc:.3f}. Con pocas épocas es normal que sea bajo; <0.5 persistente tras entrenar más sería señal de bug")
    verdict("colapso de probabilidades", "PASS" if sc.std() > 1e-3 else "WARN", f"std={sc.std():.4f}")
 
    # ---------------- XAI ----------------
    if not args.skip_xai:
        print("\n[7] XAI (IG, oclusión, deleción)")
        order = np.argsort(-sc)[: args.xai_windows]
        ig_times, oc_times, rels, corr, top_drops, rnd_drops = [], [], [], [], [], []
        T = input_shape[0]
        k = max(1, int(0.10 * T))
        for j in order:
            item = va_ds[int(j)]
            (x, f), _ = item if isinstance(item[0], (tuple, list)) else ((item[0], None), item[1])
            x = x.unsqueeze(0).to(device)
            f = f.unsqueeze(0).to(device) if f is not None else None
            sync(device)
            t0 = time.perf_counter()
            attr, _, rel = integrated_gradients(pl, model, x, f, args.ig_steps)
            sync(device)
            ig_times.append(time.perf_counter() - t0)
            rels.append(rel)
            t0 = time.perf_counter()
            drops, starts, seg = occlusion(pl, model, x, f)
            sync(device)
            oc_times.append(time.perf_counter() - t0)
            imp = attr.abs().sum(dim=-1).squeeze(0)  # (T,)
            ig_seg = np.array([float(imp[s:s + seg].sum()) for s in starts])
            corr.append(rank_corr(ig_seg, np.abs(drops)))
            top = torch.topk(imp, k).indices
            top_drops.append(abs(deletion_drop(pl, model, x, f, top)))
            rd = [abs(deletion_drop(pl, model, x, f, torch.randperm(T, device=device)[:k])) for _ in range(5)]
            rnd_drops.append(float(np.mean(rd)))
        print(f"  IG ({args.ig_steps} pasos): {np.mean(ig_times):.2f}s/ventana | oclusión: {np.mean(oc_times):.2f}s/ventana")
        print(f"  delta de completitud IG (rel.): mediana {np.median(rels):.3f}")
        print(f"  corr. rangos IG vs oclusión (por segmento): media {np.nanmean(corr):.2f}")
        print(f"  deleción 10% muestras: top-IG |Δlogit|={np.mean(top_drops):.4f} vs azar={np.mean(rnd_drops):.4f}")
        REPORT["xai"] = {"ig_s": float(np.mean(ig_times)), "occ_s": float(np.mean(oc_times)),
                         "ig_rel_delta_median": float(np.median(rels)),
                         "ig_vs_occ_rank_corr": float(np.nanmean(corr)),
                         "del_top": float(np.mean(top_drops)), "del_random": float(np.mean(rnd_drops))}
        verdict("completitud de IG", "PASS" if np.median(rels) < 0.05 else "WARN",
                f"error relativo mediano {np.median(rels):.3f}; si es alto sube --ig-steps")
        verdict("fidelidad: deleción top vs azar", "PASS" if np.mean(top_drops) > np.mean(rnd_drops) else "WARN",
                "si borrar lo 'importante' no pesa más que borrar al azar, la atribución no es fiable")
        print(f"  coste estimado para 500 ventanas: IG ≈ {500 * np.mean(ig_times) / 60:.1f} min, "
              f"oclusión ≈ {500 * np.mean(oc_times) / 60:.1f} min")
 
    # ---------------- Resumen ----------------
    print("\n==== RESUMEN ====")
    for name, status, detail in RESULTS:
        print(f"[{status:<4}] {name}")
    (workdir / "smoke_report.json").write_text(json.dumps({"results": RESULTS, "report": REPORT}, indent=2, default=str))
    print(f"\nReporte guardado en {workdir / 'smoke_report.json'}")
    return 1 if any(s == "FAIL" for _, s, _ in RESULTS) else 0
 
 
if __name__ == "__main__":
    raise SystemExit(main())
