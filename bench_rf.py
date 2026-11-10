import sys, time, re, resource, glob
import pandas as pd
from src.core.data_config import LEAKAGE_COLS, OUTPUTS_DIR
from src.core.data_splitter import split_features_target
from src.models.rf_model import build_rf_model

pattern = sys.argv[1] if len(sys.argv) > 1 else "rf_dataset_eye_*"
files = sorted(f for f in glob.glob(str(OUTPUTS_DIR / f"artifact/dataset/_comparison/{pattern}.parquet"))
               if not f.endswith(".raw.parquet"))
print("candidatos:", [f.split("/")[-1] for f in files])
path = files[0]
print("dataset:", path)
df = pd.read_parquet(path)
print("tiene medicas:", [c for c in df.columns if c.startswith(("tuar_", "bipolar_channels", "monopolar_channels"))][:3])
df = df.drop(columns=[c for c in df.columns if c.startswith("tuar_") or "channels" in c], errors="ignore")
df = df[~((df["split"] != "test") & (df["is_positive"] == -1))].copy()
df.loc[df["is_positive"] == -1, "is_positive"] = 0

X, y = split_features_target(df, "train", LEAKAGE_COLS)
X = X.rename(columns=lambda x: re.sub('[^A-Za-z0-9_]+', '', x))
print(f"train: {X.shape} | pos={int(y.sum())}")

for name, params in {
    "medio":  dict(n_estimators=300, max_depth=15, min_samples_split=10, min_samples_leaf=4, max_features="sqrt", sampling_strategy=0.5),
    "pesado": dict(n_estimators=600, max_depth=30, min_samples_split=2,  min_samples_leaf=1, max_features=0.5,    sampling_strategy=1.0),
}.items():
    t = time.time()
    model = build_rf_model(balanced=True, **params)
    model.fit(X, y)
    dt = time.time() - t
    mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6
    print(f"[{name}] fit={dt:.1f}s | pico RAM={mem:.1f} GB | estimado 60 iter = {dt*60/3600:.2f} h")
