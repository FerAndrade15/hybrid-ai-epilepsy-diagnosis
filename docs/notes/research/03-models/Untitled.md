PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> uv run python -m pipelines.artifacts.ica_cnn_rf

Loading all dataset for training...
[INFO] Creating 'artifact' annotations, it could take long...
[INFO] Index saved in: D:\Users\disenoeinnovacion\ml-outputs\artifact\annotations\annotations_index_artifact.parquet
  channel  ...                                                CSV
0  FP1-F7  ...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7  ...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7  ...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3  ...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3  ...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

[5 rows x 14 columns]
{'train': 4, 'test': 1}

==================================================
ARTIFACT: eye

==================================================
**************************************************
>> eye | patients:10 | windows: 5s (2s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage  ... genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 7690 -> sin ambiguas: 7688 | positivas: 1245
['Patient', 'Session', 'Section', 'Start', 'eye']
[INFO]: Split for eye|w5|s2|ua0.1|p10|v1 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w5_s2_sw0.0_ua0.1
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w5_s2_sw0.3_ua0.1
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w5_s2_sw0.5_ua0.1
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w5_s2_sw0.7_ua0.1
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w5_s2_sw1.0_ua0.1

************************************************************

[INFO] Sweep size weight results for eye:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
1.0             0.0049      0.1919    0.0973       0.1870     0.7620   0.1578    0.0803    0.0697          0.2568
0.7             0.0188      0.2122    0.1052       0.1933     0.6701   0.1570    0.1729    0.0299          0.2232
0.5             0.0176      0.2384    0.1052       0.2208     0.5914   0.1570    0.2516    0.1086          0.3294
0.3             0.0185      0.2819    0.0973       0.2634     0.4974   0.1578    0.3448    0.2026          0.4660
0.0             0.0178      0.2819    0.1793       0.2641     0.4974   0.0791    0.4235    0.2735          0.5376
[INFO] Best suggested size weight for eye: 0.7
[INFO] sw registrado: eye|w5|s2|ua0.1|p10|v1 = 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w5_s2_sw0.7_ua0.1 parquet and json
[INFO] Saving patient asignation for eye
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      1329          25        1304       0.018811
train     5152        1093        4059       0.212151
val       1207         127        1080       0.105220
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  ...  genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label  ... bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain  ...                      []                                  []
1          1    eye blink  ...                      []                                  []
2          2        brain  ...                      []                                  []
3          3        other  ...                      []                                  []
4          4        brain  ...                      []                                  []
5          5        brain  ...                      []                                  []
6          6        brain  ...                      []                                  []
7          7        brain  ...                      []                                  []
8          8    eye blink  ...                      []                                  []
9          9        brain  ...                      []                                  []
10        10        brain  ...                      []                                  []
11        11        brain  ...                      []                                  []
12         0        brain  ...                      []                                  []
13         1    eye blink  ...                      []                                  []
14         2        brain  ...                      []                                  []
15         3        other  ...                      []                                  []
16         4        brain  ...                      []                                  []
17         5        brain  ...                      []                                  []
18         6        brain  ...                      []                                  []
19         7        brain  ...                      []                                  []
20         8    eye blink  ...                      []                                  []
21         9        brain  ...                      []                                  []
22        10        brain  ...                      []                                  []
23        11        brain  ...                      []                                  []
24         0        brain  ...                      []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ...  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean  ...                       []                                  []            0
1         1    eye blink                eye  ...                       []                                  []            0
2         2        brain              clean  ...                       []                                  []            0
3         3        other  non_physiological  ...                       []                                  []            0
4         4        brain              clean  ...                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    99515
1     1245
Name: count, dtype: int64
[INFO] Split distribution:  split
train    69188
val      16146
test     15426
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye

============================================================
Modelo: rf_eye_w5s2_1
Train: 69188 (pos=1093) | Val: 16146 (pos = 127) | Test: 15426 (pos=25)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.3766025641025641
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2762582056892779
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.1702061211742661
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.3360488798370672
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.2701242571582928
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.3076923076923077
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.2607124419204956
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.32419786096256686
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.2969993876301286
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.2575216726160122
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.33088235294117646
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.212588578574406
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.3262316910785619
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.29357798165137616
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.23105360443622922
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.317824377457405
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.2357609710550887
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.3215003348961822
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.26525198938992045
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.2942907592701589
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.22486772486772486
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.4143126177024482
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.27129679869777534
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.3101023017902813
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.43704474505723206
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.20910973084886128
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.2469437652811736
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.21659174499387004
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.29036004645760743
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.2587090163934426
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.30883261272390367
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.19335019877123238
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.26425954997383566
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.2946375957572186
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.15755998843596414
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.22120017520805957
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.29684601113172543
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.17526777020447906
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2564753682072118
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.19570222563315426
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.3007518796992481
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.33170391061452514
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.14786967418546365
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.23229070837166513
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 27, 'min_samples_leaf': 8, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2093698175787728
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1759899434318039
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 9, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.376
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 22, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2679528403001072
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 28, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.24715768660405338
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 13, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.16378796902918405
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.20375549340791052
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 24, 'min_samples_leaf': 14, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.28653295128939826
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 11, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.2324521422060164
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 23, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.3287671232876712
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.17402513696422817
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 22, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.25569620253164554
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 25, 'min_samples_leaf': 9, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.23090992226794696
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.2400384061449832
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.27430744160782183
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 12, 'min_samples_leaf': 10, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.23565095660289315
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.4370 | fp_per_day_val(val)=394.9164 <- choosen
        adjusted: threshold=0.6153 | F2(val)=0.5398 | fp_per_day_val(val)=163.7458
[INFO] Best configuration found with validation: {'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3} | F1(val)=0.4370
Final report -------------------------
                  precision    recall  f1-score   support

no_rf_eye_w5s2_1       1.00      1.00      1.00     15401
   rf_eye_w5s2_1       0.18      0.48      0.26        25

        accuracy                           1.00     15426
       macro avg       0.59      0.74      0.63     15426
    weighted avg       1.00      1.00      1.00     15426

Confusion matrix -------------------------
[[15347    54]
 [   13    12]]
General metrics -------------------------
model                 rf_eye_w5s2_1
sensitivity                    0.48
specificity                  0.9965
precision                    0.1818
accuracy                     0.9957
f1_score                     0.2637
auc_roc                      0.9929
false_alar_rate              0.0035
fp_per_day                    60.49
TP                               12
FP                               54
TN                            15347
FN                               13
n_test_windows                15426
covered_test_hours            21.43
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_eye_w5s2_1_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_eye_w5s2_1_and_analysis_random.joblib
**************************************************
>> eye | patients:10 | windows: 2s (1s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage  ... genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15427 -> sin ambiguas: 15370 | positivas: 2002
['Patient', 'Session', 'Section', 'Start', 'eye']
[INFO]: Split for eye|w2|s1|ua0.15|p10|v1 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.0_ua0.15
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.3_ua0.15
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.5_ua0.15
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.7_ua0.15
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw1.0_ua0.15

************************************************************

[INFO] Sweep size weight results for eye:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0132      0.1689    0.0949       0.1557     0.6693   0.1577     0.173    0.0307          0.1864
0.3             0.0132      0.1689    0.0949       0.1557     0.6693   0.1577     0.173    0.0307          0.1864
0.5             0.0132      0.1689    0.0949       0.1557     0.6693   0.1577     0.173    0.0307          0.1864
0.7             0.0132      0.1689    0.0949       0.1557     0.6693   0.1577     0.173    0.0307          0.1864
1.0             0.0132      0.1689    0.0949       0.1557     0.6693   0.1577     0.173    0.0307          0.1864
[INFO] Best suggested size weight for eye: 0.0
[INFO] sw registrado: eye|w2|s1|ua0.15|p10|v1 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.0_ua0.15 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2659          35        2624       0.013163
train    10287        1737        8550       0.168854
val       2424         230        2194       0.094884
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  ...  genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label  ... bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain  ...                      []                                  []
1          1    eye blink  ...                      []                                  []
2          2        brain  ...                      []                                  []
3          3        other  ...                      []                                  []
4          4        brain  ...                      []                                  []
5          5        brain  ...                      []                                  []
6          6        brain  ...                      []                                  []
7          7        brain  ...                      []                                  []
8          8    eye blink  ...                      []                                  []
9          9        brain  ...                      []                                  []
10        10        brain  ...                      []                                  []
11        11        brain  ...                      []                                  []
12         0        brain  ...                      []                                  []
13         1    eye blink  ...                      []                                  []
14         2        brain  ...                      []                                  []
15         3        other  ...                      []                                  []
16         4        brain  ...                      []                                  []
17         5        brain  ...                      []                                  []
18         6        brain  ...                      []                                  []
19         7        brain  ...                      []                                  []
20         8    eye blink  ...                      []                                  []
21         9        brain  ...                      []                                  []
22        10        brain  ...                      []                                  []
23        11        brain  ...                      []                                  []
24         0        brain  ...                      []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ...  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean  ...                       []                                  []            0
1         1    eye blink                eye  ...                       []                                  []            0
2         2        brain              clean  ...                       []                                  []            0
3         3        other  non_physiological  ...                       []                                  []            0
4         4        brain              clean  ...                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    199465
1      2002
Name: count, dtype: int64
[INFO] Split distribution:  split
train    138173
val       32432
test      30862
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye

============================================================
Modelo: rf_eye_w2s1_1
Train: 138173 (pos=1737) | Val: 32432 (pos = 230) | Test: 30862 (pos=35)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.36839863713798976
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.24633821571238348
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.14771772612713527
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.3160621761658031
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.15940308631507547
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.25676807144850683
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.2601470988831381
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2564102564102564
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.21940516821062897
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.22142857142857142
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.30543368207897403
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.19593461860854988
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2838709677419355
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.2530949105914718
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1865815931941222
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.2692760447321954
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.17735204855842185
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.23777357470953797
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.16013628620102216
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.17506085002808464
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.19876700680272108
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.3792134831460674
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.25280898876404495
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.22289890377588306
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.3707093821510298
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1525315444817122
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.2158854767951974
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.2219411223551058
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.22957294495186373
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.16186743908672688
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.2917981072555205
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.19457194172819797
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.23180458624127617
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.2593418851087563
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.13122227698373584
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.17297887836853607
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.28453999367688904
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.1438113413304253
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.18015414258188825
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.16843033509700175
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.26656626506024095
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2996575342465753
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.11698073258522126
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.19282326252835635
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 27, 'min_samples_leaf': 8, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.15773660490736105
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1439988976160948
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 9, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.29697986577181207
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 22, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2141400407885792
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 28, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.20595968448729185
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 13, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.13696876600102406
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.1744399559309585
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 24, 'min_samples_leaf': 14, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.18839411646181745
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 11, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.23132530120481928
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 23, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.24110991379310345
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.1361533377395902
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 22, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.22380952380952382
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 25, 'min_samples_leaf': 9, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.19541641088602416
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.19234622320176317
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.24673246198986395
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 12, 'min_samples_leaf': 10, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.22759601706970128
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.3792 | fp_per_day_val(val)=1403.9467 <- choosen
        adjusted: threshold=0.6434 | F2(val)=0.5003 | fp_per_day_val(val)=499.5067
[INFO] Best configuration found with validation: {'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3} | F1(val)=0.3792
Final report -------------------------
                  precision    recall  f1-score   support

no_rf_eye_w2s1_1       1.00      0.99      1.00     30827
   rf_eye_w2s1_1       0.12      0.63      0.20        35

        accuracy                           0.99     30862
       macro avg       0.56      0.81      0.60     30862
    weighted avg       1.00      0.99      1.00     30862

Confusion matrix -------------------------
[[30666   161]
 [   13    22]]
General metrics -------------------------
model                 rf_eye_w2s1_1
sensitivity                  0.6286
specificity                  0.9948
precision                    0.1202
accuracy                     0.9944
f1_score                     0.2018
auc_roc                      0.9751
false_alar_rate              0.0052
fp_per_day                   225.36
TP                               22
FP                              161
TN                            30666
FN                               13
n_test_windows                30862
covered_test_hours            17.15
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_eye_w2s1_1_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_eye_w2s1_1_and_analysis_random.joblib

==================================================
ARTIFACT: muscle

==================================================
**************************************************
>> muscle | patients:10 | windows: 1s (0.5s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage  ... genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 30890 -> sin ambiguas: 30705 | positivas: 4097
['Patient', 'Session', 'Section', 'Start', 'muscle']
[INFO]: Split for muscle|w1|s0.5|ua0.3|p10|v1 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s0.5_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s0.5_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s0.5_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s0.5_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s0.5_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
1.0             0.0304      0.1564    0.0761       0.1260     0.7603   0.1593    0.0804    0.0696          0.1956
0.7             0.0302      0.1708    0.0761       0.1405     0.6824   0.1593    0.1583    0.0176          0.1581
0.5             0.0242      0.1960    0.0701       0.1718     0.5897   0.1729    0.2373    0.1103          0.2821
0.3             0.0166      0.2333    0.0761       0.2167     0.4954   0.1593    0.3454    0.2046          0.4214
0.0             0.0157      0.2333    0.1391       0.2176     0.4954   0.0803    0.4244    0.2744          0.4920
[INFO] Best suggested size weight for muscle: 0.7
[INFO] sw registrado: muscle|w1|s0.5|ua0.3|p10|v1 = 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s0.5_sw0.7_ua0.3 parquet and json
[INFO] Saving patient asignation for muscle
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      4861         147        4714       0.030241
train    20953        3578       17375       0.170763
val       4891         372        4519       0.076058
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  ...  genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label  ... bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain  ...                      []                                  []
1          1    eye blink  ...                      []                                  []
2          2        brain  ...                      []                                  []
3          3        other  ...                      []                                  []
4          4        brain  ...                      []                                  []
5          5        brain  ...                      []                                  []
6          6        brain  ...                      []                                  []
7          7        brain  ...                      []                                  []
8          8    eye blink  ...                      []                                  []
9          9        brain  ...                      []                                  []
10        10        brain  ...                      []                                  []
11        11        brain  ...                      []                                  []
12         0        brain  ...                      []                                  []
13         1    eye blink  ...                      []                                  []
14         2        brain  ...                      []                                  []
15         3        other  ...                      []                                  []
16         4        brain  ...                      []                                  []
17         5        brain  ...                      []                                  []
18         6        brain  ...                      []                                  []
19         7        brain  ...                      []                                  []
20         8    eye blink  ...                      []                                  []
21         9        brain  ...                      []                                  []
22        10        brain  ...                      []                                  []
23        11        brain  ...                      []                                  []
24         0        brain  ...                      []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ...  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean  ...                       []                                  []            0
1         1    eye blink                eye  ...                       []                                  []            0
2         2        brain              clean  ...                       []                                  []            0
3         3        other  non_physiological  ...                       []                                  []            0
4         4        brain              clean  ...                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    398537
1      4097
Name: count, dtype: int64
[INFO] Split distribution:  split
train    281419
val       65429
test      55786
Name: count, dtype: int64

==================================================
Starting training of Random Forest - muscle

============================================================
Modelo: rf_muscle_w1s0.5_1
Train: 281419 (pos=3578) | Val: 65429 (pos = 372) | Test: 55786 (pos=147)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.19251210582260542
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.14990460615971654
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.08008807529574302
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1928066037735849
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.10514955288313291
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.13879948503379466
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.1599509295083514
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.13257133970919835
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.12733128604598906
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.13827883520416465
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.1568590170168267
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.17169397766412692
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.142414341961967
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.11769426240470778
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.09983498349834984
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.14245258731657084
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.11805650334379691
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.13294117647058823
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.105533547907898
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.11196480168111374
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.11989404712114875
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.19054258161961193
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.18093556928508384
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1291822269644082
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.18355277839767908
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.09767364203027605
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.13384096082895047
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.15323798525361998
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.12544273907910272
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.10806185828368614
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.16129032258064516
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.12580645161290321
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.12115398280395083
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.13252829042302727
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.07150271018336986
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.09719794480639865
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.13781608260834213
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.079001455853387
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.11803096577101993
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.12092024114752963
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.12909104715620018
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.1447233606557377
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.06605817381113045
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.12886016980990309
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.10319513809495157
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.07614317379525491
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.15050017863522686
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.11544768776648082
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.10124567853811117
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.07560236026880839
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.14690451206715635
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.12226697353279632
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.16091732511081133
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1324736225087925
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.08438143151154813
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1119727047146402
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.10726874924030631
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.10056447635227708
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.13866231647634583
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.11766243953457968
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.1928 | fp_per_day_val(val)=8801.2349 <- choosen
        adjusted: threshold=0.9587 | F2(val)=0.4157 | fp_per_day_val(val)=1078.8611
[INFO] Best configuration found with validation: {'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3} | F1(val)=0.1928
Final report -------------------------
                       precision    recall  f1-score   support

no_rf_muscle_w1s0.5_1       1.00      0.95      0.97     55639
   rf_muscle_w1s0.5_1       0.04      0.69      0.07       147

             accuracy                           0.95     55786
            macro avg       0.52      0.82      0.52     55786
         weighted avg       1.00      0.95      0.97     55786

Confusion matrix -------------------------
[[52864  2775]
 [   46   101]]
General metrics -------------------------
model                 rf_muscle_w1s0.5_1
sensitivity                       0.6871
specificity                       0.9501
precision                         0.0351
accuracy                          0.9494
f1_score                          0.0668
auc_roc                           0.9588
false_alar_rate                   0.0499
fp_per_day                       4297.85
TP                                   101
FP                                  2775
TN                                 52864
FN                                    46
n_test_windows                     55786
covered_test_hours                  15.5
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w1s0.5_1_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w1s0.5_1_and_analysis_random.joblib
**************************************************
>> muscle | patients:10 | windows: 1s (1s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage  ... genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15445 -> sin ambiguas: 15328 | positivas: 2026
['Patient', 'Session', 'Section', 'Start', 'muscle']
[INFO]: Split for muscle|w1|s1|ua0.3|p10|v1 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s1_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s1_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s1_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s1_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s1_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0289      0.1692    0.0761       0.1404     0.6823   0.1594    0.1582    0.0177           0.158
0.3             0.0289      0.1692    0.0761       0.1404     0.6823   0.1594    0.1582    0.0177           0.158
0.5             0.0289      0.1692    0.0761       0.1404     0.6823   0.1594    0.1582    0.0177           0.158
0.7             0.0289      0.1692    0.0761       0.1404     0.6823   0.1594    0.1582    0.0177           0.158
1.0             0.0289      0.1692    0.0761       0.1404     0.6823   0.1594    0.1582    0.0177           0.158
[INFO] Best suggested size weight for muscle: 0.0
[INFO] sw registrado: muscle|w1|s1|ua0.3|p10|v1 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2425          70        2355       0.028866
train    10459        1770        8689       0.169232
val       2444         186        2258       0.076105
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  ...  genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label  ... bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain  ...                      []                                  []
1          1    eye blink  ...                      []                                  []
2          2        brain  ...                      []                                  []
3          3        other  ...                      []                                  []
4          4        brain  ...                      []                                  []
5          5        brain  ...                      []                                  []
6          6        brain  ...                      []                                  []
7          7        brain  ...                      []                                  []
8          8    eye blink  ...                      []                                  []
9          9        brain  ...                      []                                  []
10        10        brain  ...                      []                                  []
11        11        brain  ...                      []                                  []
12         0        brain  ...                      []                                  []
13         1    eye blink  ...                      []                                  []
14         2        brain  ...                      []                                  []
15         3        other  ...                      []                                  []
16         4        brain  ...                      []                                  []
17         5        brain  ...                      []                                  []
18         6        brain  ...                      []                                  []
19         7        brain  ...                      []                                  []
20         8    eye blink  ...                      []                                  []
21         9        brain  ...                      []                                  []
22        10        brain  ...                      []                                  []
23        11        brain  ...                      []                                  []
24         0        brain  ...                      []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ...  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean  ...                       []                                  []            0
1         1    eye blink                eye  ...                       []                                  []            0
2         2        brain              clean  ...                       []                                  []            0
3         3        other  non_physiological  ...                       []                                  []            0
4         4        brain              clean  ...                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    199006
1      2026
Name: count, dtype: int64
[INFO] Split distribution:  split
train    140509
val       32694
test      27829
Name: count, dtype: int64

==================================================
Starting training of Random Forest - muscle

============================================================
Modelo: rf_muscle_w1s1_1
Train: 140509 (pos=1770) | Val: 32694 (pos = 186) | Test: 27829 (pos=70)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.19643287539166063
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.1671365283930729
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.08186510055169958
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1988360814742968
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.10227137590676656
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.13745431431749564
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.15892420537897312
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.1339215377343627
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.12334102712060012
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1596146581035134
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.1563393708293613
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.18156424581005587
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.14401897661809557
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.12680899842384297
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.0996623461496569
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.15016088666428315
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.11668928086838534
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.13153846153846155
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.10140313642259167
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.10818970939740848
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.11822930987077261
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.18735632183908046
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.17978513483885114
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.12481751824817518
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.18058940837580323
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.09696905468418822
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1493323963457484
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.15451174289245984
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.12411603405974889
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.10227137590676656
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.1601457614115842
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.12987012987012986
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.12460156476383658
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.135632183908046
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.07280598189689098
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.102337546135779
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1444043321299639
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.08090757189341306
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.11710239651416122
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.12148608560531149
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.1287844554902847
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.14836531627576405
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.06685837526959022
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.1390910561216238
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.10109864422627396
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.07954348953830193
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.14585152838427948
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.1215867409319386
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.10736916216850505
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.078645922379894
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.1692889862577176
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.11202292562198776
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.16070403673235126
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.12913457181694607
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.0863849765258216
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.12136569751933848
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.11882998171846434
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.10023970363913706
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.1546676486834837
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.12188588266809537
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.1988 | fp_per_day_val(val)=8498.8805 <- choosen
        adjusted: threshold=0.9328 | F2(val)=0.4239 | fp_per_day_val(val)=1400.6240
[INFO] Best configuration found with validation: {'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3} | F1(val)=0.1988
Final report -------------------------
                     precision    recall  f1-score   support

no_rf_muscle_w1s1_1       1.00      0.95      0.98     27759
   rf_muscle_w1s1_1       0.04      0.74      0.07        70

           accuracy                           0.95     27829
          macro avg       0.52      0.85      0.52     27829
       weighted avg       1.00      0.95      0.97     27829

Confusion matrix -------------------------
[[26438  1321]
 [   18    52]]
General metrics -------------------------
model                 rf_muscle_w1s1_1
sensitivity                     0.7429
specificity                     0.9524
precision                       0.0379
accuracy                        0.9519
f1_score                        0.0721
auc_roc                         0.9674
false_alar_rate                 0.0476
fp_per_day                     4101.28
TP                                  52
FP                                1321
TN                               26438
FN                                  18
n_test_windows                   27829
covered_test_hours                7.73
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w1s1_1_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w1s1_1_and_analysis_random.joblib
**************************************************
>> muscle | patients:10 | windows: 2s (1s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage  ... genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15427 -> sin ambiguas: 15279 | positivas: 2092
['Patient', 'Session', 'Section', 'Start', 'muscle']
[INFO]: Split for muscle|w2|s1|ua0.3|p10|v1 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w2_s1_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w2_s1_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w2_s1_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w2_s1_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w2_s1_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0326       0.175    0.0776       0.1424     0.6822   0.1593    0.1585    0.0178          0.1602
0.3             0.0326       0.175    0.0776       0.1424     0.6822   0.1593    0.1585    0.0178          0.1602
0.5             0.0326       0.175    0.0776       0.1424     0.6822   0.1593    0.1585    0.0178          0.1602
0.7             0.0326       0.175    0.0776       0.1424     0.6822   0.1593    0.1585    0.0178          0.1602
1.0             0.0326       0.175    0.0776       0.1424     0.6822   0.1593    0.1585    0.0178          0.1602
[INFO] Best suggested size weight for muscle: 0.0
[INFO] sw registrado: muscle|w2|s1|ua0.3|p10|v1 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w2_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2422          79        2343       0.032618
train    10423        1824        8599       0.174998
val       2434         189        2245       0.077650
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  ...  genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label  ... bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain  ...                      []                                  []
1          1    eye blink  ...                      []                                  []
2          2        brain  ...                      []                                  []
3          3        other  ...                      []                                  []
4          4        brain  ...                      []                                  []
5          5        brain  ...                      []                                  []
6          6        brain  ...                      []                                  []
7          7        brain  ...                      []                                  []
8          8    eye blink  ...                      []                                  []
9          9        brain  ...                      []                                  []
10        10        brain  ...                      []                                  []
11        11        brain  ...                      []                                  []
12         0        brain  ...                      []                                  []
13         1    eye blink  ...                      []                                  []
14         2        brain  ...                      []                                  []
15         3        other  ...                      []                                  []
16         4        brain  ...                      []                                  []
17         5        brain  ...                      []                                  []
18         6        brain  ...                      []                                  []
19         7        brain  ...                      []                                  []
20         8    eye blink  ...                      []                                  []
21         9        brain  ...                      []                                  []
22        10        brain  ...                      []                                  []
23        11        brain  ...                      []                                  []
24         0        brain  ...                      []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ...  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean  ...                       []                                  []            0
1         1    eye blink                eye  ...                       []                                  []            0
2         2        brain              clean  ...                       []                                  []            0
3         3        other  non_physiological  ...                       []                                  []            0
4         4        brain              clean  ...                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    198305
1      2092
Name: count, dtype: int64
[INFO] Split distribution:  split
train    140049
val       32558
test      27790
Name: count, dtype: int64

==================================================
Starting training of Random Forest - muscle

============================================================
Modelo: rf_muscle_w2s1_1
Train: 140049 (pos=1824) | Val: 32558 (pos = 189) | Test: 27790 (pos=79)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.20241915576400887
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.17795883361921097
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.08451837939361417
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2082281675921252
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.11333333333333333
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1443368993037867
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.16263310745401743
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.13857189435930878
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.13823385916409173
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1662378784880269
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.17131062951496387
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1881720430107527
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.15110631408526715
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.12174643157010916
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.10314057248812145
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.168
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.12639405204460966
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1459478021978022
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.11334844645952794
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.11888111888111888
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.1292972315181016
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.19778099372889532
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.189584285061672
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1362397820163488
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.19369894982497082
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.10320543953375425
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.158311345646438
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.15406924052927315
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.13573938038965186
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.11423195807015186
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.1649871566884015
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.13620453507837468
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1411022576361222
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.13573232323232323
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.07587314331593738
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.0995952279505752
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.14909478168264112
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.08228123639529822
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.11939879196516365
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.13117520711874808
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.14497697424526693
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.15258855585831063
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.07074941977989069
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.14530358069538143
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.11216903612886396
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.08212392456765447
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.15683345780433158
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.11591648590021691
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.10760731959949361
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.08037764735902016
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.1761744966442953
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.12327773749093546
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.1661721068249258
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.14574759945130317
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.090971006032302
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.11657510384563849
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.10736005957552439
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.10529853254172734
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.1640625
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.12131237937689551
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.2082 | fp_per_day_val(val)=4034.9899 <- choosen
        adjusted: threshold=0.9503 | F2(val)=0.4627 | fp_per_day_val(val)=402.0394
[INFO] Best configuration found with validation: {'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3} | F1(val)=0.2082
Final report -------------------------
                     precision    recall  f1-score   support

no_rf_muscle_w2s1_1       1.00      0.95      0.98     27711
   rf_muscle_w2s1_1       0.04      0.72      0.08        79

           accuracy                           0.95     27790
          macro avg       0.52      0.84      0.53     27790
       weighted avg       1.00      0.95      0.97     27790

Confusion matrix -------------------------
[[26454  1257]
 [   22    57]]
General metrics -------------------------
model                 rf_muscle_w2s1_1
sensitivity                     0.7215
specificity                     0.9546
precision                       0.0434
accuracy                         0.954
f1_score                        0.0818
auc_roc                         0.9664
false_alar_rate                 0.0454
fp_per_day                     1954.03
TP                                  57
FP                                1257
TN                               26454
FN                                  22
n_test_windows                   27790
covered_test_hours               15.44
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w2s1_1_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w2s1_1_and_analysis_random.joblib
**************************************************
>> muscle | patients:10 | windows: 5s (2s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage  ... genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 7690 -> sin ambiguas: 7614 | positivas: 1139
['Patient', 'Session', 'Section', 'Start', 'muscle']
[INFO]: Split for muscle|w5|s2|ua0.2|p10|v1 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w5_s2_sw0.0_ua0.2
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w5_s2_sw0.3_ua0.2
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w5_s2_sw0.5_ua0.2
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w5_s2_sw0.7_ua0.2
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_muscle_w5_s2_sw1.0_ua0.2

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0447      0.1892    0.0844       0.1445     0.6824   0.1588    0.1588    0.0176          0.1621
0.3             0.0447      0.1892    0.0844       0.1445     0.6824   0.1588    0.1588    0.0176          0.1621
0.5             0.0447      0.1892    0.0844       0.1445     0.6824   0.1588    0.1588    0.0176          0.1621
0.7             0.0447      0.1892    0.0844       0.1445     0.6824   0.1588    0.1588    0.0176          0.1621
1.0             0.0447      0.1892    0.0844       0.1445     0.6824   0.1588    0.1588    0.0176          0.1621
[INFO] Best suggested size weight for muscle: 0.0
[INFO] sw registrado: muscle|w5|s2|ua0.2|p10|v1 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w5_s2_sw0.0_ua0.2 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      1209          54        1155       0.044665
train     5196         983        4213       0.189184
val       1209         102        1107       0.084367
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  ...  genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label  ... bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain  ...                      []                                  []
1          1    eye blink  ...                      []                                  []
2          2        brain  ...                      []                                  []
3          3        other  ...                      []                                  []
4          4        brain  ...                      []                                  []
5          5        brain  ...                      []                                  []
6          6        brain  ...                      []                                  []
7          7        brain  ...                      []                                  []
8          8    eye blink  ...                      []                                  []
9          9        brain  ...                      []                                  []
10        10        brain  ...                      []                                  []
11        11        brain  ...                      []                                  []
12         0        brain  ...                      []                                  []
13         1    eye blink  ...                      []                                  []
14         2        brain  ...                      []                                  []
15         3        other  ...                      []                                  []
16         4        brain  ...                      []                                  []
17         5        brain  ...                      []                                  []
18         6        brain  ...                      []                                  []
19         7        brain  ...                      []                                  []
20         8    eye blink  ...                      []                                  []
21         9        brain  ...                      []                                  []
22        10        brain  ...                      []                                  []
23        11        brain  ...                      []                                  []
24         0        brain  ...                      []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ...  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean  ...                       []                                  []            0
1         1    eye blink                eye  ...                       []                                  []            0
2         2        brain              clean  ...                       []                                  []            0
3         3        other  non_physiological  ...                       []                                  []            0
4         4        brain              clean  ...                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    98727
1     1139
Name: count, dtype: int64
[INFO] Split distribution:  split
train    69818
val      16170
test     13878
Name: count, dtype: int64

==================================================
Starting training of Random Forest - muscle

============================================================
Modelo: rf_muscle_w5s2_1
Train: 69818 (pos=983) | Val: 16170 (pos = 102) | Test: 13878 (pos=54)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.23450134770889489
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.20933589990375362
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.10602910602910603
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2236503856041131
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.1336104513064133
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1720139157325087
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.18525817895151753
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.16485575121768453
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.1654890293789513
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.19123334765792865
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.20260829063809968
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.15780141843971632
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.1963882618510158
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.15964450296247532
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.128039317123642
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.21949974476773865
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.1396735718769617
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1726144297905353
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.13424821002386636
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.1413760603204524
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.15286843009275164
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.22703549060542796
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.18847487001733101
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.16444937176644495
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.21240234375
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.13495092693565977
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.18658280922431866
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.17550143266475646
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.16679160419790104
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.13513513513513514
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.18798617113223856
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.14925373134328357
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.19123334765792865
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.16587677725118483
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.09837962962962964
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.13409961685823754
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.21566683192860683
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.10800508259212198
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.14150943396226415
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.16428808496515102
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.19196822594880847
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.20625889046941678
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.08584413398417774
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.16888045540796964
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.13766842413591096
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.10460693153000845
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1797520661157025
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.1552598225602028
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.13562136728480487
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.10852883139662355
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.16036036036036036
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1450676982591876
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.17478397486252945
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.17568101065929728
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.12643678160919541
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1529815797689666
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.14889091461561835
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.1276161306789178
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.19508987286277948
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.15806451612903225
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.2345 | fp_per_day_val(val)=1453.3581
        adjusted: threshold=0.9140 | F2(val)=0.5916 | fp_per_day_val(val)=145.3358 <- choosen
[INFO] Best configuration found with validation: {'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3} | F1(val)=0.2345
Final report -------------------------
                     precision    recall  f1-score   support

no_rf_muscle_w5s2_1       1.00      1.00      1.00     13824
   rf_muscle_w5s2_1       0.03      0.04      0.03        54

           accuracy                           0.99     13878
          macro avg       0.51      0.52      0.52     13878
       weighted avg       0.99      0.99      0.99     13878

Confusion matrix -------------------------
[[13765    59]
 [   52     2]]
General metrics -------------------------
model                 rf_muscle_w5s2_1
sensitivity                      0.037
specificity                     0.9957
precision                       0.0328
accuracy                         0.992
f1_score                        0.0348
auc_roc                         0.9596
false_alar_rate                 0.0043
fp_per_day                       73.46
TP                                   2
FP                                  59
TN                               13765
FN                                  52
n_test_windows                   13878
covered_test_hours               19.27
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w5s2_1_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w5s2_1_and_analysis_random.joblib

==================================================
ARTIFACT: non_physiological

==================================================
**************************************************
>> non_physiological | patients:10 | windows: 0.5s (0.25s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage  ... genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 61816 -> sin ambiguas: 61729 | positivas: 8320
['Patient', 'Session', 'Section', 'Start', 'non_physiological']
[INFO]: Split for non_physiological|w0.5|s0.25|ua0.2|p10|v1 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w0.5_s0.25_sw0.0_ua0.2
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w0.5_s0.25_sw0.3_ua0.2
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w0.5_s0.25_sw0.5_ua0.2
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w0.5_s0.25_sw0.7_ua0.2
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w0.5_s0.25_sw1.0_ua0.2

************************************************************

[INFO] Sweep size weight results for non_physiological:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
1.0             0.0231      0.1869    0.0222       0.1647     0.6829   0.1591    0.1580    0.0171          0.1818
0.7             0.0209      0.1944    0.0239       0.1735     0.6532   0.1727    0.1741    0.0468          0.2203
0.5             0.0145      0.2558    0.0164       0.2413     0.4966   0.2515    0.2519    0.2034          0.4447
0.3             0.0145      0.2558    0.0164       0.2413     0.4966   0.2515    0.2519    0.2034          0.4447
0.0             0.0110      0.2558    0.0239       0.2447     0.4966   0.1727    0.3307    0.2034          0.4482
[INFO] Best suggested size weight for non_physiological: 1.0
[INFO] sw registrado: non_physiological|w0.5|s0.25|ua0.2|p10|v1 = 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w0.5_s0.25_sw1.0_ua0.2 parquet and json
[INFO] Saving patient asignation for non_physiological
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      9755         225        9530       0.023065
train    42153        7877       34276       0.186867
val       9821         218        9603       0.022197
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  ...  genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label  ... bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain  ...                      []                                  []
1          1    eye blink  ...                      []                                  []
2          2        brain  ...                      []                                  []
3          3        other  ...                      []                                  []
4          4        brain  ...                      []                                  []
5          5        brain  ...                      []                                  []
6          6        brain  ...                      []                                  []
7          7        brain  ...                      []                                  []
8          8    eye blink  ...                      []                                  []
9          9        brain  ...                      []                                  []
10        10        brain  ...                      []                                  []
11        11        brain  ...                      []                                  []
12         0        brain  ...                      []                                  []
13         1    eye blink  ...                      []                                  []
14         2        brain  ...                      []                                  []
15         3        other  ...                      []                                  []
16         4        brain  ...                      []                                  []
17         5        brain  ...                      []                                  []
18         6        brain  ...                      []                                  []
19         7        brain  ...                      []                                  []
20         8    eye blink  ...                      []                                  []
21         9        brain  ...                      []                                  []
22        10        brain  ...                      []                                  []
23        11        brain  ...                      []                                  []
24         0        brain  ...                      []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ...  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean  ...                       []                                  []            0
1         1    eye blink                eye  ...                       []                                  []            0
2         2        brain              clean  ...                       []                                  []            0
3         3        other  non_physiological  ...                       []                                  []            0
4         4        brain              clean  ...                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    800806
1      8320
Name: count, dtype: int64
[INFO] Split distribution:  split
train    565781
val      131389
test     111956
Name: count, dtype: int64

==================================================
Starting training of Random Forest - non_physiological

============================================================
Modelo: rf_non_physiological_w0.5s0.25_1
Train: 565781 (pos=7877) | Val: 131389 (pos = 218) | Test: 111956 (pos=225)
        params:{'n_estimators': 190, 'max_depth': 28, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.026186195575705465
        params:{'n_estimators': 344, 'max_depth': 30, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.020065476819093885
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.015296456191570643
        params:{'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.027466325532395214
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.019284061366168614
        params:{'n_estimators': 375, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.029985007496251874
        params:{'n_estimators': 501, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.030433820274457724
        params:{'n_estimators': 395, 'max_depth': 18, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.027608721937850147
        params:{'n_estimators': 191, 'max_depth': 21, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.025780242959259403
        params:{'n_estimators': 536, 'max_depth': 29, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.02721769803597091
        params:{'n_estimators': 224, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.031954771707736744
        params:{'n_estimators': 180, 'max_depth': 34, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.02283578991073282
        params:{'n_estimators': 455, 'max_depth': 28, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.02141274920009845
        params:{'n_estimators': 313, 'max_depth': 19, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.026683467368343032
        params:{'n_estimators': 395, 'max_depth': 9, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.02136530791940747
        params:{'n_estimators': 565, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.018345305152188518
        params:{'n_estimators': 334, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.02368685971457334
        params:{'n_estimators': 184, 'max_depth': 19, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.02427941373011984
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.01933411048875494
        params:{'n_estimators': 298, 'max_depth': 11, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.023464998044583497
        params:{'n_estimators': 573, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.02473664725877562
        params:{'n_estimators': 433, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.028019404483104717
        params:{'n_estimators': 495, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.0289054470709147
        params:{'n_estimators': 528, 'max_depth': 16, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.027059161166003855
        params:{'n_estimators': 257, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.028280975311472903
        params:{'n_estimators': 524, 'max_depth': 10, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.022588327727172286
        params:{'n_estimators': 508, 'max_depth': 28, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.027380653791489008
        params:{'n_estimators': 362, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.03014599631272111
        params:{'n_estimators': 400, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.025449609772650154
        params:{'n_estimators': 166, 'max_depth': 9, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.022239665096807953
        params:{'n_estimators': 347, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.03138268414251431
        params:{'n_estimators': 534, 'max_depth': 21, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.025912253301150077
        params:{'n_estimators': 408, 'max_depth': 24, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.024194435279885625
        params:{'n_estimators': 190, 'max_depth': 21, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.028504151691659436
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.015141390733184526
        params:{'n_estimators': 592, 'max_depth': 11, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.02067581785705547
        params:{'n_estimators': 596, 'max_depth': 30, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.027658266748617086
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.01567398119122257
        params:{'n_estimators': 562, 'max_depth': 13, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.023756999830307143
        params:{'n_estimators': 206, 'max_depth': 21, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.02562574493444577
        params:{'n_estimators': 598, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.027204620600175783
        params:{'n_estimators': 338, 'max_depth': 29, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.021821729307866092
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.013635226419814862
        params:{'n_estimators': 497, 'max_depth': 26, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.02446721747455764
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.021846504559270518
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.016317319088827914
        params:{'n_estimators': 373, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.030815463759995925
        params:{'n_estimators': 257, 'max_depth': 14, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.024084460574067965
        params:{'n_estimators': 423, 'max_depth': 15, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.02215960035865249
        params:{'n_estimators': 304, 'max_depth': 8, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.017202806684519168
        params:{'n_estimators': 314, 'max_depth': 32, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.026945977660915294
        params:{'n_estimators': 355, 'max_depth': 12, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.02548788374481683
        params:{'n_estimators': 268, 'max_depth': 28, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.030213861594240974
        params:{'n_estimators': 505, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.02505164154177471
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.018876387694837963
        params:{'n_estimators': 207, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.02360902255639098
        params:{'n_estimators': 474, 'max_depth': 14, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.022899214469984636
        params:{'n_estimators': 396, 'max_depth': 10, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.021136621839414515
        params:{'n_estimators': 158, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.02793029362616376
        params:{'n_estimators': 448, 'max_depth': 17, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.02624142107387969
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.0320 | fp_per_day_val(val)=20118.2869 <- choosen
        adjusted: threshold=0.5332 | F2(val)=0.0324 | fp_per_day_val(val)=18829.4119
[INFO] Best configuration found with validation: {'n_estimators': 224, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5} | F1(val)=0.0320
Final report -------------------------
                                     precision    recall  f1-score   support

no_rf_non_physiological_w0.5s0.25_1       1.00      0.93      0.97    111731
   rf_non_physiological_w0.5s0.25_1       0.03      0.97      0.06       225

                           accuracy                           0.93    111956
                          macro avg       0.51      0.95      0.51    111956
                       weighted avg       1.00      0.93      0.96    111956

Confusion matrix -------------------------
[[104436   7295]
 [     7    218]]
General metrics -------------------------
model                 rf_non_physiological_w0.5s0.25_1
sensitivity                                     0.9689
specificity                                     0.9347
precision                                        0.029
accuracy                                        0.9348
f1_score                                        0.0563
auc_roc                                         0.9864
false_alar_rate                                 0.0653
fp_per_day                                    11259.57
TP                                                 218
FP                                                7295
TN                                              104436
FN                                                   7
n_test_windows                                  111956
covered_test_hours                               15.55
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w0.5s0.25_1_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w0.5s0.25_1_and_analysis_random.joblib
**************************************************
>> non_physiological | patients:10 | windows: 1s (0.5s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w1_s0.5_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (30890 rows)
    Patient Session Section    Montage  ... genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 30890 -> sin ambiguas: 30705 | positivas: 4159
['Patient', 'Session', 'Section', 'Start', 'non_physiological']
[INFO]: Split for non_physiological|w1|s0.5|ua0.3|p10|v1 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s0.5_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s0.5_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s0.5_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s0.5_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s0.5_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for non_physiological:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0232      0.1878    0.0227       0.1651     0.6824   0.1593    0.1583    0.0176          0.1827
0.3             0.0232      0.1878    0.0227       0.1651     0.6824   0.1593    0.1583    0.0176          0.1827
0.5             0.0232      0.1878    0.0227       0.1651     0.6824   0.1593    0.1583    0.0176          0.1827
0.7             0.0232      0.1878    0.0227       0.1651     0.6824   0.1593    0.1583    0.0176          0.1827
1.0             0.0232      0.1878    0.0227       0.1651     0.6824   0.1593    0.1583    0.0176          0.1827
[INFO] Best suggested size weight for non_physiological: 0.0
[INFO] sw registrado: non_physiological|w1|s0.5|ua0.3|p10|v1 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s0.5_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      4861         113        4748       0.023246
train    20953        3935       17018       0.187801
val       4891         111        4780       0.022695
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  ...  genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label  ... bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain  ...                      []                                  []
1          1    eye blink  ...                      []                                  []
2          2        brain  ...                      []                                  []
3          3        other  ...                      []                                  []
4          4        brain  ...                      []                                  []
5          5        brain  ...                      []                                  []
6          6        brain  ...                      []                                  []
7          7        brain  ...                      []                                  []
8          8    eye blink  ...                      []                                  []
9          9        brain  ...                      []                                  []
10        10        brain  ...                      []                                  []
11        11        brain  ...                      []                                  []
12         0        brain  ...                      []                                  []
13         1    eye blink  ...                      []                                  []
14         2        brain  ...                      []                                  []
15         3        other  ...                      []                                  []
16         4        brain  ...                      []                                  []
17         5        brain  ...                      []                                  []
18         6        brain  ...                      []                                  []
19         7        brain  ...                      []                                  []
20         8    eye blink  ...                      []                                  []
21         9        brain  ...                      []                                  []
22        10        brain  ...                      []                                  []
23        11        brain  ...                      []                                  []
24         0        brain  ...                      []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ...  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean  ...                       []                                  []            0
1         1    eye blink                eye  ...                       []                                  []            0
2         2        brain              clean  ...                       []                                  []            0
3         3        other  non_physiological  ...                       []                                  []            0
4         4        brain              clean  ...                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    398475
1      4159
Name: count, dtype: int64
[INFO] Split distribution:  split
train    281419
val       65429
test      55786
Name: count, dtype: int64

==================================================
Starting training of Random Forest - non_physiological

============================================================
Modelo: rf_non_physiological_w1s0.5_1
Train: 281419 (pos=3935) | Val: 65429 (pos = 111) | Test: 55786 (pos=113)
        params:{'n_estimators': 190, 'max_depth': 28, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.019455252918287938
        params:{'n_estimators': 344, 'max_depth': 30, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.03265557609365373
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.01626188708594054
        params:{'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.021212121212121213
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.023547400611620795
        params:{'n_estimators': 375, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.03292877975350456
        params:{'n_estimators': 501, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.03399465002229157
        params:{'n_estimators': 395, 'max_depth': 18, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.030685604068034368
        params:{'n_estimators': 191, 'max_depth': 21, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.029572932069235454
        params:{'n_estimators': 536, 'max_depth': 29, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.034957737660440365
        params:{'n_estimators': 224, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.03258178026847387
        params:{'n_estimators': 180, 'max_depth': 34, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.03278688524590164
        params:{'n_estimators': 455, 'max_depth': 28, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.035982989859339225
        params:{'n_estimators': 313, 'max_depth': 19, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.032018874283788336
        params:{'n_estimators': 395, 'max_depth': 9, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.022236159416158276
        params:{'n_estimators': 565, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.03427044609665428
        params:{'n_estimators': 334, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.022929122888489
        params:{'n_estimators': 184, 'max_depth': 19, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.03015788540003548
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.022563441364355622
        params:{'n_estimators': 298, 'max_depth': 11, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.02401157818564568
        params:{'n_estimators': 573, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.028308823529411765
        params:{'n_estimators': 433, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.02027712064886786
        params:{'n_estimators': 495, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.028285751874753323
        params:{'n_estimators': 528, 'max_depth': 16, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.027691806483140576
        params:{'n_estimators': 257, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.02653123104912068
        params:{'n_estimators': 524, 'max_depth': 10, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.019519985803646688
        params:{'n_estimators': 508, 'max_depth': 28, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.032959464777646594
        params:{'n_estimators': 362, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.03183405216676936
        params:{'n_estimators': 400, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.028347312830071452
        params:{'n_estimators': 166, 'max_depth': 9, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.023686342953312973
        params:{'n_estimators': 347, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.027662517289073305
        params:{'n_estimators': 534, 'max_depth': 21, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.029678225554514215
        params:{'n_estimators': 408, 'max_depth': 24, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.029890833477733494
        params:{'n_estimators': 190, 'max_depth': 21, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.0322112331004446
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.014566530712380017
        params:{'n_estimators': 592, 'max_depth': 11, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.022516556291390728
        params:{'n_estimators': 596, 'max_depth': 30, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.03250911240271894
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.016303974737420197
        params:{'n_estimators': 562, 'max_depth': 13, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.02318769831584086
        params:{'n_estimators': 206, 'max_depth': 21, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.028652305992819663
        params:{'n_estimators': 598, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.03057127212995072
        params:{'n_estimators': 338, 'max_depth': 29, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.03787444049122002
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.015359495212265456
        params:{'n_estimators': 497, 'max_depth': 26, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.03137550200803213
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.020456172650097165
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.01713811516813393
        params:{'n_estimators': 373, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.03543433909588747
        params:{'n_estimators': 257, 'max_depth': 14, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.026874014619463954
        params:{'n_estimators': 423, 'max_depth': 15, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.02408204895738894
        params:{'n_estimators': 304, 'max_depth': 8, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.016356186081746497
        params:{'n_estimators': 314, 'max_depth': 32, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.0363537710255019
        params:{'n_estimators': 355, 'max_depth': 12, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.02601568068424804
        params:{'n_estimators': 268, 'max_depth': 28, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.03361344537815126
        params:{'n_estimators': 505, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.029237251698340357
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.01671339227949105
        params:{'n_estimators': 207, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.026640588116274365
        params:{'n_estimators': 474, 'max_depth': 14, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.024509803921568627
        params:{'n_estimators': 396, 'max_depth': 10, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.02297266253158741
        params:{'n_estimators': 158, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.03544503206931473
        params:{'n_estimators': 448, 'max_depth': 17, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.029319064721835375
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.0379 | fp_per_day_val(val)=10832.1876 <- choosen
        adjusted: threshold=0.5535 | F2(val)=0.0400 | fp_per_day_val(val)=10220.7889
[INFO] Best configuration found with validation: {'n_estimators': 338, 'max_depth': 29, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5} | F1(val)=0.0379
Final report -------------------------
                                  precision    recall  f1-score   support

no_rf_non_physiological_w1s0.5_1       1.00      0.93      0.96     55673
   rf_non_physiological_w1s0.5_1       0.03      1.00      0.05       113

                        accuracy                           0.93     55786
                       macro avg       0.51      0.96      0.51     55786
                    weighted avg       1.00      0.93      0.96     55786

Confusion matrix -------------------------
[[51600  4073]
 [    0   113]]
General metrics -------------------------
model                 rf_non_physiological_w1s0.5_1
sensitivity                                     1.0
specificity                                  0.9268
precision                                     0.027
accuracy                                      0.927
f1_score                                     0.0526
auc_roc                                      0.9684
false_alar_rate                              0.0732
fp_per_day                                  6308.16
TP                                              113
FP                                             4073
TN                                            51600
FN                                                0
n_test_windows                                55786
covered_test_hours                             15.5
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w1s0.5_1_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w1s0.5_1_and_analysis_random.joblib
**************************************************
>> non_physiological | patients:10 | windows: 1s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w1_s1_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (15445 rows)
    Patient Session Section    Montage  ... genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15445 -> sin ambiguas: 15328 | positivas: 2073
['Patient', 'Session', 'Section', 'Start', 'non_physiological']
[INFO]: Split for non_physiological|w1|s1|ua0.3|p10|v1 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s1_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s1_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s1_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s1_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s1_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for non_physiological:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0231      0.1877    0.0221       0.1656     0.6823   0.1594    0.1582    0.0177          0.1832
0.3             0.0231      0.1877    0.0221       0.1656     0.6823   0.1594    0.1582    0.0177          0.1832
0.5             0.0231      0.1877    0.0221       0.1656     0.6823   0.1594    0.1582    0.0177          0.1832
0.7             0.0231      0.1877    0.0221       0.1656     0.6823   0.1594    0.1582    0.0177          0.1832
1.0             0.0231      0.1877    0.0221       0.1656     0.6823   0.1594    0.1582    0.0177          0.1832
[INFO] Best suggested size weight for non_physiological: 0.0
[INFO] sw registrado: non_physiological|w1|s1|ua0.3|p10|v1 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2425          56        2369       0.023093
train    10459        1963        8496       0.187685
val       2444          54        2390       0.022095
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  ...  genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label  ... bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain  ...                      []                                  []
1          1    eye blink  ...                      []                                  []
2          2        brain  ...                      []                                  []
3          3        other  ...                      []                                  []
4          4        brain  ...                      []                                  []
5          5        brain  ...                      []                                  []
6          6        brain  ...                      []                                  []
7          7        brain  ...                      []                                  []
8          8    eye blink  ...                      []                                  []
9          9        brain  ...                      []                                  []
10        10        brain  ...                      []                                  []
11        11        brain  ...                      []                                  []
12         0        brain  ...                      []                                  []
13         1    eye blink  ...                      []                                  []
14         2        brain  ...                      []                                  []
15         3        other  ...                      []                                  []
16         4        brain  ...                      []                                  []
17         5        brain  ...                      []                                  []
18         6        brain  ...                      []                                  []
19         7        brain  ...                      []                                  []
20         8    eye blink  ...                      []                                  []
21         9        brain  ...                      []                                  []
22        10        brain  ...                      []                                  []
23        11        brain  ...                      []                                  []
24         0        brain  ...                      []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ...  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean  ...                       []                                  []            0
1         1    eye blink                eye  ...                       []                                  []            0
2         2        brain              clean  ...                       []                                  []            0
3         3        other  non_physiological  ...                       []                                  []            0
4         4        brain              clean  ...                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    198959
1      2073
Name: count, dtype: int64
[INFO] Split distribution:  split
train    140509
val       32694
test      27829
Name: count, dtype: int64

==================================================
Starting training of Random Forest - non_physiological

============================================================
Modelo: rf_non_physiological_w1s1_1
Train: 140509 (pos=1963) | Val: 32694 (pos = 54) | Test: 27829 (pos=56)
        params:{'n_estimators': 190, 'max_depth': 28, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.02418574653337633
        params:{'n_estimators': 344, 'max_depth': 30, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.02811142346026067
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.016371271976653144
        params:{'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.024390243902439025
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.014479113878230651
        params:{'n_estimators': 375, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.03181898532791232
        params:{'n_estimators': 501, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.03015075376884422
        params:{'n_estimators': 395, 'max_depth': 18, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.03086934757216753
        params:{'n_estimators': 191, 'max_depth': 21, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.03111495246326707
        params:{'n_estimators': 536, 'max_depth': 29, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.034324942791762014
        params:{'n_estimators': 224, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.02816180235535074
        params:{'n_estimators': 180, 'max_depth': 34, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.028888888888888888
        params:{'n_estimators': 455, 'max_depth': 28, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.03525005507821106
        params:{'n_estimators': 313, 'max_depth': 19, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.030964797913950456
        params:{'n_estimators': 395, 'max_depth': 9, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.021021652301870926
        params:{'n_estimators': 565, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.023340248962655602
        params:{'n_estimators': 334, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.02267197522671975
        params:{'n_estimators': 184, 'max_depth': 19, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.030287296642436828
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.01417563245129398
        params:{'n_estimators': 298, 'max_depth': 11, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.016331214689265537
        params:{'n_estimators': 573, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.026685393258426966
        params:{'n_estimators': 433, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.024925224327018942
        params:{'n_estimators': 495, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.030303030303030304
        params:{'n_estimators': 528, 'max_depth': 16, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.02663115845539281
        params:{'n_estimators': 257, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.0310192023633678
        params:{'n_estimators': 524, 'max_depth': 10, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.01964905867300311
        params:{'n_estimators': 508, 'max_depth': 28, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.03445210046677039
        params:{'n_estimators': 362, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.031185031185031187
        params:{'n_estimators': 400, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.02759958227659257
        params:{'n_estimators': 166, 'max_depth': 9, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.021398002853067047
        params:{'n_estimators': 347, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.03468208092485549
        params:{'n_estimators': 534, 'max_depth': 21, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.026222537207654145
        params:{'n_estimators': 408, 'max_depth': 24, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.03112771255780861
        params:{'n_estimators': 190, 'max_depth': 21, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.03195716013128347
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.01527431421446384
        params:{'n_estimators': 592, 'max_depth': 11, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.02269679149901991
        params:{'n_estimators': 596, 'max_depth': 30, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.03355001048437828
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.01595781586068133
        params:{'n_estimators': 562, 'max_depth': 13, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.02179648961798784
        params:{'n_estimators': 206, 'max_depth': 21, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.02895900015241579
        params:{'n_estimators': 598, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.032467532467532464
        params:{'n_estimators': 338, 'max_depth': 29, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.03665521191294387
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.014845266643827794
        params:{'n_estimators': 497, 'max_depth': 26, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.030957013974880595
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.018730189222937278
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.017506469782310855
        params:{'n_estimators': 373, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.03316749585406302
        params:{'n_estimators': 257, 'max_depth': 14, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.02785127419579446
        params:{'n_estimators': 423, 'max_depth': 15, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.023766410140334992
        params:{'n_estimators': 304, 'max_depth': 8, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.01802133137182788
        params:{'n_estimators': 314, 'max_depth': 32, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.03282275711159737
        params:{'n_estimators': 355, 'max_depth': 12, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.02219289827255278
        params:{'n_estimators': 268, 'max_depth': 28, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.03186558516801854
        params:{'n_estimators': 505, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.02865094957432875
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.01783913751648181
        params:{'n_estimators': 207, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.02779708130646282
        params:{'n_estimators': 474, 'max_depth': 14, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.02425976611097288
        params:{'n_estimators': 396, 'max_depth': 10, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.021591277124041887
        params:{'n_estimators': 158, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.03788748564867968
        params:{'n_estimators': 448, 'max_depth': 17, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.027765912003417343
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.0379 | fp_per_day_val(val)=10850.8717 <- choosen
        adjusted: threshold=0.4849 | F2(val)=0.0370 | fp_per_day_val(val)=11120.4258
[INFO] Best configuration found with validation: {'n_estimators': 158, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5} | F1(val)=0.0379
Final report -------------------------
                                precision    recall  f1-score   support

no_rf_non_physiological_w1s1_1       1.00      0.93      0.96     27773
   rf_non_physiological_w1s1_1       0.03      1.00      0.05        56

                      accuracy                           0.93     27829
                     macro avg       0.51      0.96      0.51     27829
                  weighted avg       1.00      0.93      0.96     27829

Confusion matrix -------------------------
[[25773  2000]
 [    0    56]]
General metrics -------------------------
model                 rf_non_physiological_w1s1_1
sensitivity                                   1.0
specificity                                 0.928
precision                                  0.0272
accuracy                                   0.9281
f1_score                                    0.053
auc_roc                                    0.9939
false_alar_rate                             0.072
fp_per_day                                6209.35
TP                                             56
FP                                           2000
TN                                          25773
FN                                              0
n_test_windows                              27829
covered_test_hours                           7.73
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w1s1_1_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w1s1_1_and_analysis_random.joblib
**************************************************
>> non_physiological | patients:10 | windows: 2s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w2_s1_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (15427 rows)
    Patient Session Section    Montage  ... genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar  ...                    0             0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15427 -> sin ambiguas: 15279 | positivas: 2096
['Patient', 'Session', 'Section', 'Start', 'non_physiological']
[INFO]: Split for non_physiological|w2|s1|ua0.3|p10|v1 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w2_s1_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w2_s1_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w2_s1_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w2_s1_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w2_s1_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for non_physiological:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0239      0.1899    0.0242       0.1659     0.6822   0.1593    0.1585    0.0178          0.1837
0.3             0.0239      0.1899    0.0242       0.1659     0.6822   0.1593    0.1585    0.0178          0.1837
0.5             0.0239      0.1899    0.0242       0.1659     0.6822   0.1593    0.1585    0.0178          0.1837
0.7             0.0239      0.1899    0.0242       0.1659     0.6822   0.1593    0.1585    0.0178          0.1837
1.0             0.0239      0.1899    0.0242       0.1659     0.6822   0.1593    0.1585    0.0178          0.1837
[INFO] Best suggested size weight for non_physiological: 0.0
[INFO] sw registrado: non_physiological|w2|s1|ua0.3|p10|v1 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w2_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2422          58        2364       0.023947
train    10423        1979        8444       0.189869
val       2434          59        2375       0.024240
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  ...  genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar            ...                     0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label  ... bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain  ...                      []                                  []
1          1    eye blink  ...                      []                                  []
2          2        brain  ...                      []                                  []
3          3        other  ...                      []                                  []
4          4        brain  ...                      []                                  []
5          5        brain  ...                      []                                  []
6          6        brain  ...                      []                                  []
7          7        brain  ...                      []                                  []
8          8    eye blink  ...                      []                                  []
9          9        brain  ...                      []                                  []
10        10        brain  ...                      []                                  []
11        11        brain  ...                      []                                  []
12         0        brain  ...                      []                                  []
13         1    eye blink  ...                      []                                  []
14         2        brain  ...                      []                                  []
15         3        other  ...                      []                                  []
16         4        brain  ...                      []                                  []
17         5        brain  ...                      []                                  []
18         6        brain  ...                      []                                  []
19         7        brain  ...                      []                                  []
20         8    eye blink  ...                      []                                  []
21         9        brain  ...                      []                                  []
22        10        brain  ...                      []                                  []
23        11        brain  ...                      []                                  []
24         0        brain  ...                      []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ...  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean  ...                       []                                  []            0
1         1    eye blink                eye  ...                       []                                  []            0
2         2        brain              clean  ...                       []                                  []            0
3         3        other  non_physiological  ...                       []                                  []            0
4         4        brain              clean  ...                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    198301
1      2096
Name: count, dtype: int64
[INFO] Split distribution:  split
train    140049
val       32558
test      27790
Name: count, dtype: int64

==================================================
Starting training of Random Forest - non_physiological

============================================================
Modelo: rf_non_physiological_w2s1_1
Train: 140049 (pos=1979) | Val: 32558 (pos = 59) | Test: 27790 (pos=58)
        params:{'n_estimators': 190, 'max_depth': 28, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.013703323055841042
        params:{'n_estimators': 344, 'max_depth': 30, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.02431350114416476
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.01855287569573284
        params:{'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.0220125786163522
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.019027484143763214
        params:{'n_estimators': 375, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.03178835110746513
        params:{'n_estimators': 501, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.032243205895900504
        params:{'n_estimators': 395, 'max_depth': 18, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.0374567806377257
        params:{'n_estimators': 191, 'max_depth': 21, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.03729146221786065
        params:{'n_estimators': 536, 'max_depth': 29, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.02752064048036027
        params:{'n_estimators': 224, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.0333425951653237
        params:{'n_estimators': 180, 'max_depth': 34, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.025235145675613673
        params:{'n_estimators': 455, 'max_depth': 28, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.033428844317096466
        params:{'n_estimators': 313, 'max_depth': 19, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.037998146431881374
        params:{'n_estimators': 395, 'max_depth': 9, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.0289490245437382
        params:{'n_estimators': 565, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.024052065647990947
        params:{'n_estimators': 334, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.03125434088067787
        params:{'n_estimators': 184, 'max_depth': 19, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.03762456782591011
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.019048425330172706
        params:{'n_estimators': 298, 'max_depth': 11, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.024384711353067936
        params:{'n_estimators': 573, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.037751677852348994
        params:{'n_estimators': 433, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.01471129091577786
        params:{'n_estimators': 495, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.0302154492905938
        params:{'n_estimators': 528, 'max_depth': 16, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.035553892215568865
        params:{'n_estimators': 257, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.014672318226279752
        params:{'n_estimators': 524, 'max_depth': 10, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.02605071205279611
        params:{'n_estimators': 508, 'max_depth': 28, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.03209700427960057
        params:{'n_estimators': 362, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.03256003256003256
        params:{'n_estimators': 400, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.037292560134253215
        params:{'n_estimators': 166, 'max_depth': 9, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.030754510661563695
        params:{'n_estimators': 347, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.03345824411134904
        params:{'n_estimators': 534, 'max_depth': 21, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.03243670886075949
        params:{'n_estimators': 408, 'max_depth': 24, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.037672666387609875
        params:{'n_estimators': 190, 'max_depth': 21, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.02909309791332263
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.017830920914621354
        params:{'n_estimators': 592, 'max_depth': 11, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.028238182934315532
        params:{'n_estimators': 596, 'max_depth': 30, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.03588516746411483
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.01877346683354193
        params:{'n_estimators': 562, 'max_depth': 13, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.033962264150943396
        params:{'n_estimators': 206, 'max_depth': 21, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.0383421581157568
        params:{'n_estimators': 598, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.03602458147912693
        params:{'n_estimators': 338, 'max_depth': 29, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.030534351145038167
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.01770806982038958
        params:{'n_estimators': 497, 'max_depth': 26, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.039412015338730295
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.027475882281108803
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.019887305270135897
        params:{'n_estimators': 373, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.032119914346895075
        params:{'n_estimators': 257, 'max_depth': 14, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.0368429670869494
        params:{'n_estimators': 423, 'max_depth': 15, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.029862373409504026
        params:{'n_estimators': 304, 'max_depth': 8, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.020647505781301617
        params:{'n_estimators': 314, 'max_depth': 32, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.03312041637094866
        params:{'n_estimators': 355, 'max_depth': 12, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.034660648073512816
        params:{'n_estimators': 268, 'max_depth': 28, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.033952014486192846
        params:{'n_estimators': 505, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.037037037037037035
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.019580647793097823
        params:{'n_estimators': 207, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.03493317132442284
        params:{'n_estimators': 474, 'max_depth': 14, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.03235082674335011
        params:{'n_estimators': 396, 'max_depth': 10, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.028182820732753338
        params:{'n_estimators': 158, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.030534351145038167
        params:{'n_estimators': 448, 'max_depth': 17, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.03507340946166395
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.0394 | fp_per_day_val(val)=5866.0606 <- choosen
        adjusted: threshold=0.4921 | F2(val)=0.0392 | fp_per_day_val(val)=5907.1933
[INFO] Best configuration found with validation: {'n_estimators': 497, 'max_depth': 26, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0} | F1(val)=0.0394
Final report -------------------------
                                precision    recall  f1-score   support

no_rf_non_physiological_w2s1_1       1.00      0.93      0.97     27732
   rf_non_physiological_w2s1_1       0.03      1.00      0.06        58

                      accuracy                           0.93     27790
                     macro avg       0.52      0.97      0.51     27790
                  weighted avg       1.00      0.93      0.96     27790

Confusion matrix -------------------------
[[25863  1869]
 [    0    58]]
General metrics -------------------------
model                 rf_non_physiological_w2s1_1
sensitivity                                   1.0
specificity                                0.9326
precision                                  0.0301
accuracy                                   0.9327
f1_score                                   0.0584
auc_roc                                    0.9877
false_alar_rate                            0.0674
fp_per_day                                2905.39
TP                                             58
FP                                           1869
TN                                          25863
FN                                              0
n_test_windows                              27790
covered_test_hours                          15.44
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w2s1_1_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w2s1_1_and_analysis_random.joblib

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Final report
---------- eye ----------
                 F1(val)=0.4370
                 best_params={'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
                 Confusion matrix: [[15347    54]
 [   13    12]]
                 Metrics results: {'model': 'rf_eye_w5s2_1', 'sensitivity': 0.48, 'specificity': np.float64(0.9965), 'precision': 0.1818, 'accuracy': 0.9957, 'f1_score': 0.2637, 'auc_roc': 0.9929, 'false_alar_rate': np.float64(0.0035), 'fp_per_day': np.float64(60.49), 'TP': 12, 'FP': 54, 'TN': 15347, 'FN': 13, 'n_test_windows': 15426, 'covered_test_hours': 21.43}
                 F1(val)=0.3792
                 best_params={'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
                 Confusion matrix: [[30666   161]
 [   13    22]]
                 Metrics results: {'model': 'rf_eye_w2s1_1', 'sensitivity': 0.6286, 'specificity': np.float64(0.9948), 'precision': 0.1202, 'accuracy': 0.9944, 'f1_score': 0.2018, 'auc_roc': 0.9751, 'false_alar_rate': np.float64(0.0052), 'fp_per_day': np.float64(225.36), 'TP': 22, 'FP': 161, 'TN': 30666, 'FN': 13, 'n_test_windows': 30862, 'covered_test_hours': 17.15}
---------- muscle ----------
                 F1(val)=0.1928
                 best_params={'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
                 Confusion matrix: [[52864  2775]
 [   46   101]]
                 Metrics results: {'model': 'rf_muscle_w1s0.5_1', 'sensitivity': 0.6871, 'specificity': np.float64(0.9501), 'precision': 0.0351, 'accuracy': 0.9494, 'f1_score': 0.0668, 'auc_roc': 0.9588, 'false_alar_rate': np.float64(0.0499), 'fp_per_day': np.float64(4297.85), 'TP': 101, 'FP': 2775, 'TN': 52864, 'FN': 46, 'n_test_windows': 55786, 'covered_test_hours': 15.5}
                 F1(val)=0.1988
                 best_params={'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
                 Confusion matrix: [[26438  1321]
 [   18    52]]
                 Metrics results: {'model': 'rf_muscle_w1s1_1', 'sensitivity': 0.7429, 'specificity': np.float64(0.9524), 'precision': 0.0379, 'accuracy': 0.9519, 'f1_score': 0.0721, 'auc_roc': 0.9674, 'false_alar_rate': np.float64(0.0476), 'fp_per_day': np.float64(4101.28), 'TP': 52, 'FP': 1321, 'TN': 26438, 'FN': 18, 'n_test_windows': 27829, 'covered_test_hours': 7.73}
                 F1(val)=0.2082
                 best_params={'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
                 Confusion matrix: [[26454  1257]
 [   22    57]]
                 Metrics results: {'model': 'rf_muscle_w2s1_1', 'sensitivity': 0.7215, 'specificity': np.float64(0.9546), 'precision': 0.0434, 'accuracy': 0.954, 'f1_score': 0.0818, 'auc_roc': 0.9664, 'false_alar_rate': np.float64(0.0454), 'fp_per_day': np.float64(1954.03), 'TP': 57, 'FP': 1257, 'TN': 26454, 'FN': 22, 'n_test_windows': 27790, 'covered_test_hours': 15.44}
                 F1(val)=0.2345
                 best_params={'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
                 Confusion matrix: [[13765    59]
 [   52     2]]
                 Metrics results: {'model': 'rf_muscle_w5s2_1', 'sensitivity': 0.037, 'specificity': np.float64(0.9957), 'precision': 0.0328, 'accuracy': 0.992, 'f1_score': 0.0348, 'auc_roc': 0.9596, 'false_alar_rate': np.float64(0.0043), 'fp_per_day': np.float64(73.46), 'TP': 2, 'FP': 59, 'TN': 13765, 'FN': 52, 'n_test_windows': 13878, 'covered_test_hours': 19.27}
---------- non_physiological ----------
                 F1(val)=0.0320
                 best_params={'n_estimators': 224, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
                 Confusion matrix: [[104436   7295]
 [     7    218]]
                 Metrics results: {'model': 'rf_non_physiological_w0.5s0.25_1', 'sensitivity': 0.9689, 'specificity': np.float64(0.9347), 'precision': 0.029, 'accuracy': 0.9348, 'f1_score': 0.0563, 'auc_roc': 0.9864, 'false_alar_rate': np.float64(0.0653), 'fp_per_day': np.float64(11259.57), 'TP': 218, 'FP': 7295, 'TN': 104436, 'FN': 7, 'n_test_windows': 111956, 'covered_test_hours': 15.55}
                 F1(val)=0.0379
                 best_params={'n_estimators': 338, 'max_depth': 29, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
                 Confusion matrix: [[51600  4073]
 [    0   113]]
                 Metrics results: {'model': 'rf_non_physiological_w1s0.5_1', 'sensitivity': 1.0, 'specificity': np.float64(0.9268), 'precision': 0.027, 'accuracy': 0.927, 'f1_score': 0.0526, 'auc_roc': 0.9684, 'false_alar_rate': np.float64(0.0732), 'fp_per_day': np.float64(6308.16), 'TP': 113, 'FP': 4073, 'TN': 51600, 'FN': 0, 'n_test_windows': 55786, 'covered_test_hours': 15.5}
                 F1(val)=0.0379
                 best_params={'n_estimators': 158, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
                 Confusion matrix: [[25773  2000]
 [    0    56]]
                 Metrics results: {'model': 'rf_non_physiological_w1s1_1', 'sensitivity': 1.0, 'specificity': np.float64(0.928), 'precision': 0.0272, 'accuracy': 0.9281, 'f1_score': 0.053, 'auc_roc': 0.9939, 'false_alar_rate': np.float64(0.072), 'fp_per_day': np.float64(6209.35), 'TP': 56, 'FP': 2000, 'TN': 25773, 'FN': 0, 'n_test_windows': 27829, 'covered_test_hours': 7.73}
                 F1(val)=0.0394
                 best_params={'n_estimators': 497, 'max_depth': 26, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
                 Confusion matrix: [[25863  1869]
 [    0    58]]
                 Metrics results: {'model': 'rf_non_physiological_w2s1_1', 'sensitivity': 1.0, 'specificity': np.float64(0.9326), 'precision': 0.0301, 'accuracy': 0.9327, 'f1_score': 0.0584, 'auc_roc': 0.9877, 'false_alar_rate': np.float64(0.0674), 'fp_per_day': np.float64(2905.39), 'TP': 58, 'FP': 1869, 'TN': 25863, 'FN': 0, 'n_test_windows': 27790, 'covered_test_hours': 15.44}
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis>