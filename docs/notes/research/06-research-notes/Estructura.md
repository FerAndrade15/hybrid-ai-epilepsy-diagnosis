# Metodología y análisis del flujo de datos

![[Pasted image 20260523093230.png|391




## Apuntes generales
### Composición de los EEG
Extracting EDF parameters from C:\Users\ferch\Documents\Various\EngineeringDesignAndInnovation\Datasets\tuh_eeg_epilepsy\00_epilepsy\aaaaaamc\s012_2015\01_tcp_ar\aaaaaamc_s012_t001.edf...
Setting channel info structure...
Creating raw.info structure...
Reading 0 ... 64499  =      0.000 ...   257.996 secs...
<Info | 8 non-empty values
 bads: []
 ch_names: EEG FP1-REF, EEG FP2-REF, EEG F3-REF, EEG F4-REF, EEG C3-REF, ...
 chs: 31 EEG
 custom_ref_applied: False
 highpass: 0.0 Hz
 lowpass: 125.0 Hz
 meas_date: 2015-01-01 00:00:00 UTC
 nchan: 31
 projs: []
 sfreq: 250.0 Hz
 subject_info: <subject_info | his_id: aaaaaamc, sex: 2, last_name: aaaaaamc>
 
['EEG FP1-REF', 'EEG FP2-REF', 'EEG F3-REF', 'EEG F4-REF', 'EEG C3-REF', 'EEG C4-REF', 'EEG P3-REF', 'EEG P4-REF', 'EEG O1-REF', 'EEG O2-REF', 'EEG F7-REF', 'EEG F8-REF', 'EEG T3-REF', 'EEG T4-REF', 'EEG T5-REF', 'EEG T6-REF', 'EEG A1-REF', 'EEG A2-REF', 'EEG FZ-REF', 'EEG CZ-REF', 'EEG PZ-REF', 'EEG ROC-REF', 'EEG LOC-REF', 'EEG EKG1-REF', 'EMG-REF', 'EEG T1-REF', 'EEG T2-REF', 'PHOTIC-REF', 'IBI', 'BURSTS', 'SUPPR']


PyQt5
Python 3.11.9


pip list at the moment:
Package                   Version
------------------------- -----------
absl-py                   2.4.0
annotated-doc             0.0.4
annotated-types           0.7.0
anyio                     4.13.0
argon2-cffi               25.1.0
argon2-cffi-bindings      25.1.0
arrow                     1.4.0
asttokens                 3.0.1
astunparse                1.6.3
async-lru                 2.3.0
attrs                     26.1.0
babel                     2.18.0
beautifulsoup4            4.14.3
bleach                    6.3.0
captum                    0.9.0
certifi                   2026.2.25
cffi                      2.0.0
charset-normalizer        3.4.7
classes                   0.4.1
cloudpickle               3.1.2
colorama                  0.4.6
comm                      0.2.3
contourpy                 1.3.3
cycler                    0.12.1
debugpy                   1.8.20
decorator                 5.2.1
defusedxml                0.7.1
executing                 2.2.1
fastapi                   0.136.1
fastjsonschema            2.21.2
filelock                  3.29.0
flatbuffers               25.12.19
fonttools                 4.62.1
fqdn                      1.5.1
fsspec                    2026.4.0
gast                      0.7.0
google-pasta              0.2.0
grpcio                    1.80.0
h11                       0.16.0
h5py                      3.14.0
httpcore                  1.0.9
httpx                     0.28.1
idna                      3.11
ImageIO                   2.37.3
ipykernel                 7.2.0
ipython                   9.13.0
ipython_pygments_lexers   1.1.1
ipywidgets                8.1.8
isoduration               20.11.0
jedi                      0.19.2
Jinja2                    3.1.6
joblib                    1.5.3
json5                     0.14.0
jsonpointer               3.1.1
jsonschema                4.26.0
jsonschema-specifications 2025.9.1
jupyter                   1.1.1
jupyter_client            8.8.0
jupyter-console           6.6.3
jupyter_core              5.9.1
jupyter-events            0.12.0
jupyter-lsp               2.3.1
jupyter_server            2.17.0
jupyter_server_terminals  0.5.4
jupyterlab                4.5.6
jupyterlab_pygments       0.3.0
jupyterlab_server         2.28.0
jupyterlab_widgets        3.0.16
keras                     3.14.0
kiwisolver                1.5.0
lark                      1.3.1
lazy-loader               0.5
libclang                  18.1.1
lime                      0.2.0.1
llvmlite                  0.47.0
markdown-it-py            4.0.0
MarkupSafe                3.0.3
matplotlib                3.10.8
matplotlib-inline         0.2.1
mdurl                     0.1.2
mistune                   3.2.0
ml_dtypes                 0.5.4
mne                       1.12.0
mpmath                    1.3.0
namex                     0.1.0
nbclient                  0.10.4
nbconvert                 7.17.1
nbformat                  5.10.4
nest-asyncio              1.6.0
networkx                  3.6.1
notebook                  7.5.5
notebook_shim             0.2.4
numba                     0.65.1
numpy                     2.4.4
opt_einsum                3.4.0
optree                    0.19.0
overrides                 7.7.0
packaging                 26.0
pandas                    3.0.2
pandocfilters             1.5.1
parso                     0.8.6
pillow                    12.2.0
pip                       24.0
platformdirs              4.9.6
pooch                     1.9.0
prometheus_client         0.25.0
prompt_toolkit            3.0.52
protobuf                  7.34.1
psutil                    7.2.2
pure_eval                 0.2.3
pycparser                 3.0
pydantic                  2.13.3
pydantic_core             2.46.3
pyEDFlib                  0.1.42
Pygments                  2.20.0
pyparsing                 3.3.2
PyQt5                     5.15.11
PyQt5-Qt5                 5.15.2
PyQt5_sip                 12.18.0
python-dateutil           2.9.0.post0
python-json-logger        4.1.0
pywinpty                  3.0.3
PyYAML                    6.0.3
pyzmq                     27.1.0
referencing               0.37.0
requests                  2.33.1
rfc3339-validator         0.1.4
rfc3986-validator         0.1.1
rfc3987-syntax            1.1.0
rich                      15.0.0
rpds-py                   0.30.0
scikit-image              0.26.0
scikit-learn              1.8.0
scipy                     1.17.1
seaborn                   0.13.2
Send2Trash                2.1.0
setuptools                65.5.0
shap                      0.51.0
six                       1.17.0
slicer                    0.0.8
soupsieve                 2.8.3
stack-data                0.6.3
starlette                 1.0.0
sympy                     1.14.0
tensorflow                2.21.0
termcolor                 3.3.0
terminado                 0.18.1
threadpoolctl             3.6.0
tifffile                  2026.3.3
tinycss2                  1.4.0
torch                     2.11.0
torchaudio                2.11.0
torchvision               0.26.0
tornado                   6.5.5
tqdm                      4.67.3
traitlets                 5.14.3
typing_extensions         4.15.0
typing-inspection         0.4.2
tzdata                    2026.1
uri-template              1.3.0
urllib3                   2.6.3
wcwidth                   0.6.0
webcolors                 25.10.0
webencodings              0.5.1
websocket-client          1.9.0
wheel                     0.47.0
widgetsnbextension        4.0.15
wrapt                     2.1.2
Note: you may need to restart the kernel to use updated packages.

[notice] A new release of pip is available: 24.0 -> 26.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip


|   |   |   |
|---|---|---|
|**IZQUIERDOS**|**DERECHOS**|**LÍNEA MEDIA**|
|**Fp1**- Frontopolar izquierdo<br><br>**F3**- Frontal izquierdo<br><br>**F7**- Temporal anterior izquierdo<br><br>**T3**- Temporal medio izquierdo<br><br>**C3**- Central izquierdo<br><br>**P3**- Parietal izquierdo<br><br>**T5**- Temporal posterior izquierdo<br><br>**O1**- Occipital izquierdo|**Fp2**- Frontopolar derecho<br><br>**F4**- Frontal derecho<br><br>**F8**- Temporal anterior derecho<br><br>**T4**- Temporal medio derecho<br><br>**C4**- Central derecho<br><br>**P4**- Parietal derecho<br><br>**T6** - Temporal posterior derecho<br><br>**O2**- Occipital derecho|**Fz**- Frontal medio<br><br>**Cz**- Central medio<br><br>**Pz**- Parietal medio|
|**AURICULARES**|
|**A1**- Auricular izquierdo<br><br>**A2**- Auricular derecho|