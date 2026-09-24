# smoke_test_cnn.py
import pandas as pd
from pathlib import Path
from src.models.cnn_artifact_detector import binary_cnn

OUT = Path("/workspace/ml-outputs/artifact")
split_dir = OUT / "splits"
base_name = "split_train70.0_val15.0_test15.0_p10_v1_eye_w5_s2_sw0.7_ua0.1"

df_full = pd.read_parquet(split_dir / f"{base_name}.parquet")

# Reescribe rutas de Windows/WSL a las del pod
df_full["EDF_path"] = (
    df_full["EDF_path"].astype(str)
    .str.replace("\\", "/", regex=False)
    .str.replace(r"^.*?tuh_eeg_artifact/", "/workspace/data/tuh_eeg_artifact/", regex=True)
)
missing = [p for p in df_full["EDF_path"].unique() if not Path(p).exists()]
print("EDF no encontrados:", len(missing), missing[:3])
assert not missing, "Revisa la regex de rutas"

# Muestreo con positivos y negativos en cada split
def sample_split(df, split, n_pos=60, n_neg=140):
    d = df[df["split"] == split]
    return pd.concat([d[d["eye"] == 1].head(n_pos), d[d["eye"] == 0].head(n_neg)])

df_small = pd.concat([sample_split(df_full, s) for s in ["train", "val", "test"]])
summary = df_small.groupby("split")["eye"].agg(["size", "sum"])
print(summary)
assert (summary["sum"] > 0).all(), "Algún split quedó sin positivos"

results = binary_cnn(
    windowed_df=df_small,
    target_col="eye",
    model_name="smoke_test_eye",
    window_size_sec=5.0,
    sfreq=256,
    n_channels=18,
    session_cache_dir=str(OUT / "cache/sessions"),
    ica_cache_dir=str(OUT / "cache/ica"),
    models_dir="models_cnn_smoke_test",
    model_type="lightweight",
    epochs=1,
    batch_size=8,
    checkpoints_dir="./checkpoints_smoke_test",
    force_retrain=True,
)

print("\n[SMOKE TEST OK]")
print(results["metrics_results"])