#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: _analyze_model_runs.py

Código de síntesis de resultados, generado mediante Claude
======================

Consolida en un solo reporte (Markdown + CSV) todos los logs de consola
que capturaste durante el entrenamiento de los modelos de detección de
artefactos EEG (eye / muscle / non_physiological, familia RF, etc.).

FLUJO DE TRABAJO SUGERIDO
--------------------------
1. Cada vez que corrés un script de entrenamiento, copiá la salida de la
   consola (completa o parcial, no importa si quedó cortada) y pegala en
   un archivo .txt nuevo. Opcionalmente, en la primera línea del archivo
   podés poner una etiqueta/fecha manual, por ejemplo:

       # fecha: 2025-01-15 - primer sweep con BalancedRandomForest

   Si no ponés esa línea, el script te va a preguntar una etiqueta por
   archivo (o va a usar la fecha de modificación del archivo si corrés
   en modo no interactivo).

2. Correr:
       python analyze_model_runs.py logs/*.txt -o reporte

   (o "uv run python analyze_model_runs.py logs/*.txt -o reporte" si
   usás uv, como en tus otros scripts)

3. Te va a preguntar por consola SOLO lo que no pudo inferir del texto
   (por ejemplo el artifact de un bloque roto, o la etiqueta de un
   archivo). Podés dejar vacío (Enter) si no lo sabés/no importa.

4. Vas a obtener:
       reporte.csv  -> una fila por corrida de modelo, para filtrar/
                        ordenar en Excel/Sheets si querés.
       reporte.md   -> reporte legible:
                          - tabla comparativa por artifact (ordenada
                            por F1, con la mejor por F1 y la de menor
                            FP/día marcadas)
                          - evolución de cada modelo (mismo nombre,
                            ej. rf_eye_w2s1_1) a través de sus distintas
                            corridas/reruns
                          - lista de corridas incompletas o que
                            terminaron en Traceback

LIMITACIONES
------------
Este es un parser heurístico basado en el formato que ya usan tus
scripts (bloques "ARTIFACT:", "Modelo:", "Train: ... | Val: ... |
Test: ...", "best_params=...", "Metrics results: {...}", "General
metrics -----"). Si el formato cambia de esos prints, se requieren
ajustes para las expresiones regulares (están todas juntas al
principio del archivo, marcadas como RE_*). Cuando algo no se pueda
inferir automáticamente vas a ver "?" en el reporte: revisalo a mano
o completalo en el CSV.

"""

from __future__ import annotations

import argparse
import ast
import csv
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, fields
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Expresiones regulares (ajustá acá si tu formato de print cambia)
# ---------------------------------------------------------------------------

RE_ARTIFACT_HEADER = re.compile(r'^ARTIFACT:\s*([A-Za-z_]+)', re.MULTILINE)
RE_ARTIFACT_DASH = re.compile(r'^-{5,}\s*([A-Za-z_]+)\s*-{5,}\s*$', re.MULTILINE)
RE_WINDOWS = re.compile(r'windows:\s*([\d.]+)s(?:\s*\(([\d.]+)s stride\))?')
RE_MODELO = re.compile(r'^Modelo:\s*(\S+)', re.MULTILINE)
RE_TVT = re.compile(
    r'Train:\s*(\d+)\s*\(pos=(\d+)\)\s*\|\s*Val:\s*(\d+)\s*\(pos\s*=\s*(\d+)\)\s*\|\s*Test:\s*(\d+)\s*\(pos=(\d+)\)'
)
RE_BEST_PARAMS = re.compile(r"best_params\s*=\s*(\{[^\n]*\})")
RE_F1_VAL = re.compile(r'F1\(val\)\s*=\s*([\d.]+)')
RE_METRICS_DICT = re.compile(r"Metrics results:\s*(\{[^\n]*\})")
RE_TRACEBACK = re.compile(r'^Traceback \(most recent call last\):', re.MULTILINE)
RE_ERROR_LINE = re.compile(r'^(\S*Error\S*):?\s*(.*)$', re.MULTILINE)
RE_NPWRAP = re.compile(r'np\.(?:float64|int64)\(([^)]*)\)')
RE_LABEL_COMMENT = re.compile(r'#\s*(?:fecha|label|etiqueta)\s*:\s*(.+)', re.IGNORECASE)

METRIC_KEYS = [
    "model", "sensitivity", "specificity", "precision", "accuracy",
    "f1_score", "auc_roc", "false_alar_rate", "fp_per_day",
    "TP", "FP", "TN", "FN", "n_test_windows", "covered_test_hours",
]


# ---------------------------------------------------------------------------
# Estructura de una corrida
# ---------------------------------------------------------------------------

@dataclass
class Run:
    file: str
    file_label: str
    line: int
    source: str  # "final_report" | "general_metrics" | "failed"
    artifact: str | None = None
    model: str | None = None
    window_s: str | None = None
    stride_s: str | None = None
    occurrence: int = 1
    train_n: str | None = None
    train_pos: str | None = None
    val_n: str | None = None
    val_pos: str | None = None
    test_n: str | None = None
    test_pos: str | None = None
    best_params: str | None = None
    f1_val: str | None = None
    sensitivity: str | None = None
    specificity: str | None = None
    precision: str | None = None
    accuracy: str | None = None
    f1_score: str | None = None
    auc_roc: str | None = None
    false_alar_rate: str | None = None
    fp_per_day: str | None = None
    TP: str | None = None
    FP: str | None = None
    TN: str | None = None
    FN: str | None = None
    n_test_windows: str | None = None
    covered_test_hours: str | None = None
    note: str = ""

    def as_row(self) -> dict:
        return {f.name: getattr(self, f.name) for f in fields(self)}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_pydict(raw: str) -> dict | None:
    """Convierte un literal tipo {'a': 1, 'b': np.float64(0.5)} en un dict real."""
    cleaned = RE_NPWRAP.sub(r'\1', raw)
    try:
        return ast.literal_eval(cleaned)
    except Exception:
        return None


def context_before(text: str, pos: int, chars: int = 4000) -> str:
    return text[max(0, pos - chars):pos]


def find_last(pattern: re.Pattern, text: str):
    matches = list(pattern.finditer(text))
    return matches[-1] if matches else None


def window_stride_from_model(model_name: str | None):
    if not model_name:
        return None, None
    m = re.search(r'w([\d.]+)s([\d.]+)', model_name)
    if m:
        return m.group(1), m.group(2)
    return None, None


def _safe_float(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def fnum(v, nd=4):
    f = _safe_float(v)
    if f is None:
        return str(v) if v not in (None, "") else "—"
    return f"{f:.{nd}f}"


# ---------------------------------------------------------------------------
# Parsing principal
# ---------------------------------------------------------------------------

def parse_final_report_runs(text: str, filename: str, file_label: str) -> list[Run]:
    """Fuente PRIMARIA: bloques 'Metrics results: {...}' del Final report."""
    runs = []
    for m in RE_METRICS_DICT.finditer(text):
        data = parse_pydict(m.group(1))
        if not data:
            continue
        line_no = text.count('\n', 0, m.start()) + 1
        ctx = context_before(text, m.start())

        artifact = None
        am = find_last(RE_ARTIFACT_DASH, ctx) or find_last(RE_ARTIFACT_HEADER, ctx)
        if am:
            artifact = am.group(1)

        bp_m = find_last(RE_BEST_PARAMS, ctx)
        best_params = bp_m.group(1) if bp_m else None

        f1_m = find_last(RE_F1_VAL, ctx)
        f1_val = f1_m.group(1) if f1_m else None

        model_name = data.get('model')
        window_s, stride_s = window_stride_from_model(model_name)
        if window_s is None:
            wctx = find_last(RE_WINDOWS, ctx)
            if wctx:
                window_s, stride_s = wctx.group(1), wctx.group(2)

        run = Run(
            file=filename, file_label=file_label, line=line_no,
            source="final_report", artifact=artifact, model=model_name,
            window_s=window_s, stride_s=stride_s,
            best_params=best_params, f1_val=f1_val,
        )
        for k in METRIC_KEYS:
            if k != "model" and k in data:
                setattr(run, k, data[k])
        runs.append(run)
    return runs


def parse_general_metrics_runs(text: str, filename: str, file_label: str,
                                already_models: set[str]) -> list[Run]:
    """Fuente de RESPALDO: bloques 'General metrics -----' (para logs
    cortados que no llegaron al Final report)."""
    lines = text.splitlines()
    runs = []
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith("General metrics"):
            block: dict[str, str] = {}
            j = i + 1
            while j < len(lines):
                stripped = lines[j].strip()
                if not stripped:
                    break
                parts = stripped.split(None, 1)
                if len(parts) != 2:
                    break
                key, val = parts
                block[key] = RE_NPWRAP.sub(r'\1', val).strip()
                j += 1

            model_name = block.get('model')
            if model_name and model_name in already_models:
                i = j
                continue

            char_pos = sum(len(l) + 1 for l in lines[:i])
            ctx = context_before(text, char_pos)

            artifact = None
            am = find_last(RE_ARTIFACT_HEADER, ctx) or find_last(RE_ARTIFACT_DASH, ctx)
            if am:
                artifact = am.group(1)

            window_s, stride_s = window_stride_from_model(model_name)
            if window_s is None:
                wctx = find_last(RE_WINDOWS, ctx)
                if wctx:
                    window_s, stride_s = wctx.group(1), wctx.group(2)

            tvt = find_last(RE_TVT, ctx)
            bp_m = find_last(RE_BEST_PARAMS, ctx)

            run = Run(
                file=filename, file_label=file_label, line=i + 1,
                source="general_metrics", artifact=artifact, model=model_name,
                window_s=window_s, stride_s=stride_s,
                best_params=bp_m.group(1) if bp_m else None,
            )
            if tvt:
                (run.train_n, run.train_pos, run.val_n,
                 run.val_pos, run.test_n, run.test_pos) = tvt.groups()
            for k in METRIC_KEYS:
                if k != "model" and k in block:
                    setattr(run, k, block[k])
            runs.append(run)
            i = j
        else:
            i += 1
    return runs


def parse_failed_runs(text: str, filename: str, file_label: str) -> list[Run]:
    runs = []
    for m in RE_TRACEBACK.finditer(text):
        line_no = text.count('\n', 0, m.start()) + 1
        ctx = context_before(text, m.start())
        after = text[m.end(): m.end() + 3000]

        err_m = RE_ERROR_LINE.search(after)
        error_msg = f"{err_m.group(1)}: {err_m.group(2)}".strip() if err_m else "Error no identificado"

        artifact = None
        am = find_last(RE_ARTIFACT_HEADER, ctx) or find_last(RE_ARTIFACT_DASH, ctx)
        if am:
            artifact = am.group(1)
        mm = find_last(RE_MODELO, ctx)
        model_name = mm.group(1) if mm else None

        runs.append(Run(
            file=filename, file_label=file_label, line=line_no,
            source="failed", artifact=artifact, model=model_name,
            note=error_msg,
        ))
    return runs


# ---------------------------------------------------------------------------
# Interactividad
# ---------------------------------------------------------------------------

def get_file_label(path: Path, text: str, interactive: bool) -> str:
    m = RE_LABEL_COMMENT.search(text[:500])
    if m:
        return m.group(1).strip()
    default = datetime.fromtimestamp(path.stat().st_mtime).strftime('%Y-%m-%d %H:%M')
    if not interactive:
        return default
    ans = input(f"Etiqueta/fecha para '{path.name}' [Enter = {default}]: ").strip()
    return ans or default


def fill_missing_interactive(runs: list[Run], interactive: bool) -> None:
    if not interactive:
        return
    for r in runs:
        if r.source == "failed":
            continue
        if not r.artifact:
            print("\n--- Falta 'artifact' ---")
            print(f"archivo: {r.file} (línea ~{r.line}) | modelo: {r.model}")
            ans = input("Artifact (eye/muscle/non_physiological) [Enter=omitir]: ").strip()
            r.artifact = ans or r.artifact
        if not r.model:
            print("\n--- Falta 'model' ---")
            print(f"archivo: {r.file} (línea ~{r.line}) | artifact: {r.artifact}")
            ans = input("Nombre del modelo [Enter=omitir]: ").strip()
            r.model = ans or r.model


def assign_occurrences(runs: list[Run]) -> None:
    counters: dict[str, int] = defaultdict(int)
    for r in runs:
        key = r.model or f"(sin nombre @ {r.file}:{r.line})"
        counters[key] += 1
        r.occurrence = counters[key]


# ---------------------------------------------------------------------------
# Reporte Markdown
# ---------------------------------------------------------------------------

def write_markdown(runs: list[Run], out_path: Path) -> None:
    ok_runs = [r for r in runs if r.source != "failed"]
    failed_runs = [r for r in runs if r.source == "failed"]

    by_artifact: dict[str, list[Run]] = defaultdict(list)
    for r in ok_runs:
        by_artifact[r.artifact or "SIN ARTIFACT"].append(r)

    lines = [
        "# Reporte consolidado de modelos",
        "",
        f"_Generado: {datetime.now().strftime('%Y-%m-%d %H:%M')}_",
        "",
        f"Corridas totales parseadas: **{len(runs)}** "
        f"(ok: {len(ok_runs)}, fallidas/incompletas: {len(failed_runs)})",
    ]

    for artifact in sorted(by_artifact):
        runs_a = by_artifact[artifact]
        lines.append(f"\n## Artifact: `{artifact}`\n")

        # última ocurrencia de cada modelo -> tabla comparativa
        latest: dict[str, Run] = {}
        for r in runs_a:
            key = r.model or f"{r.file}:{r.line}"
            latest[key] = r  # el último visto (orden de parseo) sobreescribe
        rows = sorted(
            latest.values(),
            key=lambda r: (_safe_float(r.f1_score) if r.f1_score is not None else -1),
            reverse=True,
        )

        lines.append("| Modelo | Ventana | Stride | Sens. | Espec. | Prec. | F1 | AUC | FP/día | Ocurr. | Archivo |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|---|")
        for r in rows:
            lines.append(
                f"| {r.model or '?'} | {r.window_s or '?'}s | {r.stride_s or '?'}s "
                f"| {fnum(r.sensitivity, 3)} | {fnum(r.specificity, 3)} | {fnum(r.precision, 4)} "
                f"| {fnum(r.f1_score, 4)} | {fnum(r.auc_roc, 4)} | {fnum(r.fp_per_day, 1)} "
                f"| {r.occurrence} | {r.file_label} |"
            )

        if rows:
            best_f1 = rows[0]
            with_fp = [r for r in rows if _safe_float(r.fp_per_day) is not None]
            if with_fp:
                best_fp = min(with_fp, key=lambda r: _safe_float(r.fp_per_day))
                lines.append(
                    f"\n**Mejor F1:** `{best_f1.model}` (F1={fnum(best_f1.f1_score, 4)}) — "
                    f"**Menor FP/día:** `{best_fp.model}` "
                    f"(FP/día={fnum(best_fp.fp_per_day, 1)}, F1={fnum(best_fp.f1_score, 4)})"
                )

    # Evolución de modelos con más de una corrida
    lines.append("\n## Evolución (modelos con más de una corrida)\n")
    by_model: dict[str, list[Run]] = defaultdict(list)
    for r in ok_runs:
        if r.model:
            by_model[r.model].append(r)

    any_evo = False
    for model in sorted(by_model):
        rs = by_model[model]
        if len(rs) < 2:
            continue
        any_evo = True
        lines.append(f"\n### `{model}` ({rs[0].artifact or '?'})\n")
        lines.append("| # | Archivo | F1 | Sens. | Espec. | FP/día | ¿Cambió vs. anterior? |")
        lines.append("|---|---|---|---|---|---|---|")
        prev = None
        for r in rs:
            changed = "—"
            if prev is not None:
                same = (fnum(prev.f1_score, 4) == fnum(r.f1_score, 4)
                        and fnum(prev.fp_per_day, 1) == fnum(r.fp_per_day, 1))
                changed = "= igual" if same else "⚠️ cambió"
            lines.append(
                f"| {r.occurrence} | {r.file_label} | {fnum(r.f1_score, 4)} "
                f"| {fnum(r.sensitivity, 3)} | {fnum(r.specificity, 3)} "
                f"| {fnum(r.fp_per_day, 1)} | {changed} |"
            )
            prev = r
    if not any_evo:
        lines.append("_No se detectaron modelos con más de una corrida en los archivos analizados._")

    if failed_runs:
        lines.append("\n## Corridas incompletas / fallidas\n")
        lines.append("| Archivo | Línea | Artifact | Modelo | Error |")
        lines.append("|---|---|---|---|---|")
        for r in failed_runs:
            lines.append(f"| {r.file} | {r.line} | {r.artifact or '?'} | {r.model or '?'} | {r.note} |")

    out_path.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Consolida logs de entrenamiento (RF, etc.) en un reporte único comparable."
    )
    ap.add_argument("files", nargs="+", help="Archivos .txt con las salidas de consola")
    ap.add_argument("-o", "--output", default="reporte_modelos",
                     help="Prefijo de salida (default: reporte_modelos)")
    ap.add_argument("--no-interactive", action="store_true",
                     help="No preguntar nada; dejar vacío lo que falte")
    ap.add_argument("--no-sort", action="store_true",
                     help="No ordenar los archivos por nombre antes de procesar "
                          "(por default se ordenan alfabéticamente; nombralos con "
                          "fecha/prefijo si querés que la evolución quede en orden)")
    args = ap.parse_args()

    paths = [Path(f) for f in args.files]
    if not args.no_sort:
        paths.sort(key=lambda p: p.name)

    interactive = (not args.no_interactive) and sys.stdin.isatty()

    all_runs: list[Run] = []
    for p in paths:
        if not p.exists():
            print(f"[aviso] no existe: {p}", file=sys.stderr)
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        label = get_file_label(p, text, interactive)

        final_runs = parse_final_report_runs(text, p.name, label)
        already = {r.model for r in final_runs if r.model}
        general_runs = parse_general_metrics_runs(text, p.name, label, already)
        failed = parse_failed_runs(text, p.name, label)

        all_runs.extend(final_runs)
        all_runs.extend(general_runs)
        all_runs.extend(failed)

    if not all_runs:
        print("No se encontró ninguna corrida reconocible en los archivos dados.", file=sys.stderr)
        sys.exit(1)

    assign_occurrences(all_runs)
    fill_missing_interactive(all_runs, interactive)

    out_csv = Path(f"{args.output}.csv")
    out_md = Path(f"{args.output}.md")

    with out_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[fl.name for fl in fields(Run)])
        writer.writeheader()
        for r in all_runs:
            writer.writerow(r.as_row())

    write_markdown(all_runs, out_md)

    print("\nListo:")
    print(f"  - {out_csv}  ({len(all_runs)} filas)")
    print(f"  - {out_md}")


if __name__ == "__main__":
    main()