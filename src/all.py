# Evolutive Test Bench

# Data analysis libraries
import mne
import pandas as pd
import numpy as np
from pathlib import Path

# Internal project modules 
from implementation.core.data_config import find_project_root

# Shared config data for EEG preprocessing
from implementation.core.data_config import ALL_MONTAGES, CORPUS_PATHS, BASE_PATH

# Data integration libraries
from tabulate import tabulate

# Data analysis libraries
from IPython.display import display

# Extract by patient and session
sessions = pd.DataFrame(get_session_data("artifact", n_patients=1))

if sessions.empty:
    print("No sessions found")
else:
    display_df = sessions.copy()
    for col in ("edf", "csv"):
        if col in display_df:
            display_df[col] = display_df[col].map(lambda p: p.name if isinstance(p, Path) else str(p))

    print("\n== Session summary ==")
    print(tabulate(display_df, headers="keys", tablefmt="psql", showindex=False))
    print(f"\nTotal sessions: {len(display_df)}")
    print(f"Patients: {display_df['patient'].nunique()}")
    print(f"Montages: {', '.join(sorted(display_df['montage'].unique()))}\n")

    for idx, row in sessions.iterrows():
        print("=" * 60)
        print(f"Session {idx + 1}: patient={row['patient']} montage={row['montage']}")
        print(f"Loading: {row['edf'].name} / {row['csv'].name}")

        # Manual extraction 
        raw = load_raw_edf(row["edf"])
        ch_names = raw.ch_names
        ch_preview = ", ".join(ch_names[:10])
        if len(ch_names) > 10:
            ch_preview += ", ..."
        print(f">> Channels: {len(ch_names)} [{ch_preview}]")
        print(f">> Duration: {raw.times[-1]:.1f} s, Frequency: {raw.info['sfreq']} Hz")

        # Manual extraction 
        ann = load_annotations(row["csv"])
        print("Annotations head:")
        print(tabulate(ann.head(), headers="keys", tablefmt="psql", showindex=False))
        print()

# Visualize annotations (automated general functions)
sessions = build_annotations_index("artifact", n_patients=1)
display(sessions)