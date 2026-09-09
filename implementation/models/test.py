import pandas as pd

path = r"C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_non_physiological.parquet"
df = pd.read_parquet(path)

print("Shape:", df.shape)
print("\n¿Existe is_positive?:", "is_positive" in df.columns)
print("\nDistribución is_positive:")
print(df["is_positive"].value_counts(dropna=False))

print("\n¿Existen las columnas tuar_ que esperarías?:")
print([c for c in df.columns if c.startswith("tuar_")])

print("\nDistribución ic_target_label:")
print(df["ic_target_label"].value_counts(dropna=False))

print("\nCruce ic_target_label x tuar_non_physiological:")
print(pd.crosstab(df["ic_target_label"], df["tuar_non_physiological"]))