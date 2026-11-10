import pandas as pd
from backend.ml_service.utils.data_config import OUTPUTS_DIR
from backend.ml_service.utils.data_loader import build_annotations_index

PP = OUTPUTS_DIR / "seizure" / "pp_probs"
sess = pd.read_csv(PP / "sessions.csv")
ann = build_annotations_index(
    "seizure", n_patients=None, paths=True,
    CACHE_DIR=OUTPUTS_DIR / "seizure" / "annotations")
first = ann.drop_duplicates("Patient").set_index("Patient")
pat = sess.drop_duplicates("Patient").copy()
pat["Partition"] = pat["Patient"].map(first["Partition"])
pat["Montage"] = pat["Patient"].map(first["Montage"])
print(pat.groupby(["split", "Partition"]).size())
print(pat.groupby(["split", "Montage"]).size())
