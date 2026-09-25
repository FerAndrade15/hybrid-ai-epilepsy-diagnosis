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

