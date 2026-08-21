# Temple University EEG Corpus

## TUH EEG Corpus Structure
```text 
tuh_eeg/
│
├── tuh_eeg/                         # TUEG - General EEG Corpus
│   └── v2.0.2/
│       ├── AAREADME.txt
│       ├── DOCS/
│       │   └── *.list
│       └── edf/
│           └── <group_patient_id>/
│               └── <patient_id>/
│                   └── <session_id>/
│                       └── <montage_id>/
│                           └── *.edf
│
├── tuh_eeg_artifact/                # TUAR - Artifact Corpus
│   └── v3.0.1/
│       ├── AAREADME.txt
│       ├── DOCS/
│       └── edf/
│           └── <montage_id>/
│               ├── *.edf
│               └── *.csv
│
├── tuh_eeg_epilepsy/                # TUEP - Epilepsy Corpus
│   └── v3.0.1/
│       ├── AAREADME.txt
│       ├── DOCS/
│       │   └── metadata_v00.xlsx
│       └── <epilepsy_confirmation>/
│           └── <patient_id>/
│               └── <session_id>/
│                   └── <montage_id>/
│                       ├── *.edf
│                       └── *.csv
│
├── tuh_eeg_events/                  # TUEV - Event Corpus
│   └── v2.0.1/
│       ├── AAREADME.txt
│       └── edf/
│           ├── train/
│           └── eval/
│               └── <patient_id>/
│                   ├── *.edf
│                   ├── *.red
│                   ├── *.htk
│                   └── *.lab
│
└── tuh_eeg_seizure/                 # TUSZ - Seizure Corpus
    └── v2.0.6/
        ├── AAREADME.md
        ├── DOCS/
        │   ├── metadata_v06.xlsx
        │   └── seizure_types_v02.xlsx
        └── edf/
            ├── train/
            ├── dev/
            └── eval/
                └── <patient_id>/
                    └── <session_id>/
                        └── <montage_id>/
                            ├── *.edf
                            └── *.csv
```


## Preprocesamiento

### Exploratory Data Analysis - EDA
#### Univariate Analysis
Distribución de la información y categorías (histogramas, diagramas de barras y bar charts):
- 

## AI System Proposed Method
Analizando la variabilidad y dependencia del análisis de los electroencefalogramas (alta dimensionalidad) en lugar de proponer o implementar un modelo que trabaje cn todo el análisis y clasificación
### 