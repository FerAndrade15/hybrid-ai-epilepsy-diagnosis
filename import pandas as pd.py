import pandas as pd

df = pd.read_csv(
    r"outputs\artifact\splits\windowed_df_rf_artifact_class_v1.csv"
)

sessions = (
    df[["Patient", "Session", "EDF_path", "split"]]
    .drop_duplicates()
)

print(sessions.groupby("split").size())
print("TOTAL:", len(sessions))