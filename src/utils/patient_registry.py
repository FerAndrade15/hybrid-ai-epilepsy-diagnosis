
""""
# File: patient_registry.py

Split of patients between corpus registry, saving limitations of each split to follow 
corpus pre-divided.
"""
# patient_registry.py

# Data management libraries
import os
import sys
import json
from pathlib import Path
from datetime import datetime

# Project modules
from src.core.data_config import BASE_DIR

REG_PATH = BASE_DIR / "outputs" / "patients_corpus_registry.json"
SPLIT_PRIORITY = {  "train":0,
                    "val": 1,
                    "test": 2,
                }
FIXED_CORPUS = ("seizure",)          # Corpus with fixed distribution (train/val/test)

class RegistryConflict(ValueError):
    pass

def load_registry(path=REG_PATH):
    path = Path(path)
    return json.loads(path.read_text()) if path.exists() else {"meta": {}, "patients": {}}

def save_registry(reg, path=REG_PATH):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    reg["meta"]["updated_at"] = datetime.now().isoformat(timespec="seconds")
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(reg, indent=2, sort_keys=True))
    os.replace(tmp, path)

def folder_rules(inv, constrained=FIXED_CORPUS):
    t = inv[inv["corpus"].isin(constrained)
            & inv["split"].isin(SPLIT_PRIORITY)                    
        ]
    rules = {}
    for corpus, patient, split in zip(t["corpus"], t["patient"], t["split"]):
        cur = rules.get(patient)
        if cur is None or SPLIT_PRIORITY[split] > SPLIT_PRIORITY[cur[0]]:
            rules[patient] = (split, f"folder:{corpus}")
    return rules

def _add(reg, patient, split, source):
    if split not in SPLIT_PRIORITY:
        raise RegistryConflict(f"split inválido {split!r} para {patient}")
    cur = reg["patients"].get(patient)
    if cur is None:
        reg["patients"][patient] = {"split": split, "source": source}
    elif cur["split"] != split:
        raise RegistryConflict(f"{patient}: ya está en '{cur['split']}' ({cur['source']}), "
                               f"se intentó '{split}' ({source})")

def add_folder_rules(reg, inv, constrained=FIXED_CORPUS):
    rules = folder_rules(inv, constrained)
    for patient, (split, source) in rules.items():
        _add(reg, patient, split, source)
    reg["meta"]["constrained"] = list(constrained)
    reg["meta"]["inventory_patients"] = {
        f"{c}/{s}": int(n) for (c, s), n in
        inv[inv["corpus"].isin(constrained)].groupby(["corpus", "split"])["patient"].nunique().items()}
    return len(rules)

def verify_folder_rules(reg, inv, constrained=FIXED_CORPUS):
    now = folder_rules(inv, constrained)
    saved = {p: e["split"] for p, e in reg["patients"].items() if e["source"].startswith("folder:")}
    changed = {p: (saved[p], now[p][0]) for p in saved if p in now and saved[p] != now[p][0]}
    return changed, sorted(set(saved) - set(now)), sorted(set(now) - set(saved))

def register_assignment(reg, assignment, corpus):
    for patient, split in assignment.items():
        _add(reg, patient, split, f"splitter:{corpus}")

def forced_for(reg, patients, source_prefix=None):
    return {p: reg["patients"][p]["split"] for p in set(patients)
            if p in reg["patients"]
            and (source_prefix is None or reg["patients"][p]["source"].startswith(source_prefix))}

def reset_source(reg, source):
    gone = [p for p, e in reg["patients"].items() if e["source"] == source]
    for p in gone:
        del reg["patients"][p]
    return len(gone)

def add_shared_rules(reg, inv, corpora=("artifact", "epilepsy"), split="train"):
    """Fija un split común a los pacientes compartidos entre `corpora` que aún no tienen regla."""
    sets = [set(inv.loc[inv["corpus"] == c, "patient"].dropna()) for c in corpora]
    added = 0
    for p in sorted(set.intersection(*sets)):
        if p not in reg["patients"]:
            _add(reg, p, split, f"shared:{'+'.join(corpora)}")
            added += 1
    return added

def selftest():
    import tempfile
    import pandas as pd
    inv = pd.DataFrame({
        "corpus": ["seizure"] * 3 + ["artifact"] * 3,
        "patient": ["aaaaaaaa", "bbbbbbbb", "cccccccc", "aaaaaaaa", "bbbbbbbb", "dddddddd"],
        "split": ["test", "train", "val", "no_folder", "no_folder", "no_folder"],
    })
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "reg.json"
        reg = load_registry(path)
        assert add_folder_rules(reg, inv) == 3
        assert forced_for(reg, ["aaaaaaaa", "bbbbbbbb", "dddddddd"]) == {"aaaaaaaa": "test", "bbbbbbbb": "train"}
        register_assignment(reg, {"aaaaaaaa": "test", "bbbbbbbb": "train", "dddddddd": "val"}, "artifact")
        save_registry(reg, path)
        reg2 = load_registry(path)
        assert forced_for(reg2, ["dddddddd"], source_prefix="folder:") == {}
        assert forced_for(reg2, ["dddddddd"]) == {"dddddddd": "val"}
        try:
            register_assignment(reg2, {"dddddddd": "train"}, "epilepsy")
            raise AssertionError("debió lanzar RegistryConflict")
        except RegistryConflict:
            pass
    print("[OK] patient_registry")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
        sys.exit()

    import pandas as pd
    from src.utils.corpus_inventory import scan_all

    print(f"Registro: {REG_PATH}   (comprueba que cuelga de la raíz de tu proyecto)")
    inv = scan_all()
    reg = load_registry()
    print(f"Reglas de carpeta añadidas o confirmadas: {add_folder_rules(reg, inv)}")
    print(f"Reglas compartidas artifact+epilepsy añadidas: {add_shared_rules(reg, inv)}")   # NUEVO
    changed, gone, new = verify_folder_rules(reg, inv)
    print(f"Cambiaron respecto al disco: {len(changed)} | ya no están: {len(gone)} | nuevos: {len(new)}")
    save_registry(reg)

    print("\n", pd.DataFrame(reg["patients"]).T.groupby(["source", "split"]).size().to_string())
    print("   esperado: folder:seizure -> test 43, train 579, val 53")
    for corpus in ("artifact", "epilepsy"):
        pats = inv.loc[inv["corpus"] == corpus, "patient"].unique()
        print(f"Forzados en {corpus}: {pd.Series(forced_for(reg, pats)).value_counts().to_dict()}")
    print("   esperado: artifact train 65, val 1, test 3 | epilepsy train 17, val 3")