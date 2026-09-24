check_patients
```bash
from pathlib import Path

from src.core.data_loader import build_annotations_index
 

df = build_annotations_index("artifact", n_patients=30, paths=True, CACHE_DIR=Path("D:/Users/disenoeinnovacion/ml-outputs/artifact/annotations"))

print(df["Patient"].nunique(), "pacientes")
```

tmp_patients
``` bash
from pathlib import Path

from src.core.data_loader import build_annotations_index

df = build_annotations_index("artifact", n_patients=30, paths=True, CACHE_DIR=Path("D:/Users/disenoeinnovacion/ml-outputs/artifact/annotations"))

print(df["Patient"].nunique(), "pacientes")
```

from pathlib import Path

from src.core.data_loader import build_annotations_index
 

df = build_annotations_index("artifact", n_patients=50, paths=True, CACHE_DIR=Path("D:/Users/disenoeinnovacion/ml-outputs/artifact/annotations"))

print(df["Patient"].nunique(), "pacientes")


import pandas as pd
df = pd.read_parquet("D:\Users\disenoeinnovacion\ml-outputs\artifact\features\featured_eye_w5_s2_bipFalse_icaTrue_23961c_v4.parquet")