import re, sys, json
from datetime import datetime
from pathlib import Path
import joblib

try:
    import torch
except Exception:
    torch = None

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "/workspace/ml-outputs/artifact")
PAT = re.compile(r"(eye|muscle|non_physiological)_(A\d)_w([\d.]+)_s([\d.]+)_([0-9a-f]{8})")

# Grid esperado (WINDOW_REQUESTS_ARTIFACTS x LOSS_VARIANTS). Edita si cambias ventanas.
WINS = {"eye": [("5", "2"), ("2", "1")],
        "muscle": [("1", "0.5"), ("5", "2")],
        "non_physiological": [("1", "1"), ("2", "1")]}
VARIANTS = ["A1", "A2"]
SKIP = ("running_mean", "running_var", "num_batches_tracked")

def infer_type(sd):
    if any(k.startswith("conv.9.") for k in sd): return "paper"
    if any(k.endswith("running_mean") and k.startswith("conv.") for k in sd): return "standard"
    return "lightweight"

def folder_version(path):
    return next((p[len("models_"):] for p in path.parts if p.startswith("models_v")), "?")

def fdate(f):
    return datetime.fromtimestamp(f.stat().st_mtime).strftime("%m-%d %H:%M")

rows = {}
model_dirs = sorted(ROOT.glob("models_v*"))

# 1) Terminadas
for md in model_dirs:
    for f in md.rglob("*_analysis.joblib"):
        m = PAT.search(f.name)
        if not m: continue
        art, var, w, s, h = m.groups()
        try:
            mr = joblib.load(f).get("metrics_results", {})
        except Exception:
            mr = {}
        cfgf = f.with_name(f.name.replace("_analysis.joblib", "_cfg.json"))
        cfg = json.loads(cfgf.read_text()) if cfgf.exists() else {}
        rows[h] = dict(version=cfg.get("code_version") or folder_version(f),
                       data_v=cfg.get("split_version", "?"),
                       artifact=art, variant=var, win=f"w{w}_s{s}", hash=h,
                       tipo=cfg.get("model_type", "?"), params=None,
                       estado="LISTO", AP=mr.get("AP"), F1=mr.get("f1_score"),
                       fecha=fdate(f), ep=None)

# 2) .pt: tipo y parametros
if torch is not None:
    for md in model_dirs:
        for f in md.rglob("*.pt"):
            m = PAT.search(str(f))
            if not m or m.group(5) not in rows: continue
            try:
                d = torch.load(f, map_location="cpu", weights_only=False)
                sd = d["state_dict"]
                r = rows[m.group(5)]
                if r["tipo"] == "?":
                    r["tipo"] = d.get("model_type", infer_type(sd))
                r["params"] = sum(v.numel() for k, v in sd.items() if not k.endswith(SKIP))
            except Exception:
                pass

# 3) En curso / pausadas
if torch is not None:
    for f in ROOT.glob("*/checkpoints/*/latest.pt"):
        m = PAT.search(f.parent.name)
        if not m: continue
        art, var, w, s, h = m.groups()
        if h in rows: continue
        try:
            ck = torch.load(f, map_location="cpu", weights_only=False)
            ep, tipo = ck.get("epoch", -1) + 1, infer_type(ck["model_state"])
        except Exception:
            ep, tipo = "?", "?"
        rows[h] = dict(version="?", data_v="?", artifact=art, variant=var, win=f"w{w}_s{s}",
                       hash=h, tipo=tipo, params=None, estado="EN CURSO", AP=None, F1=None,
                       fecha=fdate(f), ep=ep)

if not rows:
    print("No encontre nada en", ROOT); sys.exit()

# Version de las corridas en curso: si solo hay una version entre las terminadas, heredarla
done_versions = {r["version"] for r in rows.values() if r["estado"] == "LISTO"}
for r in rows.values():
    if r["version"] == "?" and len(done_versions) == 1:
        r["version"] = next(iter(done_versions))

# Agrupar por configuracion = (version, dataset, tipo de modelo)
groups = {}
for r in rows.values():
    groups.setdefault((r["version"], r["data_v"], r["tipo"]), []).append(r)

def cell(rs):
    if not rs: return "--  falta"
    out = []
    for r in sorted(rs, key=lambda x: x["fecha"]):
        if r["estado"] == "LISTO":
            ap = f"AP {r['AP']:.3f}" if r["AP"] is not None else "AP ?"
            out.append(f"OK  {ap}  {r['fecha']}  [{r['hash']}]")
        else:
            out.append(f"EN CURSO ep{r['ep']}  {r['fecha']}  [{r['hash']}]")
    return "  |  ".join(out) + ("   <-- varios hashes" if len(rs) > 1 else "")

summary = []
for (ver, dv, tipo), rs in sorted(groups.items()):
    params = next((r["params"] for r in rs if r["params"]), None)
    ready = sum(1 for r in rs if r["estado"] == "LISTO")
    print("=" * 100)
    print(f"CONFIG  codigo={ver} | dataset={dv} | modelo={tipo}" + (f" | {params:,} parametros" if params else ""))
    print("=" * 100)
    done_cells = 0
    for art, ws in WINS.items():
        for (w, s) in ws:
            for v in VARIANTS:
                match = [r for r in rs if (r["artifact"], r["win"], r["variant"]) == (art, f"w{w}_s{s}", v)]
                if any(r["estado"] == "LISTO" for r in match): done_cells += 1
                print(f"  {art:<18} w{w}_s{s:<4} {v}   {cell(match)}")
        print()
    extra = [r for r in rs if (r["artifact"], r["win"]) not in
             {(a, f"w{w}_s{s}") for a, ws in WINS.items() for (w, s) in ws}]
    if extra:
        print("  Fuera del grid esperado:", ", ".join(f"{r['artifact']} {r['win']} {r['variant']} [{r['hash']}]" for r in extra), "\n")
    summary.append((ver, dv, tipo, done_cells, ready))

print("=" * 100)
print("RESUMEN  (celdas del grid con resultado final / 12)")
for ver, dv, tipo, d, n in summary:
    print(f"  codigo={ver:<4} dataset={str(dv):<4} modelo={tipo:<12} {d:>2}/12   ({n} modelos terminados)")

# ====================================================================
# 4) INVENTARIO DE MODELOS CLÁSICOS (Random Forest, XGBoost)
# ====================================================================
# Patrón esperado: rf_eye_w5_s2_7... o xgb_muscle_w1s0.5_6...
PAT_ML = re.compile(r"(rf|xgb|xgboost)_(eye|muscle|non_physiological)_w([\d.]+)_?s([\d.]+)_(\d+)")

ml_rows = []
for f in ROOT.rglob("*.joblib"):
    if "_analysis" in f.name: 
        continue  
        
    m = PAT_ML.search(f.name)
    if not m: 
        continue
        
    tipo_ml, art, w, s, version = m.groups()
    fecha_ml = fdate(f)
    
    try:
        data = joblib.load(f)
        ap = data.get("AP", data.get("metrics_results", {}).get("AP", "?"))
        if isinstance(ap, float): ap = f"{ap:.3f}"
    except Exception:
        ap = "?"

    ml_rows.append({
        "tipo": tipo_ml.upper(),
        "version": version,
        "artifact": art,
        "win": f"w{w}_s{s}",
        "fecha": fecha_ml,
        "ap": ap,
        "archivo": f.name
    })

if ml_rows:
    ml_groups = {}
    for r in ml_rows:
        ml_groups.setdefault(r["tipo"], []).append(r)
        
    # --- PRIMERA PARTE: Imprimir historial completo ---
    print("\n" + "=" * 100)
    print("CONFIG  | MODELOS CLÁSICOS (RF/XGB) - HISTORIAL COMPLETO")
    print("=" * 100)
    
    for tipo, rs in ml_groups.items():
        print(f"\n--- {tipo} ---")
        for art, ws in WINS.items():
            for (w, s) in ws:
                win_str = f"w{w}_s{s}"
                match = [r for r in rs if r["artifact"] == art and r["win"] == win_str]
                
                if not match:
                    print(f"  {art:<18} {win_str:<7} -- falta")
                else:
                    for m in sorted(match, key=lambda x: (int(x["version"]), x["fecha"])):
                        print(f"  {art:<18} {win_str:<7} v{m['version']:<3} OK  AP {m['ap']}  {m['fecha']}  [{m['archivo']}]")

    # --- SEGUNDA PARTE: Imprimir resumen de última versión ---
    print("\n" + "=" * 100)
    print("RESUMEN | MODELOS CLÁSICOS (RF/XGB) - SOLO ÚLTIMA VERSIÓN")
    print("=" * 100)

    for tipo, rs in ml_groups.items():
        print(f"\n--- {tipo} ---")
        for art, ws in WINS.items():
            for (w, s) in ws:
                win_str = f"w{w}_s{s}"
                match = [r for r in rs if r["artifact"] == art and r["win"] == win_str]
                
                if not match:
                    print(f"  {art:<18} {win_str:<7} -- falta")
                else:
                    # Toma estrictamente el último registro ordenado
                    latest = sorted(match, key=lambda x: (int(x["version"]), x["fecha"]))[-1]
                    print(f"  {art:<18} {win_str:<7} v{latest['version']:<3} OK  AP {latest['ap']}  {latest['fecha']}  [{latest['archivo']}]")
else:
    print("\n" + "=" * 100)
    print("No se encontraron modelos clásicos (RF/XGB) con el patrón esperado.")
    print("=" * 100)


# ====================================================================
# 4) INVENTARIO DE MODELOS CLÁSICOS (Random Forest, XGBoost)
# ====================================================================
# Patrón esperado: rf_eye_w5_s2_7... o xgb_muscle_w1s0.5_6...
PAT_ML = re.compile(r"(rf|xgb|xgboost)_(eye|muscle|non_physiological)_w([\d.]+)_?s([\d.]+)_(\d+)")

ml_rows = []
for f in ROOT.rglob("*.joblib"):
    if "_analysis" in f.name: 
        continue  
        
    m = PAT_ML.search(f.name)
    if not m: 
        continue
        
    tipo_ml, art, w, s, version = m.groups()
    fecha_ml = fdate(f)
    
    try:
        data = joblib.load(f)
        ap = data.get("AP", data.get("metrics_results", {}).get("AP", "?"))
        if isinstance(ap, float): ap = f"{ap:.3f}"
    except Exception:
        ap = "?"

    ml_rows.append({
        "tipo": tipo_ml.upper(),
        "version": version,
        "artifact": art,
        "win": f"w{w}_s{s}",
        "fecha": fecha_ml,
        "ap": ap,
        "archivo": f.name
    })

if ml_rows:
    ml_groups = {}
    for r in ml_rows:
        ml_groups.setdefault(r["tipo"], []).append(r)
        
    # --- PRIMERA PARTE: Imprimir historial completo ---
    print("\n" + "=" * 100)
    print("CONFIG  | MODELOS CLÁSICOS (RF/XGB) - HISTORIAL COMPLETO")
    print("=" * 100)
    
    for tipo, rs in ml_groups.items():
        print(f"\n--- {tipo} ---")
        for art, ws in WINS.items():
            for (w, s) in ws:
                win_str = f"w{w}_s{s}"
                match = [r for r in rs if r["artifact"] == art and r["win"] == win_str]
                
                if not match:
                    print(f"  {art:<18} {win_str:<7} -- falta")
                else:
                    for m in sorted(match, key=lambda x: (int(x["version"]), x["fecha"])):
                        print(f"  {art:<18} {win_str:<7} v{m['version']:<3} OK  AP {m['ap']}  {m['fecha']}  [{m['archivo']}]")

    # --- SEGUNDA PARTE: Imprimir resumen de última versión ---
    print("\n" + "=" * 100)
    print("RESUMEN | MODELOS CLÁSICOS (RF/XGB) - SOLO ÚLTIMA VERSIÓN")
    print("=" * 100)

    for tipo, rs in ml_groups.items():
        print(f"\n--- {tipo} ---")
        for art, ws in WINS.items():
            for (w, s) in ws:
                win_str = f"w{w}_s{s}"
                match = [r for r in rs if r["artifact"] == art and r["win"] == win_str]
                
                if not match:
                    print(f"  {art:<18} {win_str:<7} -- falta")
                else:
                    # Toma estrictamente el último registro ordenado
                    latest = sorted(match, key=lambda x: (int(x["version"]), x["fecha"]))[-1]
                    print(f"  {art:<18} {win_str:<7} v{latest['version']:<3} OK  AP {latest['ap']}  {latest['fecha']}  [{latest['archivo']}]")
else:
    print("\n" + "=" * 100)
    print("No se encontraron modelos clásicos (RF/XGB) con el patrón esperado.")
    print("=" * 100)
