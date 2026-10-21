Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\windows\system32> cd "C:\Users\ferch\Documents\Various\EngineeringDesignAndInnovation\hybrid-ai-epilepsy-diagnosis"
PS C:\Users\ferch\Documents\Various\EngineeringDesignAndInnovation\hybrid-ai-epilepsy-diagnosis> wsl
ferch@BlackAR:/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis$ un run python inspect_data_structure.py /mnt/d/ml-outputs/artifact/dataset/rf_dataset_muscle_w5_s2_ua0.2_p213_v5.parquet
un: command not found
ferch@BlackAR:/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis$ uv run python inspect_data_structure.py /mnt/d/ml-outputs/artifact/dataset/r
f_dataset_muscle_w5_s2_ua0.2_p213_v5.parquet
/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/bin/python3: can't open file '/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/inspect_data_structure.py': [Errno 2] No such file or directory
ferch@BlackAR:/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis$ uv run python -m test.inspect_data_structure /mnt/d/ml-outputs/artifact/data
set/rf_dataset_muscle_w5_s2_ua0.2_p213_v5.parquet
Traceback (most recent call last):
  File "<frozen runpy>", line 189, in _run_module_as_main
  File "<frozen runpy>", line 112, in _get_module_details
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/test.py", line 3, in <module>
    df = pd.read_csv(
         ^^^^^^^^^^^^
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/lib/python3.11/site-packages/pandas/io/parsers/readers.py", line 1904, in _make_engine
    self.handles = get_handle(
                   ^^^^^^^^^^^
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/lib/python3.11/site-packages/pandas/io/common.py", line 926, in get_handle
    handle = open(
             ^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'outputs\\artifact\\splits\\windowed_df_rf_artifact_class_v1.csv'
ferch@BlackAR:/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis$ uv run python test/inspect_data_structure.py /mnt/d/ml-outputs/artifact/dataset/rf_dataset_muscle_w5_s2_ua0.2_p213_v5.parquet
/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/bin/python3: can't open file '/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/test/inspect_data_structure.py': [Errno 2] No such file or directory
ferch@BlackAR:/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis$ uv run python tests/inspect_data_structure.py /mnt/d/ml-outputs/artifact/dat
aset/rf_dataset_muscle_w5_s2_ua0.2_p213_v5.parquet
Traceback (most recent call last):
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/tests/inspect_data_structure.py", line 186, in <module>
    main()
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/tests/inspect_data_structure.py", line 160, in main
    df = pd.read_parquet(args.parquet)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/lib/python3.11/site-packages/pandas/io/parquet.py", line 671, in read_parquet
    return impl.read(
           ^^^^^^^^^^
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/lib/python3.11/site-packages/pandas/io/parquet.py", line 253, in read
    path_or_handle, handles, filesystem = _get_path_or_handle(
                                          ^^^^^^^^^^^^^^^^^^^^
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/lib/python3.11/site-packages/pandas/io/parquet.py", line 141, in _get_path_or_handle
    handles = get_handle(
              ^^^^^^^^^^^
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/lib/python3.11/site-packages/pandas/io/common.py", line 935, in get_handle
    handle = open(handle, ioargs.mode)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/mnt/d/ml-outputs/artifact/dataset/rf_dataset_muscle_w5_s2_ua0.2_p213_v5.parquet'
ferch@BlackAR:/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis$   sudo mkdir -p /mnt/d
  sudo mount -t drvfs D: /mnt/d
[sudo: authenticate] Password:
ferch@BlackAR:/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis$ uv run python tests/inspect_data_structure.py /mnt/d/ml-outputs/artifact/dataset/rf_dataset_muscle_w5_s2_ua0.2_p213_v5.parquet
Traceback (most recent call last):
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/tests/inspect_data_structure.py", line 186, in <module>
    main()
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/tests/inspect_data_structure.py", line 160, in main
    df = pd.read_parquet(args.parquet)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/lib/python3.11/site-packages/pandas/io/parquet.py", line 671, in read_parquet
    return impl.read(
           ^^^^^^^^^^
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/lib/python3.11/site-packages/pandas/io/parquet.py", line 260, in read
    pa_table = self.api.parquet.read_table(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/lib/python3.11/site-packages/pyarrow/parquet/core.py", line 1964, in read_table
    return dataset.read(columns=columns, use_threads=use_threads,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/lib/python3.11/site-packages/pyarrow/parquet/core.py", line 1590, in read
    table = self._dataset.to_table(
            ^^^^^^^^^^^^^^^^^^^^^^^
  File "pyarrow/_dataset.pyx", line 589, in pyarrow._dataset.Dataset.to_table
  File "pyarrow/_dataset.pyx", line 3971, in pyarrow._dataset.Scanner.to_table
  File "pyarrow/error.pxi", line 155, in pyarrow.lib.pyarrow_internal_check_status
  File "pyarrow/error.pxi", line 89, in pyarrow.lib.check_status
OSError: [Errno 12] Cannot allocate memory
ferch@BlackAR:/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis$ uv run python test/inspect_data_structure.py /mnt/d/ml-outputs/artifact/dataset/rf_dataset_muscle_w5_s2_ua0.2_p213_v5.parquet --max-rows 100000
/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/.venv/bin/python3: can't open file '/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis/test/inspect_data_structure.py': [Errno 2] No such file or directory
ferch@BlackAR:/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis$ uv run python tests/inspect_data_structure.py /mnt/d/ml-outputs/artifact/dat
aset/rf_dataset_muscle_w5_s2_ua0.2_p213_v5.parquet --max-rows 100000
Archivo: /mnt/d/ml-outputs/artifact/dataset/rf_dataset_muscle_w5_s2_ua0.2_p213_v5.parquet
Filas: 2120686 | columnas totales: 133 | bloques (row groups): 3
Estructura calculada con las primeras 99990 filas de 2120686 (columnas de X: 108)

== Ventana elegida: {'Patient': 'aaaaaaju', 'Session': 's007', 'Section': 't000', 'Start': np.int64(0)} (16 filas) ==
     grupo  columnas  cambian entre filas  iguales en la ventana                                        ejemplos
   ic_prob         1                    1                      0                                 ic_iclabel_prob
ic_contrib        19                   19                      0    ic_contrib_FP1, ic_contrib_F3, ic_contrib_C3
   ic_feat        31                   31                      0                    ic_mean, ic_variance, ic_rms
   ventana        57                    0                     57 FP1_variance, FP1_line_length, FP1_peak_to_peak

Filas de esa ventana (columnas clave):
 ic_index    ic_raw_label  ic_iclabel_prob  is_positive
        0       eye blink         0.975747            0
        1       eye blink         0.999414            0
        2           brain         0.928242            1
        3           brain         0.775812            0
        4 muscle artifact         0.420578            0
        5           brain         0.845997            0
        6 muscle artifact         0.679034            0
        7 muscle artifact         0.943042            0
        8           brain         0.587708            0
        9      heart beat         0.427845            0
       10 muscle artifact         0.412031            0
       11           brain         0.992345            0
       12           brain         0.964472            0
       13           brain         0.996531            0
       14           brain         0.687606            0
       15           other         0.737740            0

== Columnas que NO entran a X (25) ==
ic_index, ic_raw_label, ic_target_label, Patient, Session, Section, Partition, Start, split, tuar_is_clean_window, tuar_is_ambiguous, tuar_sample_weight, tuar_eye, tuar_muscle, tuar_non_physiological, tuar_genuine_cooccurrence, tuar_weak_overlap, tuar_is_excluded, monopolar_channels_eye, monopolar_channels_muscle, monopolar_channels_non_physiological, bipolar_channels_eye, bipolar_channels_muscle, bipolar_channels_non_physiological, is_positive

== ¿Las ic_contrib_* de un componente son proporcionales entre ventanas? ==
  componente ('aaaaaaju', 's007', 't000', np.int64(2)) en 612 ventanas
  cociente ic_contrib_P4 / ic_contrib_C4: media=1.0481, desviación relativa=7.47e-17
  desviación relativa ~0 => una sola topografía fija multiplicada por un número por ventana

== Todo el archivo (2120686 filas) ==
  ventanas: 174252 | filas por ventana min/mediana/max: 3/13/18
  ventanas con 0 positivos: 125367 | con 1: 48885 | con 2 o más: 0
  proporción de filas positivas: 2.3052%
  pacientes: 213 | sin ningún positivo: 12

== Clase de ICLabel de las filas positivas vs negativas (todo el archivo) ==
is_positive            0      1
ic_raw_label
brain            1234308  18626
channel noise       5643    652
eye blink         294840  18464
heart beat          4672    180
line noise          2714    377
muscle artifact   360638   8664
other             168986   1922

ferch@BlackAR:/mnt/c/Users/ferch/Documents/Various/EngineeringDesignAndInnovation/hybrid-ai-epilepsy-diagnosis$
