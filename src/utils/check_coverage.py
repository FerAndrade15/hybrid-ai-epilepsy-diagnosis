# pipelines/artifacts/check_coverage.py

import numpy as np
import pandas as pd
from src.core.data_config import ARTIFACT_KEYWORDS, WINDOW_REQUESTS_ARTIFACTS
from src.core.data_loader import build_annotations_index, find_project_root
from src.core.windowing import get_or_build_windows

# General configuration
UMBRAL = 0.7  
WINDOWS_DIR = find_project_root("src") / "outputs" / "artifact" / "windows"
CACHE_DIR = find_project_root("src") / "outputs" / "artifact" /  "annotations"

def union_len(iv):
    """
    Toma una lista de intervalos de tiempo [(inicio1, fin1), (inicio2, fin2), ...] 
    y calcula el tiempo total real sin contar dos veces las partes solapadas.
    """
    total, cs, ce = 0.0, None, None
    for a, b in sorted(iv):
        if ce is None or a > ce:
            if ce is not None: total += ce - cs
            cs, ce = a, b
        else:
            ce = max(ce, b)
    return total + (ce - cs if ce is not None else 0.0)

def pieces(iv):
    """Agrupa intervalos solapados en bloques continuos (piezas)."""
    out = []
    for a, b in sorted(iv):
        if out and a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out

if __name__ == "__main__":
    print(f"==================================================================")
    print(f" INICIANDO DIAGNÓSTICO DE COBERTURA (UMBRAL: {UMBRAL*100}%)")
    print(f"==================================================================")

    # 1. Cargar las anotaciones originales (Ahora ultra rápido gracias a la caché)
    print("[1/4] Cargando el índice de anotaciones maestro...")
    ann = build_annotations_index("artifact", paths=True, CACHE_DIR=CACHE_DIR)
    labs = ann["label"].astype(str)
    tok = {l: set(l.lower().split("_")) for l in labs.unique()}

    # 2. Iterar sobre cada tipo de artefacto (eye, muscle, non_physiological)
    for artifact, req in WINDOW_REQUESTS_ARTIFACTS.items():
        print(f"\n" + "-"*60)
        print(f" ANALIZANDO ARTEFACTO: {artifact.upper()}")
        print(f" Tamaño ventana: {req['window_size_sec']}s | Paso: {req['stride_sec']}s")
        print("-" * 60)

        size = req["window_size_sec"]
        stride = req["stride_sec"]

        if stride != size:
            print(f"[SKIP] Ventanas solapadas detectadas, la matemática de cota no aplica aquí.")
            continue
        
        # 3. Cargar las ventanas generadas por el pipeline actual
        print("[2/4] Cargando dataset de ventanas generadas por el modelo...")
        windowed = get_or_build_windows(ann,    , ARTIFACT_KEYWORDS, WINDOWS_DIR)
        
        # 4. Aislar anotaciones que pertenezcan a este artefacto específico
        kws = ARTIFACT_KEYWORDS[artifact]
        sel = ann[labs.map(lambda l: bool(tok[l] & kws))]
        
        # 5. Calcular los segundos REALES del artefacto en todo el dataset (por unión temporal)
        secs = sum(union_len(zip(g["start_time"], g["stop_time"]))
                   for _, g in sel.groupby(["Patient", "Session", "Section"]))
        
        # Calcular cuál es el máximo teórico de ventanas que podrían ser positivas
        bound = secs / (UMBRAL * size)
        
        # Contar cuántas ventanas generó tu código como positivas realmente
        actual = int(windowed[artifact].sum())
        
        print(f"[INFO GENERAL]")
        print(f"  Tiempo total real del artefacto : {secs:,.0f} s")
        print(f"  Tope teórico máximo de ventanas : {bound:,.0f}")
        print(f"  Ventanas positivas actuales     : {actual:,}")
        print(f"  Ratio actuales / tope teórico   : {actual / bound:.2f}")

        # ----------------------------------------------------------------------
        # ANÁLISIS EXACTO: VENTANA POR VENTANA
        # ----------------------------------------------------------------------
        print(f"\n[3/4] Re-calculando matemáticamente ventana por ventana (Verdad Absoluta)...")
        dur = ann.drop_duplicates(["Patient", "Session", "Section"]).set_index(["Patient", "Session", "Section"])["Duration"]
        cov = {}
        
        # Calcular cobertura ventana por ventana usando la unión temporal estricta
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
            
            for a, b in merged:
                b = min(b, dur[key])
                for k in range(int(a // size), int(np.ceil(b / size))):
                    ov = min(b, (k + 1) * size) - max(a, k * size)
                    if ov > 0:
                        cov[key + (k * size,)] = cov.get(key + (k * size,), 0.0) + ov

        # Identificar ventanas matemáticamente correctas (>= umbral)
        union_pos = {k for k, v in cov.items() if v / size >= UMBRAL - 1e-3}
        
        # Identificar ventanas que el código arrojó como positivas
        act = windowed.loc[windowed[artifact] == 1, ["Patient", "Session", "Section", "Start"]]
        actual_pos = set(map(tuple, act.itertuples(index=False, name=None)))
        
        inflated = actual_pos - union_pos
        missed = union_pos - actual_pos

        print(f"\n[4/4] RESULTADOS DEL EMPAREJAMIENTO:")
        print(f"  Positivas por unión matemática  : {len(union_pos):,}")
        print(f"  Positivas arrojadas por código  : {len(actual_pos):,}")
        print(f"  Ventanas INFLADAS (Falsas Pos.) : {len(inflated):,} ({(len(inflated) / len(actual_pos) if len(actual_pos) > 0 else 0):.1%})")
        print(f"  Positivas omitidas por código   : {len(missed):,}")

        # ----------------------------------------------------------------------
        # ANÁLISIS DE VENTANAS INFLADAS (Si existen)
        # ----------------------------------------------------------------------
        if not inflated:
            print("\n  >>> ESTADO PERFECTO: No hay ventanas infladas. El cálculo coincide. <<<")
            continue

        print(f"\n  [!] ANALIZANDO EL ORIGEN DE LAS {len(inflated):,} VENTANAS INFLADAS...")
        detail = {}
        for r in sel.itertuples():
            key = (r.Patient, r.Session, r.Section)
            lo, hi = r.start_time, min(r.stop_time, dur[key])
            for k in range(int(lo // size), int(np.ceil(hi / size))):
                w = key + (k * size,)
                if w in actual_pos:
                    detail.setdefault(w, []).append((r.channel, r.start_time, r.stop_time, r.label))

        recs = []
        for w, items in detail.items():
            w0, w1 = w[3], w[3] + size
            clip = [(ch, max(a, w0), min(b, w1), lab) for ch, a, b, lab in items if min(b, w1) > max(a, w0)]
            total = sum(b - a for _, a, b, _ in clip)                         # Lo que el código sumaba mal
            
            by_ch = {}
            for ch, a, b, _ in clip:
                by_ch.setdefault(ch, []).append((a, b))
                
            s_ch = sum(union_len(v) for v in by_ch.values())                  # Unión dentro de cada canal
            uni = union_len([(a, b) for _, a, b, _ in clip])                  # Unión matemática total
            real = pieces([(a, b) for _, a, b, _ in items])                   # Eventos originales sin cortar
            
            recs.append({
                "inflated": w in inflated, "patient": w[0],
                "sum_cov": total / size, "uni_cov": uni / size,
                "cross": (s_ch - uni) / size,            # Error por sumar canales
                "same": (total - s_ch) / size,           # Error por sumar solapes del mismo canal
                "n_ch": len(by_ch),
                "n_pieces": len(pieces([(a, b) for _, a, b, _ in clip])),
                "longest": max(b - a for a, b in real),
                "compound": any("_" in lab for _, _, _, lab in clip),
            })

        d = pd.DataFrame(recs)
        inf, ok = d[d["inflated"]].copy(), d[~d["inflated"]]
        thr = UMBRAL * size
        inf["tipo"] = np.select(
            [inf["n_pieces"] > 1, inf["longest"] >= thr],
            ["varios eventos separados", "evento largo cortado por el borde"],
            default="un evento corto (< umbral)")

        print(f"    - Tipos de infladas detectadas:\n{inf['tipo'].value_counts(normalize=True).round(3).to_string()}")
        print(f"    - Error matemático: Cobertura por SUMA (errónea) vs UNIÓN (real)")
        print(f"      Mediana: {inf['sum_cov'].median():.2f} (Suma) vs {inf['uni_cov'].median():.2f} (Unión)")
        ex_c, ex_s = inf["cross"].sum(), inf["same"].sum()
        print(f"    - Origen del error: {ex_c / (ex_c + ex_s):.1%} por canales repetidos.")
    
    print("\n================ DIAGNÓSTICO FINALIZADO ================\n")