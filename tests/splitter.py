import pandas as pd
from src.core.data_config import ARTIFACT_KEYWORDS, WINDOW_REQUESTS_ARTIFACTS
from src.core.data_loader import build_annotations_index
from src.core.windowing import label_windowing
from src.core.corpus_inventory import scan_all
from src.core.patient_registry import load_registry, forced_for
from src.core.data_splitter import (grouped_multilabel_split, grouped_split_from_labels,
                                    split_balance_report)

ARTIFACTS = ["muscle"]        # empieza con uno: ventana de 5 s, la que genera menos ventanas

inv = scan_all()
reg = load_registry()
ann = build_annotations_index("artifact", paths=True)          # corpus COMPLETO
patients = ann["Patient"].unique()

# 1) Restricciones que llegan al splitter
forced = forced_for(reg, patients)
inv_ar = set(inv.loc[inv["corpus"] == "artifact", "patient"].dropna())
inv_sz = set(inv.loc[inv["corpus"] == "seizure", "patient"].dropna())
print(f"pacientes: anotaciones {len(patients)} | inventario {len(inv_ar)}")
print(f"forzados: {len(forced)} | artifact∩TUSZ en inventario: {len(inv_ar & inv_sz)} (esperado 69)")
print(pd.Series(forced).value_counts().to_dict())

sz = inv.loc[inv["corpus"] == "seizure", ["patient", "split"]].drop_duplicates().rename(columns={"split": "tusz"})

for art in ARTIFACTS:
    print("\n" + "=" * 60 + f"\n{art}")
    w = label_windowing(ann, WINDOW_REQUESTS_ARTIFACTS[art], ARTIFACT_KEYWORDS, unreviewd_tokens=True)

    # 2) Multilabel con registro por defecto
    out, asg, rep = grouped_multilabel_split(w, ARTIFACT_KEYWORDS)
    assert out["split"].notna().all(), "hay pacientes sin split"
    assert (out.groupby("Patient")["split"].nunique() == 1).all(), "un paciente en dos splits"
    assert all(asg[p] == s for p, s in forced.items()), "un forzado no se respetó"
    print(rep.round(1).to_string())

    # 3) ¿Qué habría pasado sin el registro?
    _, asg0, _ = grouped_multilabel_split(w, ARTIFACT_KEYWORDS, forced={})
    print("pacientes fijados que quedarían mal sin registro:", sum(asg0[p] != s for p, s in forced.items()))

    # 4) Auditoría contra las carpetas de TUSZ: solo debe salir la diagonal
    m = sz.merge(pd.Series(asg, name="mine").rename_axis("patient").reset_index(), on="patient")
    print(pd.crosstab(m["tusz"], m["mine"]).to_string())
    assert (m["tusz"] == m["mine"]).all(), "hay pacientes de TUSZ fuera de su carpeta"

    # 5) Tu splitter por is_positive, aquí con la etiqueta de ventana como sustituto
    wt = w.rename(columns={"is_excluded": "tuar_is_excluded", "is_ambiguous": "tuar_is_ambiguous"})
    for sw in [0.0, 0.5, 1.0]:
        try:
            o, a, _ = grouped_split_from_labels(wt, target_col=art, size_weight=sw)
            b = split_balance_report(o, target_col=art)
            print(f"\nsw={sw}\n", b.round(4).to_string())
        except ValueError as e:
            print(f"\nsw={sw}: {e}")