``` bash 
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> uv run python -m pipelines.artifacts.ica_cnn_rf

Loading all dataset for training...
  channel  start_time  stop_time label  confidence   Patient  ...    Montage Partition NoChannels  Duration                                                EDF                                                CSV
0  FP1-F7     22.9737    30.0688  eyem         1.0  aaaaaaju  ...  01_tcp_ar                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7    136.7987   140.1117  eyem         1.0  aaaaaaju  ...  01_tcp_ar                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7    145.0133   148.0498  eyem         1.0  aaaaaaju  ...  01_tcp_ar                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3     22.9737    30.0688  eyem         1.0  aaaaaaju  ...  01_tcp_ar                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3    136.7987   140.1117  eyem         1.0  aaaaaaju  ...  01_tcp_ar                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

[5 rows x 14 columns]
{'train': 10, 'test': 2}

==================================================
ARTIFACT: eye

==================================================
**************************************************
>> eye | patients:30 | windows: 5s (2s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  non_physiological is_ambiguous  sample_weight  distinguish  genuine_cooccurrence weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      5       2      0  ...                  0            0            1.0            0                     0            0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar                      5       2      2  ...                  0            0            1.0            0                     0            0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar                      5       2      4  ...                  0            0            1.0            0                     0            0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar                      5       2      6  ...                  0            0            1.0            0                     0            0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar                      5       2      8  ...                  0            0            1.0            0                     0            0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 20530 -> sin ambiguas: 20495 | positivas: 4802
['Patient', 'Session', 'Section', 'Start', 'eye']
[INFO]: Split for eye|w5|s2|ua0.1|p30|v3 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_eye_w5_s2_sw0.0_ua0.1
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_eye_w5_s2_sw0.3_ua0.1
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_eye_w5_s2_sw0.5_ua0.1
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_eye_w5_s2_sw0.7_ua0.1
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_eye_w5_s2_sw1.0_ua0.1

************************************************************

[INFO] Sweep size weight results for eye:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.2352      0.2382    0.2169       0.0213     0.6901   0.1617    0.1481    0.0117          0.0330
0.5             0.2376      0.2205    0.3120       0.0914     0.7301   0.1232    0.1466    0.0301          0.1216
0.3             0.2376      0.2161    0.3560       0.1399     0.7459   0.1074    0.1466    0.0459          0.1859
0.7             0.2057      0.2084    0.4510       0.2453     0.7452   0.1085    0.1463    0.0452          0.2904
1.0             0.1984      0.1986    0.4588       0.2604     0.7170   0.1374    0.1456    0.0170          0.2774
[INFO] Best suggested size weight for eye: 0.0
[INFO] sw registrado: eye|w5|s2|ua0.1|p30|v3 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_eye_w5_s2_sw0.0_ua0.1 parquet and json
[INFO] Saving patient asignation for eye
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      3036         714        2322       0.235178
train    14144        3369       10775       0.238193
val       3315         719        2596       0.216893
Broken rules: 0 | splits per patient: {'train': 19, 'test': 6, 'val': 5}
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  is_ambiguous sample_weight  distinguish  genuine_cooccurrence  weak_overlap is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      5       2      0  ...             0         1.000            0                     0             0             0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      5       2      2  ...             0         1.000            0                     0             0             0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      5       2      4  ...             0         1.000            0                     0             0             0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      5       2      6  ...             0         1.000            0                     0             0             0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      5       2      8  ...             0         1.000            0                     0             0             0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      5       2     10  ...             0         1.000            0                     0             0             0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      5       2     12  ...             0         1.000            0                     0             0             0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      5       2     14  ...             0         1.000            0                     0             0             0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      5       2     16  ...             0         1.000            0                     0             0             0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      5       2     18  ...             0         0.948            0                     0             0             0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label    ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
4          4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
16         4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ic_iclabel_prob   ic_mean  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean         0.687185 -2.295624  ...                                    []                    []                       []                                  []            0
1         1    eye blink                eye         0.949668 -0.078697  ...                                    []                    []                       []                                  []            0
2         2        brain              clean         0.994398  0.010555  ...                                    []                    []                       []                                  []            0
3         3        other  non_physiological         0.726641 -2.448747  ...                                    []                    []                       []                                  []            0
4         4        brain              clean         0.999643  0.005801  ...                                    []                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    254065
1      4802
Name: count, dtype: int64
[INFO] Split distribution:  split
train    183295
val       44121
test      31451
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye

============================================================
Modelo: rf_eye_w5s2_3
Train: 183295 (pos=3369) | Val: 44121 (pos = 719) | Test: 31451 (pos=714)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.27011361001623
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.3360287511230907
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.23507588532883641
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2723653886444584
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.31227821149751595
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2892148691448575
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.27849185946872324
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.29255734123888283
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.3304782298358315
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.3689074377701595
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2971503562054743
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.36754507628294036
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.3165137614678899
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.31229960241118376
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.3078054417480828
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.3024614100959533
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.3298870176934556
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.32345264727815065
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.308794176353176
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.3441835645677695
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.3436344111681184
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.23420865862313697
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.3092053501180173
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.3668274829479288
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.24092009685230023
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.26386365602560774
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.36485697606538237
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.31951538187433187
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.37026447462473194
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.33402413751066684
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.2807373583629291
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.3040129712201054
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.3539071347678369
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.29868168085690744
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.18582922398131327
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.30234012147195427
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.30726256983240224
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.22434064188115665
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.34155483012936766
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.3404722679846238
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.3316831683168317
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.28735632183908044
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.13831178824253618
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.35445620298355224
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 27, 'min_samples_leaf': 8, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.3133828607303547
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.20471854778674914
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 9, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2631578947368421
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 22, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.34026465028355385
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 28, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.29824224378061664
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 13, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.2050355586143611
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.35696517412935325
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 24, 'min_samples_leaf': 14, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.3723932472691162
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 11, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.29722854465122506
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 23, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.3555596601403768
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.22882118524231906
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 22, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.32832320648118535
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 25, 'min_samples_leaf': 9, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.3263093289689034
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.3057573457660197
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.3658748049245708
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 12, 'min_samples_leaf': 10, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.3093200740055504
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.3724 | fp_per_day_val(val)=1428.7401 <- choosen
        adjusted: threshold=0.6308 | F2(val)=0.4037 | fp_per_day_val(val)=875.7299
[INFO] Best configuration found with validation: {'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 24, 'min_samples_leaf': 14, 'max_features': 0.3, 'sampling_strategy': 0.3} | F1(val)=0.3724
Final report -------------------------
                  precision    recall  f1-score   support

no_rf_eye_w5s2_3       0.99      0.88      0.93     30737
   rf_eye_w5s2_3       0.11      0.64      0.19       714

        accuracy                           0.87     31451
       macro avg       0.55      0.76      0.56     31451
    weighted avg       0.97      0.87      0.91     31451

Confusion matrix -------------------------
[[27039  3698]
 [  260   454]]
General metrics -------------------------
model                 rf_eye_w5s2_3
sensitivity                  0.6359
specificity                  0.8797
precision                    0.1093
accuracy                     0.8742
f1_score                     0.1866
auc_roc                      0.8976
false_alar_rate              0.1203
fp_per_day                  2031.78
TP                              454
FP                             3698
TN                            27039
FN                              260
n_test_windows                31451
covered_test_hours            43.68
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_eye_w5s2_3_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_eye_w5s2_3_and_analysis_random.joblib
**************************************************
>> eye | patients:30 | windows: 2s (1s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  non_physiological is_ambiguous  sample_weight  distinguish  genuine_cooccurrence weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1      0  ...                  0            0            1.0            0                     0            0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1      1  ...                  0            0            1.0            0                     0            0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1      2  ...                  0            0            1.0            0                     0            0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1      3  ...                  0            0            1.0            0                     0            0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1      4  ...                  0            0            1.0            0                     0            0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 41186 -> sin ambiguas: 40944 | positivas: 7830
['Patient', 'Session', 'Section', 'Start', 'eye']
[INFO]: Split for eye|w2|s1|ua0.15|p30|v3 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_eye_w2_s1_sw0.0_ua0.15
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_eye_w2_s1_sw0.3_ua0.15
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_eye_w2_s1_sw0.5_ua0.15
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_eye_w2_s1_sw0.7_ua0.15
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_eye_w2_s1_sw1.0_ua0.15

************************************************************

[INFO] Sweep size weight results for eye:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.1947      0.1882    0.2009       0.0127     0.6896   0.1623    0.1481    0.0123           0.025
0.3             0.1947      0.1882    0.2009       0.0127     0.6896   0.1623    0.1481    0.0123           0.025
0.5             0.1947      0.1882    0.2009       0.0127     0.6896   0.1623    0.1481    0.0123           0.025
0.7             0.1947      0.1882    0.2009       0.0127     0.6896   0.1623    0.1481    0.0123           0.025
1.0             0.1947      0.1882    0.2009       0.0127     0.6896   0.1623    0.1481    0.0123           0.025
[INFO] Best suggested size weight for eye: 0.0
[INFO] sw registrado: eye|w2|s1|ua0.15|p30|v3 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_eye_w2_s1_sw0.0_ua0.15 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      6065        1181        4884       0.194724
train    28235        5314       22921       0.188206
val       6644        1335        5309       0.200933
Broken rules: 0 | splits per patient: {'train': 19, 'test': 6, 'val': 5}
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  is_ambiguous sample_weight  distinguish  genuine_cooccurrence  weak_overlap is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1      0  ...             0           1.0            0                     0             0             0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1      1  ...             0           1.0            0                     0             0             0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1      2  ...             0           1.0            0                     0             0             0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1      3  ...             0           1.0            0                     0             0             0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1      4  ...             0           1.0            0                     0             0             0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      2       1      5  ...             0           1.0            0                     0             0             0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      2       1      6  ...             0           1.0            0                     0             0             0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      2       1      7  ...             0           1.0            0                     0             0             0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      2       1      8  ...             0           1.0            0                     0             0             0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      2       1      9  ...             0           1.0            0                     0             0             0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label    ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
4          4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
16         4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ic_iclabel_prob   ic_mean  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean         0.687185 -5.572612  ...                                    []                    []                       []                                  []            0
1         1    eye blink                eye         0.949668 -0.205541  ...                                    []                    []                       []                                  []            0
2         2        brain              clean         0.994398  0.024749  ...                                    []                    []                       []                                  []            0
3         3        other  non_physiological         0.726641 -6.139340  ...                                    []                    []                       []                                  []            0
4         4        brain              clean         0.999643  0.029892  ...                                    []                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    509298
1      7830
Name: count, dtype: int64
[INFO] Split distribution:  split
train    365913
val       88434
test      62781
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye

============================================================
Modelo: rf_eye_w2s1_3
Train: 365913 (pos=5314) | Val: 88434 (pos = 1335) | Test: 62781 (pos=1181)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.24580814417702748
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2928191728984593
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.17789706517047907
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.26128266033254155
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.29331037080889083
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.29014189693801345
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.3117350611951044
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.30499010460842524
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.32256929787533417
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.3207281818892101
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2808084421391522
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.30338345864661653
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.31958762886597936
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.3173816740498951
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2647869504315214
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.28114663726571115
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.26685198054204307
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.3399348422496571
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.29555446995603324
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.3284135199028816
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.29585956674847935
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.2705703599812997
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.3089909393634322
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.3483085458888803
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.2378675591680612
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.21649110061750818
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.32471910112359553
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.2959660043093129
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.32829633591869484
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.28863912194607144
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.27984150569588906
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.2875423600222548
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.3132213388048217
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.314506989044201
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.13901635241114635
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.24727934626854112
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.3199374125010294
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.17561105207226355
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.29546911733276343
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.27450285887770076
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.34004834810636586
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.30568105354224745
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.10567393851122439
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.3145519354636983
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 27, 'min_samples_leaf': 8, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2570524650672291
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1623764791997072
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 9, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.29925633903772064
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 22, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2962066607039512
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 28, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.2619789222170073
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 13, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.1531527388124914
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.32300174052751374
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 24, 'min_samples_leaf': 14, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.3229789446321809
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 11, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.33311014395714766
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 23, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.34575604752542954
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.17082191072259867
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 22, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.29114113365571564
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 25, 'min_samples_leaf': 9, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.2768166089965398
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.27697285810876077
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.31120856877793707
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 12, 'min_samples_leaf': 10, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.2993602712012685
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.3483 | fp_per_day_val(val)=3289.0698 <- choosen
        adjusted: threshold=0.4947 | F2(val)=0.3489 | fp_per_day_val(val)=3362.3448
[INFO] Best configuration found with validation: {'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3} | F1(val)=0.3483
Final report -------------------------
                  precision    recall  f1-score   support

no_rf_eye_w2s1_3       0.99      0.90      0.94     61600
   rf_eye_w2s1_3       0.09      0.55      0.16      1181

        accuracy                           0.89     62781
       macro avg       0.54      0.72      0.55     62781
    weighted avg       0.97      0.89      0.93     62781

Confusion matrix -------------------------
[[55354  6246]
 [  537   644]]
General metrics -------------------------
model                 rf_eye_w2s1_3
sensitivity                  0.5453
specificity                  0.8986
precision                    0.0935
accuracy                      0.892
f1_score                     0.1596
auc_roc                      0.8726
false_alar_rate              0.1014
fp_per_day                  4297.91
TP                              644
FP                             6246
TN                            55354
FN                              537
n_test_windows                62781
covered_test_hours            34.88
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_eye_w2s1_3_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_eye_w2s1_3_and_analysis_random.joblib

==================================================
ARTIFACT: muscle

==================================================
**************************************************
>> muscle | patients:30 | windows: 1s (0.5s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  non_physiological is_ambiguous  sample_weight  distinguish  genuine_cooccurrence weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    0.0  ...                  0            0            1.0            0                     0            0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    0.5  ...                  0            0            1.0            0                     0            0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    1.0  ...                  0            0            1.0            0                     0            0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    1.5  ...                  0            0            1.0            0                     0            0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    2.0  ...                  0            0            1.0            0                     0            0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 82466 -> sin ambiguas: 81589 | positivas: 14610
['Patient', 'Session', 'Section', 'Start', 'muscle']
[INFO]: Split for muscle|w1|s0.5|ua0.3|p30|v3 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w1_s0.5_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w1_s0.5_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w1_s0.5_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w1_s0.5_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w1_s0.5_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.1469      0.1911    0.1665       0.0442     0.6563   0.1615    0.1822    0.0437          0.0878
0.5             0.1292      0.1849    0.2119       0.0827     0.6921   0.1373    0.1705    0.0205          0.1033
0.3             0.1333      0.1790    0.2496       0.1163     0.7120   0.1139    0.1741    0.0361          0.1524
1.0             0.1162      0.1721    0.2669       0.1506     0.7160   0.1517    0.1322    0.0178          0.1684
0.7             0.1404      0.1661    0.3210       0.1806     0.7449   0.1082    0.1469    0.0449          0.2255
[INFO] Best suggested size weight for muscle: 0.0
[INFO] sw registrado: muscle|w1|s0.5|ua0.3|p30|v3 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_muscle_w1_s0.5_sw0.0_ua0.3 parquet and json
[INFO] Saving patient asignation for muscle
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test     14865        2184       12681       0.146922
train    53549       10233       43316       0.191096
val      13175        2193       10982       0.166452
Broken rules: 0 | splits per patient: {'train': 18, 'test': 7, 'val': 5}
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  is_ambiguous sample_weight  distinguish  genuine_cooccurrence  weak_overlap is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    0.0  ...             0           1.0            0                     0             0             0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    0.5  ...             0           1.0            0                     0             0             0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    1.0  ...             0           1.0            0                     0             0             0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    1.5  ...             0           1.0            0                     0             0             0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    2.0  ...             0           1.0            0                     0             0             0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    2.5  ...             0           1.0            0                     0             0             0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    3.0  ...             0           1.0            0                     0             0             0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    3.5  ...             0           1.0            0                     0             0             0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    4.0  ...             0           1.0            0                     0             0             0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    4.5  ...             0           1.0            0                     0             0             0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label    ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
4          4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
16         4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ic_iclabel_prob    ic_mean  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean         0.687185 -21.157149  ...                                    []                    []                       []                                  []            0
1         1    eye blink                eye         0.949668  -0.418452  ...                                    []                    []                       []                                  []            0
2         2        brain              clean         0.994398   0.014797  ...                                    []                    []                       []                                  []            0
3         3        other  non_physiological         0.726641 -12.346357  ...                                    []                    []                       []                                  []            0
4         4        brain              clean         0.999643   0.066017  ...                                    []                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    1016152
1      14610
Name: count, dtype: int64
[INFO] Split distribution:  split
train    691605
val      169839
test     169318
Name: count, dtype: int64

==================================================
Starting training of Random Forest - muscle

============================================================
Modelo: rf_muscle_w1s0.5_3
Train: 691605 (pos=10233) | Val: 169839 (pos = 2193) | Test: 169318 (pos=2184)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1859382099045888
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.14748827239118953
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.06779985902081298
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.19576341782696655
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.08864420248891948
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.12895414536649114
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.14897621889633642
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.11144500172950536
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.11195454198431655
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.11555922410235246
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.14532496707723294
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1334343475708806
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.13498117349561642
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.09226098816489947
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.08018184359391206
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.16759010368094793
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.08618960107215369
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.14525769873128425
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.08876564884243687
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.10543563794288446
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.08968251967974729
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.181078136016922
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.16220212210819274
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1320697914894174
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.1772089588973665
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.07671019017882487
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.11174439633912424
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.13197546855586983
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.10686256429171534
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.08899968786450034
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.14713971397139713
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.09695227036043758
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.09773954084713796
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.10429082240762813
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.06374444089178269
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.07534416470296415
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.11629391488028226
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.06671818336700173
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.09051998135356189
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.08525728082088427
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.12108055957549445
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.13682642876576975
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.06171484533297312
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.09081873950443813
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.08143370990683715
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.0653117870948912
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.14425511632756413
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.08743244778396274
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.0791962003253544
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.0644962061055232
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.10297662976629766
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.11233225733317499
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.13553179174820162
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.14103872540681522
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.06710681968797032
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.08430128034767927
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.08124897459990753
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.08156350033360071
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.1336869670314913
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.0897392338401427
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.1958 | fp_per_day_val(val)=16074.4423 <- choosen
        adjusted: threshold=0.5884 | F2(val)=0.2061 | fp_per_day_val(val)=11794.6055
[INFO] Best configuration found with validation: {'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3} | F1(val)=0.1958
Final report -------------------------
                       precision    recall  f1-score   support

no_rf_muscle_w1s0.5_3       1.00      0.94      0.97    167134
   rf_muscle_w1s0.5_3       0.12      0.67      0.21      2184

             accuracy                           0.93    169318
            macro avg       0.56      0.81      0.59    169318
         weighted avg       0.98      0.93      0.96    169318

Confusion matrix -------------------------
[[156610  10524]
 [   714   1470]]
General metrics -------------------------
model                 rf_muscle_w1s0.5_3
sensitivity                       0.6731
specificity                        0.937
precision                         0.1226
accuracy                          0.9336
f1_score                          0.2074
auc_roc                           0.9399
false_alar_rate                    0.063
fp_per_day                       5370.21
TP                                  1470
FP                                 10524
TN                                156610
FN                                   714
n_test_windows                    169318
covered_test_hours                 47.03
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w1s0.5_3_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w1s0.5_3_and_analysis_random.joblib
**************************************************
>> muscle | patients:30 | windows: 1s (1s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  non_physiological is_ambiguous  sample_weight  distinguish  genuine_cooccurrence weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1      0  ...                  0            0            1.0            0                     0            0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1      1  ...                  0            0            1.0            0                     0            0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1      2  ...                  0            0            1.0            0                     0            0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1      3  ...                  0            0            1.0            0                     0            0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1      4  ...                  0            0            1.0            0                     0            0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 41233 -> sin ambiguas: 40753 | positivas: 7252
['Patient', 'Session', 'Section', 'Start', 'muscle']
[INFO]: Split for muscle|w1|s1|ua0.3|p30|v3 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w1_s1_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w1_s1_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w1_s1_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w1_s1_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w1_s1_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.1466      0.1898    0.1651       0.0432     0.6562   0.1614    0.1824    0.0438           0.087
0.3             0.1466      0.1898    0.1651       0.0432     0.6562   0.1614    0.1824    0.0438           0.087
0.5             0.1466      0.1898    0.1651       0.0432     0.6562   0.1614    0.1824    0.0438           0.087
0.7             0.1466      0.1898    0.1651       0.0432     0.6562   0.1614    0.1824    0.0438           0.087
1.0             0.1466      0.1898    0.1651       0.0432     0.6562   0.1614    0.1824    0.0438           0.087
[INFO] Best suggested size weight for muscle: 0.0
[INFO] sw registrado: muscle|w1|s1|ua0.3|p30|v3 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_muscle_w1_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      7434        1090        6344       0.146624
train    26741        5076       21665       0.189821
val       6578        1086        5492       0.165096
Broken rules: 0 | splits per patient: {'train': 18, 'test': 7, 'val': 5}
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  is_ambiguous sample_weight  distinguish  genuine_cooccurrence  weak_overlap is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1      0  ...             0           1.0            0                     0             0             0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1      1  ...             0           1.0            0                     0             0             0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1      2  ...             0           1.0            0                     0             0             0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1      3  ...             0           1.0            0                     0             0             0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1      4  ...             0           1.0            0                     0             0             0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1       1      5  ...             0           1.0            0                     0             0             0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1       1      6  ...             0           1.0            0                     0             0             0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1       1      7  ...             0           1.0            0                     0             0             0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1       1      8  ...             0           1.0            0                     0             0             0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1       1      9  ...             0           1.0            0                     0             0             0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label    ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
4          4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
16         4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ic_iclabel_prob    ic_mean  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean         0.687185 -21.157149  ...                                    []                    []                       []                                  []            0
1         1    eye blink                eye         0.949668  -0.418452  ...                                    []                    []                       []                                  []            0
2         2        brain              clean         0.994398   0.014797  ...                                    []                    []                       []                                  []            0
3         3        other  non_physiological         0.726641 -12.346357  ...                                    []                    []                       []                                  []            0
4         4        brain              clean         0.999643   0.066017  ...                                    []                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    507606
1      7252
Name: count, dtype: int64
[INFO] Split distribution:  split
train    345386
val       84792
test      84680
Name: count, dtype: int64

==================================================
Starting training of Random Forest - muscle

============================================================
Modelo: rf_muscle_w1s1_3
Train: 345386 (pos=5076) | Val: 84792 (pos = 1086) | Test: 84680 (pos=1090)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.19482346321564215
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.14995825573180913
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.06749869477662034
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.19969278033794163
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.08563174359956585
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.12126042177538009
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.14769221370314933
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.10404897389017852
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.1039983844911147
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.11854540312507365
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.1400593471810089
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1430340922496166
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.12668038592083813
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.0882417638200308
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.0797432728247435
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.16313481914504932
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.08256408657144639
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1359572180408579
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.08541298850026244
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.09496061292759253
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.08551103603969401
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.1860665397516091
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.16951954158095797
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.12519661068547364
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.17697306576204683
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.0729479597472754
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.11246808038192517
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.13373458206256242
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.10255441053594876
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.08570139828597204
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.14612905225314574
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.10218819246597025
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.09447582609951093
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.09724920943345906
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.06373389046691237
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.07402025961920689
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1131833082307079
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.06639440477354984
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.08696715298720352
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.08015956075290834
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.11695215593620792
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.12956064424235783
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.06152625913545975
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.08757005604483586
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.07889359217632462
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.06508996319959723
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1392331243621519
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.08570362922842409
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.07697039930182983
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.06394178118486593
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.1083927241782789
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.10638297872340426
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.13817535143679782
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.13530239099859354
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.06533704279124665
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.08199624280126883
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.07961830701650244
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.08064637807987687
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.13268599486910707
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.0872952589787036
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.1997 | fp_per_day_val(val)=15952.9012 <- choosen
        adjusted: threshold=0.7634 | F2(val)=0.2240 | fp_per_day_val(val)=2763.4305
[INFO] Best configuration found with validation: {'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3} | F1(val)=0.1997
Final report -------------------------
                     precision    recall  f1-score   support

no_rf_muscle_w1s1_3       1.00      0.94      0.97     83590
   rf_muscle_w1s1_3       0.13      0.67      0.22      1090

           accuracy                           0.94     84680
          macro avg       0.56      0.81      0.59     84680
       weighted avg       0.98      0.94      0.96     84680

Confusion matrix -------------------------
[[78713  4877]
 [  358   732]]
General metrics -------------------------
model                 rf_muscle_w1s1_3
sensitivity                     0.6716
specificity                     0.9417
precision                       0.1305
accuracy                        0.9382
f1_score                        0.2185
auc_roc                         0.9412
false_alar_rate                 0.0583
fp_per_day                     4976.06
TP                                 732
FP                                4877
TN                               78713
FN                                 358
n_test_windows                   84680
covered_test_hours               23.52
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w1s1_3_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w1s1_3_and_analysis_random.joblib
**************************************************
>> muscle | patients:30 | windows: 2s (1s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  non_physiological is_ambiguous  sample_weight  distinguish  genuine_cooccurrence weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1      0  ...                  0            0            1.0            0                     0            0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1      1  ...                  0            0            1.0            0                     0            0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1      2  ...                  0            0            1.0            0                     0            0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1      3  ...                  0            0            1.0            0                     0            0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1      4  ...                  0            0            1.0            0                     0            0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 41186 -> sin ambiguas: 40276 | positivas: 7479
['Patient', 'Session', 'Section', 'Start', 'muscle']
[INFO]: Split for muscle|w2|s1|ua0.3|p30|v3 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w2_s1_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w2_s1_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w2_s1_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w2_s1_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w2_s1_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0              0.152      0.1978    0.1749       0.0457     0.6557   0.1611    0.1833    0.0443          0.0901
0.3              0.152      0.1978    0.1749       0.0457     0.6557   0.1611    0.1833    0.0443          0.0901
0.5              0.152      0.1978    0.1749       0.0457     0.6557   0.1611    0.1833    0.0443          0.0901
0.7              0.152      0.1978    0.1749       0.0457     0.6557   0.1611    0.1833    0.0443          0.0901
1.0              0.152      0.1978    0.1749       0.0457     0.6557   0.1611    0.1833    0.0443          0.0901
[INFO] Best suggested size weight for muscle: 0.0
[INFO] sw registrado: muscle|w2|s1|ua0.3|p30|v3 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_muscle_w2_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      7381        1122        6259       0.152012
train    26407        5222       21185       0.197751
val       6488        1135        5353       0.174938
Broken rules: 0 | splits per patient: {'train': 18, 'test': 7, 'val': 5}
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  is_ambiguous sample_weight  distinguish  genuine_cooccurrence  weak_overlap is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1      0  ...             0           1.0            0                     0             0             0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1      1  ...             0           1.0            0                     0             0             0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1      2  ...             0           1.0            0                     0             0             0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1      3  ...             0           1.0            0                     0             0             0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1      4  ...             0           1.0            0                     0             0             0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      2       1      5  ...             0           1.0            0                     0             0             0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      2       1      6  ...             0           1.0            0                     0             0             0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      2       1      7  ...             0           1.0            0                     0             0             0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      2       1      8  ...             0           1.0            0                     0             0             0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      2       1      9  ...             0           1.0            0                     0             0             0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label    ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
4          4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
16         4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ic_iclabel_prob   ic_mean  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean         0.687185 -5.572612  ...                                    []                    []                       []                                  []            0
1         1    eye blink                eye         0.949668 -0.205541  ...                                    []                    []                       []                                  []            0
2         2        brain              clean         0.994398  0.024749  ...                                    []                    []                       []                                  []            0
3         3        other  non_physiological         0.726641 -6.139340  ...                                    []                    []                       []                                  []            0
4         4        brain              clean         0.999643  0.029892  ...                                    []                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    501447
1      7479
Name: count, dtype: int64
[INFO] Split distribution:  split
train    341206
test      84034
val       83686
Name: count, dtype: int64

==================================================
Starting training of Random Forest - muscle

============================================================
Modelo: rf_muscle_w2s1_3
Train: 341206 (pos=5222) | Val: 83686 (pos = 1135) | Test: 84034 (pos=1122)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.19899335823993358
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.16367942871283628
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.07236521337473377
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.21800798487077117
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.09063006223889504
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1405027932960894
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.1683748169838946
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.11889004992453268
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.11951135184971765
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.12742138364779873
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.1635930993456276
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.16236483545914096
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.14292548738189212
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.09638186260419661
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.0865171000344191
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.16697588126159554
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.08864793875524521
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.14465830186380801
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.09058681165101495
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.1032827377395323
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.09373229644126281
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.21547576847116018
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.18811431403320394
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.13754792488735904
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.19499234441142033
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.07731108606613706
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.12107644342342765
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.14994937161236524
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.11536391766446925
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.09477529638819962
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.16892847045518802
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.10747513634905358
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.10545917867293933
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.10767411464492438
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.06761103698055662
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.0795554546228745
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.12054556551950796
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.0708144598759655
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.09498850734833182
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.08572774375883184
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.13028470582128676
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.14479236743930035
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.06523213444141752
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.09518407572185689
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.08595988538681948
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.06933310487473533
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.15599076092260647
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.09471041468271145
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.08159658295898078
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.0682072441626869
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.11570616430721213
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1134175758514617
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.15545926113360323
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.14451746379457223
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.06966879577794767
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.08644685148955798
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.08514656880057737
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.0895519968879668
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.14880300422469098
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.09520122476991572
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.2180 | fp_per_day_val(val)=7054.5993 <- choosen
        adjusted: threshold=0.5482 | F2(val)=0.2273 | fp_per_day_val(val)=5729.9907
[INFO] Best configuration found with validation: {'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3} | F1(val)=0.2180
Final report -------------------------
                     precision    recall  f1-score   support

no_rf_muscle_w2s1_3       1.00      0.96      0.98     82912
   rf_muscle_w2s1_3       0.17      0.66      0.27      1122

           accuracy                           0.95     84034
          macro avg       0.58      0.81      0.62     84034
       weighted avg       0.98      0.95      0.97     84034

Confusion matrix -------------------------
[[79253  3659]
 [  379   743]]
General metrics -------------------------
model                 rf_muscle_w2s1_3
sensitivity                     0.6622
specificity                     0.9559
precision                       0.1688
accuracy                        0.9519
f1_score                         0.269
auc_roc                         0.9416
false_alar_rate                 0.0441
fp_per_day                     1881.01
TP                                 743
FP                                3659
TN                               79253
FN                                 379
n_test_windows                   84034
covered_test_hours               46.69
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w2s1_3_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w2s1_3_and_analysis_random.joblib
**************************************************
>> muscle | patients:30 | windows: 5s (2s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  non_physiological is_ambiguous  sample_weight  distinguish  genuine_cooccurrence weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      5       2      0  ...                  0            0            1.0            0                     0            0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar                      5       2      2  ...                  0            0            1.0            0                     0            0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar                      5       2      4  ...                  0            0            1.0            0                     0            0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar                      5       2      6  ...                  0            0            1.0            0                     0            0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar                      5       2      8  ...                  0            0            1.0            0                     0            0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 20530 -> sin ambiguas: 19995 | positivas: 4138
['Patient', 'Session', 'Section', 'Start', 'muscle']
[INFO]: Split for muscle|w5|s2|ua0.2|p30|v3 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w5_s2_sw0.0_ua0.2
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w5_s2_sw0.3_ua0.2
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w5_s2_sw0.5_ua0.2
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w5_s2_sw0.7_ua0.2
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_muscle_w5_s2_sw1.0_ua0.2

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.1668      0.2178    0.2086       0.0511     0.6546   0.1616    0.1838    0.0454          0.0965
0.3             0.1668      0.2178    0.2086       0.0511     0.6546   0.1616    0.1838    0.0454          0.0965
0.5             0.1668      0.2178    0.2086       0.0511     0.6546   0.1616    0.1838    0.0454          0.0965
0.7             0.1668      0.2178    0.2086       0.0511     0.6546   0.1616    0.1838    0.0454          0.0965
1.0             0.1668      0.2178    0.2086       0.0511     0.6546   0.1616    0.1838    0.0454          0.0965
[INFO] Best suggested size weight for muscle: 0.0
[INFO] sw registrado: muscle|w5|s2|ua0.2|p30|v3 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_muscle_w5_s2_sw0.0_ua0.2 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      3676         613        3063       0.166757
train    13088        2851       10237       0.217833
val       3231         674        2557       0.208604
Broken rules: 0 | splits per patient: {'train': 18, 'test': 7, 'val': 5}
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  is_ambiguous sample_weight  distinguish  genuine_cooccurrence  weak_overlap is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      5       2      0  ...             0         1.000            0                     0             0             0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      5       2      2  ...             0         1.000            0                     0             0             0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      5       2      4  ...             0         1.000            0                     0             0             0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      5       2      6  ...             0         1.000            0                     0             0             0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      5       2      8  ...             0         1.000            0                     0             0             0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      5       2     10  ...             0         1.000            0                     0             0             0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      5       2     12  ...             0         1.000            0                     0             0             0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      5       2     14  ...             0         1.000            0                     0             0             0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      5       2     16  ...             0         1.000            0                     0             0             0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      5       2     18  ...             0         0.948            0                     0             0             0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label    ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
4          4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
16         4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ic_iclabel_prob   ic_mean  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean         0.687185 -2.295624  ...                                    []                    []                       []                                  []            0
1         1    eye blink                eye         0.949668 -0.078697  ...                                    []                    []                       []                                  []            0
2         2        brain              clean         0.994398  0.010555  ...                                    []                    []                       []                                  []            0
3         3        other  non_physiological         0.726641 -2.448747  ...                                    []                    []                       []                                  []            0
4         4        brain              clean         0.999643  0.005801  ...                                    []                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    248457
1      4138
Name: count, dtype: int64
[INFO] Split distribution:  split
train    169089
test      41858
val       41648
Name: count, dtype: int64

==================================================
Starting training of Random Forest - muscle

============================================================
Modelo: rf_muscle_w5s2_3
Train: 169089 (pos=2851) | Val: 41648 (pos = 674) | Test: 41858 (pos=613)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.22191673212882954
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.17547641631456412
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.08650926604544026
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.20707831325301204
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.12589564020564303
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.18617913451861792
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.22192360941444744
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.14883116883116884
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.14230048337772516
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.18341145302628897
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.21168362323596981
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.17353491018450784
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.1761006289308176
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.1232741617357002
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.10836968375136315
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.17717899844047824
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.1159201969357387
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.18277382163445235
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.12562204150989198
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.13748520440681053
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.12516388069485415
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.24069753162225224
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.19247897080653142
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.16893121436370254
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.24338085539714868
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.09557136975827796
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1757270909911653
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.19434749880243618
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.13867047891350964
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.11668189432008527
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.21428571428571427
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.14780567267152164
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.13915409585640634
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.14996288047512993
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.08034060568157217
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.09507104533930782
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.15406643757159222
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.08543500012828079
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.1270002025521572
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.12217675297080349
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.15515487225864796
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.17846195763231387
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.07719824601892453
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.14183708165347064
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.10644687666844635
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.08283920474363446
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2045177045177045
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.11975252410233052
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.09939552564342245
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.08040759163567876
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.17573515340945334
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.14728300958937793
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.20184967704051673
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.18179978413383702
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.08123986038051227
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.10612327931104631
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.10568162994864999
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.11259911894273128
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.1896921975662133
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.12825732899022801
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.2434 | fp_per_day_val(val)=2757.4645 <- choosen
        adjusted: threshold=0.6698 | F2(val)=0.2550 | fp_per_day_val(val)=927.7295
[INFO] Best configuration found with validation: {'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3} | F1(val)=0.2434
Final report -------------------------
                     precision    recall  f1-score   support

no_rf_muscle_w5s2_3       1.00      0.95      0.97     41245
   rf_muscle_w5s2_3       0.17      0.68      0.27       613

           accuracy                           0.95     41858
          macro avg       0.58      0.82      0.62     41858
       weighted avg       0.98      0.95      0.96     41858

Confusion matrix -------------------------
[[39174  2071]
 [  194   419]]
General metrics -------------------------
model                 rf_muscle_w5s2_3
sensitivity                     0.6835
specificity                     0.9498
precision                       0.1683
accuracy                        0.9459
f1_score                        0.2701
auc_roc                         0.9212
false_alar_rate                 0.0502
fp_per_day                      854.96
TP                                 419
FP                                2071
TN                               39174
FN                                 194
n_test_windows                   41858
covered_test_hours               58.14
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w5s2_3_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w5s2_3_and_analysis_random.joblib

==================================================
ARTIFACT: non_physiological

==================================================
**************************************************
>> non_physiological | patients:30 | windows: 0.5s (0.25s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  non_physiological is_ambiguous  sample_weight  distinguish  genuine_cooccurrence weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25   0.00  ...                  0            0            1.0            0                     0            0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25   0.25  ...                  0            0            1.0            0                     0            0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25   0.50  ...                  0            0            1.0            0                     0            0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25   0.75  ...                  0            0            1.0            0                     0            0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25   1.00  ...                  0            0            1.0            0                     0            0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 165026 -> sin ambiguas: 164525 | positivas: 20210
['Patient', 'Session', 'Section', 'Start', 'non_physiological']
[INFO]: Split for non_physiological|w0.5|s0.25|ua0.2|p30|v3 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w0.5_s0.25_sw0.0_ua0.2
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w0.5_s0.25_sw0.3_ua0.2
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w0.5_s0.25_sw0.5_ua0.2
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w0.5_s0.25_sw0.7_ua0.2
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w0.5_s0.25_sw1.0_ua0.2

************************************************************

[INFO] Sweep size weight results for non_physiological:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
1.0             0.0385      0.1378    0.1252       0.0992     0.7159   0.1531    0.1311    0.0189          0.1182
0.7             0.0426      0.1423    0.1282       0.0997     0.6865   0.1377    0.1759    0.0259          0.1256
0.5             0.0476      0.1537    0.1005       0.1061     0.6277   0.1634    0.2088    0.0723          0.1783
0.3             0.0451      0.1725    0.0843       0.1274     0.5532   0.1851    0.2617    0.1468          0.2742
0.0             0.0508      0.2219    0.0457       0.1762     0.4301   0.2997    0.2702    0.2699          0.4461
[INFO] Best suggested size weight for non_physiological: 1.0
[INFO] sw registrado: non_physiological|w0.5|s0.25|ua0.2|p30|v3 = 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w0.5_s0.25_sw1.0_ua0.2 parquet and json
[INFO] Saving patient asignation for non_physiological
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test     21563         831       20732       0.038538
train   117778       16225      101553       0.137759
val      25184        3154       22030       0.125238
Broken rules: 0 | splits per patient: {'train': 19, 'val': 7, 'test': 4}
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  is_ambiguous sample_weight  distinguish  genuine_cooccurrence  weak_overlap is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25   0.00  ...             0           1.0            0                     0             0             0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25   0.25  ...             0           1.0            0                     0             0             0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25   0.50  ...             0           1.0            0                     0             0             0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25   0.75  ...             0           1.0            0                     0             0             0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25   1.00  ...             0           1.0            0                     0             0             0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25   1.25  ...             0           1.0            0                     0             0             0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25   1.50  ...             0           1.0            0                     0             0             0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25   1.75  ...             0           1.0            0                     0             0             0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25   2.00  ...             0           1.0            0                     0             0             0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25   2.25  ...             0           1.0            0                     0             0             0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label    ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
4          4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
16         4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ic_iclabel_prob    ic_mean  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean         0.687185 -21.031338  ...                                    []                    []                       []                                  []            0
1         1    eye blink                eye         0.949668  -0.947051  ...                                    []                    []                       []                                  []            0
2         2        brain              clean         0.994398   0.271020  ...                                    []                    []                       []                                  []            0
3         3        other  non_physiological         0.726641 -30.377848  ...                                    []                    []                       []                                  []            0
4         4        brain              clean         0.999643  -0.071157  ...                                    []                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    2058042
1      20210
Name: count, dtype: int64
[INFO] Split distribution:  split
train    1498071
val       315724
test      264457
Name: count, dtype: int64

==================================================
Starting training of Random Forest - non_physiological

============================================================
Modelo: rf_non_physiological_w0.5s0.25_3
Train: 1498071 (pos=16225) | Val: 315724 (pos = 3154) | Test: 264457 (pos=831)
        params:{'n_estimators': 190, 'max_depth': 28, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.14319174617772157
        params:{'n_estimators': 344, 'max_depth': 30, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.11037756438236578
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.04909025821413563
        params:{'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.14479682995071652
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.062303702187858676
        params:{'n_estimators': 375, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.09553810840059831
        params:{'n_estimators': 501, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.13004036247081635
        params:{'n_estimators': 395, 'max_depth': 18, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.0832895961065916
        params:{'n_estimators': 191, 'max_depth': 21, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.08097655305777134
        params:{'n_estimators': 536, 'max_depth': 29, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.09627016129032258
        params:{'n_estimators': 224, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.12513523260007212
        params:{'n_estimators': 180, 'max_depth': 34, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.11869667337743266
        params:{'n_estimators': 455, 'max_depth': 28, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.09969491749548988
        params:{'n_estimators': 313, 'max_depth': 19, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.08036758942669227
        params:{'n_estimators': 395, 'max_depth': 9, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.06244622798124189
        params:{'n_estimators': 565, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.1118748089182793
        params:{'n_estimators': 334, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.0666249074654063
        params:{'n_estimators': 184, 'max_depth': 19, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.0919361250993904
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.06235216324284503
        params:{'n_estimators': 298, 'max_depth': 11, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.06970378005711486
        params:{'n_estimators': 573, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.07712232914122294
        params:{'n_estimators': 433, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.14363672349930726
        params:{'n_estimators': 495, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.14305591790590486
        params:{'n_estimators': 528, 'max_depth': 16, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.0857625440461283
        params:{'n_estimators': 257, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.13780352078122568
        params:{'n_estimators': 524, 'max_depth': 10, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.05808317510675287
        params:{'n_estimators': 508, 'max_depth': 28, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.09446236654962839
        params:{'n_estimators': 362, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.12394105309035439
        params:{'n_estimators': 400, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.08197201050906537
        params:{'n_estimators': 166, 'max_depth': 9, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.06367844288860637
        params:{'n_estimators': 347, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.13465067645426998
        params:{'n_estimators': 534, 'max_depth': 21, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.08985288942939866
        params:{'n_estimators': 408, 'max_depth': 24, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.08218980101016247
        params:{'n_estimators': 190, 'max_depth': 21, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.09062506064310803
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.04807985463237357
        params:{'n_estimators': 592, 'max_depth': 11, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.05885990426677049
        params:{'n_estimators': 596, 'max_depth': 30, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.09053702637136325
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.048409575088561585
        params:{'n_estimators': 562, 'max_depth': 13, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.07109461364489204
        params:{'n_estimators': 206, 'max_depth': 21, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.06804464847482115
        params:{'n_estimators': 598, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.0884431553576535
        params:{'n_estimators': 338, 'max_depth': 29, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.10376908396946564
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.048044845918320714
        params:{'n_estimators': 497, 'max_depth': 26, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.0802660753880266
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.05831777927802708
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.050295347320777874
        params:{'n_estimators': 373, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.10594963141076344
        params:{'n_estimators': 257, 'max_depth': 14, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.07108076480622
        params:{'n_estimators': 423, 'max_depth': 15, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.063859882680867
        params:{'n_estimators': 304, 'max_depth': 8, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.049609030958687024
        params:{'n_estimators': 314, 'max_depth': 32, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.0929561409857422
        params:{'n_estimators': 355, 'max_depth': 12, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.07788800291404147
        params:{'n_estimators': 268, 'max_depth': 28, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.13183603687949036
        params:{'n_estimators': 505, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.09025455807204592
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.04993694911728764
        params:{'n_estimators': 207, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.07112976845562148
        params:{'n_estimators': 474, 'max_depth': 14, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.06830882453900125
        params:{'n_estimators': 396, 'max_depth': 10, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.06381284302738471
        params:{'n_estimators': 158, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.10444230615026863
        params:{'n_estimators': 448, 'max_depth': 17, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.08010622782385338
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.1448 | fp_per_day_val(val)=30514.9156 <- choosen
        adjusted: threshold=0.7715 | F2(val)=0.1913 | fp_per_day_val(val)=6633.4393
[INFO] Best configuration found with validation: {'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3} | F1(val)=0.1448
Final report -------------------------
                                     precision    recall  f1-score   support

no_rf_non_physiological_w0.5s0.25_3       1.00      0.91      0.95    263626
   rf_non_physiological_w0.5s0.25_3       0.02      0.68      0.04       831

                           accuracy                           0.91    264457
                          macro avg       0.51      0.79      0.50    264457
                       weighted avg       1.00      0.91      0.95    264457

Confusion matrix -------------------------
[[239026  24600]
 [   268    563]]
General metrics -------------------------
model                 rf_non_physiological_w0.5s0.25_3
sensitivity                                     0.6775
specificity                                     0.9067
precision                                       0.0224
accuracy                                         0.906
f1_score                                        0.0433
auc_roc                                         0.9076
false_alar_rate                                 0.0933
fp_per_day                                    16073.99
TP                                                 563
FP                                               24600
TN                                              239026
FN                                                 268
n_test_windows                                  264457
covered_test_hours                               36.73
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w0.5s0.25_3_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w0.5s0.25_3_and_analysis_random.joblib
**************************************************
>> non_physiological | patients:30 | windows: 1s (0.5s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w1_s0.5_ua0.3_ub0.1_urTrue_dcd979_L3.parquet (82466 rows)
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  non_physiological is_ambiguous  sample_weight  distinguish  genuine_cooccurrence weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    0.0  ...                  0            0            1.0            0                     0            0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    0.5  ...                  0            0            1.0            0                     0            0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    1.0  ...                  0            0            1.0            0                     0            0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    1.5  ...                  0            0            1.0            0                     0            0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    2.0  ...                  0            0            1.0            0                     0            0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 82466 -> sin ambiguas: 81589 | positivas: 10124
['Patient', 'Session', 'Section', 'Start', 'non_physiological']
[INFO]: Split for non_physiological|w1|s0.5|ua0.3|p30|v3 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w1_s0.5_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w1_s0.5_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w1_s0.5_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w1_s0.5_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w1_s0.5_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for non_physiological:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0386      0.1389    0.1277       0.1003     0.7163   0.1527     0.131     0.019          0.1193
0.3             0.0386      0.1389    0.1277       0.1003     0.7163   0.1527     0.131     0.019          0.1193
0.5             0.0386      0.1389    0.1277       0.1003     0.7163   0.1527     0.131     0.019          0.1193
0.7             0.0386      0.1389    0.1277       0.1003     0.7163   0.1527     0.131     0.019          0.1193
1.0             0.0386      0.1389    0.1277       0.1003     0.7163   0.1527     0.131     0.019          0.1193
[INFO] Best suggested size weight for non_physiological: 0.0
[INFO] sw registrado: non_physiological|w1|s0.5|ua0.3|p30|v3 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w1_s0.5_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test     10687         413       10274       0.038645
train    58445        8120       50325       0.138934
val      12457        1591       10866       0.127719
Broken rules: 0 | splits per patient: {'train': 19, 'val': 7, 'test': 4}
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  is_ambiguous sample_weight  distinguish  genuine_cooccurrence  weak_overlap is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    0.0  ...             0           1.0            0                     0             0             0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    0.5  ...             0           1.0            0                     0             0             0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    1.0  ...             0           1.0            0                     0             0             0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    1.5  ...             0           1.0            0                     0             0             0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    2.0  ...             0           1.0            0                     0             0             0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    2.5  ...             0           1.0            0                     0             0             0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    3.0  ...             0           1.0            0                     0             0             0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    3.5  ...             0           1.0            0                     0             0             0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    4.0  ...             0           1.0            0                     0             0             0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    4.5  ...             0           1.0            0                     0             0             0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label    ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
4          4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
16         4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ic_iclabel_prob    ic_mean  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean         0.687185 -21.157149  ...                                    []                    []                       []                                  []            0
1         1    eye blink                eye         0.949668  -0.418452  ...                                    []                    []                       []                                  []            0
2         2        brain              clean         0.994398   0.014797  ...                                    []                    []                       []                                  []            0
3         3        other  non_physiological         0.726641 -12.346357  ...                                    []                    []                       []                                  []            0
4         4        brain              clean         0.999643   0.066017  ...                                    []                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    1020638
1      10124
Name: count, dtype: int64
[INFO] Split distribution:  split
train    743503
val      156165
test     131094
Name: count, dtype: int64

==================================================
Starting training of Random Forest - non_physiological

============================================================
Modelo: rf_non_physiological_w1s0.5_3
Train: 743503 (pos=8120) | Val: 156165 (pos = 1591) | Test: 131094 (pos=413)
        params:{'n_estimators': 190, 'max_depth': 28, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1489303262428663
        params:{'n_estimators': 344, 'max_depth': 30, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.13102447785939622
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.05222309918442515
        params:{'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.15677270239036556
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.06298835911337905
        params:{'n_estimators': 375, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.10516152989231341
        params:{'n_estimators': 501, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.14000919463367745
        params:{'n_estimators': 395, 'max_depth': 18, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.08984213364095749
        params:{'n_estimators': 191, 'max_depth': 21, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.0892880233791088
        params:{'n_estimators': 536, 'max_depth': 29, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.11149705425166478
        params:{'n_estimators': 224, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.13308763308763308
        params:{'n_estimators': 180, 'max_depth': 34, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.12730505345216658
        params:{'n_estimators': 455, 'max_depth': 28, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.11885631960990746
        params:{'n_estimators': 313, 'max_depth': 19, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.08554110276887762
        params:{'n_estimators': 395, 'max_depth': 9, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.06794131268733014
        params:{'n_estimators': 565, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.1193211121008955
        params:{'n_estimators': 334, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.06560245887076716
        params:{'n_estimators': 184, 'max_depth': 19, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.11151633033471108
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.06304493628437291
        params:{'n_estimators': 298, 'max_depth': 11, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.07408704970736131
        params:{'n_estimators': 573, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.07583406958643611
        params:{'n_estimators': 433, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.15513370075525618
        params:{'n_estimators': 495, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.15146124523506987
        params:{'n_estimators': 528, 'max_depth': 16, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.09957585461082553
        params:{'n_estimators': 257, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.14417460041263766
        params:{'n_estimators': 524, 'max_depth': 10, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.05724246599325574
        params:{'n_estimators': 508, 'max_depth': 28, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.11035142411789713
        params:{'n_estimators': 362, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.1361875279870724
        params:{'n_estimators': 400, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.08461004015591328
        params:{'n_estimators': 166, 'max_depth': 9, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.06757184310676803
        params:{'n_estimators': 347, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.1396916073460826
        params:{'n_estimators': 534, 'max_depth': 21, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.10276360951195831
        params:{'n_estimators': 408, 'max_depth': 24, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.091202497321464
        params:{'n_estimators': 190, 'max_depth': 21, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.10420956639406954
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.04911961817147662
        params:{'n_estimators': 592, 'max_depth': 11, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.06259633358475716
        params:{'n_estimators': 596, 'max_depth': 30, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.10506808223265748
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.05049154441727791
        params:{'n_estimators': 562, 'max_depth': 13, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.06934247022352749
        params:{'n_estimators': 206, 'max_depth': 21, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.0807693604775341
        params:{'n_estimators': 598, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.106904621654753
        params:{'n_estimators': 338, 'max_depth': 29, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.12232445150060253
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.04897313403432737
        params:{'n_estimators': 497, 'max_depth': 26, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.08892379408188082
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.05942690964264829
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.05410141202299054
        params:{'n_estimators': 373, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.11421696278471834
        params:{'n_estimators': 257, 'max_depth': 14, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.07810431559438707
        params:{'n_estimators': 423, 'max_depth': 15, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.06963661104870453
        params:{'n_estimators': 304, 'max_depth': 8, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.052845419617397825
        params:{'n_estimators': 314, 'max_depth': 32, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.11002958297547476
        params:{'n_estimators': 355, 'max_depth': 12, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.07685502009316406
        params:{'n_estimators': 268, 'max_depth': 28, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.14265350410620825
        params:{'n_estimators': 505, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.10677003377341111
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.04981360915677833
        params:{'n_estimators': 207, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.0770440906817803
        params:{'n_estimators': 474, 'max_depth': 14, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.07166208093261367
        params:{'n_estimators': 396, 'max_depth': 10, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.07135533952142949
        params:{'n_estimators': 158, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.12913318201337343
        params:{'n_estimators': 448, 'max_depth': 17, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.08745923510228283
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.1568 | fp_per_day_val(val)=14100.9624 <- choosen
        adjusted: threshold=0.7299 | F2(val)=0.2092 | fp_per_day_val(val)=3549.1691
[INFO] Best configuration found with validation: {'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3} | F1(val)=0.1568
Final report -------------------------
                                  precision    recall  f1-score   support

no_rf_non_physiological_w1s0.5_3       1.00      0.92      0.96    130681
   rf_non_physiological_w1s0.5_3       0.02      0.64      0.04       413

                        accuracy                           0.91    131094
                       macro avg       0.51      0.78      0.50    131094
                    weighted avg       1.00      0.91      0.95    131094

Confusion matrix -------------------------
[[119636  11045]
 [   150    263]]
General metrics -------------------------
model                 rf_non_physiological_w1s0.5_3
sensitivity                                  0.6368
specificity                                  0.9155
precision                                    0.0233
accuracy                                     0.9146
f1_score                                     0.0449
auc_roc                                      0.9017
false_alar_rate                              0.0845
fp_per_day                                  7279.42
TP                                              263
FP                                            11045
TN                                           119636
FN                                              150
n_test_windows                               131094
covered_test_hours                            36.41
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w1s0.5_3_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w1s0.5_3_and_analysis_random.joblib
**************************************************
>> non_physiological | patients:30 | windows: 1s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w1_s1_ua0.3_ub0.1_urTrue_dcd979_L3.parquet (41233 rows)
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  non_physiological is_ambiguous  sample_weight  distinguish  genuine_cooccurrence weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1      0  ...                  0            0            1.0            0                     0            0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1      1  ...                  0            0            1.0            0                     0            0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1      2  ...                  0            0            1.0            0                     0            0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1      3  ...                  0            0            1.0            0                     0            0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1      4  ...                  0            0            1.0            0                     0            0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 41233 -> sin ambiguas: 40753 | positivas: 5014
['Patient', 'Session', 'Section', 'Start', 'non_physiological']
[INFO]: Split for non_physiological|w1|s1|ua0.3|p30|v3 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w1_s1_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w1_s1_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w1_s1_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w1_s1_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w1_s1_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for non_physiological:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0376      0.1379    0.1264       0.1003     0.7162   0.1528    0.1311    0.0189          0.1193
0.3             0.0376      0.1379    0.1264       0.1003     0.7162   0.1528    0.1311    0.0189          0.1193
0.5             0.0376      0.1379    0.1264       0.1003     0.7162   0.1528    0.1311    0.0189          0.1193
0.7             0.0376      0.1379    0.1264       0.1003     0.7162   0.1528    0.1311    0.0189          0.1193
1.0             0.0376      0.1379    0.1264       0.1003     0.7162   0.1528    0.1311    0.0189          0.1193
[INFO] Best suggested size weight for non_physiological: 0.0
[INFO] sw registrado: non_physiological|w1|s1|ua0.3|p30|v3 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w1_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      5341         201        5140       0.037633
train    29186        4026       25160       0.137943
val       6226         787        5439       0.126405
Broken rules: 0 | splits per patient: {'train': 19, 'val': 7, 'test': 4}
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  is_ambiguous sample_weight  distinguish  genuine_cooccurrence  weak_overlap is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1      0  ...             0           1.0            0                     0             0             0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1      1  ...             0           1.0            0                     0             0             0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1      2  ...             0           1.0            0                     0             0             0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1      3  ...             0           1.0            0                     0             0             0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1      4  ...             0           1.0            0                     0             0             0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1       1      5  ...             0           1.0            0                     0             0             0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1       1      6  ...             0           1.0            0                     0             0             0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1       1      7  ...             0           1.0            0                     0             0             0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1       1      8  ...             0           1.0            0                     0             0             0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1       1      9  ...             0           1.0            0                     0             0             0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label    ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
4          4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
16         4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ic_iclabel_prob    ic_mean  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean         0.687185 -21.157149  ...                                    []                    []                       []                                  []            0
1         1    eye blink                eye         0.949668  -0.418452  ...                                    []                    []                       []                                  []            0
2         2        brain              clean         0.994398   0.014797  ...                                    []                    []                       []                                  []            0
3         3        other  non_physiological         0.726641 -12.346357  ...                                    []                    []                       []                                  []            0
4         4        brain              clean         0.999643   0.066017  ...                                    []                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    509844
1      5014
Name: count, dtype: int64
[INFO] Split distribution:  split
train    371296
val       78044
test      65518
Name: count, dtype: int64

==================================================
Starting training of Random Forest - non_physiological

============================================================
Modelo: rf_non_physiological_w1s1_3
Train: 371296 (pos=4026) | Val: 78044 (pos = 787) | Test: 65518 (pos=201)
        params:{'n_estimators': 190, 'max_depth': 28, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.15774074545223254
        params:{'n_estimators': 344, 'max_depth': 30, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.13242193411693487
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.053737743424466716
        params:{'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1655490360435876
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.06648984485702866
        params:{'n_estimators': 375, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.10940612549800798
        params:{'n_estimators': 501, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.14051378548637813
        params:{'n_estimators': 395, 'max_depth': 18, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.0889967637540453
        params:{'n_estimators': 191, 'max_depth': 21, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.09163185554507479
        params:{'n_estimators': 536, 'max_depth': 29, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.11803936009164928
        params:{'n_estimators': 224, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.14520586444329944
        params:{'n_estimators': 180, 'max_depth': 34, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1336555322697917
        params:{'n_estimators': 455, 'max_depth': 28, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.11659014496945158
        params:{'n_estimators': 313, 'max_depth': 19, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.08590025891063953
        params:{'n_estimators': 395, 'max_depth': 9, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.07071819080850111
        params:{'n_estimators': 565, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.13401455167986304
        params:{'n_estimators': 334, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.06979309295603225
        params:{'n_estimators': 184, 'max_depth': 19, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.10352370108467669
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.06642621524631166
        params:{'n_estimators': 298, 'max_depth': 11, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.07665656128194023
        params:{'n_estimators': 573, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.08107495180859507
        params:{'n_estimators': 433, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.16274459649571557
        params:{'n_estimators': 495, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.1570162202942286
        params:{'n_estimators': 528, 'max_depth': 16, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.09427402316065363
        params:{'n_estimators': 257, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.14446071254270376
        params:{'n_estimators': 524, 'max_depth': 10, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.06126627897452699
        params:{'n_estimators': 508, 'max_depth': 28, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1221705305133117
        params:{'n_estimators': 362, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.11756479885524733
        params:{'n_estimators': 400, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.08816590090649447
        params:{'n_estimators': 166, 'max_depth': 9, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.0710106176858095
        params:{'n_estimators': 347, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.1496523460883179
        params:{'n_estimators': 534, 'max_depth': 21, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.09689922480620156
        params:{'n_estimators': 408, 'max_depth': 24, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.09884001247908336
        params:{'n_estimators': 190, 'max_depth': 21, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.10321201651392264
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.04904404616496747
        params:{'n_estimators': 592, 'max_depth': 11, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.06439671789972877
        params:{'n_estimators': 596, 'max_depth': 30, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.10697811365197762
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.05216293441424679
        params:{'n_estimators': 562, 'max_depth': 13, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.07319015148421869
        params:{'n_estimators': 206, 'max_depth': 21, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.08636020365904164
        params:{'n_estimators': 598, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.10281351967001169
        params:{'n_estimators': 338, 'max_depth': 29, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.12160091918805055
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.04853949770562984
        params:{'n_estimators': 497, 'max_depth': 26, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.09898020395920816
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.06336013080801199
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.055511666619642804
        params:{'n_estimators': 373, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.11749745676500509
        params:{'n_estimators': 257, 'max_depth': 14, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.08210437071908257
        params:{'n_estimators': 423, 'max_depth': 15, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.0692054125917427
        params:{'n_estimators': 304, 'max_depth': 8, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.05430947406290213
        params:{'n_estimators': 314, 'max_depth': 32, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.12380989695568703
        params:{'n_estimators': 355, 'max_depth': 12, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.07961069250089702
        params:{'n_estimators': 268, 'max_depth': 28, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.13561713636185474
        params:{'n_estimators': 505, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.10050395968322534
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.053389948489489074
        params:{'n_estimators': 207, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.07777707423119948
        params:{'n_estimators': 474, 'max_depth': 14, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.07483075192350187
        params:{'n_estimators': 396, 'max_depth': 10, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.07446583049149375
        params:{'n_estimators': 158, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.13625781713607524
        params:{'n_estimators': 448, 'max_depth': 17, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.09273939851516295
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.1655 | fp_per_day_val(val)=14392.9886 <- choosen
        adjusted: threshold=0.7285 | F2(val)=0.2233 | fp_per_day_val(val)=3192.7836
[INFO] Best configuration found with validation: {'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3} | F1(val)=0.1655
Final report -------------------------
                                precision    recall  f1-score   support

no_rf_non_physiological_w1s1_3       1.00      0.91      0.95     65317
   rf_non_physiological_w1s1_3       0.02      0.69      0.05       201

                      accuracy                           0.91     65518
                     macro avg       0.51      0.80      0.50     65518
                  weighted avg       1.00      0.91      0.95     65518

Confusion matrix -------------------------
[[59677  5640]
 [   62   139]]
General metrics -------------------------
model                 rf_non_physiological_w1s1_3
sensitivity                                0.6915
specificity                                0.9137
precision                                  0.0241
accuracy                                    0.913
f1_score                                   0.0465
auc_roc                                    0.9042
false_alar_rate                            0.0863
fp_per_day                                7437.59
TP                                            139
FP                                           5640
TN                                          59677
FN                                             62
n_test_windows                              65518
covered_test_hours                           18.2
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w1s1_3_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w1s1_3_and_analysis_random.joblib
**************************************************
>> non_physiological | patients:30 | windows: 2s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w2_s1_ua0.3_ub0.1_urTrue_dcd979_L3.parquet (41186 rows)
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  non_physiological is_ambiguous  sample_weight  distinguish  genuine_cooccurrence weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1      0  ...                  0            0            1.0            0                     0            0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1      1  ...                  0            0            1.0            0                     0            0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1      2  ...                  0            0            1.0            0                     0            0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1      3  ...                  0            0            1.0            0                     0            0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1      4  ...                  0            0            1.0            0                     0            0              0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 41186 -> sin ambiguas: 40276 | positivas: 5118
['Patient', 'Session', 'Section', 'Start', 'non_physiological']
[INFO]: Split for non_physiological|w2|s1|ua0.3|p30|v3 not found

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w2_s1_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w2_s1_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w2_s1_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w2_s1_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w2_s1_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for non_physiological:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0414      0.1424    0.1286        0.101     0.7173   0.1513    0.1314    0.0186          0.1197
0.3             0.0414      0.1424    0.1286        0.101     0.7173   0.1513    0.1314    0.0186          0.1197
0.5             0.0414      0.1424    0.1286        0.101     0.7173   0.1513    0.1314    0.0186          0.1197
0.7             0.0414      0.1424    0.1286        0.101     0.7173   0.1513    0.1314    0.0186          0.1197
1.0             0.0414      0.1424    0.1286        0.101     0.7173   0.1513    0.1314    0.0186          0.1197
[INFO] Best suggested size weight for non_physiological: 0.0
[INFO] sw registrado: non_physiological|w2|s1|ua0.3|p30|v3 = 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_non_physiological_w2_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      5291         219        5072       0.041391
train    28890        4115       24775       0.142437
val       6095         784        5311       0.128630
Broken rules: 0 | splits per patient: {'train': 19, 'val': 7, 'test': 4}
    Patient Session Section    Montage Partition  Window_size  stride  Start  ...  is_ambiguous sample_weight  distinguish  genuine_cooccurrence  weak_overlap is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1      0  ...             0           1.0            0                     0             0             0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1      1  ...             0           1.0            0                     0             0             0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1      2  ...             0           1.0            0                     0             0             0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1      3  ...             0           1.0            0                     0             0             0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1      4  ...             0           1.0            0                     0             0             0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      2       1      5  ...             0           1.0            0                     0             0             0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      2       1      6  ...             0           1.0            0                     0             0             0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      2       1      7  ...             0           1.0            0                     0             0             0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      2       1      8  ...             0           1.0            0                     0             0             0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      2       1      9  ...             0           1.0            0                     0             0             0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label    ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
4          4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink                eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain              clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other  non_physiological         0.726641  ...                                    []                    []                       []                                  []
16         4        brain              clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain              clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain              clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain              clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink                eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain              clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain              clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain              clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain              clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label    ic_target_label  ic_iclabel_prob   ic_mean  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain              clean         0.687185 -5.572612  ...                                    []                    []                       []                                  []            0
1         1    eye blink                eye         0.949668 -0.205541  ...                                    []                    []                       []                                  []            0
2         2        brain              clean         0.994398  0.024749  ...                                    []                    []                       []                                  []            0
3         3        other  non_physiological         0.726641 -6.139340  ...                                    []                    []                       []                                  []            0
4         4        brain              clean         0.999643  0.029892  ...                                    []                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    503808
1      5118
Name: count, dtype: int64
[INFO] Split distribution:  split
train    367603
val       76420
test      64903
Name: count, dtype: int64

==================================================
Starting training of Random Forest - non_physiological

============================================================
Modelo: rf_non_physiological_w2s1_3
Train: 367603 (pos=4115) | Val: 76420 (pos = 784) | Test: 64903 (pos=219)
        params:{'n_estimators': 190, 'max_depth': 28, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1601879538658693
        params:{'n_estimators': 344, 'max_depth': 30, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.13849394418114797
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.058731401722787784
        params:{'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.15972417675204054
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.07676203768318214
        params:{'n_estimators': 375, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.11944641829932663
        params:{'n_estimators': 501, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.14874693305292674
        params:{'n_estimators': 395, 'max_depth': 18, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.09750177275950472
        params:{'n_estimators': 191, 'max_depth': 21, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.09910775566231983
        params:{'n_estimators': 536, 'max_depth': 29, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.12890750886239125
        params:{'n_estimators': 224, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.15003454742868425
        params:{'n_estimators': 180, 'max_depth': 34, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.134863573438128
        params:{'n_estimators': 455, 'max_depth': 28, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.11712707182320442
        params:{'n_estimators': 313, 'max_depth': 19, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.09425991445318688
        params:{'n_estimators': 395, 'max_depth': 9, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.07885815866716275
        params:{'n_estimators': 565, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.13017989539628713
        params:{'n_estimators': 334, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.07457039883713984
        params:{'n_estimators': 184, 'max_depth': 19, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.11589004242403339
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.07655463216932083
        params:{'n_estimators': 298, 'max_depth': 11, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.08642299520137513
        params:{'n_estimators': 573, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.0856860763064482
        params:{'n_estimators': 433, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.1565938095936629
        params:{'n_estimators': 495, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.17221972084646556
        params:{'n_estimators': 528, 'max_depth': 16, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.10247319266689726
        params:{'n_estimators': 257, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.1497814001187456
        params:{'n_estimators': 524, 'max_depth': 10, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.06645955058163139
        params:{'n_estimators': 508, 'max_depth': 28, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.12631221206857488
        params:{'n_estimators': 362, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.1344285396425128
        params:{'n_estimators': 400, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.09504706468444374
        params:{'n_estimators': 166, 'max_depth': 9, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.081860935302391
        params:{'n_estimators': 347, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.15665730900340885
        params:{'n_estimators': 534, 'max_depth': 21, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.10550586920067076
        params:{'n_estimators': 408, 'max_depth': 24, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.101712154602475
        params:{'n_estimators': 190, 'max_depth': 21, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.10635124250469855
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.052466739834569155
        params:{'n_estimators': 592, 'max_depth': 11, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.07095252358843793
        params:{'n_estimators': 596, 'max_depth': 30, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.11272168051829069
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.05668262070361641
        params:{'n_estimators': 562, 'max_depth': 13, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.08142826039625517
        params:{'n_estimators': 206, 'max_depth': 21, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.08833067131310197
        params:{'n_estimators': 598, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.11096926249631739
        params:{'n_estimators': 338, 'max_depth': 29, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.12171507607192254
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.05046473905095394
        params:{'n_estimators': 497, 'max_depth': 26, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.09719135719831856
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.07078313253012049
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.05978452979236787
        params:{'n_estimators': 373, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.12107639010392973
        params:{'n_estimators': 257, 'max_depth': 14, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.09004109257916365
        params:{'n_estimators': 423, 'max_depth': 15, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.07708779443254818
        params:{'n_estimators': 304, 'max_depth': 8, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.05827261710626711
        params:{'n_estimators': 314, 'max_depth': 32, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.12780069562403948
        params:{'n_estimators': 355, 'max_depth': 12, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.0888648860958366
        params:{'n_estimators': 268, 'max_depth': 28, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.138290450982806
        params:{'n_estimators': 505, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.10938137534917297
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.05728436315899394
        params:{'n_estimators': 207, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.08654704307388793
        params:{'n_estimators': 474, 'max_depth': 14, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.08166909859093582
        params:{'n_estimators': 396, 'max_depth': 10, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.0832865835239287
        params:{'n_estimators': 158, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.1302014018276994
        params:{'n_estimators': 448, 'max_depth': 17, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.09960906121137471
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.1722 | fp_per_day_val(val)=7925.4645 <- choosen
        adjusted: threshold=0.7276 | F2(val)=0.2299 | fp_per_day_val(val)=2050.8977
[INFO] Best configuration found with validation: {'n_estimators': 495, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5} | F1(val)=0.1722
Final report -------------------------
                                precision    recall  f1-score   support

no_rf_non_physiological_w2s1_3       1.00      0.90      0.94     64684
   rf_non_physiological_w2s1_3       0.02      0.64      0.04       219

                      accuracy                           0.89     64903
                     macro avg       0.51      0.77      0.49     64903
                  weighted avg       1.00      0.89      0.94     64903

Confusion matrix -------------------------
[[57913  6771]
 [   78   141]]
General metrics -------------------------
model                 rf_non_physiological_w2s1_3
sensitivity                                0.6438
specificity                                0.8953
precision                                  0.0204
accuracy                                   0.8945
f1_score                                   0.0395
auc_roc                                    0.9056
false_alar_rate                            0.1047
fp_per_day                                4506.84
TP                                            141
FP                                           6771
TN                                          57913
FN                                             78
n_test_windows                              64903
covered_test_hours                          36.06
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w2s1_3_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w2s1_3_and_analysis_random.joblib

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Final report
---------- eye ----------
                 F1(val)=0.3724
                 best_params={'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 24, 'min_samples_leaf': 14, 'max_features': 0.3, 'sampling_strategy': 0.3}
                 Confusion matrix: [[27039  3698]
 [  260   454]]
                 Metrics results: {'model': 'rf_eye_w5s2_3', 'sensitivity': 0.6359, 'specificity': np.float64(0.8797), 'precision': 0.1093, 'accuracy': 0.8742, 'f1_score': 0.1866, 'auc_roc': 0.8976, 'false_alar_rate': np.float64(0.1203), 'fp_per_day': np.float64(2031.78), 'TP': 454, 'FP': 3698, 'TN': 27039, 'FN': 260, 'n_test_windows': 31451, 'covered_test_hours': 43.68}
                 F1(val)=0.3483
                 best_params={'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
                 Confusion matrix: [[55354  6246]
 [  537   644]]
                 Metrics results: {'model': 'rf_eye_w2s1_3', 'sensitivity': 0.5453, 'specificity': np.float64(0.8986), 'precision': 0.0935, 'accuracy': 0.892, 'f1_score': 0.1596, 'auc_roc': 0.8726, 'false_alar_rate': np.float64(0.1014), 'fp_per_day': np.float64(4297.91), 'TP': 644, 'FP': 6246, 'TN': 55354, 'FN': 537, 'n_test_windows': 62781, 'covered_test_hours': 34.88}
---------- muscle ----------
                 F1(val)=0.1958
                 best_params={'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
                 Confusion matrix: [[156610  10524]
 [   714   1470]]
                 Metrics results: {'model': 'rf_muscle_w1s0.5_3', 'sensitivity': 0.6731, 'specificity': np.float64(0.937), 'precision': 0.1226, 'accuracy': 0.9336, 'f1_score': 0.2074, 'auc_roc': 0.9399, 'false_alar_rate': np.float64(0.063), 'fp_per_day': np.float64(5370.21), 'TP': 1470, 'FP': 10524, 'TN': 156610, 'FN': 714, 'n_test_windows': 169318, 'covered_test_hours': 47.03}
                 F1(val)=0.1997
                 best_params={'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
                 Confusion matrix: [[78713  4877]
 [  358   732]]
                 Metrics results: {'model': 'rf_muscle_w1s1_3', 'sensitivity': 0.6716, 'specificity': np.float64(0.9417), 'precision': 0.1305, 'accuracy': 0.9382, 'f1_score': 0.2185, 'auc_roc': 0.9412, 'false_alar_rate': np.float64(0.0583), 'fp_per_day': np.float64(4976.06), 'TP': 732, 'FP': 4877, 'TN': 78713, 'FN': 358, 'n_test_windows': 84680, 'covered_test_hours': 23.52}
                 F1(val)=0.2180
                 best_params={'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
                 Confusion matrix: [[79253  3659]
 [  379   743]]
                 Metrics results: {'model': 'rf_muscle_w2s1_3', 'sensitivity': 0.6622, 'specificity': np.float64(0.9559), 'precision': 0.1688, 'accuracy': 0.9519, 'f1_score': 0.269, 'auc_roc': 0.9416, 'false_alar_rate': np.float64(0.0441), 'fp_per_day': np.float64(1881.01), 'TP': 743, 'FP': 3659, 'TN': 79253, 'FN': 379, 'n_test_windows': 84034, 'covered_test_hours': 46.69}
                 F1(val)=0.2434
                 best_params={'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
                 Confusion matrix: [[39174  2071]
 [  194   419]]
                 Metrics results: {'model': 'rf_muscle_w5s2_3', 'sensitivity': 0.6835, 'specificity': np.float64(0.9498), 'precision': 0.1683, 'accuracy': 0.9459, 'f1_score': 0.2701, 'auc_roc': 0.9212, 'false_alar_rate': np.float64(0.0502), 'fp_per_day': np.float64(854.96), 'TP': 419, 'FP': 2071, 'TN': 39174, 'FN': 194, 'n_test_windows': 41858, 'covered_test_hours': 58.14}
---------- non_physiological ----------
                 F1(val)=0.1448
                 best_params={'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
                 Confusion matrix: [[239026  24600]
 [   268    563]]
                 Metrics results: {'model': 'rf_non_physiological_w0.5s0.25_3', 'sensitivity': 0.6775, 'specificity': np.float64(0.9067), 'precision': 0.0224, 'accuracy': 0.906, 'f1_score': 0.0433, 'auc_roc': 0.9076, 'false_alar_rate': np.float64(0.0933), 'fp_per_day': np.float64(16073.99), 'TP': 563, 'FP': 24600, 'TN': 239026, 'FN': 268, 'n_test_windows': 264457, 'covered_test_hours': 36.73}
                 F1(val)=0.1568
                 best_params={'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
                 Confusion matrix: [[119636  11045]
 [   150    263]]
                 Metrics results: {'model': 'rf_non_physiological_w1s0.5_3', 'sensitivity': 0.6368, 'specificity': np.float64(0.9155), 'precision': 0.0233, 'accuracy': 0.9146, 'f1_score': 0.0449, 'auc_roc': 0.9017, 'false_alar_rate': np.float64(0.0845), 'fp_per_day': np.float64(7279.42), 'TP': 263, 'FP': 11045, 'TN': 119636, 'FN': 150, 'n_test_windows': 131094, 'covered_test_hours': 36.41}
                 F1(val)=0.1655
                 best_params={'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
                 Confusion matrix: [[59677  5640]
 [   62   139]]
                 Metrics results: {'model': 'rf_non_physiological_w1s1_3', 'sensitivity': 0.6915, 'specificity': np.float64(0.9137), 'precision': 0.0241, 'accuracy': 0.913, 'f1_score': 0.0465, 'auc_roc': 0.9042, 'false_alar_rate': np.float64(0.0863), 'fp_per_day': np.float64(7437.59), 'TP': 139, 'FP': 5640, 'TN': 59677, 'FN': 62, 'n_test_windows': 65518, 'covered_test_hours': 18.2}
                 F1(val)=0.1722
                 best_params={'n_estimators': 495, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
                 Confusion matrix: [[57913  6771]
 [   78   141]]
                 Metrics results: {'model': 'rf_non_physiological_w2s1_3', 'sensitivity': 0.6438, 'specificity': np.float64(0.8953), 'precision': 0.0204, 'accuracy': 0.8945, 'f1_score': 0.0395, 'auc_roc': 0.9056, 'false_alar_rate': np.float64(0.1047), 'fp_per_day': np.float64(4506.84), 'TP': 141, 'FP': 6771, 'TN': 57913, 'FN': 78, 'n_test_windows': 64903, 'covered_test_hours': 36.06}
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis>
```



