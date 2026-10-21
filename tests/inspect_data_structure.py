"""Inspecciona la estructura del dataset largo (una fila por ventana x componente).

Uso, desde cualquier carpeta:
    python inspect_dataset_structure.py ruta/al/archivo.parquet
    python inspect_dataset_structure.py ruta/al/archivo.parquet --max-rows 100000 --no-show

Es el parquet que sale de build_ml_dataset (por ejemplo rf_dataset_muscle_w5_s2_...parquet) o el
"featured_*.parquet" de get_or_build_features. Necesita pandas, numpy, matplotlib y pyarrow.

El archivo se lee POR BLOQUES, nunca entero, porque en formato largo puede ocupar decenas de GB:
  - La estructura (columnas, una ventana, mapa de calor, proporcionalidad de ic_contrib_*) se
    calcula con las primeras --max-rows filas (se descarta la última ventana por si quedó cortada).
  - Los conteos de ventanas, filas y positivos se calculan sobre TODO el archivo, en streaming,
    leyendo solo unas pocas columnas.

Qué hace:
  1. Agrupa las columnas con la misma regla que split_features_target (qué entra a X).
  2. Elige una ventana y cuenta qué columnas cambian entre sus componentes y cuáles se repiten.
  3. Dibuja X de esa ventana como mapa de calor, con las columnas agrupadas.
  4. Comprueba si las ic_contrib_* de un componente son proporcionales entre ventanas.
  5. Resume cuántos positivos hay por ventana y cómo se reparten entre clases de ICLabel.
"""
import argparse

import matplotlib
import numpy as np
import pandas as pd
import pyarrow.parquet as pq

# Igual que LEAKAGE_COLS en src/core/data_config.py
LEAKAGE_COLS = ["ic_index", "ic_raw_label", "ic_target_label", "Patient", "Session",
                "Section", "Start", "split", "is_positive", "Partition"]
WINDOW_KEY = ["Patient", "Session", "Section", "Start"]
GROUPS = ["ic_prob", "ic_contrib", "ic_feat", "ventana", "otros"]
COLORS = {"ic_prob": "#7F77DD", "ic_contrib": "#AFA9EC", "ic_feat": "#534AB7",
          "ventana": "#1D9E75", "otros": "#888780"}
LABELS = {"ic_prob": "probabilidad ICLabel", "ic_contrib": "ic_contrib_* (por electrodo)",
          "ic_feat": "rasgos del componente", "ventana": "rasgos de la ventana",
          "otros": "otras / no numéricas"}


def x_columns(df):
    """Columnas que le quedan al modelo: lo mismo que hace split_features_target."""
    drop = set(LEAKAGE_COLS)
    drop |= {c for c in df.columns if c.startswith("tuar_") or "_channels_" in c}
    return [c for c in df.columns if c not in drop]


def group_of(col, df):
    if not pd.api.types.is_numeric_dtype(df[col]):
        return "otros"
    if col == "ic_iclabel_prob":
        return "ic_prob"
    if col.startswith("ic_contrib_"):
        return "ic_contrib"
    if col.startswith("ic_"):
        return "ic_feat"
    return "ventana"


def load_head(pf, max_rows, batch_size):
    """Primeras ~max_rows filas, leídas por bloques. Descarta la última ventana (puede estar cortada)."""
    total = pf.metadata.num_rows
    parts, n = [], 0
    for batch in pf.iter_batches(batch_size=batch_size):
        part = batch.to_pandas()
        parts.append(part)
        n += len(part)
        if n >= max_rows:
            break
    df = pd.concat(parts, ignore_index=True)
    if n < total and all(c in df.columns for c in WINDOW_KEY) and len(df):
        last = df.iloc[-1][WINDOW_KEY]
        df = df[~(df[WINDOW_KEY] == last).all(axis=1)].reset_index(drop=True)
    return df, total


def pick_window(df):
    pos = df[df["is_positive"] == 1] if "is_positive" in df.columns else df.iloc[0:0]
    first = (pos if len(pos) else df).iloc[0]
    mask = (df[WINDOW_KEY] == first[WINDOW_KEY]).all(axis=1)
    return df[mask]


def summarize(df, xcols, win):
    varies = win[xcols].nunique(dropna=False) > 1
    rows = []
    for g in GROUPS:
        cols = [c for c in xcols if group_of(c, df) == g]
        if cols:
            rows.append({"grupo": g, "columnas": len(cols),
                         "cambian entre filas": int(varies[cols].sum()),
                         "iguales en la ventana": int((~varies[cols]).sum()),
                         "ejemplos": ", ".join(cols[:3])})
    return pd.DataFrame(rows)


def heatmap(df, xcols, win, out, show):
    import matplotlib.pyplot as plt
    num = [c for c in xcols if group_of(c, df) != "otros"]
    num.sort(key=lambda c: GROUPS.index(group_of(c, df)))
    sample = df[num].sample(min(len(df), 50000), random_state=0)
    mu, sd = sample.mean(), sample.std().replace(0, 1).fillna(1)
    z = ((win[num] - mu) / sd).clip(-3, 3).to_numpy(dtype=float)

    names = []
    for _, r in win.iterrows():
        label = str(r["ic_raw_label"]) if "ic_raw_label" in win.columns else "IC"
        tag = f"{label} {r['ic_iclabel_prob']:.2f}" if "ic_iclabel_prob" in win.columns else label
        if "is_positive" in win.columns and r["is_positive"] == 1:
            tag += "  <- y=1"
        names.append(tag)

    fig, (ax_bar, ax) = plt.subplots(2, 1, figsize=(13, 0.34 * len(win) + 3), sharex=True,
                                     gridspec_kw={"height_ratios": [1, 12], "hspace": 0.05})
    bar = np.array([matplotlib.colors.to_rgb(COLORS[group_of(c, df)]) for c in num])[None]
    ax_bar.imshow(bar, aspect="auto")
    ax_bar.set_yticks([])
    ax.imshow(z, aspect="auto", cmap="coolwarm", vmin=-3, vmax=3)
    ax.set_yticks(range(len(win)))
    ax.set_yticklabels(names, fontsize=8)
    ax.set_xlabel(f"{len(num)} columnas de X (z-score contra la muestra cargada)")
    edges = np.cumsum([sum(group_of(c, df) == g for c in num) for g in GROUPS])[:-1]
    for e in edges:
        ax.axvline(e - 0.5, color="black", lw=0.6)
    handles = [matplotlib.patches.Patch(color=COLORS[g], label=LABELS[g])
               for g in GROUPS if any(group_of(c, df) == g for c in num)]
    ax_bar.legend(handles=handles, ncol=len(handles), loc="lower center",
                  bbox_to_anchor=(0.5, 1.0), frameon=False, fontsize=9)
    fig.savefig(out, dpi=140, bbox_inches="tight")
    print(f"\nFigura guardada en {out}")
    if show:
        plt.show()


def contrib_check(df):
    cc = [c for c in df.columns if c.startswith("ic_contrib_")]
    key = ["Patient", "Session", "Section", "ic_index"]
    if len(cc) < 2 or "ic_index" not in df.columns:
        print("\n(sin ic_contrib_* o ic_index: se omite la comprobación de proporcionalidad)")
        return
    base = df[df["is_positive"] == 1] if "is_positive" in df.columns and (df["is_positive"] == 1).any() else df
    k = base.iloc[0][key]
    sub = df[(df[key] == k).all(axis=1)]
    print("\n== ¿Las ic_contrib_* de un componente son proporcionales entre ventanas? ==")
    if len(sub) < 3:
        print("  el componente elegido aparece en menos de 3 ventanas; no se puede comprobar")
        return
    a, b = sub[cc].mean().nlargest(2).index
    ratio = sub[a] / sub[b].replace(0, np.nan)
    cv = ratio.std() / ratio.mean() if ratio.mean() else np.nan
    print(f"  componente {tuple(k.values)} en {len(sub)} ventanas")
    print(f"  cociente {a} / {b}: media={ratio.mean():.4f}, desviación relativa={cv:.2e}")
    print("  desviación relativa ~0 => una sola topografía fija multiplicada por un número por ventana")


def global_counts(pf, batch_size):
    """Conteos sobre TODO el archivo en streaming, leyendo solo unas pocas columnas."""
    names = set(pf.schema_arrow.names)
    cols = [c for c in WINDOW_KEY + ["is_positive", "ic_raw_label"] if c in names]
    has_pos, has_lab = "is_positive" in cols, "ic_raw_label" in cols
    partials, cross = [], []
    for batch in pf.iter_batches(batch_size=batch_size, columns=cols):
        d = batch.to_pandas()
        agg = {"n": ("Start", "size")}
        if has_pos:
            agg["pos"] = ("is_positive", "sum")
        partials.append(d.groupby(WINDOW_KEY, dropna=False).agg(**agg))
        if has_pos and has_lab:
            cross.append(d.groupby(["ic_raw_label", "is_positive"]).size())
    win = pd.concat(partials).groupby(level=list(range(len(WINDOW_KEY))), dropna=False).sum()
    ct = None
    if cross:
        ct = pd.concat(cross).groupby(level=[0, 1]).sum().unstack(fill_value=0)
    return win, ct, has_pos


def report_global(win, ct, has_pos, total_rows):
    sizes = win["n"]
    print(f"\n== Todo el archivo ({total_rows} filas) ==")
    print(f"  ventanas: {len(sizes)} | filas por ventana min/mediana/max: "
          f"{sizes.min()}/{int(sizes.median())}/{sizes.max()}")
    if not has_pos:
        print("  (no hay columna is_positive en este archivo)")
        return
    pos = win["pos"]
    print(f"  ventanas con 0 positivos: {(pos == 0).sum()} | con 1: {(pos == 1).sum()} | "
          f"con 2 o más: {(pos >= 2).sum()}")
    print(f"  proporción de filas positivas: {pos.sum() / sizes.sum():.4%}")
    if "Patient" in win.index.names:
        per_patient = pos.groupby(level="Patient").sum()
        print(f"  pacientes: {len(per_patient)} | sin ningún positivo: {(per_patient == 0).sum()}")
    if ct is not None:
        print("\n== Clase de ICLabel de las filas positivas vs negativas (todo el archivo) ==")
        print(ct.to_string())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("parquet")
    ap.add_argument("--out", default="dataset_structure.png")
    ap.add_argument("--max-rows", type=int, default=200_000,
                    help="filas que se cargan en memoria para la estructura (por defecto 200000)")
    ap.add_argument("--batch-size", type=int, default=50_000, help=argparse.SUPPRESS)
    ap.add_argument("--no-show", action="store_true", help="solo guarda la figura")
    args = ap.parse_args()
    if args.no_show:
        matplotlib.use("Agg")

    pf = pq.ParquetFile(args.parquet)
    names = pf.schema_arrow.names
    missing = [c for c in WINDOW_KEY if c not in names]
    if missing:
        raise SystemExit(f"Faltan columnas de identificación en el archivo: {missing}")
    print(f"Archivo: {args.parquet}")
    print(f"Filas: {pf.metadata.num_rows} | columnas totales: {len(names)} | "
          f"bloques (row groups): {pf.metadata.num_row_groups}")

    df, total = load_head(pf, args.max_rows, args.batch_size)
    xcols = x_columns(df)
    print(f"Estructura calculada con las primeras {len(df)} filas de {total} "
          f"(columnas de X: {len(xcols)})")
    win = pick_window(df)

    print(f"\n== Ventana elegida: {dict(win.iloc[0][WINDOW_KEY])} ({len(win)} filas) ==")
    print(summarize(df, xcols, win).to_string(index=False))

    cols = [c for c in ["ic_index", "ic_raw_label", "ic_iclabel_prob", "is_positive"] if c in win.columns]
    print("\nFilas de esa ventana (columnas clave):")
    print(win[cols].to_string(index=False))

    excluded = [c for c in df.columns if c not in xcols]
    print(f"\n== Columnas que NO entran a X ({len(excluded)}) ==")
    print(", ".join(excluded))

    contrib_check(df)
    gwin, ct, has_pos = global_counts(pf, args.batch_size)
    report_global(gwin, ct, has_pos, total)
    heatmap(df, xcols, win, args.out, show=not args.no_show)


if __name__ == "__main__":
    main()