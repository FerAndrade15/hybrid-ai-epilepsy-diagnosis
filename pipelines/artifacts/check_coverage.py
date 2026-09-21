# pipelines/artifacts/check_coverage.py: diagnóstico de una sola vez, no modifica nada
import numpy as np
import pandas as pd
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
    # --- Prueba exacta: cobertura por unión de cada ventana ---
    dur = ann.drop_duplicates(["Patient", "Session", "Section"]).set_index(["Patient", "Session", "Section"])["Duration"]
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
        for a, b in merged:
            b = min(b, dur[key])
            for k in range(int(a // size), int(np.ceil(b / size))):
                ov = min(b, (k + 1) * size) - max(a, k * size)
                if ov > 0:
                    cov[key + (k * size,)] = cov.get(key + (k * size,), 0.0) + ov

    union_pos = {k for k, v in cov.items() if v / size >= UMBRAL - 1e-3}
    act = windowed.loc[windowed[artifact] == 1, ["Patient", "Session", "Section", "Start"]]
    actual_pos = set(map(tuple, act.itertuples(index=False, name=None)))
    print(f"   por unión: {len(union_pos):,} | actuales: {len(actual_pos):,} | "
          f"infladas: {len(actual_pos - union_pos):,} ({len(actual_pos - union_pos) / len(actual_pos):.1%}) | "
          f"por unión que no están en actuales: {len(union_pos - actual_pos):,}")  

     # --- ¿De dónde sale la cobertura extra de las infladas? ---
    inflated = actual_pos - union_pos
    if not inflated:
        print("   sin infladas")
        continue

    detail = {}                                    # ventana positiva actual -> filas de anotación que la tocan
    for r in sel.itertuples():
        key = (r.Patient, r.Session, r.Section)
        lo, hi = r.start_time, min(r.stop_time, dur[key])
        for k in range(int(lo // size), int(np.ceil(hi / size))):
            w = key + (k * size,)
            if w in actual_pos:
                detail.setdefault(w, []).append((r.channel, r.start_time, r.stop_time, r.label))

    def pieces(iv):
        out = []
        for a, b in sorted(iv):
            if out and a <= out[-1][1]:
                out[-1][1] = max(out[-1][1], b)
            else:
                out.append([a, b])
        return out

    recs = []
    for w, items in detail.items():
        w0, w1 = w[3], w[3] + size
        clip = [(ch, max(a, w0), min(b, w1), lab) for ch, a, b, lab in items if min(b, w1) > max(a, w0)]
        total = sum(b - a for _, a, b, _ in clip)                         # lo que suma label_windowing
        by_ch = {}
        for ch, a, b, _ in clip:
            by_ch.setdefault(ch, []).append((a, b))
        s_ch = sum(union_len(v) for v in by_ch.values())                  # unión dentro de cada canal
        uni = union_len([(a, b) for _, a, b, _ in clip])                  # unión entre canales
        real = pieces([(a, b) for _, a, b, _ in items])                   # eventos sin recortar
        recs.append({
            "inflated": w in inflated, "patient": w[0],
            "sum_cov": total / size, "uni_cov": uni / size,
            "cross": (s_ch - uni) / size,            # exceso por repetir el evento en varios canales
            "same": (total - s_ch) / size,           # exceso por solapes dentro de un mismo canal
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

    print(f"   Tipo de ventana inflada:\n{inf['tipo'].value_counts(normalize=True).round(3).to_string()}")
    print(f"   Cobertura suma vs unión (mediana): {inf['sum_cov'].median():.2f} vs {inf['uni_cov'].median():.2f} "
          f"| unión p25/p50/p75: {inf['uni_cov'].quantile([.25, .5, .75]).round(2).tolist()}")
    ex_c, ex_s = inf["cross"].sum(), inf["same"].sum()
    print(f"   Exceso por canales repetidos: {ex_c / (ex_c + ex_s):.1%} | por solape en el mismo canal: {ex_s / (ex_c + ex_s):.1%}")
    print(f"   Canales anotados (mediana): infladas {inf['n_ch'].median():.0f} vs positivas reales {ok['n_ch'].median():.0f}")
    print(f"   Etiqueta compuesta: infladas {inf['compound'].mean():.1%} vs positivas reales {ok['compound'].mean():.1%}")
    top = inf["patient"].value_counts()
    print(f"   Pacientes con infladas: {len(top)} | los 5 principales concentran {top.head(5).sum() / len(inf):.1%}")
    print(f"   Destino aproximado (solo esta categoría): limpia {(inf['uni_cov'] <= 0.1).mean():.1%}, "
          f"ambigua {(inf['uni_cov'] > 0.1).mean():.1%}")
    dup = sel.duplicated(["Patient", "Session", "Section", "channel", "start_time", "stop_time", "label"]).sum()
    print(f"   Filas de anotación duplicadas exactas: {dup}")     