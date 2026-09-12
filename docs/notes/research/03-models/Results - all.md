# Artifacts

## ICA+ICLabel + RF

PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> $Host.UI.RawUI.BufferSize = New-Object System.Management.Automation.Host.Size(300, 3000)
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> $Host.UI.RawUI.WindowSize = New-Object System.Management.Automation.Host.Size(300, 50)
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> uv run python -m implementation.models.rf_model

Loading 30 artifact patients, 1 sessions per patient for testing...
  channel  start_time  stop_time label  confidence   Patient Session Section    Montage  NoChannels  Duration                                                EDF                                                CSV
0  FP1-F7     22.9737    30.0688  eyem         1.0  aaaaaaju    s005    t000  01_tcp_ar          36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7    136.7987   140.1117  eyem         1.0  aaaaaaju    s005    t000  01_tcp_ar          36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7    145.0133   148.0498  eyem         1.0  aaaaaaju    s005    t000  01_tcp_ar          36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3     22.9737    30.0688  eyem         1.0  aaaaaaju    s005    t000  01_tcp_ar          36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3    136.7987   140.1117  eyem         1.0  aaaaaaju    s005    t000  01_tcp_ar          36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

--------------------------------------------------
ARTIFACT: eye | windows: 20s

--------------------------------------------------

Generating windows...
    Patient Session Section    Montage  Window_size  stride  Start  end Raw_labels                                        Label_spans  N_channels_annotated  No_channels  ...  channels_non_physiological is_clean_window  eye  muscle  non_physiological is_ambiguous  sample_weight distinguish  genuine_cooccurrence weak_overlap  is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar           20      20      0   20         []                                                 []                     0           36  ...                          []               1    0       0                  0            0            1.0           0                     0            0              0            0
1  aaaaaaju    s005    t000  01_tcp_ar           20      20     20   40     [eyem]  [{'label': 'eyem', 'start_in_window': 2.974, '...                     8           36  ...                          []               0    1       0                  0            0            1.0           0                     0            0              0            0
2  aaaaaaju    s005    t000  01_tcp_ar           20      20     40   60         []                                                 []                     0           36  ...                          []               1    0       0                  0            0            1.0           0                     0            0              0            0
3  aaaaaaju    s005    t000  01_tcp_ar           20      20     60   80         []                                                 []                     0           36  ...                          []               1    0       0                  0            0            1.0           0                     0            0              0            0
4  aaaaaaju    s005    t000  01_tcp_ar           20      20     80  100         []                                                 []                     0           36  ...                          []               1    0       0                  0            0            1.0           0                     0            0              0            0

[5 rows x 33 columns]

Starting features extraction from channels and ICA components...
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob   ic_mean  ic_variance    ic_rms  ic_skewness  ic_kurtosis    ic_zcr  ic_hjorth_mobility  ...  tuar_is_ambiguous  tuar_sample_weight  tuar_eye  tuar_muscle  tuar_non_physiological  tuar_genuine_cooccurrence  tuar_weak_overlap  tuar_is_excluded  channels_eye  channels_muscle  channels_non_physiological
0         0        brain           clean         0.668147 -0.543517    67.881789  8.256949    -1.203878    14.060019  0.290096            0.156263  ...                  0                 1.0         0            0                       0                          0                  0                 0            []               []                          []
1         1    eye blink             eye         0.974591 -0.019422     1.173228  1.083331    -1.352785    13.611691  0.202188            0.428000  ...                  0                 1.0         0            0                       0                          0                  0                 0            []               []                          []
2         2        brain           clean         0.998497  0.001357     0.581291  0.762426    -0.340861     7.290907  0.219379            0.498479  ...                  0                 1.0         0            0                       0                          0                  0                 0            []               []                          []
3         3        brain           clean         0.985737  0.035036    48.080807  6.934121    -9.597875   259.658194  0.304747            0.452778  ...                  0                 1.0         0            0                       0                          0                  0                 0            []               []                          []
4         4        brain           clean         0.998654 -0.001120     0.448729  0.669873    -0.519709    13.046675  0.236570            0.640895  ...                  0                 1.0         0            0                       0                          0                  0                 0            []               []                          []

[5 rows x 135 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob   ic_mean  ic_variance    ic_rms  ic_skewness  ic_kurtosis    ic_zcr  ic_hjorth_mobility  ...  tuar_sample_weight  tuar_eye  tuar_muscle  tuar_non_physiological  tuar_genuine_cooccurrence  tuar_weak_overlap  tuar_is_excluded  channels_eye  channels_muscle  channels_non_physiological  is_positive
0         0        brain           clean         0.668147 -0.543517    67.881789  8.256949    -1.203878    14.060019  0.290096            0.156263  ...                 1.0         0            0                       0                          0                  0                 0            []               []                          []            0
1         1    eye blink             eye         0.974591 -0.019422     1.173228  1.083331    -1.352785    13.611691  0.202188            0.428000  ...                 1.0         0            0                       0                          0                  0                 0            []               []                          []            0
2         2        brain           clean         0.998497  0.001357     0.581291  0.762426    -0.340861     7.290907  0.219379            0.498479  ...                 1.0         0            0                       0                          0                  0                 0            []               []                          []            0
3         3        brain           clean         0.985737  0.035036    48.080807  6.934121    -9.597875   259.658194  0.304747            0.452778  ...                 1.0         0            0                       0                          0                  0                 0            []               []                          []            0
4         4        brain           clean         0.998654 -0.001120     0.448729  0.669873    -0.519709    13.046675  0.236570            0.640895  ...                 1.0         0            0                       0                          0                  0                 0            []               []                          []            0

[5 rows x 136 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_Fp1', 'ic_contrib_Fp2', 'ic_contrib_F3', 'ic_contrib_F4', 'ic_contrib_C3', 'ic_contrib_C4', 'ic_contrib_P3', 'ic_contrib_P4', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_F7', 'ic_contrib_F8', 'ic_contrib_T7', 'ic_contrib_T8', 'ic_contrib_P7', 'ic_contrib_P8', 'ic_contrib_Fz', 'ic_contrib_Cz', 'ic_contrib_Pz', 'ic_contrib_Ft9', 'ic_contrib_Ft10', 'Fp1_variance', 'Fp1_line_length', 'Fp1_peak_to_peak', 'Fp2_variance', 'Fp2_line_length', 'Fp2_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'Fz_variance', 'Fz_line_length', 'Fz_peak_to_peak', 'Cz_variance', 'Cz_line_length', 'Cz_peak_to_peak', 'Pz_variance', 'Pz_line_length', 'Pz_peak_to_peak', 'Ft9_variance', 'Ft9_line_length', 'Ft9_peak_to_peak', 'Ft10_variance', 'Ft10_line_length', 'Ft10_peak_to_peak', 'Patient', 'Session', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'channels_eye', 'channels_muscle', 'channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    19073
1      331
Name: count, dtype: int64
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_eye_sw0.0 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_eye_sw0.3 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_eye_sw0.5 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_eye_sw0.7 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_eye_sw1.0 parquet and json

[INFO] Sweep size weight results for eye:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.5             0.0176      0.0171    0.0164       0.0013     0.7212   0.1415    0.1372    0.0212          0.0225
0.7             0.0184      0.0169    0.0166       0.0017     0.7287   0.1394    0.1319    0.0287          0.0304
1.0             0.0166      0.0164    0.0214       0.0050     0.7369   0.1324    0.1307    0.0369          0.0419
0.3             0.0191      0.0177    0.0132       0.0060     0.6882   0.1800    0.1319    0.0300          0.0359
0.0             0.0128      0.0238    0.0085       0.0153     0.5047   0.2981    0.1972    0.1953          0.2106
[INFO] Best suggested size weight for eye: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_eye_sw0.5 parquet and json
[INFO] Split distribution:  split
train    13995
val       2746
test      2663
Name: count, dtype: int64

Starting training of Random Forest (eye)

============================================================
Modelo: rf_eye
Train: 13995 (pos=239) | Val: 2746 (pos = 45) | Test: 2663 (pos=47)
[DEBUG] y_val dist (rf_eye): {0: 2701, 1: 45}
[DEBUG] y_val hash (rf_eye): 14916259634655694632
       ic_iclabel_prob   ic_mean  ic_variance    ic_rms  ic_skewness  ic_kurtosis    ic_zcr  ic_hjorth_mobility  ic_hjorth_complexity  ic_line_length  ic_peak_to_peak  ...  Cz_line_length  Cz_peak_to_peak   Pz_variance  Pz_line_length  Pz_peak_to_peak  Ft9_variance  Ft9_line_length  Ft9_peak_to_peak  Ft10_variance  Ft10_line_length  Ft10_peak_to_peak
3180          0.642444  0.001411     0.014871  0.121953     0.012626     0.288434  0.329947            0.964226              1.639659      475.350859         0.958336  ...        0.010286         0.000031  1.673852e-11        0.009086         0.000027  9.163862e-11         0.015640          0.000075   5.490629e-11          0.014360            0.00006
3181          0.664108 -0.003486     0.025758  0.160531    -0.148393     0.273015  0.275444            0.820819              1.875976      533.191611         1.188199  ...        0.010286         0.000031  1.673852e-11        0.009086         0.000027  9.163862e-11         0.015640          0.000075   5.490629e-11          0.014360            0.00006
3182          0.997867 -0.012280     0.388755  0.623623     0.081362     0.022411  0.250635            0.744049              2.020334     1890.155223         4.573506  ...        0.010286         0.000031  1.673852e-11        0.009086         0.000027  9.163862e-11         0.015640          0.000075   5.490629e-11          0.014360            0.00006
3183          0.994250  0.020114     1.349641  1.161914     0.576142     1.623992  0.172690            0.374568              3.849973     1743.604704         9.302648  ...        0.010286         0.000031  1.673852e-11        0.009086         0.000027  9.163862e-11         0.015640          0.000075   5.490629e-11          0.014360            0.00006
3184          0.963927  0.011256     0.292739  0.541170     0.042605     0.262850  0.443837            1.289669              1.220617     2821.586160         4.250128  ...        0.010286         0.000031  1.673852e-11        0.009086         0.000027  9.163862e-11         0.015640          0.000075   5.490629e-11          0.014360            0.00006
...                ...       ...          ...       ...          ...          ...       ...                 ...                   ...             ...              ...  ...             ...              ...           ...             ...              ...           ...              ...               ...            ...               ...                ...
14973         0.976388 -0.002998     0.982580  0.991256    -0.058809     1.646588  0.409846            1.230477              1.235406     4600.064520        11.206141  ...        0.006284         0.000027  2.066235e-11        0.005318         0.000045  9.696328e-10         0.018898          0.000226   5.145729e-10          0.012688            0.00017
14974         0.997074  0.000064     0.745070  0.863174    -0.904886     7.556552  0.366087            1.131021              1.288268     3435.212067        14.291766  ...        0.006284         0.000027  2.066235e-11        0.005318         0.000045  9.696328e-10         0.018898          0.000226   5.145729e-10          0.012688            0.00017
14975         0.493931  0.003217     0.744876  0.863068    -0.385295     1.737341  0.269584            0.794639              1.867132     2697.009712         8.424901  ...        0.006284         0.000027  2.066235e-11        0.005318         0.000045  9.696328e-10         0.018898          0.000226   5.145729e-10          0.012688            0.00017
14976         0.448800  0.000903     0.735657  0.857705     0.387096     0.829742  0.376636            1.166115              1.292755     3869.451899         7.909703  ...        0.006284         0.000027  2.066235e-11        0.005318         0.000045  9.696328e-10         0.018898          0.000226   5.145729e-10          0.012688            0.00017
14977         0.683256 -0.005898     1.286058  1.134060    -0.078256     2.538363  0.388943            1.135901              1.362745     4970.115927        15.137425  ...        0.006284         0.000027  2.066235e-11        0.005318         0.000045  9.696328e-10         0.018898          0.000226   5.145729e-10          0.012688            0.00017

[2746 rows x 116 columns]
[DEBUG] X_val hash (rf_eye): 2987194404400190162
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.1701931922723091
        params:{'n_estimators': 536, 'max_depth': 7, 'min_samples_split': 22, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.14683153013910355
        params:{'n_estimators': 386, 'max_depth': 29, 'min_samples_split': 23, 'min_samples_leaf': 11, 'max_features': 0.3}
        f2 score:0.15873015873015872
        params:{'n_estimators': 503, 'max_depth': 17, 'min_samples_split': 8, 'min_samples_leaf': 12, 'max_features': 'log2'}
        f2 score:0.1442672741078208
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.11695906432748537
        params:{'n_estimators': 439, 'max_depth': 15, 'min_samples_split': 25, 'min_samples_leaf': 9, 'max_features': 'log2'}
        f2 score:0.15314569536423842
        params:{'n_estimators': 352, 'max_depth': 10, 'min_samples_split': 7, 'min_samples_leaf': 9, 'max_features': 'sqrt'}
        f2 score:0.13372472276581865
        params:{'n_estimators': 178, 'max_depth': 26, 'min_samples_split': 25, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.16488046166529266
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.20247469066366705
        params:{'n_estimators': 586, 'max_depth': 16, 'min_samples_split': 27, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.12658227848101267
        params:{'n_estimators': 491, 'max_depth': 9, 'min_samples_split': 14, 'min_samples_leaf': 8, 'max_features': 'sqrt'}
        f2 score:0.16142384105960264
        params:{'n_estimators': 169, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.13679890560875513
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.14295676429567644
        params:{'n_estimators': 296, 'max_depth': 27, 'min_samples_split': 14, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.23564064801178203
        params:{'n_estimators': 508, 'max_depth': 9, 'min_samples_split': 16, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.14878621769772904
        params:{'n_estimators': 364, 'max_depth': 13, 'min_samples_split': 10, 'min_samples_leaf': 9, 'max_features': 'log2'}
        f2 score:0.14028776978417265
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 0.5}
        f2 score:0.15482054890921887
        params:{'n_estimators': 465, 'max_depth': 7, 'min_samples_split': 12, 'min_samples_leaf': 11, 'max_features': 'log2'}
        f2 score:0.11891279728199321
        params:{'n_estimators': 345, 'max_depth': 25, 'min_samples_split': 26, 'min_samples_leaf': 7, 'max_features': 0.5}
        f2 score:0.1558073654390935
        params:{'n_estimators': 279, 'max_depth': 10, 'min_samples_split': 22, 'min_samples_leaf': 10, 'max_features': 0.3}
        f2 score:0.16331658291457288
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.13456090651558072
        params:{'n_estimators': 504, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 'log2'}
        f2 score:0.14212827988338192
        params:{'n_estimators': 274, 'max_depth': 24, 'min_samples_split': 18, 'min_samples_leaf': 7, 'max_features': 0.5}
        f2 score:0.15732924021488873
        params:{'n_estimators': 405, 'max_depth': 5, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.14695077149155034
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 0.3}
        f2 score:0.1501072194424589
        params:{'n_estimators': 404, 'max_depth': 6, 'min_samples_split': 24, 'min_samples_leaf': 9, 'max_features': 'log2'}
        f2 score:0.11750881316098707
        params:{'n_estimators': 404, 'max_depth': 18, 'min_samples_split': 7, 'min_samples_leaf': 9, 'max_features': 'log2'}
        f2 score:0.12515262515262515
        params:{'n_estimators': 286, 'max_depth': 20, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.17458777885548013
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.14316392269148176
        params:{'n_estimators': 534, 'max_depth': 5, 'min_samples_split': 10, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.12492192379762648
        params:{'n_estimators': 535, 'max_depth': 12, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.5}
        f2 score:0.1598360655737705
        params:{'n_estimators': 447, 'max_depth': 8, 'min_samples_split': 18, 'min_samples_leaf': 8, 'max_features': 'sqrt'}
        f2 score:0.13020833333333334
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 7, 'max_features': 0.3}
        f2 score:0.16289592760180996
        params:{'n_estimators': 516, 'max_depth': 13, 'min_samples_split': 9, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.17635843660629172
        params:{'n_estimators': 197, 'max_depth': 7, 'min_samples_split': 24, 'min_samples_leaf': 11, 'max_features': 0.3}
        f2 score:0.1474820143884892
        params:{'n_estimators': 357, 'max_depth': 22, 'min_samples_split': 9, 'min_samples_leaf': 13, 'max_features': 'sqrt'}
        f2 score:0.1343381389252949
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.5}
        f2 score:0.1542513167795335
        params:{'n_estimators': 350, 'max_depth': 9, 'min_samples_split': 14, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.1527331189710611
        params:{'n_estimators': 457, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.15261627906976744
        params:{'n_estimators': 189, 'max_depth': 13, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.14874141876430205
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.3}
        f2 score:0.15879478827361562
        params:{'n_estimators': 269, 'max_depth': 24, 'min_samples_split': 29, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.15029325513196481
        params:{'n_estimators': 267, 'max_depth': 22, 'min_samples_split': 24, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.1475037821482602
        params:{'n_estimators': 272, 'max_depth': 6, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.11997600479904019
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 22, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.16726943942133815
        params:{'n_estimators': 287, 'max_depth': 25, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 'log2'}
        f2 score:0.20301624129930396
        params:{'n_estimators': 358, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 11, 'max_features': 0.3}
        f2 score:0.15905383360522024
        params:{'n_estimators': 473, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.16918967052537845
        params:{'n_estimators': 213, 'max_depth': 19, 'min_samples_split': 7, 'min_samples_leaf': 10, 'max_features': 'log2'}
        f2 score:0.13636363636363635
        params:{'n_estimators': 187, 'max_depth': 23, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.18907563025210083
        params:{'n_estimators': 230, 'max_depth': 17, 'min_samples_split': 9, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.16075845012366036
        params:{'n_estimators': 215, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 4, 'max_features': 0.3}
        f2 score:0.16853932584269662
        params:{'n_estimators': 507, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 14, 'max_features': 0.5}
        f2 score:0.13157894736842105
        params:{'n_estimators': 411, 'max_depth': 16, 'min_samples_split': 13, 'min_samples_leaf': 9, 'max_features': 0.3}
        f2 score:0.15879163439194424
        params:{'n_estimators': 282, 'max_depth': 5, 'min_samples_split': 8, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.1135718341851221
        params:{'n_estimators': 367, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 2, 'max_features': 0.3}
        f2 score:0.17479300827966882
        params:{'n_estimators': 274, 'max_depth': 17, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 0.3}
        f2 score:0.1589958158995816
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 'log2'}
        f2 score:0.15128006206361522
        params:{'n_estimators': 513, 'max_depth': 11, 'min_samples_split': 28, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.15267175572519084
        params:{'n_estimators': 384, 'max_depth': 26, 'min_samples_split': 15, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.2533532041728763
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.2534 | fp_per_day_val(val)=718.9512 <- choosen
        adjusted: threshold=0.7309 | F2(val)=0.4470 | fp_per_day_val(val)=149.4538
[INFO] Best configuration found with validation: {'n_estimators': 384, 'max_depth': 26, 'min_samples_split': 15, 'min_samples_leaf': 5, 'max_features': 'sqrt'} | F1(val)=0.2534
Final report -------------------------
              precision    recall  f1-score   support

   no_rf_eye       1.00      0.89      0.94      2616
      rf_eye       0.11      0.77      0.20        47

    accuracy                           0.89      2663
   macro avg       0.55      0.83      0.57      2663
weighted avg       0.98      0.89      0.93      2663

Confusion matrix -------------------------
[[2337  279]
 [  11   36]]
General metrics -------------------------
model                 rf_eye
sensitivity            0.766
specificity           0.8933
precision             0.1143
accuracy              0.8911
f1_score              0.1989
auc_roc               0.9503
false_alar_rate       0.1067
fp_per_day             452.6
TP                        36
FP                       279
TN                      2337
FN                        11
n_test_windows          2663
covered_test_hours     14.79
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_eye_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_eye_and_analysis_random.joblib

--------------------------------------------------
ARTIFACT: muscle | windows: 5s

--------------------------------------------------

Generating windows...
    Patient Session Section    Montage  Window_size  stride  Start  end Raw_labels  ... muscle  non_physiological  is_ambiguous  sample_weight distinguish  genuine_cooccurrence  weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar            5       5      0    5         []  ...      0                  0             0            1.0           0                     0             0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar            5       5      5   10         []  ...      0                  0             0            1.0           0                     0             0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar            5       5     10   15         []  ...      0                  0             0            1.0           0                     0             0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar            5       5     15   20         []  ...      0                  0             0            1.0           0                     0             0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar            5       5     20   25     [eyem]  ...      0                  0             0            1.0           0                     0             0              0           0

[5 rows x 33 columns]

Starting features extraction from channels and ICA components...
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob   ic_mean  ic_variance     ic_rms  ...  tuar_non_physiological  tuar_genuine_cooccurrence  tuar_weak_overlap  tuar_is_excluded  channels_eye  channels_muscle  channels_non_physiological
0         0        brain           clean         0.668147 -2.197917   261.640990  16.323965  ...                       0                          0                  0                 0            []               []                          []
1         1    eye blink             eye         0.974591 -0.115596     0.833358   0.920174  ...                       0                          0                  0                 0            []               []                          []
2         2        brain           clean         0.998497 -0.001832     0.052856   0.229912  ...                       0                          0                  0                 0            []               []                          []
3         3        brain           clean         0.985737  0.133040   178.135610  13.347408  ...                       0                          0                  0                 0            []               []                          []
4         4        brain           clean         0.998654  0.000667     0.040675   0.201681  ...                       0                          0                  0                 0            []               []                          []

[5 rows x 135 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob   ic_mean  ic_variance     ic_rms  ...  tuar_genuine_cooccurrence  tuar_weak_overlap  tuar_is_excluded  channels_eye  channels_muscle  channels_non_physiological  is_positive
0         0        brain           clean         0.668147 -2.197917   261.640990  16.323965  ...                          0                  0                 0            []               []                          []            0
1         1    eye blink             eye         0.974591 -0.115596     0.833358   0.920174  ...                          0                  0                 0            []               []                          []            0
2         2        brain           clean         0.998497 -0.001832     0.052856   0.229912  ...                          0                  0                 0            []               []                          []            0
3         3        brain           clean         0.985737  0.133040   178.135610  13.347408  ...                          0                  0                 0            []               []                          []            0
4         4        brain           clean         0.998654  0.000667     0.040675   0.201681  ...                          0                  0                 0            []               []                          []            0

[5 rows x 136 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_Fp1', 'ic_contrib_Fp2', 'ic_contrib_F3', 'ic_contrib_F4', 'ic_contrib_C3', 'ic_contrib_C4', 'ic_contrib_P3', 'ic_contrib_P4', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_F7', 'ic_contrib_F8', 'ic_contrib_T7', 'ic_contrib_T8', 'ic_contrib_P7', 'ic_contrib_P8', 'ic_contrib_Fz', 'ic_contrib_Cz', 'ic_contrib_Pz', 'ic_contrib_Ft9', 'ic_contrib_Ft10', 'Fp1_variance', 'Fp1_line_length', 'Fp1_peak_to_peak', 'Fp2_variance', 'Fp2_line_length', 'Fp2_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'Fz_variance', 'Fz_line_length', 'Fz_peak_to_peak', 'Cz_variance', 'Cz_line_length', 'Cz_peak_to_peak', 'Pz_variance', 'Pz_line_length', 'Pz_peak_to_peak', 'Ft9_variance', 'Ft9_line_length', 'Ft9_peak_to_peak', 'Ft10_variance', 'Ft10_line_length', 'Ft10_peak_to_peak', 'Patient', 'Session', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'channels_eye', 'channels_muscle', 'channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    81477
1     1012
Name: count, dtype: int64
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_muscle_sw0.0 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_muscle_sw0.3 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_muscle_sw0.5 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_muscle_sw0.7 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_muscle_sw1.0 parquet and json

[INFO] Sweep size weight results for muscle:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.3             0.0184      0.0113    0.0126       0.0071     0.7488   0.1454    0.1058    0.0488          0.0559
1.0             0.0159      0.0105    0.0188       0.0084     0.7389   0.1262    0.1350    0.0389          0.0472
0.7             0.0190      0.0105    0.0188       0.0085     0.7865   0.1057    0.1078    0.0865          0.0950
0.5             0.0196      0.0108    0.0155       0.0088     0.7782   0.1187    0.1031    0.0782          0.0871
0.0             0.0103      0.0162    0.0063       0.0099     0.5318   0.2890    0.1791    0.1682          0.1781
[INFO] Best suggested size weight for muscle: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_muscle_sw1.0 parquet and json
[INFO] Split distribution:  split
train    60949
test     11134
val      10406
Name: count, dtype: int64

Starting training of Random Forest (muscle)

============================================================
Modelo: rf_muscle
Train: 60949 (pos=639) | Val: 10406 (pos = 196) | Test: 11134 (pos=177)
[DEBUG] y_val dist (rf_muscle): {0: 10210, 1: 196}
[DEBUG] y_val hash (rf_muscle): 13192582570427786139
       ic_iclabel_prob   ic_mean  ic_variance    ic_rms  ic_skewness  ic_kurtosis    ic_zcr  ...  Pz_peak_to_peak  Ft9_variance  Ft9_line_length  Ft9_peak_to_peak  Ft10_variance  Ft10_line_length  Ft10_peak_to_peak
8342          0.574590 -0.004624     0.009586  0.098020     0.025493    -0.032391  0.173573  ...         0.000055  6.981430e-11         0.002279          0.000061   1.391130e-10          0.002329           0.000060
8343          0.471572  0.001707     0.014206  0.119200    -0.014295    -0.169514  0.187647  ...         0.000055  6.981430e-11         0.002279          0.000061   1.391130e-10          0.002329           0.000060
8344          0.485015 -0.001238     0.010110  0.100559    -0.115981    -0.355648  0.077404  ...         0.000055  6.981430e-11         0.002279          0.000061   1.391130e-10          0.002329           0.000060
8345          0.461798 -0.001398     0.009286  0.096373     0.062201     0.508493  0.092260  ...         0.000055  6.981430e-11         0.002279          0.000061   1.391130e-10          0.002329           0.000060
8346          0.558959 -0.002356     0.027100  0.164637    -0.069107    -0.014585  0.069586  ...         0.000055  6.981430e-11         0.002279          0.000061   1.391130e-10          0.002329           0.000060
...                ...       ...          ...       ...          ...          ...       ...  ...              ...           ...              ...               ...            ...               ...                ...
63705         0.976388  0.000818     0.936471  0.967715    -0.135705     1.422196  0.397185  ...         0.000035  1.286236e-09         0.004362          0.000220   8.051530e-10          0.003185           0.000164
63706         0.997074  0.001086     0.671340  0.819354    -1.278574     8.282017  0.351837  ...         0.000035  1.286236e-09         0.004362          0.000220   8.051530e-10          0.003185           0.000164
63707         0.493931 -0.016589     0.624657  0.790527    -0.128786     0.817568  0.268178  ...         0.000035  1.286236e-09         0.004362          0.000220   8.051530e-10          0.003185           0.000164
63708         0.448800 -0.007397     0.743975  0.862572     0.382967     0.373135  0.394840  ...         0.000035  1.286236e-09         0.004362          0.000220   8.051530e-10          0.003185           0.000164
63709         0.683256 -0.010506     1.110119  1.053674    -0.482179     4.302310  0.415168  ...         0.000035  1.286236e-09         0.004362          0.000220   8.051530e-10          0.003185           0.000164

[10406 rows x 116 columns]
[DEBUG] X_val hash (rf_muscle): 7996105293807356524
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.2836734693877551
        params:{'n_estimators': 536, 'max_depth': 7, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.1850574712643678
        params:{'n_estimators': 386, 'max_depth': 29, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.26714801444043323
        params:{'n_estimators': 503, 'max_depth': 17, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.23693605972086984
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.20895895895895897
        params:{'n_estimators': 439, 'max_depth': 15, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.23801865551624315
        params:{'n_estimators': 352, 'max_depth': 10, 'min_samples_split': 3, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.18926359256710254
        params:{'n_estimators': 178, 'max_depth': 26, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.28904227782571185
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.22718293164757014
        params:{'n_estimators': 586, 'max_depth': 16, 'min_samples_split': 13, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.23289246693502014
        params:{'n_estimators': 491, 'max_depth': 9, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.20169322709163345
        params:{'n_estimators': 169, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.2542103590721322
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.23649728347714924
        params:{'n_estimators': 296, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 1, 'max_features': 'log2'}
        f2 score:0.2583862194016319
        params:{'n_estimators': 508, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'sqrt'}
        f2 score:0.186660596403369
        params:{'n_estimators': 364, 'max_depth': 13, 'min_samples_split': 4, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.2189578713968958
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.23076923076923078
        params:{'n_estimators': 465, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.150510661171833
        params:{'n_estimators': 345, 'max_depth': 25, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.2478883584282042
        params:{'n_estimators': 279, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.2163604030823948
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 'sqrt'}
        f2 score:0.17761609244596618
        params:{'n_estimators': 504, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.24863760217983652
        params:{'n_estimators': 274, 'max_depth': 24, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5}
        f2 score:0.2646696758309397
        params:{'n_estimators': 405, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 2, 'max_features': 0.3}
        f2 score:0.16834677419354838
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.3}
        f2 score:0.23809523809523808
        params:{'n_estimators': 404, 'max_depth': 6, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'log2'}
        f2 score:0.14711033274956217
        params:{'n_estimators': 404, 'max_depth': 18, 'min_samples_split': 3, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.23644578313253012
        params:{'n_estimators': 286, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.24779735682819384
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.18497631400857206
        params:{'n_estimators': 534, 'max_depth': 5, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.16226195102992616
        params:{'n_estimators': 535, 'max_depth': 12, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.21544487968662562
        params:{'n_estimators': 447, 'max_depth': 8, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.16872095372802587
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.2247406838263542
        params:{'n_estimators': 516, 'max_depth': 13, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.21367521367521367
        params:{'n_estimators': 197, 'max_depth': 7, 'min_samples_split': 12, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.1891953498974242
        params:{'n_estimators': 357, 'max_depth': 22, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.2414113277623027
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5}
        f2 score:0.19596056744409715
        params:{'n_estimators': 350, 'max_depth': 9, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.2006980802792321
        params:{'n_estimators': 457, 'max_depth': 20, 'min_samples_split': 9, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.2374536881104749
        params:{'n_estimators': 189, 'max_depth': 13, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.2127659574468085
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.2598844957796535
        params:{'n_estimators': 269, 'max_depth': 24, 'min_samples_split': 14, 'min_samples_leaf': 2, 'max_features': 0.3}
        f2 score:0.25136798905608754
        params:{'n_estimators': 267, 'max_depth': 22, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.24268617021276595
        params:{'n_estimators': 272, 'max_depth': 6, 'min_samples_split': 3, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.14667365112624411
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.22262885025922538
        params:{'n_estimators': 287, 'max_depth': 25, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.2829334540516071
        params:{'n_estimators': 358, 'max_depth': 26, 'min_samples_split': 2, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.2461085401766933
        params:{'n_estimators': 473, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.2727981293842556
        params:{'n_estimators': 213, 'max_depth': 19, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 'log2'}
        f2 score:0.2453010512902198
        params:{'n_estimators': 187, 'max_depth': 23, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.2895419187554019
        params:{'n_estimators': 230, 'max_depth': 17, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.24075255102040816
        params:{'n_estimators': 215, 'max_depth': 21, 'min_samples_split': 3, 'min_samples_leaf': 2, 'max_features': 0.3}
        f2 score:0.23583305055989143
        params:{'n_estimators': 507, 'max_depth': 9, 'min_samples_split': 5, 'min_samples_leaf': 7, 'max_features': 0.5}
        f2 score:0.19289221416880992
        params:{'n_estimators': 411, 'max_depth': 16, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.23757079924480806
        params:{'n_estimators': 282, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.14251781472684086
        params:{'n_estimators': 367, 'max_depth': 16, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.3}
        f2 score:0.225939979303208
        params:{'n_estimators': 274, 'max_depth': 17, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.3}
        f2 score:0.23505708529214236
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.18492993337927865
        params:{'n_estimators': 513, 'max_depth': 11, 'min_samples_split': 14, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.20755222281735405
        params:{'n_estimators': 384, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.2737752161383285
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.2895 | fp_per_day_val(val)=2318.1703 <- choosen
        adjusted: threshold=0.8726 | F2(val)=0.3366 | fp_per_day_val(val)=745.6006
[INFO] Best configuration found with validation: {'n_estimators': 187, 'max_depth': 23, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt'} | F1(val)=0.2895
Final report -------------------------
              precision    recall  f1-score   support

no_rf_muscle       1.00      0.86      0.92     10957
   rf_muscle       0.08      0.75      0.14       177

    accuracy                           0.86     11134
   macro avg       0.54      0.80      0.53     11134
weighted avg       0.98      0.86      0.91     11134

Confusion matrix -------------------------
[[9417 1540]
 [  45  132]]
General metrics -------------------------
model                 rf_muscle
sensitivity              0.7458
specificity              0.8595
precision                0.0789
accuracy                 0.8576
f1_score                 0.1428
auc_roc                  0.8599
false_alar_rate          0.1405
fp_per_day              2390.08
TP                          132
FP                         1540
TN                         9417
FN                           45
n_test_windows            11134
covered_test_hours        15.46
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_muscle_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_muscle_and_analysis_random.joblib

--------------------------------------------------
ARTIFACT: non_physiological | windows: 1s

--------------------------------------------------

Generating windows...
    Patient Session Section    Montage  Window_size  stride  Start  end Raw_labels Label_spans  ...  eye  muscle  non_physiological is_ambiguous  sample_weight  distinguish  genuine_cooccurrence weak_overlap  is_unreviewed is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar            1       1      0    1         []          []  ...    0       0                  0            0            1.0            0                     0            0              0           0
1  aaaaaaju    s005    t000  01_tcp_ar            1       1      1    2         []          []  ...    0       0                  0            0            1.0            0                     0            0              0           0
2  aaaaaaju    s005    t000  01_tcp_ar            1       1      2    3         []          []  ...    0       0                  0            0            1.0            0                     0            0              0           0
3  aaaaaaju    s005    t000  01_tcp_ar            1       1      3    4         []          []  ...    0       0                  0            0            1.0            0                     0            0              0           0
4  aaaaaaju    s005    t000  01_tcp_ar            1       1      4    5         []          []  ...    0       0                  0            0            1.0            0                     0            0              0           0

[5 rows x 33 columns]

Starting features extraction from channels and ICA components...
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob    ic_mean  ic_variance  ...  tuar_genuine_cooccurrence  tuar_weak_overlap  tuar_is_excluded  channels_eye  channels_muscle  channels_non_physiological
0         0        brain           clean         0.668147 -20.668835   655.548249  ...                          0                  0                 0            []               []                          []
1         1    eye blink             eye         0.974591  -0.587446     3.884727  ...                          0                  0                 0            []               []                          []
2         2        brain           clean         0.998497  -0.046700     0.258632  ...                          0                  0                 0            []               []                          []
3         3        brain           clean         0.985737   1.221418   888.058062  ...                          0                  0                 0            []               []                          []
4         4        brain           clean         0.998654   0.024583     0.199335  ...                          0                  0                 0            []               []                          []

[5 rows x 135 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob    ic_mean  ic_variance     ic_rms  ...  tuar_genuine_cooccurrence  tuar_weak_overlap  tuar_is_excluded  channels_eye  channels_muscle  channels_non_physiological  is_positive
0         0        brain           clean         0.668147 -20.668835   655.548249  32.905151  ...                          0                  0                 0            []               []                          []            0
1         1    eye blink             eye         0.974591  -0.587446     3.884727   2.056653  ...                          0                  0                 0            []               []                          []            0
2         2        brain           clean         0.998497  -0.046700     0.258632   0.510698  ...                          0                  0                 0            []               []                          []            0
3         3        brain           clean         0.985737   1.221418   888.058062  29.825324  ...                          0                  0                 0            []               []                          []            0
4         4        brain           clean         0.998654   0.024583     0.199335   0.447146  ...                          0                  0                 0            []               []                          []            0

[5 rows x 136 columns]
['ic_index', 'ic_raw_label', 'ic_target_label', 'ic_iclabel_prob', 'ic_mean', 'ic_variance', 'ic_rms', 'ic_skewness', 'ic_kurtosis', 'ic_zcr', 'ic_hjorth_mobility', 'ic_hjorth_complexity', 'ic_line_length', 'ic_peak_to_peak', 'ic_peak_to_mean', 'ic_peak_position', 'ic_n_peaks', 'ic_baseline_shift', 'ic_delta_power', 'ic_theta_power', 'ic_alpha_power', 'ic_beta_power', 'ic_gamma_power', 'ic_ratio_high_low', 'ic_spectral_entropy', 'ic_dwt_energy_A4', 'ic_dwt_var_A4', 'ic_dwt_energy_D4', 'ic_dwt_var_D4', 'ic_dwt_energy_D3', 'ic_dwt_var_D3', 'ic_dwt_energy_D2', 'ic_dwt_var_D2', 'ic_dwt_energy_D1', 'ic_dwt_var_D1', 'ic_contrib_Fp1', 'ic_contrib_Fp2', 'ic_contrib_F3', 'ic_contrib_F4', 'ic_contrib_C3', 'ic_contrib_C4', 'ic_contrib_P3', 'ic_contrib_P4', 'ic_contrib_O1', 'ic_contrib_O2', 'ic_contrib_F7', 'ic_contrib_F8', 'ic_contrib_T7', 'ic_contrib_T8', 'ic_contrib_P7', 'ic_contrib_P8', 'ic_contrib_Fz', 'ic_contrib_Cz', 'ic_contrib_Pz', 'ic_contrib_Ft9', 'ic_contrib_Ft10', 'Fp1_variance', 'Fp1_line_length', 'Fp1_peak_to_peak', 'Fp2_variance', 'Fp2_line_length', 'Fp2_peak_to_peak', 'F3_variance', 'F3_line_length', 'F3_peak_to_peak', 'F4_variance', 'F4_line_length', 'F4_peak_to_peak', 'C3_variance', 'C3_line_length', 'C3_peak_to_peak', 'C4_variance', 'C4_line_length', 'C4_peak_to_peak', 'P3_variance', 'P3_line_length', 'P3_peak_to_peak', 'P4_variance', 'P4_line_length', 'P4_peak_to_peak', 'O1_variance', 'O1_line_length', 'O1_peak_to_peak', 'O2_variance', 'O2_line_length', 'O2_peak_to_peak', 'F7_variance', 'F7_line_length', 'F7_peak_to_peak', 'F8_variance', 'F8_line_length', 'F8_peak_to_peak', 'T7_variance', 'T7_line_length', 'T7_peak_to_peak', 'T8_variance', 'T8_line_length', 'T8_peak_to_peak', 'P7_variance', 'P7_line_length', 'P7_peak_to_peak', 'P8_variance', 'P8_line_length', 'P8_peak_to_peak', 'Fz_variance', 'Fz_line_length', 'Fz_peak_to_peak', 'Cz_variance', 'Cz_line_length', 'Cz_peak_to_peak', 'Pz_variance', 'Pz_line_length', 'Pz_peak_to_peak', 'Ft9_variance', 'Ft9_line_length', 'Ft9_peak_to_peak', 'Ft10_variance', 'Ft10_line_length', 'Ft10_peak_to_peak', 'Patient', 'Session', 'Start', 'split', 'tuar_is_clean_window', 'tuar_is_ambiguous', 'tuar_sample_weight', 'tuar_eye', 'tuar_muscle', 'tuar_non_physiological', 'tuar_genuine_cooccurrence', 'tuar_weak_overlap', 'tuar_is_excluded', 'channels_eye', 'channels_muscle', 'channels_non_physiological', 'is_positive']
[INFO] Positive count:
is_positive
0    415406
1      2584
Name: count, dtype: int64
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_non_physiological_sw0.0 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_non_physiological_sw0.3 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_non_physiological_sw0.5 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_non_physiological_sw0.7 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_non_physiological_sw1.0 parquet and json

[INFO] Sweep size weight results for non_physiological:
             test_rate  train_rate  val_rate  rate_spread  train_pct  val_pct  test_pct  size_dev  combined_score
size_weight
0.7             0.0051      0.0067    0.0047       0.0020     0.6930   0.1556    0.1514    0.0070          0.0090
0.5             0.0057      0.0068    0.0042       0.0027     0.6737   0.1751    0.1512    0.0263          0.0290
0.3             0.0041      0.0076    0.0039       0.0037     0.6053   0.1980    0.1967    0.0947          0.0983
1.0             0.0033      0.0072    0.0045       0.0039     0.6984   0.1530    0.1486    0.0030          0.0069
0.0             0.0019      0.0115    0.0070       0.0096     0.3767   0.1328    0.4905    0.3405          0.3502
[INFO] Best suggested size weight for non_physiological: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p30_v3_non_physiological_sw1.0 parquet and json
[INFO] Split distribution:  split
train    291921
val       63949
test      62120
Name: count, dtype: int64

Starting training of Random Forest (non_physiological)

============================================================
Modelo: rf_non_physiological
Train: 291921 (pos=2091) | Val: 63949 (pos = 288) | Test: 62120 (pos=205)
[DEBUG] y_val dist (rf_non_physiological): {0: 63661, 1: 288}
[DEBUG] y_val hash (rf_non_physiological): 13426045529429572135
        ic_iclabel_prob   ic_mean  ic_variance    ic_rms  ic_skewness  ic_kurtosis    ic_zcr  ...  Pz_peak_to_peak  Ft9_variance  Ft9_line_length  Ft9_peak_to_peak  Ft10_variance  Ft10_line_length  Ft10_peak_to_peak
18694          0.485032 -0.013838     0.026351  0.162919    -0.017119    -0.098192  0.411765  ...         0.000018  3.889192e-11         0.000905          0.000038   5.617099e-11          0.001206           0.000036
18695          0.476992 -0.037102     0.112078  0.336830    -0.215919    -0.191008  0.556863  ...         0.000018  3.889192e-11         0.000905          0.000038   5.617099e-11          0.001206           0.000036
18696          0.996422 -0.199559     0.407774  0.669027    -0.262384    -0.485576  0.137255  ...         0.000018  3.889192e-11         0.000905          0.000038   5.617099e-11          0.001206           0.000036
18697          0.997372  0.037411     0.501055  0.708840     0.087679     0.467397  0.227451  ...         0.000018  3.889192e-11         0.000905          0.000038   5.617099e-11          0.001206           0.000036
18698          0.991453 -0.018534     0.465716  0.682685    -0.525656     1.337213  0.529412  ...         0.000018  3.889192e-11         0.000905          0.000038   5.617099e-11          0.001206           0.000036
...                 ...       ...          ...       ...          ...          ...       ...  ...              ...           ...              ...               ...            ...               ...                ...
394193         0.998963 -0.044810     0.214566  0.465375     0.304724    -0.071976  0.203922  ...         0.000061  3.619838e-10         0.000826          0.000080   8.336842e-10          0.000749           0.000109
394194         0.962670 -0.002612     0.085900  0.293099     0.152622     0.219799  0.282353  ...         0.000061  3.619838e-10         0.000826          0.000080   8.336842e-10          0.000749           0.000109
394195         0.970779  0.042951     0.153477  0.394109    -0.044338     0.022375  0.364706  ...         0.000061  3.619838e-10         0.000826          0.000080   8.336842e-10          0.000749           0.000109
394196         0.355652 -0.072953     0.201642  0.454933    -0.280636     0.315708  0.301961  ...         0.000061  3.619838e-10         0.000826          0.000080   8.336842e-10          0.000749           0.000109
394197         0.941264  0.059386     0.438159  0.664594    -0.141351    -0.137880  0.313725  ...         0.000061  3.619838e-10         0.000826          0.000080   8.336842e-10          0.000749           0.000109

[63949 rows x 116 columns]
[DEBUG] X_val hash (rf_non_physiological): 1802116258614933884
        params:{'n_estimators': 190, 'max_depth': 28, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.11042097998619738
        params:{'n_estimators': 536, 'max_depth': 7, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.02689664414112602
        params:{'n_estimators': 386, 'max_depth': 34, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.10338225909380983
        params:{'n_estimators': 503, 'max_depth': 20, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.10401392961876833
        params:{'n_estimators': 375, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.044695652173913046
        params:{'n_estimators': 439, 'max_depth': 17, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.06670387943064471
        params:{'n_estimators': 352, 'max_depth': 11, 'min_samples_split': 3, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.0262522209578567
        params:{'n_estimators': 178, 'max_depth': 30, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.07607192254495158
        params:{'n_estimators': 224, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.07742673040947828
        params:{'n_estimators': 586, 'max_depth': 18, 'min_samples_split': 13, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.042428528134154965
        params:{'n_estimators': 491, 'max_depth': 10, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.0333181887021051
        params:{'n_estimators': 169, 'max_depth': 21, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.07541720154043646
        params:{'n_estimators': 565, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.12875808702270708
        params:{'n_estimators': 296, 'max_depth': 32, 'min_samples_split': 6, 'min_samples_leaf': 1, 'max_features': 'log2'}
        f2 score:0.08336140114516673
        params:{'n_estimators': 508, 'max_depth': 10, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'sqrt'}
        f2 score:0.028297639719596115
        params:{'n_estimators': 364, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.03792480222808213
        params:{'n_estimators': 573, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.036509095526842124
        params:{'n_estimators': 465, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.02363339249002829
        params:{'n_estimators': 345, 'max_depth': 29, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.042392951875710495
        params:{'n_estimators': 279, 'max_depth': 12, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.052599810295766145
        params:{'n_estimators': 524, 'max_depth': 10, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 'sqrt'}
        f2 score:0.025659467760433877
        params:{'n_estimators': 504, 'max_depth': 28, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.1182411627047666
        params:{'n_estimators': 274, 'max_depth': 28, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5}
        f2 score:0.052985911981049745
        params:{'n_estimators': 405, 'max_depth': 6, 'min_samples_split': 3, 'min_samples_leaf': 2, 'max_features': 0.3}
        f2 score:0.025357559836544075
        params:{'n_estimators': 347, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.3}
        f2 score:0.047731651777894554
        params:{'n_estimators': 404, 'max_depth': 7, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'log2'}
        f2 score:0.024341883973303592
        params:{'n_estimators': 404, 'max_depth': 21, 'min_samples_split': 3, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.0710193363571258
        params:{'n_estimators': 286, 'max_depth': 23, 'min_samples_split': 2, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.05003929787791459
        params:{'n_estimators': 592, 'max_depth': 11, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.0261701958286897
        params:{'n_estimators': 534, 'max_depth': 6, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.02421349086412969
        params:{'n_estimators': 535, 'max_depth': 13, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.03657020612297997
        params:{'n_estimators': 447, 'max_depth': 8, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.024699873238386398
        params:{'n_estimators': 598, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.054659183912077636
        params:{'n_estimators': 516, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.059562540667701086
        params:{'n_estimators': 197, 'max_depth': 7, 'min_samples_split': 12, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.024910905835002925
        params:{'n_estimators': 357, 'max_depth': 26, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.11114433811802232
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5}
        f2 score:0.025780392010870578
        params:{'n_estimators': 350, 'max_depth': 9, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.02975455300801689
        params:{'n_estimators': 457, 'max_depth': 23, 'min_samples_split': 9, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.03686769488360112
        params:{'n_estimators': 189, 'max_depth': 15, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.03398898911835405
        params:{'n_estimators': 314, 'max_depth': 32, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.09385877672799602
        params:{'n_estimators': 269, 'max_depth': 27, 'min_samples_split': 14, 'min_samples_leaf': 2, 'max_features': 0.3}
        f2 score:0.0392792933635582
        params:{'n_estimators': 267, 'max_depth': 26, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.10856453558504221
        params:{'n_estimators': 272, 'max_depth': 7, 'min_samples_split': 3, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.02353630808583203
        params:{'n_estimators': 207, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.044347082709980765
        params:{'n_estimators': 287, 'max_depth': 29, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.1135898485468686
        params:{'n_estimators': 358, 'max_depth': 30, 'min_samples_split': 2, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.09192266635037362
        params:{'n_estimators': 473, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.07333938674303275
        params:{'n_estimators': 213, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 'log2'}
        f2 score:0.08812457221081452
        params:{'n_estimators': 187, 'max_depth': 27, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.11180532719500165
        params:{'n_estimators': 230, 'max_depth': 19, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.0384279769096523
        params:{'n_estimators': 215, 'max_depth': 25, 'min_samples_split': 3, 'min_samples_leaf': 2, 'max_features': 0.3}
        f2 score:0.04612764346879879
        params:{'n_estimators': 507, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 7, 'max_features': 0.5}
        f2 score:0.02549296046659843
        params:{'n_estimators': 411, 'max_depth': 18, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.041373122424564666
        params:{'n_estimators': 282, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.022882181110029213
        params:{'n_estimators': 367, 'max_depth': 19, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.3}
        f2 score:0.07572815533980583
        params:{'n_estimators': 274, 'max_depth': 19, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.3}
        f2 score:0.05007089684509039
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.02924557453758884
        params:{'n_estimators': 513, 'max_depth': 13, 'min_samples_split': 14, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.029083530605343254
        params:{'n_estimators': 384, 'max_depth': 30, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.09903593339176162
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.1288 | fp_per_day_val(val)=8819.8283 <- choosen
        adjusted: threshold=0.7284 | F2(val)=0.1398 | fp_per_day_val(val)=3703.3011
[INFO] Best configuration found with validation: {'n_estimators': 565, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'log2'} | F1(val)=0.1288
Final report -------------------------
                         precision    recall  f1-score   support

no_rf_non_physiological       1.00      0.70      0.82     61915
   rf_non_physiological       0.01      0.89      0.02       205

               accuracy                           0.70     62120
              macro avg       0.50      0.79      0.42     62120
           weighted avg       1.00      0.70      0.82     62120

Confusion matrix -------------------------
[[43476 18439]
 [   23   182]]
General metrics -------------------------
model                 rf_non_physiological
sensitivity                         0.8878
specificity                         0.7022
precision                           0.0098
accuracy                            0.7028
f1_score                            0.0193
auc_roc                               0.89
false_alar_rate                     0.2978
fp_per_day                         25646.0
TP                                     182
FP                                   18439
TN                                   43476
FN                                      23
n_test_windows                       62120
covered_test_hours                   17.26
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_non_physiological_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_non_physiological_and_analysis_random.joblib

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Final report
---------- eye ----------
                 F1(val)=0.2534
                 best_params={'n_estimators': 384, 'max_depth': 26, 'min_samples_split': 15, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
                 Confusion matrix: [[2337  279]
 [  11   36]]
                 Metrics results: {'model': 'rf_eye', 'sensitivity': 0.766, 'specificity': np.float64(0.8933), 'precision': 0.1143, 'accuracy': 0.8911, 'f1_score': 0.1989, 'auc_roc': 0.9503, 'false_alar_rate': np.float64(0.1067), 'fp_per_day': np.float64(452.6), 'TP': 36, 'FP': 279, 'TN': 2337, 'FN': 11, 'n_test_windows': 2663, 'covered_test_hours': 14.79}
---------- muscle ----------
                 F1(val)=0.2895
                 best_params={'n_estimators': 187, 'max_depth': 23, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
                 Confusion matrix: [[9417 1540]
 [  45  132]]
                 Metrics results: {'model': 'rf_muscle', 'sensitivity': 0.7458, 'specificity': np.float64(0.8595), 'precision': 0.0789, 'accuracy': 0.8576, 'f1_score': 0.1428, 'auc_roc': 0.8599, 'false_alar_rate': np.float64(0.1405), 'fp_per_day': np.float64(2390.08), 'TP': 132, 'FP': 1540, 'TN': 9417, 'FN': 45, 'n_test_windows': 11134, 'covered_test_hours': 15.46}
---------- non_physiological ----------
                 F1(val)=0.1288
                 best_params={'n_estimators': 565, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'log2'}
                 Confusion matrix: [[43476 18439]
 [   23   182]]
                 Metrics results: {'model': 'rf_non_physiological', 'sensitivity': 0.8878, 'specificity': np.float64(0.7022), 'precision': 0.0098, 'accuracy': 0.7028, 'f1_score': 0.0193, 'auc_roc': 0.89, 'false_alar_rate': np.float64(0.2978), 'fp_per_day': np.float64(25646.0), 'TP': 182, 'FP': 18439, 'TN': 43476, 'FN': 23, 'n_test_windows': 62120, 'covered_test_hours': 17.26}
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis>