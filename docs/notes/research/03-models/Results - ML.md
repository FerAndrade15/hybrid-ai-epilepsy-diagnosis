
## A

``` bash
Loading all dataset for training...
  channel  start_time  stop_time label  confidence  ... Partition NoChannels  Duration                                                EDF                                                CSV
0  FP1-F7     22.9737    30.0688  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7    136.7987   140.1117  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7    145.0133   148.0498  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3     22.9737    30.0688  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3    136.7987   140.1117  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

[5 rows x 14 columns]
{'train': 4, 'test': 1}

==================================================
ARTIFACT: eye

==================================================
**************************************************
>> eye | windows: 2s (1s stride)
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\dataset\rf_dataset_eye_w2_s1_ua0.15_v1.parquet
[INFO] Split distribution:  split
train    137926
val       32679
test      30862
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w2s1_1_and_analysis_random.joblib
**************************************************
>> eye | windows: 1s (1s stride)
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\dataset\rf_dataset_eye_w1_s1_ua0.3_v1.parquet
[INFO] Split distribution:  split
train    137545
val       32694
test      30793
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w1s1_1_and_analysis_random.joblib
**************************************************
>> eye | windows: 1s (0.5s stride)
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\dataset\rf_dataset_eye_w1_s0.5_ua0.3_v1.parquet
[INFO] Split distribution:  split
train    275530
val       65429
test      61675
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w1s0.5_1_and_analysis_random.joblib
**************************************************
>> eye | windows: 0.5s (0.5s stride)
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\dataset\rf_dataset_eye_w0.5_s0.5_ua0.6_v1.parquet
[INFO] Split distribution:  split
train    275199
val       65430
test      61646
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w0.5s0.5_1_and_analysis_random.joblib
**************************************************
>> eye | windows: 0.5s (0.25s stride)
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\dataset\rf_dataset_eye_w0.5_s0.25_ua0.6_v1.parquet
[INFO] Split distribution:  split
train    549626
val      130872
test     123308
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w0.5s0.25_1_and_analysis_random.joblib

==================================================
ARTIFACT: muscle

==================================================
**************************************************
>> muscle | windows: 1s (0.5s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w1_s0.5_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (30890 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 30890 -> sin ambiguas: 30705 | positivas: 4097
['Patient', 'Session', 'Section', 'Start', 'muscle']

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
1.0             0.0303      0.1553    0.0758       0.1250     0.7610   0.1589    0.0802    0.0698          0.1948
0.7             0.0301      0.1695    0.0758       0.1394     0.6832   0.1589    0.1579    0.0168          0.1562
0.5             0.0241      0.1945    0.0698       0.1704     0.5907   0.1726    0.2366    0.1093          0.2797
0.3             0.0166      0.2312    0.0758       0.2147     0.4969   0.1589    0.3442    0.2031          0.4177
0.0             0.0157      0.2312    0.1385       0.2155     0.4969   0.0802    0.4229    0.2729          0.4884
[INFO] Best suggested size weight for muscle: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s0.5_sw0.7_ua0.3 parquet and json
[INFO] Saving patient asignation for muscle
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      4878         147        4731       0.030135
train    21104        3578       17526       0.169541
val       4908         372        4536       0.075795
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w1s0.5_1_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w1s0.5_1_and_analysis_random.joblib
**************************************************
>> muscle | windows: 1s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w1_s1_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (15445 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15445 -> sin ambiguas: 15328 | positivas: 2026
['Patient', 'Session', 'Section', 'Start', 'muscle']

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
0.0             0.0287      0.1677    0.0758        0.139     0.6832   0.1589    0.1579    0.0168          0.1558
0.3             0.0287      0.1677    0.0758        0.139     0.6832   0.1589    0.1579    0.0168          0.1558
0.5             0.0287      0.1677    0.0758        0.139     0.6832   0.1589    0.1579    0.0168          0.1558
0.7             0.0287      0.1677    0.0758        0.139     0.6832   0.1589    0.1579    0.0168          0.1558
1.0             0.0287      0.1677    0.0758        0.139     0.6832   0.1589    0.1579    0.0168          0.1558
[INFO] Best suggested size weight for muscle: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2439          70        2369       0.028700
train    10552        1770        8782       0.167741
val       2454         186        2268       0.075795
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w1s1_1_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w1s1_1_and_analysis_random.joblib
**************************************************
>> muscle | windows: 2s (1s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15427 -> sin ambiguas: 15279 | positivas: 2092
['Patient', 'Session', 'Section', 'Start', 'muscle']

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
0.0             0.0324       0.173    0.0772       0.1406     0.6833   0.1587     0.158    0.0167          0.1573
0.3             0.0324       0.173    0.0772       0.1406     0.6833   0.1587     0.158    0.0167          0.1573
0.5             0.0324       0.173    0.0772       0.1406     0.6833   0.1587     0.158    0.0167          0.1573
0.7             0.0324       0.173    0.0772       0.1406     0.6833   0.1587     0.158    0.0167          0.1573
1.0             0.0324       0.173    0.0772       0.1406     0.6833   0.1587     0.158    0.0167          0.1573
[INFO] Best suggested size weight for muscle: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w2_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2437          79        2358       0.032417
train    10542        1824        8718       0.173022
val       2448         189        2259       0.077206
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w2s1_1_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w2s1_1_and_analysis_random.joblib
**************************************************
>> muscle | windows: 5s (2s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 7690 -> sin ambiguas: 7614 | positivas: 1139
['Patient', 'Session', 'Section', 'Start', 'muscle']

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
0.0             0.0444      0.1869     0.084       0.1425     0.6839    0.158    0.1581    0.0161          0.1586
0.3             0.0444      0.1869     0.084       0.1425     0.6839    0.158    0.1581    0.0161          0.1586
0.5             0.0444      0.1869     0.084       0.1425     0.6839    0.158    0.1581    0.0161          0.1586
0.7             0.0444      0.1869     0.084       0.1425     0.6839    0.158    0.1581    0.0161          0.1586
1.0             0.0444      0.1869     0.084       0.1425     0.6839    0.158    0.1581    0.0161          0.1586
[INFO] Best suggested size weight for muscle: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w5_s2_sw0.0_ua0.2 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      1216          54        1162       0.044408
train     5259         983        4276       0.186918
val       1215         102        1113       0.083951
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          0.948            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w5s2_1_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w5s2_1_and_analysis_random.joblib

==================================================
ARTIFACT: non_physiological

==================================================
**************************************************
>> non_physiological | windows: 0.5s (0.25s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 61816 -> sin ambiguas: 61729 | positivas: 8320
['Patient', 'Session', 'Section', 'Start', 'non_physiological']

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
1.0             0.0231      0.1865    0.0222       0.1644     0.6831   0.1590    0.1579    0.0169          0.1812
0.7             0.0209      0.1941    0.0239       0.1732     0.6534   0.1727    0.1739    0.0466          0.2198
0.5             0.0145      0.2552    0.0164       0.2408     0.4969   0.2514    0.2517    0.2031          0.4439
0.3             0.0145      0.2552    0.0164       0.2408     0.4969   0.2514    0.2517    0.2031          0.4439
0.0             0.0110      0.2552    0.0239       0.2442     0.4969   0.1727    0.3304    0.2031          0.4473
[INFO] Best suggested size weight for non_physiological: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w0.5_s0.25_sw1.0_ua0.2 parquet and json
[INFO] Saving patient asignation for non_physiological
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      9760         225        9535       0.023053
train    42228        7877       34351       0.186535
val       9828         218        9610       0.022182
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_non_physiological_w0.5s0.25_1_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_non_physiological_w0.5s0.25_1_and_analysis_random.joblib
**************************************************
>> non_physiological | windows: 1s (0.5s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w1_s0.5_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (30890 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 30890 -> sin ambiguas: 30705 | positivas: 4159
['Patient', 'Session', 'Section', 'Start', 'non_physiological']

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
0.0             0.0232      0.1865    0.0226       0.1638     0.6832   0.1589    0.1579    0.0168          0.1806
0.3             0.0232      0.1865    0.0226       0.1638     0.6832   0.1589    0.1579    0.0168          0.1806
0.5             0.0232      0.1865    0.0226       0.1638     0.6832   0.1589    0.1579    0.0168          0.1806
0.7             0.0232      0.1865    0.0226       0.1638     0.6832   0.1589    0.1579    0.0168          0.1806
1.0             0.0232      0.1865    0.0226       0.1638     0.6832   0.1589    0.1579    0.0168          0.1806
[INFO] Best suggested size weight for non_physiological: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s0.5_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      4878         113        4765       0.023165
train    21104        3935       17169       0.186458
val       4908         111        4797       0.022616
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_non_physiological_w1s0.5_1_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_non_physiological_w1s0.5_1_and_analysis_random.joblib
**************************************************
>> non_physiological | windows: 1s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w1_s1_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (15445 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15445 -> sin ambiguas: 15328 | positivas: 2073
['Patient', 'Session', 'Section', 'Start', 'non_physiological']

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
0.0              0.023       0.186     0.022        0.164     0.6832   0.1589    0.1579    0.0168          0.1808
0.3              0.023       0.186     0.022        0.164     0.6832   0.1589    0.1579    0.0168          0.1808
0.5              0.023       0.186     0.022        0.164     0.6832   0.1589    0.1579    0.0168          0.1808
0.7              0.023       0.186     0.022        0.164     0.6832   0.1589    0.1579    0.0168          0.1808
1.0              0.023       0.186     0.022        0.164     0.6832   0.1589    0.1579    0.0168          0.1808
[INFO] Best suggested size weight for non_physiological: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2439          56        2383       0.022960
train    10552        1963        8589       0.186031
val       2454          54        2400       0.022005
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_non_physiological_w1s1_1_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_non_physiological_w1s1_1_and_analysis_random.joblib
**************************************************
>> non_physiological | windows: 2s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w2_s1_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (15427 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15427 -> sin ambiguas: 15279 | positivas: 2096
['Patient', 'Session', 'Section', 'Start', 'non_physiological']

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
0.0             0.0238      0.1877    0.0241       0.1639     0.6833   0.1587     0.158    0.0167          0.1806
0.3             0.0238      0.1877    0.0241       0.1639     0.6833   0.1587     0.158    0.0167          0.1806
0.5             0.0238      0.1877    0.0241       0.1639     0.6833   0.1587     0.158    0.0167          0.1806
0.7             0.0238      0.1877    0.0241       0.1639     0.6833   0.1587     0.158    0.0167          0.1806
1.0             0.0238      0.1877    0.0241       0.1639     0.6833   0.1587     0.158    0.0167          0.1806
[INFO] Best suggested size weight for non_physiological: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w2_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2437          58        2379       0.023800
train    10542        1979        8563       0.187725
val       2448          59        2389       0.024101
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_non_physiological_w2s1_1_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_non_physiological_w2s1_1_and_analysis_random.joblib

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Final report
---------- eye ----------
                 F1(val)=0.3727
                 best_params={'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
                 Confusion matrix: [[30667   160]
 [    7    28]]
                 Metrics results: {'model': 'rf_eye_w2s1_1', 'sensitivity': 0.8, 'specificity': np.float64(0.9948), 'precision': 0.1489, 'accuracy': 0.9946, 'f1_score': 0.2511, 'auc_roc': 0.9608, 'false_alar_rate': np.float64(0.0052), 'fp_per_day': np.float64(223.96), 'TP': 28, 'FP': 160, 'TN': 30667, 'FN': 7, 'n_test_windows': 30862, 'covered_test_hours': 17.15}
                 F1(val)=0.3158
                 best_params={'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
                 Confusion matrix: [[30479   289]
 [    6    19]]
                 Metrics results: {'model': 'rf_eye_w1s1_1', 'sensitivity': 0.76, 'specificity': np.float64(0.9906), 'precision': 0.0617, 'accuracy': 0.9904, 'f1_score': 0.1141, 'auc_roc': 0.9519, 'false_alar_rate': np.float64(0.0094), 'fp_per_day': np.float64(810.89), 'TP': 19, 'FP': 289, 'TN': 30479, 'FN': 6, 'n_test_windows': 30793, 'covered_test_hours': 8.55}
                 F1(val)=0.3295
                 best_params={'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
                 Confusion matrix: [[61077   543]
 [   17    38]]
                 Metrics results: {'model': 'rf_eye_w1s0.5_1', 'sensitivity': 0.6909, 'specificity': np.float64(0.9912), 'precision': 0.0654, 'accuracy': 0.9909, 'f1_score': 0.1195, 'auc_roc': 0.9528, 'false_alar_rate': np.float64(0.0088), 'fp_per_day': np.float64(760.68), 'TP': 38, 'FP': 543, 'TN': 61077, 'FN': 17, 'n_test_windows': 61675, 'covered_test_hours': 17.13}
                 F1(val)=0.2994
                 best_params={'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
                 Confusion matrix: [[60526  1075]
 [   16    29]]
                 Metrics results: {'model': 'rf_eye_w0.5s0.5_1', 'sensitivity': 0.6444, 'specificity': np.float64(0.9825), 'precision': 0.0263, 'accuracy': 0.9823, 'f1_score': 0.0505, 'auc_roc': 0.9469, 'false_alar_rate': np.float64(0.0175), 'fp_per_day': np.float64(3013.33), 'TP': 29, 'FP': 1075, 'TN': 60526, 'FN': 16, 'n_test_windows': 61646, 'covered_test_hours': 8.56}
                 F1(val)=0.2993
                 best_params={'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
                 Confusion matrix: [[120546   2672]
 [    24     66]]
                 Metrics results: {'model': 'rf_eye_w0.5s0.25_1', 'sensitivity': 0.7333, 'specificity': np.float64(0.9783), 'precision': 0.0241, 'accuracy': 0.9781, 'f1_score': 0.0467, 'auc_roc': 0.9507, 'false_alar_rate': np.float64(0.0217), 'fp_per_day': np.float64(3744.46), 'TP': 66, 'FP': 2672, 'TN': 120546, 'FN': 24, 'n_test_windows': 123308, 'covered_test_hours': 17.13}
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
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> uv run python -m pipelines.artifacts.ica_cnn_rf

Loading all dataset for training...
  channel  start_time  stop_time label  confidence  ... Partition NoChannels  Duration                                                EDF                                                CSV
0  FP1-F7     22.9737    30.0688  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7    136.7987   140.1117  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7    145.0133   148.0498  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3     22.9737    30.0688  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3    136.7987   140.1117  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

[5 rows x 14 columns]
<ArrowStringArray>
['aaaaaaju', 'aaaaaall', 'aaaaaarq', 'aaaaaayg', 'aaaaaayx', 'aaaaabbn',
 'aaaaabdo', 'aaaaabiw', 'aaaaabsk', 'aaaaabuv']
Length: 10, dtype: str
10
{'train': 4, 'test': 1}

==================================================
ARTIFACT: eye

==================================================
**************************************************
>> eye | windows: 2s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w2_s1_ua0.15_ub0.1_urTrue_dcd979_L1.parquet (15427 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15427 -> sin ambiguas: 15370 | positivas: 2002
['Patient', 'Session', 'Section', 'Start', 'eye']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.0_ua0.15 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.3_ua0.15 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.5_ua0.15 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.7_ua0.15 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw1.0_ua0.15 parquet and json

************************************************************

[INFO] Sweep size weight results for eye:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
1.0             0.0024      0.1517    0.0891       0.1493     0.7611   0.1587    0.0802    0.0698          0.2191
0.7             0.0131      0.1696    0.0891       0.1564     0.6686   0.1587    0.1727    0.0314          0.1878
0.5             0.0121      0.1892    0.0945       0.1771     0.5908   0.1577    0.2514    0.1092          0.2863
0.3             0.0140      0.2237    0.0806       0.2097     0.4970   0.1738    0.3292    0.2030          0.4127
0.0             0.0124      0.2237    0.1671       0.2113     0.4970   0.0799    0.4231    0.2731          0.4844
[INFO] Best suggested size weight for eye: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.7_ua0.15 parquet and json
[INFO] Saving patient asignation for eye
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2664          35        2629       0.013138
train    10315        1749        8566       0.169559
val       2448         218        2230       0.089052
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[INFO] Featured windows loaded from cache: featured_eye_w2_s1_bipFalse_icaTrue_23961c_v1.parquet (202191 rows)
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\pipelines\artifacts\ica_cnn_rf.py", line 241, in <module>
    rf_features_dataset = build_ml_dataset(featured_windows, target_artifact=artifact, output_path=rf_dataset_path)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\src\core\feature_extractor.py", line 357, in build_ml_dataset
    subset.to_parquet(output_path, index=False)
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\core\frame.py", line 3135, in to_parquet
    return to_parquet(
           ^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\io\parquet.py", line 490, in to_parquet
    impl.write(
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\io\parquet.py", line 199, in write
    path_or_handle, handles, filesystem = _get_path_or_handle(
                                          ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\io\parquet.py", line 141, in _get_path_or_handle
    handles = get_handle(
              ^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\io\common.py", line 935, in get_handle
    handle = open(handle, ioargs.mode)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument: "C:\\Users\\diseñoeinnovacion\\Documents\\MariaAndrade\\hybrid-ai-epilepsy-diagnosis\\outputs\\artifact\\dataset\\rf_dataset_eye_w2_s1_ua0.15_p<ArrowStringArray>\n['aaaaaaju', 'aaaaaall', 'aaaaaarq', 'aaaaaayg', 'aaaaaayx', 'aaaaabbn',\n 'aaaaabdo', 'aaaaabiw', 'aaaaabsk', 'aaaaabuv']\nLength: 10, dtype: str_v1.parquet"
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> uv run python -m pipelines.artifacts.ica_cnn_rf

Loading all dataset for training...
  channel  start_time  stop_time label  confidence  ... Partition NoChannels  Duration                                                EDF                                                CSV
0  FP1-F7     22.9737    30.0688  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7    136.7987   140.1117  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7    145.0133   148.0498  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3     22.9737    30.0688  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3    136.7987   140.1117  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

[5 rows x 14 columns]
<ArrowStringArray>
['aaaaaaju', 'aaaaaall', 'aaaaaarq', 'aaaaaayg', 'aaaaaayx', 'aaaaabbn',
 'aaaaabdo', 'aaaaabiw', 'aaaaabsk', 'aaaaabuv']
Length: 10, dtype: str
>> 10
{'train': 4, 'test': 1}

==================================================
ARTIFACT: eye

==================================================
**************************************************
>> eye | windows: 2s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w2_s1_ua0.15_ub0.1_urTrue_dcd979_L1.parquet (15427 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15427 -> sin ambiguas: 15370 | positivas: 2002
['Patient', 'Session', 'Section', 'Start', 'eye']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.0_ua0.15 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.3_ua0.15 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.5_ua0.15 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.7_ua0.15 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw1.0_ua0.15 parquet and json

************************************************************

[INFO] Sweep size weight results for eye:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
1.0             0.0024      0.1517    0.0891       0.1493     0.7611   0.1587    0.0802    0.0698          0.2191
0.7             0.0131      0.1696    0.0891       0.1564     0.6686   0.1587    0.1727    0.0314          0.1878
0.5             0.0121      0.1892    0.0945       0.1771     0.5908   0.1577    0.2514    0.1092          0.2863
0.3             0.0140      0.2237    0.0806       0.2097     0.4970   0.1738    0.3292    0.2030          0.4127
0.0             0.0124      0.2237    0.1671       0.2113     0.4970   0.0799    0.4231    0.2731          0.4844
[INFO] Best suggested size weight for eye: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.7_ua0.15 parquet and json
[INFO] Saving patient asignation for eye
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2664          35        2629       0.013138
train    10315        1749        8566       0.169559
val       2448         218        2230       0.089052
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[INFO] Featured windows loaded from cache: featured_eye_w2_s1_bipFalse_icaTrue_23961c_v1.parquet (202191 rows)
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\pipelines\artifacts\ica_cnn_rf.py", line 241, in <module>
    rf_features_dataset = build_ml_dataset(featured_windows, target_artifact=artifact, output_path=rf_dataset_path)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\src\core\feature_extractor.py", line 357, in build_ml_dataset
    subset.to_parquet(output_path, index=False)
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\core\frame.py", line 3135, in to_parquet
    return to_parquet(
           ^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\io\parquet.py", line 490, in to_parquet
    impl.write(
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\io\parquet.py", line 199, in write
    path_or_handle, handles, filesystem = _get_path_or_handle(
                                          ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\io\parquet.py", line 141, in _get_path_or_handle
    handles = get_handle(
              ^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\io\common.py", line 935, in get_handle
    handle = open(handle, ioargs.mode)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument: "C:\\Users\\diseñoeinnovacion\\Documents\\MariaAndrade\\hybrid-ai-epilepsy-diagnosis\\outputs\\artifact\\dataset\\rf_dataset_eye_w2_s1_ua0.15_p<ArrowStringArray>\n['aaaaaaju', 'aaaaaall', 'aaaaaarq', 'aaaaaayg', 'aaaaaayx', 'aaaaabbn',\n 'aaaaabdo', 'aaaaabiw', 'aaaaabsk', 'aaaaabuv']\nLength: 10, dtype: str_v1.parquet"
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> uv run python -m pipelines.artifacts.ica_cnn_rf

Loading all dataset for training...
  channel  start_time  stop_time label  confidence  ... Partition NoChannels  Duration                                                EDF                                                CSV
0  FP1-F7     22.9737    30.0688  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7    136.7987   140.1117  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7    145.0133   148.0498  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3     22.9737    30.0688  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3    136.7987   140.1117  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

[5 rows x 14 columns]
{'train': 4, 'test': 1}

==================================================
ARTIFACT: eye

==================================================
**************************************************
>> eye | windows: 2s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w2_s1_ua0.15_ub0.1_urTrue_dcd979_L1.parquet (15427 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15427 -> sin ambiguas: 15370 | positivas: 2002
['Patient', 'Session', 'Section', 'Start', 'eye']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.0_ua0.15 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.3_ua0.15 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.5_ua0.15 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.7_ua0.15 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw1.0_ua0.15 parquet and json

************************************************************

[INFO] Sweep size weight results for eye:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
1.0             0.0024      0.1517    0.0891       0.1493     0.7611   0.1587    0.0802    0.0698          0.2191
0.7             0.0131      0.1696    0.0891       0.1564     0.6686   0.1587    0.1727    0.0314          0.1878
0.5             0.0121      0.1892    0.0945       0.1771     0.5908   0.1577    0.2514    0.1092          0.2863
0.3             0.0140      0.2237    0.0806       0.2097     0.4970   0.1738    0.3292    0.2030          0.4127
0.0             0.0124      0.2237    0.1671       0.2113     0.4970   0.0799    0.4231    0.2731          0.4844
[INFO] Best suggested size weight for eye: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w2_s1_sw0.7_ua0.15 parquet and json
[INFO] Saving patient asignation for eye
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2664          35        2629       0.013138
train    10315        1749        8566       0.169559
val       2448         218        2230       0.089052
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[INFO] Featured windows loaded from cache: featured_eye_w2_s1_bipFalse_icaTrue_23961c_v1.parquet (202191 rows)
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    199465
1      2002
Name: count, dtype: int64
[INFO] Split distribution:  split
train    137926
val       32679
test      30862
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w2s1_1_and_analysis_random.joblib
Final report -------------------------
                  precision    recall  f1-score   support

no_rf_eye_w2s1_1       1.00      0.99      1.00     30827
   rf_eye_w2s1_1       0.15      0.80      0.25        35

        accuracy                           0.99     30862
       macro avg       0.57      0.90      0.62     30862
    weighted avg       1.00      0.99      1.00     30862

Confusion matrix -------------------------
[[30667   160]
 [    7    28]]
General metrics -------------------------
model                 rf_eye_w2s1_1
sensitivity                     0.8
specificity                  0.9948
precision                    0.1489
accuracy                     0.9946
f1_score                     0.2511
auc_roc                      0.9608
false_alar_rate              0.0052
fp_per_day                   223.96
TP                               28
FP                              160
TN                            30667
FN                                7
n_test_windows                30862
covered_test_hours            17.15
**************************************************
>> eye | windows: 1s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w1_s1_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (15445 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15445 -> sin ambiguas: 15328 | positivas: 1732
['Patient', 'Session', 'Section', 'Start', 'eye']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s1_sw0.0_ua0.3 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s1_sw0.3_ua0.3 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s1_sw0.5_ua0.3 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s1_sw0.7_ua0.3 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s1_sw1.0_ua0.3 parquet and json

************************************************************

[INFO] Sweep size weight results for eye:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0094      0.1452    0.0848       0.1358     0.6685   0.1589    0.1726    0.0315          0.1673
0.3             0.0094      0.1452    0.0848       0.1358     0.6685   0.1589    0.1726    0.0315          0.1673
0.5             0.0094      0.1452    0.0848       0.1358     0.6685   0.1589    0.1726    0.0315          0.1673
0.7             0.0094      0.1452    0.0848       0.1358     0.6685   0.1589    0.1726    0.0315          0.1673
1.0             0.0094      0.1452    0.0848       0.1358     0.6685   0.1589    0.1726    0.0315          0.1673
[INFO] Best suggested size weight for eye: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2666          25        2641       0.009377
train    10325        1499        8826       0.145182
val       2454         208        2246       0.084760
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[INFO] Featured windows loaded from cache: featured_eye_w1_s1_bipFalse_icaTrue_23961c_v1.parquet (202429 rows)
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    199300
1      1732
Name: count, dtype: int64
[INFO] Split distribution:  split
train    137545
val       32694
test      30793
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w1s1_1_and_analysis_random.joblib
Final report -------------------------
                  precision    recall  f1-score   support

no_rf_eye_w1s1_1       1.00      0.99      1.00     30768
   rf_eye_w1s1_1       0.06      0.76      0.11        25

        accuracy                           0.99     30793
       macro avg       0.53      0.88      0.55     30793
    weighted avg       1.00      0.99      0.99     30793

Confusion matrix -------------------------
[[30479   289]
 [    6    19]]
General metrics -------------------------
model                 rf_eye_w1s1_1
sensitivity                    0.76
specificity                  0.9906
precision                    0.0617
accuracy                     0.9904
f1_score                     0.1141
auc_roc                      0.9519
false_alar_rate              0.0094
fp_per_day                   810.89
TP                               19
FP                              289
TN                            30479
FN                                6
n_test_windows                30793
covered_test_hours             8.55
**************************************************
>> eye | windows: 1s (0.5s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w1_s0.5_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (30890 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 30890 -> sin ambiguas: 30705 | positivas: 3573
['Patient', 'Session', 'Section', 'Start', 'eye']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s0.5_sw0.0_ua0.3 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s0.5_sw0.3_ua0.3 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s0.5_sw0.5_ua0.3 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s0.5_sw0.7_ua0.3 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s0.5_sw1.0_ua0.3 parquet and json

************************************************************

[INFO] Sweep size weight results for eye:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0103      0.1503    0.0844         0.14     0.6685   0.1589    0.1726    0.0315          0.1715
0.3             0.0103      0.1503    0.0844         0.14     0.6685   0.1589    0.1726    0.0315          0.1715
0.5             0.0103      0.1503    0.0844         0.14     0.6685   0.1589    0.1726    0.0315          0.1715
0.7             0.0103      0.1503    0.0844         0.14     0.6685   0.1589    0.1726    0.0315          0.1715
1.0             0.0103      0.1503    0.0844         0.14     0.6685   0.1589    0.1726    0.0315          0.1715
[INFO] Best suggested size weight for eye: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s0.5_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      5332          55        5277       0.010315
train    20650        3104       17546       0.150315
val       4908         414        4494       0.084352
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[INFO] Featured windows loaded from cache: featured_eye_w1_s0.5_bipFalse_icaTrue_23961c_v1.parquet (404858 rows)
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    399061
1      3573
Name: count, dtype: int64
[INFO] Split distribution:  split
train    275530
val       65429
test      61675
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w1s0.5_1_and_analysis_random.joblib
Final report -------------------------
                    precision    recall  f1-score   support

no_rf_eye_w1s0.5_1       1.00      0.99      1.00     61620
   rf_eye_w1s0.5_1       0.07      0.69      0.12        55

          accuracy                           0.99     61675
         macro avg       0.53      0.84      0.56     61675
      weighted avg       1.00      0.99      0.99     61675

Confusion matrix -------------------------
[[61077   543]
 [   17    38]]
General metrics -------------------------
model                 rf_eye_w1s0.5_1
sensitivity                    0.6909
specificity                    0.9912
precision                      0.0654
accuracy                       0.9909
f1_score                       0.1195
auc_roc                        0.9528
false_alar_rate                0.0088
fp_per_day                     760.68
TP                                 38
FP                                543
TN                              61077
FN                                 17
n_test_windows                  61675
covered_test_hours              17.13
**************************************************
>> eye | windows: 0.5s (0.5s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w0.5_s0.5_ua0.6_ub0.1_urTrue_dcd979_L1.parquet (30908 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                    0.5     0.5  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                    0.5     0.5  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                    0.5     0.5  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                    0.5     0.5  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                    0.5     0.5  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 30908 -> sin ambiguas: 30672 | positivas: 3288
['Patient', 'Session', 'Section', 'Start', 'eye']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.5_sw0.0_ua0.6 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.5_sw0.3_ua0.6 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.5_sw0.5_ua0.6 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.5_sw0.7_ua0.6 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.5_sw1.0_ua0.6 parquet and json

************************************************************

[INFO] Sweep size weight results for eye:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0084      0.1375    0.0818       0.1291     0.6684    0.159    0.1726    0.0316          0.1606
0.3             0.0084      0.1375    0.0818       0.1291     0.6684    0.159    0.1726    0.0316          0.1606
0.5             0.0084      0.1375    0.0818       0.1291     0.6684    0.159    0.1726    0.0316          0.1606
0.7             0.0084      0.1375    0.0818       0.1291     0.6684    0.159    0.1726    0.0316          0.1606
1.0             0.0084      0.1375    0.0818       0.1291     0.6684    0.159    0.1726    0.0316          0.1606
[INFO] Best suggested size weight for eye: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.5_sw0.0_ua0.6 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      5334          45        5289       0.008436
train    20660        2841       17819       0.137512
val       4914         402        4512       0.081807
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                    0.5     0.5  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                    0.5     0.5  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                    0.5     0.5  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                    0.5     0.5  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                    0.5     0.5  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                    0.5     0.5  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                    0.5     0.5  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                    0.5     0.5  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                    0.5     0.5  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                    0.5     0.5  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[INFO] Featured windows loaded from cache: featured_eye_w0.5_s0.5_bipFalse_icaTrue_23961c_v1.parquet (405096 rows)
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    398987
1      3288
Name: count, dtype: int64
[INFO] Split distribution:  split
train    275199
val       65430
test      61646
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w0.5s0.5_1_and_analysis_random.joblib
Final report -------------------------
                      precision    recall  f1-score   support

no_rf_eye_w0.5s0.5_1       1.00      0.98      0.99     61601
   rf_eye_w0.5s0.5_1       0.03      0.64      0.05        45

            accuracy                           0.98     61646
           macro avg       0.51      0.81      0.52     61646
        weighted avg       1.00      0.98      0.99     61646

Confusion matrix -------------------------
[[60526  1075]
 [   16    29]]
General metrics -------------------------
model                 rf_eye_w0.5s0.5_1
sensitivity                      0.6444
specificity                      0.9825
precision                        0.0263
accuracy                         0.9823
f1_score                         0.0505
auc_roc                          0.9469
false_alar_rate                  0.0175
fp_per_day                      3013.33
TP                                   29
FP                                 1075
TN                                60526
FN                                   16
n_test_windows                    61646
covered_test_hours                 8.56
**************************************************
>> eye | windows: 0.5s (0.25s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w0.5_s0.25_ua0.6_ub0.1_urTrue_dcd979_L1.parquet (61816 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 61816 -> sin ambiguas: 61298 | positivas: 6528
['Patient', 'Session', 'Section', 'Start', 'eye']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.25_sw0.0_ua0.6 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.25_sw0.3_ua0.6 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.25_sw0.5_ua0.6 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.25_sw0.7_ua0.6 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.25_sw1.0_ua0.6 parquet and json

************************************************************

[INFO] Sweep size weight results for eye:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0084      0.1364    0.0818       0.1279     0.6684    0.159    0.1726    0.0316          0.1595
0.3             0.0084      0.1364    0.0818       0.1279     0.6684    0.159    0.1726    0.0316          0.1595
0.5             0.0084      0.1364    0.0818       0.1279     0.6684    0.159    0.1726    0.0316          0.1595
0.7             0.0084      0.1364    0.0818       0.1279     0.6684    0.159    0.1726    0.0316          0.1595
1.0             0.0084      0.1364    0.0818       0.1279     0.6684    0.159    0.1726    0.0316          0.1595
[INFO] Best suggested size weight for eye: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.25_sw0.0_ua0.6 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test     10668          90       10578       0.008436
train    41320        5634       35686       0.136350
val       9828         804        9024       0.081807
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[INFO] Featured windows loaded from cache: featured_eye_w0.5_s0.25_bipFalse_icaTrue_23961c_v1.parquet (810192 rows)
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    797278
1      6528
Name: count, dtype: int64
[INFO] Split distribution:  split
train    549626
val      130872
test     123308
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w0.5s0.25_1_and_analysis_random.joblib
Final report -------------------------
                       precision    recall  f1-score   support

no_rf_eye_w0.5s0.25_1       1.00      0.98      0.99    123218
   rf_eye_w0.5s0.25_1       0.02      0.73      0.05        90

             accuracy                           0.98    123308
            macro avg       0.51      0.86      0.52    123308
         weighted avg       1.00      0.98      0.99    123308

Confusion matrix -------------------------
[[120546   2672]
 [    24     66]]
General metrics -------------------------
model                 rf_eye_w0.5s0.25_1
sensitivity                       0.7333
specificity                       0.9783
precision                         0.0241
accuracy                          0.9781
f1_score                          0.0467
auc_roc                           0.9507
false_alar_rate                   0.0217
fp_per_day                       3744.46
TP                                    66
FP                                  2672
TN                                120546
FN                                    24
n_test_windows                    123308
covered_test_hours                 17.13

==================================================
ARTIFACT: muscle

==================================================
**************************************************
>> muscle | windows: 1s (0.5s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w1_s0.5_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (30890 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 30890 -> sin ambiguas: 30705 | positivas: 4097
['Patient', 'Session', 'Section', 'Start', 'muscle']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s0.5_sw0.0_ua0.3 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s0.5_sw0.3_ua0.3 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s0.5_sw0.5_ua0.3 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s0.5_sw0.7_ua0.3 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s0.5_sw1.0_ua0.3 parquet and json

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
1.0             0.0303      0.1553    0.0758       0.1250     0.7610   0.1589    0.0802    0.0698          0.1948
0.7             0.0301      0.1695    0.0758       0.1394     0.6832   0.1589    0.1579    0.0168          0.1562
0.5             0.0241      0.1945    0.0698       0.1704     0.5907   0.1726    0.2366    0.1093          0.2797
0.3             0.0166      0.2312    0.0758       0.2147     0.4969   0.1589    0.3442    0.2031          0.4177
0.0             0.0157      0.2312    0.1385       0.2155     0.4969   0.0802    0.4229    0.2729          0.4884
[INFO] Best suggested size weight for muscle: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s0.5_sw0.7_ua0.3 parquet and json
[INFO] Saving patient asignation for muscle
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      4878         147        4731       0.030135
train    21104        3578       17526       0.169541
val       4908         372        4536       0.075795
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[INFO] Featured windows loaded from cache: featured_muscle_w1_s0.5_bipFalse_icaTrue_23961c_v1.parquet (404858 rows)
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w1s0.5_1_and_analysis_random.joblib
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
**************************************************
>> muscle | windows: 1s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w1_s1_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (15445 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15445 -> sin ambiguas: 15328 | positivas: 2026
['Patient', 'Session', 'Section', 'Start', 'muscle']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s1_sw0.0_ua0.3 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s1_sw0.3_ua0.3 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s1_sw0.5_ua0.3 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s1_sw0.7_ua0.3 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s1_sw1.0_ua0.3 parquet and json

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0287      0.1677    0.0758        0.139     0.6832   0.1589    0.1579    0.0168          0.1558
0.3             0.0287      0.1677    0.0758        0.139     0.6832   0.1589    0.1579    0.0168          0.1558
0.5             0.0287      0.1677    0.0758        0.139     0.6832   0.1589    0.1579    0.0168          0.1558
0.7             0.0287      0.1677    0.0758        0.139     0.6832   0.1589    0.1579    0.0168          0.1558
1.0             0.0287      0.1677    0.0758        0.139     0.6832   0.1589    0.1579    0.0168          0.1558
[INFO] Best suggested size weight for muscle: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w1_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2439          70        2369       0.028700
train    10552        1770        8782       0.167741
val       2454         186        2268       0.075795
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[INFO] Featured windows loaded from cache: featured_muscle_w1_s1_bipFalse_icaTrue_23961c_v1.parquet (202429 rows)
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w1s1_1_and_analysis_random.joblib
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
**************************************************
>> muscle | windows: 2s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w2_s1_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (15427 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15427 -> sin ambiguas: 15279 | positivas: 2092
['Patient', 'Session', 'Section', 'Start', 'muscle']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w2_s1_sw0.0_ua0.3 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w2_s1_sw0.3_ua0.3 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w2_s1_sw0.5_ua0.3 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w2_s1_sw0.7_ua0.3 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w2_s1_sw1.0_ua0.3 parquet and json

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0324       0.173    0.0772       0.1406     0.6833   0.1587     0.158    0.0167          0.1573
0.3             0.0324       0.173    0.0772       0.1406     0.6833   0.1587     0.158    0.0167          0.1573
0.5             0.0324       0.173    0.0772       0.1406     0.6833   0.1587     0.158    0.0167          0.1573
0.7             0.0324       0.173    0.0772       0.1406     0.6833   0.1587     0.158    0.0167          0.1573
1.0             0.0324       0.173    0.0772       0.1406     0.6833   0.1587     0.158    0.0167          0.1573
[INFO] Best suggested size weight for muscle: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w2_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2437          79        2358       0.032417
train    10542        1824        8718       0.173022
val       2448         189        2259       0.077206
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[INFO] Featured windows loaded from cache: featured_muscle_w2_s1_bipFalse_icaTrue_23961c_v1.parquet (202191 rows)
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w2s1_1_and_analysis_random.joblib
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
**************************************************
>> muscle | windows: 5s (2s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w5_s2_ua0.2_ub0.1_urTrue_dcd979_L1.parquet (7690 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 7690 -> sin ambiguas: 7614 | positivas: 1139
['Patient', 'Session', 'Section', 'Start', 'muscle']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w5_s2_sw0.0_ua0.2 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w5_s2_sw0.3_ua0.2 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w5_s2_sw0.5_ua0.2 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w5_s2_sw0.7_ua0.2 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w5_s2_sw1.0_ua0.2 parquet and json

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0444      0.1869     0.084       0.1425     0.6839    0.158    0.1581    0.0161          0.1586
0.3             0.0444      0.1869     0.084       0.1425     0.6839    0.158    0.1581    0.0161          0.1586
0.5             0.0444      0.1869     0.084       0.1425     0.6839    0.158    0.1581    0.0161          0.1586
0.7             0.0444      0.1869     0.084       0.1425     0.6839    0.158    0.1581    0.0161          0.1586
1.0             0.0444      0.1869     0.084       0.1425     0.6839    0.158    0.1581    0.0161          0.1586
[INFO] Best suggested size weight for muscle: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_muscle_w5_s2_sw0.0_ua0.2 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      1216          54        1162       0.044408
train     5259         983        4276       0.186918
val       1215         102        1113       0.083951
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          0.948            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[INFO] Featured windows loaded from cache: featured_muscle_w5_s2_bipFalse_icaTrue_23961c_v1.parquet (100787 rows)
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w5s2_1_and_analysis_random.joblib
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

==================================================
ARTIFACT: non_physiological

==================================================
**************************************************
>> non_physiological | windows: 0.5s (0.25s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w0.5_s0.25_ua0.2_ub0.1_urTrue_dcd979_L1.parquet (61816 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 61816 -> sin ambiguas: 61729 | positivas: 8320
['Patient', 'Session', 'Section', 'Start', 'non_physiological']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w0.5_s0.25_sw0.0_ua0.2 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w0.5_s0.25_sw0.3_ua0.2 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w0.5_s0.25_sw0.5_ua0.2 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w0.5_s0.25_sw0.7_ua0.2 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w0.5_s0.25_sw1.0_ua0.2 parquet and json

************************************************************

[INFO] Sweep size weight results for non_physiological:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
1.0             0.0231      0.1865    0.0222       0.1644     0.6831   0.1590    0.1579    0.0169          0.1812
0.7             0.0209      0.1941    0.0239       0.1732     0.6534   0.1727    0.1739    0.0466          0.2198
0.5             0.0145      0.2552    0.0164       0.2408     0.4969   0.2514    0.2517    0.2031          0.4439
0.3             0.0145      0.2552    0.0164       0.2408     0.4969   0.2514    0.2517    0.2031          0.4439
0.0             0.0110      0.2552    0.0239       0.2442     0.4969   0.1727    0.3304    0.2031          0.4473
[INFO] Best suggested size weight for non_physiological: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w0.5_s0.25_sw1.0_ua0.2 parquet and json
[INFO] Saving patient asignation for non_physiological
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      9760         225        9535       0.023053
train    42228        7877       34351       0.186535
val       9828         218        9610       0.022182
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                    0.5    0.25  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[INFO] Featured windows loaded from cache: featured_non_physiological_w0.5_s0.25_bipFalse_icaTrue_23961c_v1.parquet (810192 rows)
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_non_physiological_w0.5s0.25_1_and_analysis_random.joblib
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
**************************************************
>> non_physiological | windows: 1s (0.5s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w1_s0.5_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (30890 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 30890 -> sin ambiguas: 30705 | positivas: 4159
['Patient', 'Session', 'Section', 'Start', 'non_physiological']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s0.5_sw0.0_ua0.3 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s0.5_sw0.3_ua0.3 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s0.5_sw0.5_ua0.3 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s0.5_sw0.7_ua0.3 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s0.5_sw1.0_ua0.3 parquet and json

************************************************************

[INFO] Sweep size weight results for non_physiological:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0232      0.1865    0.0226       0.1638     0.6832   0.1589    0.1579    0.0168          0.1806
0.3             0.0232      0.1865    0.0226       0.1638     0.6832   0.1589    0.1579    0.0168          0.1806
0.5             0.0232      0.1865    0.0226       0.1638     0.6832   0.1589    0.1579    0.0168          0.1806
0.7             0.0232      0.1865    0.0226       0.1638     0.6832   0.1589    0.1579    0.0168          0.1806
1.0             0.0232      0.1865    0.0226       0.1638     0.6832   0.1589    0.1579    0.0168          0.1806
[INFO] Best suggested size weight for non_physiological: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s0.5_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      4878         113        4765       0.023165
train    21104        3935       17169       0.186458
val       4908         111        4797       0.022616
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[INFO] Featured windows loaded from cache: featured_non_physiological_w1_s0.5_bipFalse_icaTrue_23961c_v1.parquet (404858 rows)
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_non_physiological_w1s0.5_1_and_analysis_random.joblib
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
**************************************************
>> non_physiological | windows: 1s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w1_s1_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (15445 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15445 -> sin ambiguas: 15328 | positivas: 2073
['Patient', 'Session', 'Section', 'Start', 'non_physiological']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s1_sw0.0_ua0.3 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s1_sw0.3_ua0.3 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s1_sw0.5_ua0.3 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s1_sw0.7_ua0.3 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s1_sw1.0_ua0.3 parquet and json

************************************************************

[INFO] Sweep size weight results for non_physiological:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0              0.023       0.186     0.022        0.164     0.6832   0.1589    0.1579    0.0168          0.1808
0.3              0.023       0.186     0.022        0.164     0.6832   0.1589    0.1579    0.0168          0.1808
0.5              0.023       0.186     0.022        0.164     0.6832   0.1589    0.1579    0.0168          0.1808
0.7              0.023       0.186     0.022        0.164     0.6832   0.1589    0.1579    0.0168          0.1808
1.0              0.023       0.186     0.022        0.164     0.6832   0.1589    0.1579    0.0168          0.1808
[INFO] Best suggested size weight for non_physiological: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w1_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2439          56        2383       0.022960
train    10552        1963        8589       0.186031
val       2454          54        2400       0.022005
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[INFO] Featured windows loaded from cache: featured_non_physiological_w1_s1_bipFalse_icaTrue_23961c_v1.parquet (202429 rows)
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_non_physiological_w1s1_1_and_analysis_random.joblib
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
**************************************************
>> non_physiological | windows: 2s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w2_s1_ua0.3_ub0.1_urTrue_dcd979_L1.parquet (15427 rows)
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15427 -> sin ambiguas: 15279 | positivas: 2096
['Patient', 'Session', 'Section', 'Start', 'non_physiological']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w2_s1_sw0.0_ua0.3 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w2_s1_sw0.3_ua0.3 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w2_s1_sw0.5_ua0.3 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w2_s1_sw0.7_ua0.3 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w2_s1_sw1.0_ua0.3 parquet and json

************************************************************

[INFO] Sweep size weight results for non_physiological:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.0238      0.1877    0.0241       0.1639     0.6833   0.1587     0.158    0.0167          0.1806
0.3             0.0238      0.1877    0.0241       0.1639     0.6833   0.1587     0.158    0.0167          0.1806
0.5             0.0238      0.1877    0.0241       0.1639     0.6833   0.1587     0.158    0.0167          0.1806
0.7             0.0238      0.1877    0.0241       0.1639     0.6833   0.1587     0.158    0.0167          0.1806
1.0             0.0238      0.1877    0.0241       0.1639     0.6833   0.1587     0.158    0.0167          0.1806
[INFO] Best suggested size weight for non_physiological: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_non_physiological_w2_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2437          58        2379       0.023800
train    10542        1979        8563       0.187725
val       2448          59        2389       0.024101
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[INFO] Featured windows loaded from cache: featured_non_physiological_w2_s1_bipFalse_icaTrue_23961c_v1.parquet (202191 rows)
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

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
[INFO] Pretrained model found, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_non_physiological_w2s1_1_and_analysis_random.joblib
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

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Final report
---------- eye ----------
                 F1(val)=0.3727
                 best_params={'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
                 Confusion matrix: [[30667   160]
 [    7    28]]
                 Metrics results: {'model': 'rf_eye_w2s1_1', 'sensitivity': 0.8, 'specificity': np.float64(0.9948), 'precision': 0.1489, 'accuracy': 0.9946, 'f1_score': 0.2511, 'auc_roc': 0.9608, 'false_alar_rate': np.float64(0.0052), 'fp_per_day': np.float64(223.96), 'TP': 28, 'FP': 160, 'TN': 30667, 'FN': 7, 'n_test_windows': 30862, 'covered_test_hours': 17.15}
                 F1(val)=0.3158
                 best_params={'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
                 Confusion matrix: [[30479   289]
 [    6    19]]
                 Metrics results: {'model': 'rf_eye_w1s1_1', 'sensitivity': 0.76, 'specificity': np.float64(0.9906), 'precision': 0.0617, 'accuracy': 0.9904, 'f1_score': 0.1141, 'auc_roc': 0.9519, 'false_alar_rate': np.float64(0.0094), 'fp_per_day': np.float64(810.89), 'TP': 19, 'FP': 289, 'TN': 30479, 'FN': 6, 'n_test_windows': 30793, 'covered_test_hours': 8.55}
                 F1(val)=0.3295
                 best_params={'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
                 Confusion matrix: [[61077   543]
 [   17    38]]
                 Metrics results: {'model': 'rf_eye_w1s0.5_1', 'sensitivity': 0.6909, 'specificity': np.float64(0.9912), 'precision': 0.0654, 'accuracy': 0.9909, 'f1_score': 0.1195, 'auc_roc': 0.9528, 'false_alar_rate': np.float64(0.0088), 'fp_per_day': np.float64(760.68), 'TP': 38, 'FP': 543, 'TN': 61077, 'FN': 17, 'n_test_windows': 61675, 'covered_test_hours': 17.13}
                 F1(val)=0.2994
                 best_params={'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
                 Confusion matrix: [[60526  1075]
 [   16    29]]
                 Metrics results: {'model': 'rf_eye_w0.5s0.5_1', 'sensitivity': 0.6444, 'specificity': np.float64(0.9825), 'precision': 0.0263, 'accuracy': 0.9823, 'f1_score': 0.0505, 'auc_roc': 0.9469, 'false_alar_rate': np.float64(0.0175), 'fp_per_day': np.float64(3013.33), 'TP': 29, 'FP': 1075, 'TN': 60526, 'FN': 16, 'n_test_windows': 61646, 'covered_test_hours': 8.56}
                 F1(val)=0.2993
                 best_params={'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
                 Confusion matrix: [[120546   2672]
 [    24     66]]
                 Metrics results: {'model': 'rf_eye_w0.5s0.25_1', 'sensitivity': 0.7333, 'specificity': np.float64(0.9783), 'precision': 0.0241, 'accuracy': 0.9781, 'f1_score': 0.0467, 'auc_roc': 0.9507, 'false_alar_rate': np.float64(0.0217), 'fp_per_day': np.float64(3744.46), 'TP': 66, 'FP': 2672, 'TN': 120546, 'FN': 24, 'n_test_windows': 123308, 'covered_test_hours': 17.13}
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
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> uv run python -m pipelines.artifacts.ica_cnn_rf

Loading all dataset for training...
  channel  start_time  stop_time label  confidence  ... Partition NoChannels  Duration                                                EDF                                                CSV
0  FP1-F7     22.9737    30.0688  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7    136.7987   140.1117  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7    145.0133   148.0498  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3     22.9737    30.0688  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3    136.7987   140.1117  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

[5 rows x 14 columns]
{'train': 13, 'test': 3}

==================================================
ARTIFACT: eye

==================================================
**************************************************
>> eye | windows: 5s (2s stride)

************************************************************
Generating windows...
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\pipelines\artifacts\ica_cnn_rf.py", line 129, in <module>
    windowed_annotations_corpus_patient = get_or_build_windows(annotations_df=database_corpus_patient,
                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\src\core\windowing.py", line 289, in get_or_build_windows
    w = label_windowing(annotations_df, window, taxonomy, unreviewed_tokens=unreviewed_tokens,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\src\core\windowing.py", line 130, in label_windowing
    matching_rows = overlapping[overlapping["label"]==span["label"]]
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\core\ops\common.py", line 85, in new_method
    return method(self, other)
           ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\core\arraylike.py", line 42, in __eq__
    return self._cmp_method(other, operator.eq)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\core\series.py", line 6735, in _cmp_method
    res_values = ops.comparison_op(lvalues, rvalues, op)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\core\ops\array_ops.py", line 341, in comparison_op
    res_values = op(lvalues, rvalues)
                 ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\core\ops\common.py", line 85, in new_method
    return method(self, other)
           ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\core\arraylike.py", line 42, in __eq__
    return self._cmp_method(other, operator.eq)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\core\arrays\string_arrow.py", line 588, in _cmp_method
    result = super()._cmp_method(other, op)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\core\arrays\arrow\array.py", line 944, in _cmp_method
    result = pc_func(self._pa_array, self._box_pa(other))
                                     ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\core\arrays\arrow\array.py", line 527, in _box_pa
    return cls._box_pa_scalar(value, pa_type)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pandas\core\arrays\string_arrow.py", line 173, in _box_pa_scalar
    pa_scalar = pc.cast(pa_scalar, pa.large_string())
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\pyarrow\compute.py", line 414, in cast
    return call_function("cast", [arr], options, memory_pool)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> uv run python -m pipelines.artifacts.ica_cnn_rf

Loading all dataset for training...
  channel  start_time  stop_time label  confidence  ... Partition NoChannels  Duration                                                EDF                                                CSV
0  FP1-F7     22.9737    30.0688  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7    136.7987   140.1117  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7    145.0133   148.0498  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3     22.9737    30.0688  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3    136.7987   140.1117  eyem         1.0  ...                   36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

[5 rows x 14 columns]
{'train': 13, 'test': 3}

==================================================
ARTIFACT: eye

==================================================
**************************************************
>> eye | windows: 5s (2s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 38834 -> sin ambiguas: 38778 | positivas: 11340
['Patient', 'Session', 'Section', 'Start', 'eye']

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_eye_w5_s2_sw0.0_ua0.1
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_eye_w5_s2_sw0.3_ua0.1
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_eye_w5_s2_sw0.5_ua0.1
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_eye_w5_s2_sw0.7_ua0.1
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_eye_w5_s2_sw1.0_ua0.1

************************************************************

[INFO] Sweep size weight results for eye:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.2357      0.2988    0.3371       0.1014     0.6841   0.1299    0.1860    0.0360          0.1374
0.3             0.2477      0.2873    0.3788       0.1311     0.7087   0.1241    0.1673    0.0259          0.1570
0.5             0.2622      0.2702    0.4801       0.2179     0.7312   0.1101    0.1587    0.0399          0.2578
0.7             0.2548      0.2674    0.4767       0.2218     0.7173   0.1270    0.1557    0.0230          0.2449
1.0             0.2233      0.2631    0.4929       0.2696     0.6997   0.1517    0.1487    0.0017          0.2713
[INFO] Best suggested size weight for eye: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p50_v2_eye_w5_s2_sw0.0_ua0.1 parquet and json
[INFO] Saving patient asignation for eye
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      7222        1702        5520       0.235669
train    26566        7937       18629       0.298765
val       5046        1701        3345       0.337099
Broken rules: 0 | splits per patient: {'train': 33, 'test': 10, 'val': 7}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          1.000            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      5       2  ...          0.948            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[WARN] ICA failed for aaaaaimu_s008_t000: One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
[SKIP] Session aaaaaimu_s008_t000 discarted by ICA error One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    479070
1     11312
Name: count, dtype: int64
[INFO] Split distribution:  split
train    342499
test      84801
val       63082
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye

============================================================
Modelo: rf_eye_w5s2_2
Train: 342499 (pos=7909) | Val: 63082 (pos = 1701) | Test: 84801 (pos=1702)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.4894548348587346
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.48266925817946227
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.25881851560451086
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.49183286706975904
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.3872224594363792
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.4593344955658304
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.4446734889199735
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.4467709771437337
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.4221950057834932
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.44066695539194456
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.47587948450017414
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.41538667022839587
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.46662125340599453
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.4347517730496454
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.35583851544763595
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.49853624935422763
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.3955839168737294
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.4563758389261745
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.38582635145952293
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.4168650321352059
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.404405181161583
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.48906907523350096
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.4610480485150054
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.44457443696987425
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.4756441013872953
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.3265450996051289
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.43423182489971146
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.4279963041182682
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.4310637431267395
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.38361437943935367
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.45771224886584577
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.4091787156822572
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.42132914847161573
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.4311708860759494
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.22697868031726387
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.34639969919157737
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.465544020273032
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2506110529155953
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.40971526263043095
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.37588451740730255
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.45265908392253307
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.47041577825159914
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.2031003996608938
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.40216972653742455
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 27, 'min_samples_leaf': 8, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.3677277716794731
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.2448283281591
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 9, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.4709427851745232
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 22, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.4091737545565006
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 28, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.382039740915578
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 13, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.2368085043204561
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.39462245404868357
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 24, 'min_samples_leaf': 14, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.42181199596774194
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 11, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.4441994451952486
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 23, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.4630217425805428
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.25623449536493015
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 22, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.4083646906421566
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 25, 'min_samples_leaf': 9, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.3866394587047578
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.37663188944119735
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.4791733163102458
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 12, 'min_samples_leaf': 10, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.4123417721518987
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.4985 | fp_per_day_val(val)=1000.3893 <- choosen
        adjusted: threshold=0.5772 | F2(val)=0.5121 | fp_per_day_val(val)=748.1006
[INFO] Best configuration found with validation: {'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 0.5, 'sampling_strategy': 0.3} | F1(val)=0.4985
Final report -------------------------
                  precision    recall  f1-score   support

no_rf_eye_w5s2_2       0.99      0.97      0.98     83099
   rf_eye_w5s2_2       0.33      0.75      0.46      1702

        accuracy                           0.96     84801
       macro avg       0.66      0.86      0.72     84801
    weighted avg       0.98      0.96      0.97     84801

Confusion matrix -------------------------
[[80525  2574]
 [  432  1270]]
General metrics -------------------------
model                 rf_eye_w5s2_2
sensitivity                  0.7462
specificity                   0.969
precision                    0.3304
accuracy                     0.9646
f1_score                      0.458
auc_roc                      0.9423
false_alar_rate               0.031
fp_per_day                   524.51
TP                             1270
FP                             2574
TN                            80525
FN                              432
n_test_windows                84801
covered_test_hours           117.78
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w5s2_2_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w5s2_2_and_analysis_random.joblib
**************************************************
>> eye | windows: 2s (1s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 77870 -> sin ambiguas: 77421 | positivas: 19147
['Patient', 'Session', 'Section', 'Start', 'eye']

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_eye_w2_s1_sw0.0_ua0.15
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_eye_w2_s1_sw0.3_ua0.15
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_eye_w2_s1_sw0.5_ua0.15
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_eye_w2_s1_sw0.7_ua0.15
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_eye_w2_s1_sw1.0_ua0.15

************************************************************

[INFO] Sweep size weight results for eye:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.1994      0.2517    0.2818       0.0825     0.6841   0.1299    0.1861    0.0361          0.1185
0.3             0.1994      0.2517    0.2818       0.0825     0.6841   0.1299    0.1861    0.0361          0.1185
0.5             0.1994      0.2517    0.2818       0.0825     0.6841   0.1299    0.1861    0.0361          0.1185
0.7             0.1994      0.2517    0.2818       0.0825     0.6841   0.1299    0.1861    0.0361          0.1185
1.0             0.1994      0.2517    0.2818       0.0825     0.6841   0.1299    0.1861    0.0361          0.1185
[INFO] Best suggested size weight for eye: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p50_v2_eye_w2_s1_sw0.0_ua0.15 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test     14489        2889       11600       0.199393
train    53269       13408       39861       0.251704
val      10112        2850        7262       0.281843
Broken rules: 0 | splits per patient: {'train': 33, 'test': 10, 'val': 7}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[WARN] ICA failed for aaaaaimu_s008_t000: One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
[SKIP] Session aaaaaimu_s008_t000 discarted by ICA error One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    959906
1     19109
Name: count, dtype: int64
[INFO] Split distribution:  split
train    683723
test     169331
val      125961
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye

============================================================
Modelo: rf_eye_w2s1_2
Train: 683723 (pos=13370) | Val: 125961 (pos = 2850) | Test: 169331 (pos=2889)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.4912531631642645
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.46801548529818415
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.22436420619633704
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.49882147981143676
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.2909766654121189
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.43637629520416105
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.441384474581912
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.4265682957648881
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.39665546900956106
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.4290876242095754
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.4683155275867115
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.4153565467179069
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.4487690504103165
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.39849268186121023
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.28618189257381854
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.47214854111405835
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.31492361927144535
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.4334028671608007
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.29411764705882354
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.33194424486276763
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.34838076545632973
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.49103306021887355
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.4578940403193789
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.42594029485032875
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.49789251844046367
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.2504898119122257
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.4172104243287065
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.41265804121051275
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.4013291489754477
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.2924635727731171
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.4607438952566484
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.3789376355056753
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.3876317588228946
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.41650417284143204
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.19192664562237802
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.2738542288981821
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.4320289034954077
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.21526144452578622
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.3343512313738796
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.3204663356947621
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.4229682566062822
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.46053926392442435
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.16053360465773558
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.3735998621402723
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 27, 'min_samples_leaf': 8, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2751536473603058
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.20789833410944705
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 9, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.4636031883222895
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 22, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.35777736935612325
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 28, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.3366062710209396
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 13, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.20271061413266203
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.3826288605460103
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 24, 'min_samples_leaf': 14, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.36814352774741177
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 11, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.43045045758884354
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 23, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.4350503673074385
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.21043600343186958
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 22, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.3725126528559303
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 25, 'min_samples_leaf': 9, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.32507780766999
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.3228389875013129
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.46046974702448296
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 12, 'min_samples_leaf': 10, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.38406921832171986
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.4988 | fp_per_day_val(val)=2115.7406 <- choosen
        adjusted: threshold=0.5797 | F2(val)=0.5061 | fp_per_day_val(val)=1477.4859
[INFO] Best configuration found with validation: {'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.3} | F1(val)=0.4988
Final report -------------------------
                  precision    recall  f1-score   support

no_rf_eye_w2s1_2       1.00      0.97      0.98    166442
   rf_eye_w2s1_2       0.33      0.75      0.46      2889

        accuracy                           0.97    169331
       macro avg       0.66      0.86      0.72    169331
    weighted avg       0.98      0.97      0.98    169331

Confusion matrix -------------------------
[[162027   4415]
 [   708   2181]]
General metrics -------------------------
model                 rf_eye_w2s1_2
sensitivity                  0.7549
specificity                  0.9735
precision                    0.3307
accuracy                     0.9697
f1_score                     0.4599
auc_roc                      0.9667
false_alar_rate              0.0265
fp_per_day                  1126.36
TP                             2181
FP                             4415
TN                           162027
FN                              708
n_test_windows               169331
covered_test_hours            94.07
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w2s1_2_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w2s1_2_and_analysis_random.joblib

==================================================
ARTIFACT: muscle

==================================================
**************************************************
>> muscle | windows: 1s (0.5s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 155890 -> sin ambiguas: 154307 | positivas: 34169
['Patient', 'Session', 'Section', 'Start', 'muscle']

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w1_s0.5_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w1_s0.5_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w1_s0.5_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w1_s0.5_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w1_s0.5_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.3             0.1760      0.2185    0.2838       0.1078     0.7069   0.1217    0.1713    0.0283          0.1361
0.0             0.1485      0.2577    0.1794       0.1092     0.5955   0.1832    0.2213    0.1045          0.2137
0.5             0.1775      0.2064    0.3594       0.1820     0.7199   0.1149    0.1652    0.0351          0.2171
0.7             0.2032      0.1904    0.4197       0.2292     0.7392   0.1174    0.1434    0.0392          0.2685
1.0             0.1131      0.1934    0.4535       0.3404     0.7077   0.1447    0.1476    0.0077          0.3481
[INFO] Best suggested size weight for muscle: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p50_v2_muscle_w1_s0.5_sw0.3_ua0.3 parquet and json
[INFO] Saving patient asignation for muscle
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test     26710        4702       22008       0.176039
train   110204       24081       86123       0.218513
val      18976        5386       13590       0.283832
Broken rules: 0 | splits per patient: {'train': 33, 'test': 9, 'val': 8}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[WARN] ICA failed for aaaaaimu_s008_t000: One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
[SKIP] Session aaaaaimu_s008_t000 discarted by ICA error One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    1917572
1      34022
Name: count, dtype: int64
[INFO] Split distribution:  split
train    1384774
test      317303
val       249517
Name: count, dtype: int64

==================================================
Starting training of Random Forest - muscle

============================================================
Modelo: rf_muscle_w1s0.5_2
Train: 1384774 (pos=23934) | Val: 249517 (pos = 5386) | Test: 317303 (pos=4702)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.38469012790615503
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.28202911419024695
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.11720924524084002
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.3925054948982327
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.14768440260161875
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.22869947102301813
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.2967432235710247
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.21099361940879194
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.20528035844769024
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.2199452958798246
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2951064855444174
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.25888993805318916
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.25769860898058
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.1749151593138072
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.13435778193398373
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.3000024932681759
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.15129115205623658
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.24136354350089015
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.14818417457113459
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.1650355199516324
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.162991490154668
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.3945568563358263
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.33044306545826385
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.2157200863050237
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.3667540086682817
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1324110671936759
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.21554980265670756
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.2691936390736556
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.19090477743839152
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.14609332759552893
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.2983827003452662
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.18047605320594653
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.18742699756298037
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.20159038013964314
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.11355156037991859
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.1298067300322686
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.22762810258990995
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.1160015275921329
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.16092369527123898
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.154293997851974
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.2268716120085724
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2655335201317037
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.11117684046795624
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.17677092573657374
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.13913715511440108
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.11494549109559032
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.26122789244860917
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.16195748232521603
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1380979424683086
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.11464826357969723
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.19972983404091085
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.17963948497854076
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.2780643714253673
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.2389042664884986
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.11806595041761513
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.15585964953726397
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.14366429349918394
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.13856144377216775
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.25592783505154637
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.16705930035210376
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.3946 | fp_per_day_val(val)=10493.6818 <- choosen
        adjusted: threshold=0.6359 | F2(val)=0.4344 | fp_per_day_val(val)=5513.2949
[INFO] Best configuration found with validation: {'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3} | F1(val)=0.3946
Final report -------------------------
                       precision    recall  f1-score   support

no_rf_muscle_w1s0.5_2       0.99      0.90      0.95    312601
   rf_muscle_w1s0.5_2       0.08      0.56      0.14      4702

             accuracy                           0.90    317303
            macro avg       0.54      0.73      0.54    317303
         weighted avg       0.98      0.90      0.93    317303

Confusion matrix -------------------------
[[282112  30489]
 [  2069   2633]]
General metrics -------------------------
model                 rf_muscle_w1s0.5_2
sensitivity                         0.56
specificity                       0.9025
precision                         0.0795
accuracy                          0.8974
f1_score                          0.1392
auc_roc                           0.8932
false_alar_rate                   0.0975
fp_per_day                        8302.0
TP                                  2633
FP                                 30489
TN                                282112
FN                                  2069
n_test_windows                    317303
covered_test_hours                 88.14
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w1s0.5_2_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w1s0.5_2_and_analysis_random.joblib
**************************************************
>> muscle | windows: 1s (1s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 77945 -> sin ambiguas: 77039 | positivas: 16986
['Patient', 'Session', 'Section', 'Start', 'muscle']

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w1_s1_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w1_s1_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w1_s1_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w1_s1_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w1_s1_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.1757      0.2172    0.2816        0.106     0.7069   0.1217    0.1713    0.0283          0.1342
0.3             0.1757      0.2172    0.2816        0.106     0.7069   0.1217    0.1713    0.0283          0.1342
0.5             0.1757      0.2172    0.2816        0.106     0.7069   0.1217    0.1713    0.0283          0.1342
0.7             0.1757      0.2172    0.2816        0.106     0.7069   0.1217    0.1713    0.0283          0.1342
1.0             0.1757      0.2172    0.2816        0.106     0.7069   0.1217    0.1713    0.0283          0.1342
[INFO] Best suggested size weight for muscle: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p50_v2_muscle_w1_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test     13355        2346       11009       0.175665
train    55102       11968       43134       0.217197
val       9488        2672        6816       0.281619
Broken rules: 0 | splits per patient: {'train': 33, 'test': 9, 'val': 8}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1       1  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[WARN] ICA failed for aaaaaimu_s008_t000: One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
[SKIP] Session aaaaaimu_s008_t000 discarted by ICA error One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    957447
1     16913
Name: count, dtype: int64
[INFO] Split distribution:  split
train    691479
test     158576
val      124305
Name: count, dtype: int64

==================================================
Starting training of Random Forest - muscle

============================================================
Modelo: rf_muscle_w1s1_2
Train: 691479 (pos=11895) | Val: 124305 (pos = 2672) | Test: 158576 (pos=2346)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.38500197436909933
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2848855033841945
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.11769512964229563
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.3915855305237723
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.15006782076924846
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.23301202169769827
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.2998174071819842
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2087499390333122
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.1928657799274486
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.21520778977166147
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.29346982704678
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.25573873121869783
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2518922438349475
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.17318376352375128
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1367580809234155
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.2946454911987413
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.14978651117946834
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.23590541027440123
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.15036035828593797
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.16852695913399285
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.15876893014167073
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.3866144535421858
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.3284001446574123
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.21716229751666494
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.3691576357954923
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.13308389608809393
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.20772122187022962
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.2628579717352563
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.18599878602190942
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.14898851831601967
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.30435108402437805
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.18119164072921298
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1779437912640763
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.20045391658505496
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.11370633916048031
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.12968129838487838
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.21625671765192228
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.1163300948719974
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.15965932798272095
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.15270265513721534
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.21698014991671294
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2614888528230973
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.11140279740157678
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.16896038440446035
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.14027294621354028
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1148028676934785
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2691115361783524
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.16097345350065076
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1368238146271421
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.11463023340061067
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.19408907126908453
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.18330154693791056
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.2739606126914661
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.23750524188936753
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.11878321389071225
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.15047997427889032
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.1435832968954963
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.140834535449057
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.24742288636726867
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.1663845869971877
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.3916 | fp_per_day_val(val)=10599.7345 <- choosen
        adjusted: threshold=0.6276 | F2(val)=0.4417 | fp_per_day_val(val)=5661.3008
[INFO] Best configuration found with validation: {'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3} | F1(val)=0.3916
Final report -------------------------
                     precision    recall  f1-score   support

no_rf_muscle_w1s1_2       0.99      0.91      0.95    156230
   rf_muscle_w1s1_2       0.08      0.55      0.14      2346

           accuracy                           0.90    158576
          macro avg       0.54      0.73      0.54    158576
       weighted avg       0.98      0.90      0.94    158576

Confusion matrix -------------------------
[[141599  14631]
 [  1046   1300]]
General metrics -------------------------
model                 rf_muscle_w1s1_2
sensitivity                     0.5541
specificity                     0.9063
precision                       0.0816
accuracy                        0.9011
f1_score                        0.1423
auc_roc                          0.893
false_alar_rate                 0.0937
fp_per_day                     7971.69
TP                                1300
FP                               14631
TN                              141599
FN                                1046
n_test_windows                  158576
covered_test_hours               44.05
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w1s1_2_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_muscle_w1s1_2_and_analysis_random.joblib
**************************************************
>> muscle | windows: 2s (1s stride)

************************************************************
Generating windows...
    Patient Session Section    Montage Partition  Window_size  stride  ...  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 77870 -> sin ambiguas: 76296 | positivas: 17374
['Patient', 'Session', 'Section', 'Start', 'muscle']

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w2_s1_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w2_s1_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w2_s1_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w2_s1_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w2_s1_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0             0.1797      0.2219    0.2914       0.1117      0.707   0.1217    0.1713    0.0283            0.14
0.3             0.1797      0.2219    0.2914       0.1117      0.707   0.1217    0.1713    0.0283            0.14
0.5             0.1797      0.2219    0.2914       0.1117      0.707   0.1217    0.1713    0.0283            0.14
0.7             0.1797      0.2219    0.2914       0.1117      0.707   0.1217    0.1713    0.0283            0.14
1.0             0.1797      0.2219    0.2914       0.1117      0.707   0.1217    0.1713    0.0283            0.14
[INFO] Best suggested size weight for muscle: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p50_v2_muscle_w2_s1_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test     13340        2397       10943       0.179685
train    55051       12215       42836       0.221885
val       9479        2762        6717       0.291381
Broken rules: 0 | splits per patient: {'train': 33, 'test': 9, 'val': 8}
    Patient Session Section    Montage Partition  Window_size  stride  ...  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      2       1  ...            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[WARN] ICA failed for aaaaaimu_s008_t000: One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
[SKIP] Session aaaaaimu_s008_t000 discarted by ICA error One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
3          3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
6          6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
7          7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
9          9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
10        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  ...                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  ...                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  ...                                    []                    []                       []                                  []
16         4        brain           clean         0.999643  ...                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  ...                                    []                    []                       []                                  []
18         6        brain           clean         0.999535  ...                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  ...                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  ...                                    []                    []                       []                                  []
21         9        brain           clean         0.773097  ...                                    []                    []                       []                                  []
22        10        brain           clean         0.919012  ...                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  ...                                    []                    []                       []                                  []
24         0        brain           clean         0.687185  ...                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob  ...  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185  ...                    []                       []                                  []            0
1         1    eye blink             eye         0.949668  ...                    []                       []                                  []            0
2         2        brain           clean         0.994398  ...                    []                       []                                  []            0
3         3        other             NaN         0.726641  ...                    []                       []                                  []            0
4         4        brain           clean         0.999643  ...                    []                       []                                  []            0

[5 rows x 133 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_FP1', 'ic_contrib_F3', 'ic_contrib_C3', 'ic_contrib_P3', 'ic_contrib_FP2', 'ic_contrib_F4', 'ic_contrib_C4', 'ic_contrib_P4', 'ic_contrib_F7', 'ic_contrib_T7', 'ic_contrib_P7', 'ic_contrib_F8', 'ic_contrib_T8', 'ic_contrib_P8', 'ic_contrib_FZ', 'ic_contrib_CZ', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_PZ', 'FP1_variance', 'FP1_line_length', 'FP1_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'FP2_variance', 'FP2_line_length', 'FP2_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'FZ_variance', 'FZ_line_length', 'FZ_peak_to_peak', 'CZ_variance', 'CZ_line_length', 'CZ_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'PZ_variance', 'PZ_line_length', 'PZ_peak_to_peak', 'Patient', 'Session', 'Section', 'Partition', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'monopolar_channels_eye', 'monopolar_channels_muscle', 'monopolar_channels_non_physiological', 'bipolar_channels_eye', 'bipolar_channels_muscle', 'bipolar_channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    947652
1     17294
Name: count, dtype: int64
[INFO] Split distribution:  split
train    685044
test     156725
val      123177
Name: count, dtype: int64

==================================================
Starting training of Random Forest - muscle

============================================================
Modelo: rf_muscle_w2s1_2
Train: 685044 (pos=12135) | Val: 123177 (pos = 2762) | Test: 156725 (pos=2397)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.4034090909090909
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.3065309666216477
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.12336250426782153
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.4098867897055076
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.16246735747588328
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2533741744041352
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.32874460653379906
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2289583727693552
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.2126669981235265
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.2402372444815265
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.319480988495073
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.28132573524595533
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2754838572007767
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.193250792477505
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.14746956249797802
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.31071349023684014
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.15953955080414498
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.26286387551546914
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.16258899985664452
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.1816100571673383
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.16937635588359973
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.40547511145499426
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.3531044853813008
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.23295082836784128
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.38709456216142085
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.13869710015433354
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.22808617544825688
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.29215080758036927
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2031686717705675
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.15999765657039078
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.3279583875162549
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1950364795771816
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.19459819746718057
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.2182655510151132
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.11879143007769626
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.13721851647524952
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.24007075385681462
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.12175540691588453
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\pipelines\artifacts\ica_cnn_rf.py", line 257, in <module>
    results.setdefault(artifact, []).append(  train_binary_model(   df=rf_features_dataset,
                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\src\models\ml_models.py", line 306, in train_binary_model
    best_model, best_params, best_score = _search_random(X_train, y_train, X_val, y_val, search_kwargs, search_data, verbose, build_model_fn, balanced)
                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\src\models\ml_models.py", line 157, in _search_random
    model.fit(X_train, y_train)
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\sklearn\base.py", line 1336, in wrapper
    return fit_method(estimator, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\imblearn\ensemble\_forest.py", line 676, in fit
    samplers_trees = Parallel(
                     ^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\sklearn\utils\parallel.py", line 91, in __call__
    return super().__call__(iterable_with_config_and_warning_filters)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\joblib\parallel.py", line 2072, in __call__
    return output if self.return_generator else list(output)
                                                ^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\joblib\parallel.py", line 1682, in _get_outputs
    yield from self._retrieve()
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\joblib\parallel.py", line 1800, in _retrieve
    time.sleep(0.01)
KeyboardInterrupt
PS C:\Users\diseñoeinnovacion\Docume
```

## B

``` bash
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> uv run python -m pipelines.artifacts.ica_cnn_rf

Loading all dataset for training...
  channel  ...                                                CSV
0  FP1-F7  ...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7  ...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7  ...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3  ...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3  ...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

[5 rows x 14 columns]
{'train': 13, 'test': 3}

==================================================
ARTIFACT: eye

==================================================
**************************************************
>> eye | windows: 5s (2s stride)
[INFO] Existing dataset, loading: D:\Users\disenoeinnovacion\ml-outputs\artifact\dataset\rf_dataset_eye_w5_s2_ua0.1_p50_v2.parquet
[INFO] Split distribution:  split
train    342499
test      84801
val       63082
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye
[INFO] Pretrained model found, loading: D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_eye_w5s2_2_and_analysis_random.joblib
Final report -------------------------
                  precision    recall  f1-score   support

no_rf_eye_w5s2_2       0.99      0.97      0.98     83099
   rf_eye_w5s2_2       0.33      0.75      0.46      1702

        accuracy                           0.96     84801
       macro avg       0.66      0.86      0.72     84801
    weighted avg       0.98      0.96      0.97     84801

Confusion matrix -------------------------
[[80525  2574]
 [  432  1270]]
General metrics -------------------------
model                 rf_eye_w5s2_2
sensitivity                  0.7462
specificity                   0.969
precision                    0.3304
accuracy                     0.9646
f1_score                      0.458
auc_roc                      0.9423
false_alar_rate               0.031
fp_per_day                   524.51
TP                             1270
FP                             2574
TN                            80525
FN                              432
n_test_windows                84801
covered_test_hours           117.78
**************************************************
>> eye | windows: 2s (1s stride)
[INFO] Existing dataset, loading: D:\Users\disenoeinnovacion\ml-outputs\artifact\dataset\rf_dataset_eye_w2_s1_ua0.15_p50_v2.parquet
[INFO] Split distribution:  split
train    683723
test     169331
val      125961
Name: count, dtype: int64

==================================================
Starting training of Random Forest - eye
[INFO] Pretrained model found, loading: D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_eye_w2s1_2_and_analysis_random.joblib
Final report -------------------------
                  precision    recall  f1-score   support

no_rf_eye_w2s1_2       1.00      0.97      0.98    166442
   rf_eye_w2s1_2       0.33      0.75      0.46      2889

        accuracy                           0.97    169331
       macro avg       0.66      0.86      0.72    169331
    weighted avg       0.98      0.97      0.98    169331

Confusion matrix -------------------------
[[162027   4415]
 [   708   2181]]
General metrics -------------------------
model                 rf_eye_w2s1_2
sensitivity                  0.7549
specificity                  0.9735
precision                    0.3307
accuracy                     0.9697
f1_score                     0.4599
auc_roc                      0.9667
false_alar_rate              0.0265
fp_per_day                  1126.36
TP                             2181
FP                             4415
TN                           162027
FN                              708
n_test_windows               169331
covered_test_hours            94.07

==================================================
ARTIFACT: muscle

==================================================
**************************************************
>> muscle | windows: 1s (0.5s stride)
[INFO] Existing dataset, loading: D:\Users\disenoeinnovacion\ml-outputs\artifact\dataset\rf_dataset_muscle_w1_s0.5_ua0.3_p50_v2.parquet
[INFO] Split distribution:  split
train    1384774
test      317303
val       249517
Name: count, dtype: int64

==================================================
Starting training of Random Forest - muscle
[INFO] Pretrained model found, loading: D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w1s0.5_2_and_analysis_random.joblib
Final report -------------------------
                       precision    recall  f1-score   support

no_rf_muscle_w1s0.5_2       0.99      0.90      0.95    312601
   rf_muscle_w1s0.5_2       0.08      0.56      0.14      4702

             accuracy                           0.90    317303
            macro avg       0.54      0.73      0.54    317303
         weighted avg       0.98      0.90      0.93    317303

Confusion matrix -------------------------
[[282112  30489]
 [  2069   2633]]
General metrics -------------------------
model                 rf_muscle_w1s0.5_2
sensitivity                         0.56
specificity                       0.9025
precision                         0.0795
accuracy                          0.8974
f1_score                          0.1392
auc_roc                           0.8932
false_alar_rate                   0.0975
fp_per_day                        8302.0
TP                                  2633
FP                                 30489
TN                                282112
FN                                  2069
n_test_windows                    317303
covered_test_hours                 88.14
**************************************************
>> muscle | windows: 1s (1s stride)
[INFO] Existing dataset, loading: D:\Users\disenoeinnovacion\ml-outputs\artifact\dataset\rf_dataset_muscle_w1_s1_ua0.3_p50_v2.parquet
[INFO] Split distribution:  split
train    691479
test     158576
val      124305
Name: count, dtype: int64

==================================================
Starting training of Random Forest - muscle
[INFO] Pretrained model found, loading: D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w1s1_2_and_analysis_random.joblib
Final report -------------------------
                     precision    recall  f1-score   support

no_rf_muscle_w1s1_2       0.99      0.91      0.95    156230
   rf_muscle_w1s1_2       0.08      0.55      0.14      2346

           accuracy                           0.90    158576
          macro avg       0.54      0.73      0.54    158576
       weighted avg       0.98      0.90      0.94    158576

Confusion matrix -------------------------
[[141599  14631]
 [  1046   1300]]
General metrics -------------------------
model                 rf_muscle_w1s1_2
sensitivity                     0.5541
specificity                     0.9063
precision                       0.0816
accuracy                        0.9011
f1_score                        0.1423
auc_roc                          0.893
false_alar_rate                 0.0937
fp_per_day                     7971.69
TP                                1300
FP                               14631
TN                              141599
FN                                1046
n_test_windows                  158576
covered_test_hours               44.05
**************************************************
>> muscle | windows: 2s (1s stride)
[INFO] Existing dataset, loading: D:\Users\disenoeinnovacion\ml-outputs\artifact\dataset\rf_dataset_muscle_w2_s1_ua0.3_p50_v2.parquet
[INFO] Split distribution:  split
train    685044
test     156725
val      123177
Name: count, dtype: int64

==================================================
Starting training of Random Forest - muscle

============================================================
Modelo: rf_muscle_w2s1_2
Train: 685044 (pos=12135) | Val: 123177 (pos = 2762) | Test: 156725 (pos=2397)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.4034090909090909
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.3065309666216477
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.12336250426782153
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.4098867897055076
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.16246735747588328
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2533741744041352
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.32874460653379906
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2289583727693552
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.2126669981235265
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.2402372444815265
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.319480988495073
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.28132573524595533
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2754838572007767
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.193250792477505
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.14746956249797802
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.31071349023684014
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.15953955080414498
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.26286387551546914
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.16258899985664452
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.1816100571673383
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.16937635588359973
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.40547511145499426
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.3531044853813008
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.23295082836784128
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.38709456216142085
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.13869710015433354
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.22808617544825688
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.29215080758036927
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2031686717705675
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.15999765657039078
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.3279583875162549
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1950364795771816
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.19459819746718057
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.2182655510151132
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.11879143007769626
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.13721851647524952
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.24007075385681462
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.12175540691588453
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.1690382606099806
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.15919576570879881
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.24075777082950156
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.27839353240318165
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.11599295531342957
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.18137807102242248
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.14974922903016935
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.11980663705252156
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.29159892839969775
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.17399524770689082
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.14649483652568882
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.1190527728473094
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.21478521478521478
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.19372416653556257
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.2972245236122618
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.25598010578668984
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.1231040184027029
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.16397878558285528
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.15349866840467014
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.15246111823401529
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.277088948787062
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.18256108852300632
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.4099 | fp_per_day_val(val)=4969.9798 <- choosen
        adjusted: threshold=0.5556 | F2(val)=0.4386 | fp_per_day_val(val)=3736.5157
[INFO] Best configuration found with validation: {'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3} | F1(val)=0.4099
Final report -------------------------
                     precision    recall  f1-score   support

no_rf_muscle_w2s1_2       0.99      0.91      0.95    154328
   rf_muscle_w2s1_2       0.08      0.54      0.14      2397

           accuracy                           0.90    156725
          macro avg       0.54      0.73      0.55    156725
       weighted avg       0.98      0.90      0.94    156725

Confusion matrix -------------------------
[[140043  14285]
 [  1094   1303]]
General metrics -------------------------
model                 rf_muscle_w2s1_2
sensitivity                     0.5436
specificity                     0.9074
precision                       0.0836
accuracy                        0.9019
f1_score                        0.1449
auc_roc                         0.8901
false_alar_rate                 0.0926
fp_per_day                     3937.55
TP                                1303
FP                               14285
TN                              140043
FN                                1094
n_test_windows                  156725
covered_test_hours               87.07
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w2s1_2_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w2s1_2_and_analysis_random.joblib
**************************************************
>> muscle | windows: 5s (2s stride)

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
Ventanas: 38834 -> sin ambiguas: 37860 | positivas: 9393
['Patient', 'Session', 'Section', 'Start', 'muscle']

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w5_s2_sw0.0_ua0.2
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w5_s2_sw0.3_ua0.2
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w5_s2_sw0.5_ua0.2
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w5_s2_sw0.7_ua0.2
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_muscle_w5_s2_sw1.0_ua0.2

************************************************************

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.3             0.2040      0.2399    0.3026       0.0986     0.7076   0.1266    0.1657    0.0234          0.1219
0.0             0.1740      0.2785    0.1975       0.1045     0.6081   0.1837    0.2082    0.0919          0.1964
0.5             0.2110      0.2236    0.4078       0.1968     0.7329   0.1098    0.1573    0.0402          0.2370
0.7             0.2169      0.2139    0.4568       0.2429     0.7385   0.1134    0.1480    0.0385          0.2814
1.0             0.1350      0.2157    0.4792       0.3443     0.7078   0.1445    0.1477    0.0078          0.3521
[INFO] Best suggested size weight for muscle: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p50_v2_muscle_w5_s2_sw0.3_ua0.2 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      6436        1313        5123       0.204009
train    27480        6592       20888       0.239884
val       4918        1488        3430       0.302562
Broken rules: 0 | splits per patient: {'train': 33, 'test': 10, 'val': 7}
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
[WARN] ICA failed for aaaaaimu_s008_t000: One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
[SKIP] Session aaaaaimu_s008_t000 discarted by ICA error One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
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
0    469358
1      9344
Name: count, dtype: int64
[INFO] Split distribution:  split
train    340810
test      75474
val       62418
Name: count, dtype: int64

==================================================
Starting training of Random Forest - muscle

============================================================
Modelo: rf_muscle_w5s2_2
Train: 340810 (pos=6543) | Val: 62418 (pos = 1488) | Test: 75474 (pos=1313)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.4571572580645161
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.4258315450643777
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.17617629541393687
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.45832488339079297
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.23987345900463114
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.4000587889476778
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.45866364665911663
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.3553286469290369
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.30620308178585537
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.32404098165356204
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.4425846063884219
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.3817705299941759
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.3874014835419564
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.3248338532483385
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.24566860659575893
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.4354090525723925
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.2309679858835392
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.39964317573595004
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.24002351250734766
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.27616391664730033
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.24997442280803464
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.46106773580924243
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.4701676149469476
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.34942233632862646
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.4683129159834089
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.19507676019057701
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.31669910110277083
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.41602654704111103
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.3137513751375138
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.25217600715588123
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.46135933634114396
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.3239775097487984
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.28170688220610957
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.35748841472730053
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.15254690585911784
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.21048723367795738
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.32414521705724164
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.16873647032015496
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.25767389467755564
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.22617199627444892
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.3320177602368032
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.4091388837151549
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.13978838767979518
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.2615005971985957
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.21514806045192786
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.16203450613369486
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.428101724485003
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.28779404181046453
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.234514687100894
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.15567226890756303
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.3078411539645543
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.307044343575419
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.4187625754527163
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.39414083181363607
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.17236961636113765
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.2659651933299352
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.24567439374707728
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.26339446242358866
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.4076687116564417
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.3131655583083409
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.4702 | fp_per_day_val(val)=1614.2728 <- choosen
        adjusted: threshold=0.5531 | F2(val)=0.4834 | fp_per_day_val(val)=1220.8786
[INFO] Best configuration found with validation: {'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5} | F1(val)=0.4702
Final report -------------------------
                     precision    recall  f1-score   support

no_rf_muscle_w5s2_2       0.99      0.91      0.95     74161
   rf_muscle_w5s2_2       0.09      0.56      0.16      1313

           accuracy                           0.90     75474
          macro avg       0.54      0.73      0.55     75474
       weighted avg       0.98      0.90      0.93     75474

Confusion matrix -------------------------
[[67133  7028]
 [  583   730]]
General metrics -------------------------
model                 rf_muscle_w5s2_2
sensitivity                      0.556
specificity                     0.9052
precision                       0.0941
accuracy                        0.8992
f1_score                         0.161
auc_roc                         0.8878
false_alar_rate                 0.0948
fp_per_day                     1609.08
TP                                 730
FP                                7028
TN                               67133
FN                                 583
n_test_windows                   75474
covered_test_hours              104.83
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w5s2_2_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_muscle_w5s2_2_and_analysis_random.joblib

==================================================
ARTIFACT: non_physiological

==================================================
**************************************************
>> non_physiological | windows: 0.5s (0.25s stride)

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
Ventanas: 311930 -> sin ambiguas: 311057 | positivas: 29648
['Patient', 'Session', 'Section', 'Start', 'non_physiological']

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_non_physiological_w0.5_s0.25_sw0.0_ua0.2
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_non_physiological_w0.5_s0.25_sw0.3_ua0.2
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_non_physiological_w0.5_s0.25_sw0.5_ua0.2
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_non_physiological_w0.5_s0.25_sw0.7_ua0.2
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_non_physiological_w0.5_s0.25_sw1.0_ua0.2

************************************************************

[INFO] Sweep size weight results for non_physiological:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.5             0.0645      0.0944    0.1447       0.0803     0.7036   0.1184    0.1780    0.0316          0.1119
0.3             0.0780      0.0902    0.1587       0.0807     0.7312   0.1007    0.1682    0.0493          0.1300
0.7             0.0701      0.0899    0.1564       0.0863     0.7198   0.1237    0.1565    0.0263          0.1126
1.0             0.0406      0.0903    0.1677       0.1271     0.7099   0.1505    0.1396    0.0104          0.1375
0.0             0.0463      0.1060    0.2197       0.1734     0.6279   0.0649    0.3072    0.1572          0.3306
[INFO] Best suggested size weight for non_physiological: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p50_v2_non_physiological_w0.5_s0.25_sw0.5_ua0.2 parquet and json
[INFO] Saving patient asignation for non_physiological
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test     55524        3580       51944       0.064477
train   219486       20724      198762       0.094421
val      36920        5344       31576       0.144745
Broken rules: 0 | splits per patient: {'train': 32, 'test': 10, 'val': 8}
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
[WARN] ICA failed for aaaaaimu_s008_t000: One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
[SKIP] Session aaaaaimu_s008_t000 discarted by ICA error One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
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
0    3904246
1      29507
Name: count, dtype: int64
[INFO] Split distribution:  split
train    2817744
test      647678
val       468331
Name: count, dtype: int64

==================================================
Starting training of Random Forest - non_physiological

============================================================
Modelo: rf_non_physiological_w0.5s0.25_2
Train: 2817744 (pos=20583) | Val: 468331 (pos = 5344) | Test: 647678 (pos=3580)
        params:{'n_estimators': 190, 'max_depth': 28, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.11974880900822867
        params:{'n_estimators': 344, 'max_depth': 30, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.10807348047618766
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.055786840819598886
        params:{'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.11729943454785086
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.06636860816282432
        params:{'n_estimators': 375, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.0999328294802959
        params:{'n_estimators': 501, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.11776357304788838
        params:{'n_estimators': 395, 'max_depth': 18, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.09051637454944851
        params:{'n_estimators': 191, 'max_depth': 21, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.08106901931567126
        params:{'n_estimators': 536, 'max_depth': 29, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.08957265977307408
        params:{'n_estimators': 224, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.10512930506189484
        params:{'n_estimators': 180, 'max_depth': 34, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.10928308247769064
        params:{'n_estimators': 455, 'max_depth': 28, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.09720925248381121
        params:{'n_estimators': 313, 'max_depth': 19, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.08465152087595612
        params:{'n_estimators': 395, 'max_depth': 9, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.06591719492868463
        params:{'n_estimators': 565, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.11707170373340589
        params:{'n_estimators': 334, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.0697899927965867
        params:{'n_estimators': 184, 'max_depth': 19, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.09145920519522564
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.0662189578571612
        params:{'n_estimators': 298, 'max_depth': 11, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.07307472767920849
        params:{'n_estimators': 573, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.07610181388303965
        params:{'n_estimators': 433, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.12403641134984418
        params:{'n_estimators': 495, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.11376349449531478
        params:{'n_estimators': 528, 'max_depth': 16, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.08575594676088082
        params:{'n_estimators': 257, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.12180695722893793
        params:{'n_estimators': 524, 'max_depth': 10, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.0648315482620934
        params:{'n_estimators': 508, 'max_depth': 28, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.0860849868917424
        params:{'n_estimators': 362, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.11563683738039456
        params:{'n_estimators': 400, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.07867409348333461
        params:{'n_estimators': 166, 'max_depth': 9, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.0679441442735643
        params:{'n_estimators': 347, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.1177393112441189
        params:{'n_estimators': 534, 'max_depth': 21, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.09070576540755468
        params:{'n_estimators': 408, 'max_depth': 24, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.07885415495333409
        params:{'n_estimators': 190, 'max_depth': 21, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.09245122643903657
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.055291834107943236
        params:{'n_estimators': 592, 'max_depth': 11, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.06278972163144815
        params:{'n_estimators': 596, 'max_depth': 30, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.08778058664363114
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.05565982514649241
        params:{'n_estimators': 562, 'max_depth': 13, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.07296283767178144
        params:{'n_estimators': 206, 'max_depth': 21, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.07613697683301704
        params:{'n_estimators': 598, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.08575075279743244
        params:{'n_estimators': 338, 'max_depth': 29, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.10115414700076092
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.05491851629571319
        params:{'n_estimators': 497, 'max_depth': 26, 'min_samples_split': 11, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.08011393095013361
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.06267349167480504
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.055952021978758336
        params:{'n_estimators': 373, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1066853816287066
        params:{'n_estimators': 257, 'max_depth': 14, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.074978856780835
        params:{'n_estimators': 423, 'max_depth': 15, 'min_samples_split': 14, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.0666060890541107
        params:{'n_estimators': 304, 'max_depth': 8, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.05631679912304741
        params:{'n_estimators': 314, 'max_depth': 32, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.0868690673195203
        params:{'n_estimators': 355, 'max_depth': 12, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.07497494048364867
        params:{'n_estimators': 268, 'max_depth': 28, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.1167334378447425
        params:{'n_estimators': 505, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.09264521483405952
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.05707115334007989
        params:{'n_estimators': 207, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.07419864884289205
        params:{'n_estimators': 474, 'max_depth': 14, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.0706343555325733
        params:{'n_estimators': 396, 'max_depth': 10, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.06820114970589218
        params:{'n_estimators': 158, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.09929143419252702
        params:{'n_estimators': 448, 'max_depth': 17, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.08036630252734323
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.1240 | fp_per_day_val(val)=35988.9463 <- choosen
        adjusted: threshold=0.8449 | F2(val)=0.1941 | fp_per_day_val(val)=7553.9189
[INFO] Best configuration found with validation: {'n_estimators': 433, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3} | F1(val)=0.1240
Final report -------------------------
                                     precision    recall  f1-score   support

no_rf_non_physiological_w0.5s0.25_2       1.00      0.80      0.89    644098
   rf_non_physiological_w0.5s0.25_2       0.02      0.74      0.04      3580

                           accuracy                           0.80    647678
                          macro avg       0.51      0.77      0.46    647678
                       weighted avg       0.99      0.80      0.88    647678

Confusion matrix -------------------------
[[514537 129561]
 [   930   2650]]
General metrics -------------------------
model                 rf_non_physiological_w0.5s0.25_2
sensitivity                                     0.7402
specificity                                     0.7988
precision                                         0.02
accuracy                                        0.7985
f1_score                                         0.039
auc_roc                                         0.8483
false_alar_rate                                 0.2012
fp_per_day                                    34566.78
TP                                                2650
FP                                              129561
TN                                              514537
FN                                                 930
n_test_windows                                  647678
covered_test_hours                               89.96
Model saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w0.5s0.25_2_random.joblib
Model with metrics saved in D:\Users\disenoeinnovacion\ml-outputs\artifact\models\rf_non_physiological_w0.5s0.25_2_and_analysis_random.joblib
**************************************************
>> non_physiological | windows: 1s (0.5s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w1_s0.5_ua0.3_ub0.1_urTrue_dcd979_L2.parquet (155890 rows)
    Patient Session Section    Montage Partition  Window_size  stride  Start  end  ... muscle  non_physiological  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    0.0  1.0  ...      0                  0             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    0.5  1.5  ...      0                  0             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    1.0  2.0  ...      0                  0             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    1.5  2.5  ...      0                  0             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    2.0  3.0  ...      0                  0             0            1.0           0                     0             0              0           0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 155890 -> sin ambiguas: 154307 | positivas: 14854
['Patient', 'Session', 'Section', 'Start', 'non_physiological']

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_non_physiological_w1_s0.5_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_non_physiological_w1_s0.5_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_non_physiological_w1_s0.5_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_non_physiological_w1_s0.5_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p50_v2_non_physiological_w1_s0.5_sw1.0_ua0.3

************************************************************

[INFO] Sweep size weight results for non_physiological:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.0              0.065      0.0945    0.1453       0.0803     0.7037   0.1183     0.178    0.0317          0.1119
0.3              0.065      0.0945    0.1453       0.0803     0.7037   0.1183     0.178    0.0317          0.1119
0.5              0.065      0.0945    0.1453       0.0803     0.7037   0.1183     0.178    0.0317          0.1119
0.7              0.065      0.0945    0.1453       0.0803     0.7037   0.1183     0.178    0.0317          0.1119
1.0              0.065      0.0945    0.1453       0.0803     0.7037   0.1183     0.178    0.0317          0.1119
[INFO] Best suggested size weight for non_physiological: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p50_v2_non_physiological_w1_s0.5_sw0.0_ua0.3 parquet and json
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test     27750        1804       25946       0.065009
train   109692       10370       99322       0.094537
val      18448        2680       15768       0.145273
Broken rules: 0 | splits per patient: {'train': 32, 'test': 10, 'val': 8}
    Patient Session Section    Montage Partition  Window_size  stride  Start  end  ... non_physiological  is_ambiguous  sample_weight  distinguish genuine_cooccurrence  weak_overlap  is_unreviewed  is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    0.0  1.0  ...                 0             0            1.0            0                    0             0              0            0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    0.5  1.5  ...                 0             0            1.0            0                    0             0              0            0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    1.0  2.0  ...                 0             0            1.0            0                    0             0              0            0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    1.5  2.5  ...                 0             0            1.0            0                    0             0              0            0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    2.0  3.0  ...                 0             0            1.0            0                    0             0              0            0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    2.5  3.5  ...                 0             0            1.0            0                    0             0              0            0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    3.0  4.0  ...                 0             0            1.0            0                    0             0              0            0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    3.5  4.5  ...                 0             0            1.0            0                    0             0              0            0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    4.0  5.0  ...                 0             0            1.0            0                    0             0              0            0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      1     0.5    4.5  5.5  ...                 0             0            1.0            0                    0             0              0            0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
[WARN] ICA failed for aaaaaimu_s008_t000: One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
[SKIP] Session aaaaaimu_s008_t000 discarted by ICA error One PCA component captures most of the explained variance (99.4121647598012%), your threshold results in 1 component. You should select a higher value.
    ic_index ic_raw_label    ic_target_label  ic_iclabel_prob    ic_mean  ...  monopolar_channels_muscle  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain              clean         0.687185 -21.157149  ...                         []                                    []                    []                       []                                  []
1          1    eye blink                eye         0.949668  -0.418452  ...                         []                                    []                    []                       []                                  []
2          2        brain              clean         0.994398   0.014797  ...                         []                                    []                    []                       []                                  []
3          3        other  non_physiological         0.726641 -12.346357  ...                         []                                    []                    []                       []                                  []
4          4        brain              clean         0.999643   0.066017  ...                         []                                    []                    []                       []                                  []
5          5        brain              clean         0.993584   6.095223  ...                         []                                    []                    []                       []                                  []
6          6        brain              clean         0.999535  -0.061540  ...                         []                                    []                    []                       []                                  []
7          7        brain              clean         0.978230  -0.551214  ...                         []                                    []                    []                       []                                  []
8          8    eye blink                eye         0.823060  -0.025609  ...                         []                                    []                    []                       []                                  []
9          9        brain              clean         0.773097   0.031989  ...                         []                                    []                    []                       []                                  []
10        10        brain              clean         0.919012  -1.369515  ...                         []                                    []                    []                       []                                  []
11        11        brain              clean         0.936563   0.046924  ...                         []                                    []                    []                       []                                  []
12         0        brain              clean         0.687185  -0.681473  ...                         []                                    []                    []                       []                                  []
13         1    eye blink                eye         0.949668   0.054157  ...                         []                                    []                    []                       []                                  []
14         2        brain              clean         0.994398  -0.094578  ...                         []                                    []                    []                       []                                  []
15         3        other  non_physiological         0.726641   3.021981  ...                         []                                    []                    []                       []                                  []
16         4        brain              clean         0.999643   0.116980  ...                         []                                    []                    []                       []                                  []
17         5        brain              clean         0.993584   0.586572  ...                         []                                    []                    []                       []                                  []
18         6        brain              clean         0.999535   0.009813  ...                         []                                    []                    []                       []                                  []
19         7        brain              clean         0.978230   0.226806  ...                         []                                    []                    []                       []                                  []
20         8    eye blink                eye         0.823060  -0.003268  ...                         []                                    []                    []                       []                                  []
21         9        brain              clean         0.773097  -0.453420  ...                         []                                    []                    []                       []                                  []
22        10        brain              clean         0.919012  -0.634592  ...                         []                                    []                    []                       []                                  []
23        11        brain              clean         0.936563   0.169795  ...                         []                                    []                    []                       []                                  []
24         0        brain              clean         0.687185  10.011926  ...                         []                                    []                    []                       []                                  []

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
0    1936811
1      14783
Name: count, dtype: int64
[INFO] Split distribution:  split
train    1398557
test      319795
val       233242
Name: count, dtype: int64

==================================================
Starting training of Random Forest - non_physiological

============================================================
Modelo: rf_non_physiological_w1s0.5_2
Train: 1398557 (pos=10299) | Val: 233242 (pos = 2680) | Test: 319795 (pos=1804)
        params:{'n_estimators': 190, 'max_depth': 28, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.12612882215219956
        params:{'n_estimators': 344, 'max_depth': 30, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.11371107161119093
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 8, 'min_samples_leaf': 7, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.05667423732971295
        params:{'n_estimators': 481, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1312738044858231
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.06672353430636307
        params:{'n_estimators': 375, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.0975240893574731
        params:{'n_estimators': 501, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.12420862597685231
        params:{'n_estimators': 395, 'max_depth': 18, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.08712865347989743
        params:{'n_estimators': 191, 'max_depth': 21, 'min_samples_split': 13, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.08325598000714031
        params:{'n_estimators': 536, 'max_depth': 29, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.09861567256418406
        params:{'n_estimators': 224, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.11707269680114644
        params:{'n_estimators': 180, 'max_depth': 34, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.11897370921761166
        params:{'n_estimators': 455, 'max_depth': 28, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.09510424888820437
        params:{'n_estimators': 313, 'max_depth': 19, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.08467675692663729
        params:{'n_estimators': 395, 'max_depth': 9, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.0652349320247441
        params:{'n_estimators': 565, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.12043108934451177
        params:{'n_estimators': 334, 'max_depth': 14, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.06938055192377017
        params:{'n_estimators': 184, 'max_depth': 19, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.09525716823251805
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.06669830359983103
        params:{'n_estimators': 298, 'max_depth': 11, 'min_samples_split': 9, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.07089211134811522
        params:{'n_estimators': 573, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.07668871173976617
        params:{'n_estimators': 433, 'max_depth': 26, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.1373593333906022
        params:{'n_estimators': 495, 'max_depth': 29, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.13267802902463718
        params:{'n_estimators': 528, 'max_depth': 16, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.08619458248441882
        params:{'n_estimators': 257, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.1296567682221365
        params:{'n_estimators': 524, 'max_depth': 10, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.06239775760300772
        params:{'n_estimators': 508, 'max_depth': 28, 'min_samples_split': 12, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.09422665353127017
        params:{'n_estimators': 362, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.11822575077666551
        params:{'n_estimators': 400, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.07898746358023041
        params:{'n_estimators': 166, 'max_depth': 9, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.0674644759489822
        params:{'n_estimators': 347, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.12733707778718165
        params:{'n_estimators': 534, 'max_depth': 21, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.0926992034212938
        params:{'n_estimators': 408, 'max_depth': 24, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.08416065767931166
        params:{'n_estimators': 190, 'max_depth': 21, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.09309372569354421
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.05592561059080817
        params:{'n_estimators': 592, 'max_depth': 11, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.06358148507154716
        params:{'n_estimators': 596, 'max_depth': 30, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.09155802557468157
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 13, 'min_samples_leaf': 2, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.05633021275164682
        params:{'n_estimators': 562, 'max_depth': 13, 'min_samples_split': 7, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.0716896100108092
        params:{'n_estimators': 206, 'max_depth': 21, 'min_samples_split': 8, 'min_samples_leaf': 6, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.07462686567164178
        params:{'n_estimators': 598, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.08992139428497793
        params:{'n_estimators': 338, 'max_depth': 29, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.09742809707019794
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 1, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.05552631906085933
```
