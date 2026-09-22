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



## Visualization of data distribution to correct training between corpus

dir> uv run python -m pipelines.artifacts.ica_cnn_rf

Loading all dataset for training...
  channel  start_time  stop_time label  confidence   Patient Session Section    Montage Partition  NoChannels  Duration                                                EDF                                                CSV
0  FP1-F7     22.9737    30.0688  eyem         1.0  aaaaaaju    s005    t000  01_tcp_ar                    36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7    136.7987   140.1117  eyem         1.0  aaaaaaju    s005    t000  01_tcp_ar                    36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7    145.0133   148.0498  eyem         1.0  aaaaaaju    s005    t000  01_tcp_ar                    36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3     22.9737    30.0688  eyem         1.0  aaaaaaju    s005    t000  01_tcp_ar                    36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3    136.7987   140.1117  eyem         1.0  aaaaaaju    s005    t000  01_tcp_ar                    36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
{'train': 4, 'test': 1}

==================================================
ARTIFACT: eye

==================================================
**************************************************
>> eye | windows: 2s (1s stride)

************************************************************
Generating windows...
[INFO] Windows loaded from cache: windows_w2_s1_ua0.15_ub0.1_urTrue_dcd979_L1.parquet (15427 rows)
    Patient Session Section    Montage Partition  Window_size  stride  Start  end Raw_labels  ...  eye  muscle  non_physiological is_ambiguous  sample_weight  distinguish  genuine_cooccurrence weak_overlap is_unreviewed  is_excluded
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1      0    2             ...    0       0                  0            0            1.0            0                     0            0             0            0
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1      1    3             ...    0       0                  0            0            1.0            0                     0            0             0            0
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1      2    4             ...    0       0                  0            0            1.0            0                     0            0             0            0
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1      3    5             ...    0       0                  0            0            1.0            0                     0            0             0            0
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1      4    6             ...    0       0                  0            0            1.0            0                     0            0             0            0

[5 rows x 36 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded']
Ventanas: 15427 -> sin ambiguas: 15370 | positivas: 2002
['Patient', 'Session', 'Section', 'Start', 'eye']

************************************************************
Size weight: 0.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_sw0.0_ua0.7 parquet and json
Size weight: 0.3
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_sw0.3_ua0.7 parquet and json
Size weight: 0.5
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_sw0.5_ua0.7 parquet and json
Size weight: 0.7
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_sw0.7_ua0.7 parquet and json
Size weight: 1.0
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_sw1.0_ua0.7 parquet and json

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
[INFO] Loading existing split from split_train70.0_val15.0_test15.0_p10_v1_eye_sw0.7_ua0.7 parquet and json
[INFO] Saving patient asignation for eye
[DEBUG] Split balance (positive rate):
        n_total  n_positive  n_negative  positive_rate
split
test      2664          35        2629       0.013138
train    10315        1749        8566       0.169559
val       2448         218        2230       0.089052
Broken rules: 0 | splits per patient: {'train': 6, 'test': 2, 'val': 2}
    Patient Session Section    Montage Partition  Window_size  stride  Start  end Raw_labels  ...  muscle  non_physiological  is_ambiguous sample_weight  distinguish  genuine_cooccurrence  weak_overlap is_unreviewed is_excluded  split
0  aaaaaaju    s005    t000  01_tcp_ar                      2       1      0    2             ...       0                  0             0           1.0            0                     0             0             0           0  train
1  aaaaaaju    s005    t000  01_tcp_ar                      2       1      1    3             ...       0                  0             0           1.0            0                     0             0             0           0  train
2  aaaaaaju    s005    t000  01_tcp_ar                      2       1      2    4             ...       0                  0             0           1.0            0                     0             0             0           0  train
3  aaaaaaju    s005    t000  01_tcp_ar                      2       1      3    5             ...       0                  0             0           1.0            0                     0             0             0           0  train
4  aaaaaaju    s005    t000  01_tcp_ar                      2       1      4    6             ...       0                  0             0           1.0            0                     0             0             0           0  train
5  aaaaaaju    s005    t000  01_tcp_ar                      2       1      5    7             ...       0                  0             0           1.0            0                     0             0             0           0  train
6  aaaaaaju    s005    t000  01_tcp_ar                      2       1      6    8             ...       0                  0             0           1.0            0                     0             0             0           0  train
7  aaaaaaju    s005    t000  01_tcp_ar                      2       1      7    9             ...       0                  0             0           1.0            0                     0             0             0           0  train
8  aaaaaaju    s005    t000  01_tcp_ar                      2       1      8   10             ...       0                  0             0           1.0            0                     0             0             0           0  train
9  aaaaaaju    s005    t000  01_tcp_ar                      2       1      9   11             ...       0                  0             0           1.0            0                     0             0             0           0  train

[10 rows x 37 columns]
['Patient', 'Session', 'Section', 'Montage', 'Partition', 'Window_size', 'stride', 'Start', 'end', 'Raw_labels', 'N_channels_annotated', 'No_channels', 'Session_duration', 'EDF_path', 'is_clean', 'is_excluded_unreviewed', 'coverage_eye', 'monopolar_channels_eye', 'bipolar_channels_eye', 'coverage_muscle', 'monopolar_channels_muscle', 'bipolar_channels_muscle', 'coverage_non_physiological', 'monopolar_channels_non_physiological', 'bipolar_channels_non_physiological', 'is_clean_window', 'eye', 'muscle', 'non_physiological', 'is_ambiguous', 'sample_weight', 'distinguish', 'genuine_cooccurrence', 'weak_overlap', 'is_unreviewed', 'is_excluded', 'split']

Starting features extraction from channels and ICA components...
    ic_index ic_raw_label ic_target_label  ic_iclabel_prob   ic_mean  ...  monopolar_channels_muscle  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological
0          0        brain           clean         0.687185 -5.572612  ...                         []                                    []                    []                       []                                  []
1          1    eye blink             eye         0.949668 -0.205541  ...                         []                                    []                    []                       []                                  []
2          2        brain           clean         0.994398  0.024749  ...                         []                                    []                    []                       []                                  []
3          3        other             NaN         0.726641 -6.139340  ...                         []                                    []                    []                       []                                  []
4          4        brain           clean         0.999643  0.029892  ...                         []                                    []                    []                       []                                  []
5          5        brain           clean         0.993584  3.231581  ...                         []                                    []                    []                       []                                  []
6          6        brain           clean         0.999535 -0.055872  ...                         []                                    []                    []                       []                                  []
7          7        brain           clean         0.978230 -0.261133  ...                         []                                    []                    []                       []                                  []
8          8    eye blink             eye         0.823060 -0.000386  ...                         []                                    []                    []                       []                                  []
9          9        brain           clean         0.773097 -0.002573  ...                         []                                    []                    []                       []                                  []
10        10        brain           clean         0.919012 -0.800122  ...                         []                                    []                    []                       []                                  []
11        11        brain           clean         0.936563  0.033306  ...                         []                                    []                    []                       []                                  []
12         0        brain           clean         0.687185  4.834056  ...                         []                                    []                    []                       []                                  []
13         1    eye blink             eye         0.949668  0.008954  ...                         []                                    []                    []                       []                                  []
14         2        brain           clean         0.994398  0.017750  ...                         []                                    []                    []                       []                                  []
15         3        other             NaN         0.726641  0.039946  ...                         []                                    []                    []                       []                                  []
16         4        brain           clean         0.999643 -0.008541  ...                         []                                    []                    []                       []                                  []
17         5        brain           clean         0.993584  0.191285  ...                         []                                    []                    []                       []                                  []
18         6        brain           clean         0.999535 -0.023079  ...                         []                                    []                    []                       []                                  []
19         7        brain           clean         0.978230  0.032919  ...                         []                                    []                    []                       []                                  []
20         8    eye blink             eye         0.823060  0.010806  ...                         []                                    []                    []                       []                                  []
21         9        brain           clean         0.773097 -0.016280  ...                         []                                    []                    []                       []                                  []
22        10        brain           clean         0.919012 -0.118276  ...                         []                                    []                    []                       []                                  []
23        11        brain           clean         0.936563  0.000676  ...                         []                                    []                    []                       []                                  []
24         0        brain           clean         0.687185 -0.169162  ...                         []                                    []                    []                       []                                  []

[25 rows x 132 columns]
[INFO] Successful features extraction
   ic_index ic_raw_label ic_target_label  ic_iclabel_prob   ic_mean  ...  monopolar_channels_non_physiological  bipolar_channels_eye  bipolar_channels_muscle  bipolar_channels_non_physiological  is_positive
0         0        brain           clean         0.687185 -5.572612  ...                                    []                    []                       []                                  []            0
1         1    eye blink             eye         0.949668 -0.205541  ...                                    []                    []                       []                                  []            0
2         2        brain           clean         0.994398  0.024749  ...                                    []                    []                       []                                  []            0
3         3        other             NaN         0.726641 -6.139340  ...                                    []                    []                       []                                  []            0
4         4        brain           clean         0.999643  0.029892  ...                                    []                    []                       []                                  []            0

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

============================================================
Modelo: rf_eye_w2s1_1
Train: 137926 (pos=1749) | Val: 32679 (pos = 218) | Test: 30862 (pos=35)
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\pipelines\artifacts\ica_cnn_rf.py", line 243, in <module>
    results.setdefault(artifact, []).append(  train_binary_model( df=rf_features_dataset,
                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\src\models\ml_models.py", line 283, in train_binary_model
    best_model, best_params, best_score = _search_random(X_train, y_train, X_val, y_val, search_kwargs, search_data, verbose, build_model_fn, balanced)
                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\src\models\ml_models.py", line 152, in _search_random
    model.fit(X_train, y_train)
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\sklearn\base.py", line 1329, in wrapper
    estimator._validate_params()
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\sklearn\base.py", line 492, in _validate_params
    validate_parameter_constraints(
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\.venv\Lib\site-packages\sklearn\utils\_param_validation.py", line 98, in validate_parameter_constraints
    raise InvalidParameterError(
sklearn.utils._param_validation.InvalidParameterError: The 'max_depth' parameter of BalancedRandomForestClassifier must be an int in the range [1, inf) or None. Got 24.0 instead.
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis>



#### Results

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

============================================================
Modelo: rf_eye_w2s1_1
Train: 137926 (pos=1749) | Val: 32679 (pos = 218) | Test: 30862 (pos=35)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.33861386138613864
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.21930870083432658
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.13485067754242863
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.3008365508365508
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.14536225196123673
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.23996952767902488
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.24691358024691357
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2449091909741332
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.1863157894736842
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.19057377049180327
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2856681730148483
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.17286004806803476
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.25116822429906543
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.23989569752281617
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.16896011147883644
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.24481327800829875
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.16034985422740525
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.21171062182434067
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.14626218851570963
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.16076341127922972
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.17363045496750232
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.37272727272727274
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.24271844660194175
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.20022497187851518
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.36363636363636365
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.13869625520110956
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1871871871871872
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.21292858702773532
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2034498009730208
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.16216216216216217
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.275
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.18315358869468204
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1949831365935919
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.2540786306499064
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.11369908378408213
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.17651362721785258
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.2537182852143482
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.12956642649475414
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.16426563598032326
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.14985727878211227
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.23246650906225375
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2762520193861066
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.10163183509876897
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.1761160293840648
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 27, 'min_samples_leaf': 8, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.14815389388768227
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.13811420982735723
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 9, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2770618556701031
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 22, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.20515574650912996
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 28, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.20514455782312926
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 13, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.12728380024360536
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.1570593149540518
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 24, 'min_samples_leaf': 14, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1755868544600939
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 11, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.21601447636281385
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 23, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.21322994911558033
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.12746305418719212
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 22, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.2241094597782496
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 25, 'min_samples_leaf': 9, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.1935483870967742
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.18751208196404406
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2176498572787821
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 12, 'min_samples_leaf': 10, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.2185294787161393
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.3727 | fp_per_day_val(val)=1538.7497 <- choosen
        adjusted: threshold=0.6482 | F2(val)=0.4975 | fp_per_day_val(val)=545.9653
[INFO] Best configuration found with validation: {'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3} | F1(val)=0.3727
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
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w2s1_1_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w2s1_1_and_analysis_random.joblib
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
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s1_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s1_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s1_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s1_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s1_sw1.0_ua0.3

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

============================================================
Modelo: rf_eye_w1s1_1
Train: 137545 (pos=1499) | Val: 32694 (pos = 208) | Test: 30793 (pos=25)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2892561983471074
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.19406392694063926
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.12335526315789473
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2572976226301535
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.1381340579710145
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.22524752475247525
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.22100760456273763
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2222222222222222
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.1689119170984456
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.17493897477624085
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2511415525114155
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.15792244253377785
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2292920607623961
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.21342215642733778
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.15963803995219394
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.20080321285140562
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.15011345784604643
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1777382803821373
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.13867838739011823
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.15087347803070408
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.1630730204747237
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.3157894736842105
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2189519023689878
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.16500305561214096
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.300794551645857
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.13861684496007232
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.17227564102564102
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.18949268097052335
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.17981806642690926
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1458538184201901
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.25659001682557486
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.16512662559890487
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.17693588676103247
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.2336567926455567
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.10887679146761471
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.16993820428934933
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.22784810126582278
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.11932731544454062
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.15437084903966972
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.1457840819542947
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.20019895548371053
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.24760136180748993
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.10361892978657594
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.16875602700096431
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 27, 'min_samples_leaf': 8, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.14592813431664836
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1251604621309371
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 9, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.24851190476190477
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 22, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.18612693246541903
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 28, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1855176540993417
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 13, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.1260770400405474
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.15193823915900131
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 24, 'min_samples_leaf': 14, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.15730748125114322
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 11, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.197522955370489
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 23, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.17782195714601282
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.11704462326261887
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 22, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.20039207144412982
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 25, 'min_samples_leaf': 9, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.1780185758513932
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.17399267399267399
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.19039185299977862
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 12, 'min_samples_leaf': 10, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.19885762640152316
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.3158 | fp_per_day_val(val)=4151.6609 <- choosen
        adjusted: threshold=0.7746 | F2(val)=0.4831 | fp_per_day_val(val)=692.3839
[INFO] Best configuration found with validation: {'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3} | F1(val)=0.3158
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
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w1s1_1_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w1s1_1_and_analysis_random.joblib
**************************************************
>> eye | windows: 1s (0.5s stride)

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
Ventanas: 30890 -> sin ambiguas: 30705 | positivas: 3573
['Patient', 'Session', 'Section', 'Start', 'eye']

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s0.5_sw0.0_ua0.3
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s0.5_sw0.3_ua0.3
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s0.5_sw0.5_ua0.3
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s0.5_sw0.7_ua0.3
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w1_s0.5_sw1.0_ua0.3

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

============================================================
Modelo: rf_eye_w1s0.5_1
Train: 275530 (pos=3104) | Val: 65429 (pos = 414) | Test: 61675 (pos=55)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.30902004454342985
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.23917031183857768
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.1261232349165597
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2950257289879931
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.12592389816589106
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.22127231581594167
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.2347814776274714
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2084844089920232
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.1966324530042671
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.22946859903381642
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.25742574257425743
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.2123981229933317
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2143765903307888
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.20771513353115728
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1577834179357022
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.2435488547405045
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.16549648946840523
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1820140010770059
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.1289277159363111
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.137890625
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.16917827694057436
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.32952980523313
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2415491993978377
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.17515274949083504
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.31037093111279335
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.12074851435073966
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.2223083882641851
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.21540086864655475
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.17145135566188197
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1361079865016873
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.2539891670326453
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.19339920117721252
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.20114606478774413
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.22160314043307586
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.10476342032675579
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.16169694862209857
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.23624275003536568
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.11883218723609604
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.14505189180354663
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.16124636627906977
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.20307022845400702
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.21907894736842104
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.08974932855863921
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.2035366722050795
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 27, 'min_samples_leaf': 8, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.13009845288326302
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.12502373868456035
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 9, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2452937820878494
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 22, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.17521658717025212
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 28, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1735576923076923
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 13, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.12537200025327677
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.1875532821824382
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 24, 'min_samples_leaf': 14, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.14834425953941838
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 11, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.22278481012658227
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 23, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1841190527916576
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.10822868473231989
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 22, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1886394772894931
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 25, 'min_samples_leaf': 9, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.16991200149784685
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.16860570805308125
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.223782648641554
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 12, 'min_samples_leaf': 10, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.1998685795641222
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.3295 | fp_per_day_val(val)=4083.0335 <- choosen
        adjusted: threshold=0.7195 | F2(val)=0.4773 | fp_per_day_val(val)=1204.3100
[INFO] Best configuration found with validation: {'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3} | F1(val)=0.3295
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
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w1s0.5_1_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w1s0.5_1_and_analysis_random.joblib
**************************************************
>> eye | windows: 0.5s (0.5s stride)

************************************************************
Generating windows...
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
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.5_sw0.0_ua0.6
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.5_sw0.3_ua0.6
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.5_sw0.5_ua0.6
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.5_sw0.7_ua0.6
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.5_sw1.0_ua0.6

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

============================================================
Modelo: rf_eye_w0.5s0.5_1
Train: 275199 (pos=2841) | Val: 65430 (pos = 402) | Test: 61646 (pos=45)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2852464667356084
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.23356524208433907
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.11972633979475485
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.26757188498402557
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.12106865065945215
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2137546468401487
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.21616893664875672
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.20066492519591547
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.18040957850254632
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.22176068605118585
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.24269728237174829
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.2157948982221077
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.2108782306802109
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.19425106669660902
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1629106706489275
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.23899462443701874
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.17317073170731706
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.18954918032786885
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.12137902896776825
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.15839836492010406
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.17857142857142858
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.29940658155008093
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.23292136357462992
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.18231984418956937
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.28650807431845804
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.15126737530662307
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.21685173089483997
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.19779975552839205
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.18075549301872498
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.14123601926687893
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.2348993288590604
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.17520085180524633
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1931106471816284
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.20271066588096642
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.10813124108416548
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.15721358464344654
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.22802883282506237
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.12378193310508297
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.1734622669723856
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.18808091853471842
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.1953493862134089
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.218436873747495
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.09218219539796303
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.20693928128872366
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 27, 'min_samples_leaf': 8, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.1491671500787271
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.11391570238023863
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 9, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2275189599133261
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 22, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.1736800317586344
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 28, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1657280029544825
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 13, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.11823370758326539
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.20515896820635873
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 24, 'min_samples_leaf': 14, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.17213690655425073
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 11, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.21212493851451059
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 23, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.18903269754768393
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.13003355704697986
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 22, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.178117048346056
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 25, 'min_samples_leaf': 9, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.16871019865031842
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.16041374474053297
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.22764900662251655
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 12, 'min_samples_leaf': 10, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.18480387110058685
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.2994 | fp_per_day_val(val)=9560.3851 <- choosen
        adjusted: threshold=0.7974 | F2(val)=0.4631 | fp_per_day_val(val)=1756.2586
[INFO] Best configuration found with validation: {'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3} | F1(val)=0.2994
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
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w0.5s0.5_1_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w0.5s0.5_1_and_analysis_random.joblib
**************************************************
>> eye | windows: 0.5s (0.25s stride)

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
Ventanas: 61816 -> sin ambiguas: 61298 | positivas: 6528
['Patient', 'Session', 'Section', 'Start', 'eye']

************************************************************
Size weight: 0.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.25_sw0.0_ua0.6
Size weight: 0.3
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.25_sw0.3_ua0.6
Size weight: 0.5
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.25_sw0.5_ua0.6
Size weight: 0.7
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.25_sw0.7_ua0.6
Size weight: 1.0
[INFO] Existing split metadata does not match current configuration.
[INFO] Computing and saving new split...
[INFO] Saved new split to split_train70.0_val15.0_test15.0_p10_v1_eye_w0.5_s0.25_sw1.0_ua0.6

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

============================================================
Modelo: rf_eye_w0.5s0.25_1
Train: 549626 (pos=5634) | Val: 130872 (pos = 804) | Test: 123308 (pos=90)
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.29931662870159453
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.24304021210782148
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.11713276061658441
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.286192396807689
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.14134203548847643
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.2150065818341378
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.23351182810275875
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.20331280272678348
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.17651411055913752
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.21709412836870198
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.24367967265819085
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.2425091614572106
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.20895145508490626
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.19414475162957967
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.1606019272231267
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.22768166089965397
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.16099690740403858
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.18751749230338652
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.14120143650016323
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.3}
        f2 score:0.16239641870654348
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 0.3, 'sampling_strategy': 0.7}
        f2 score:0.16655450874831762
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.2969003424040368
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.2454565201650858
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.18353846988017133
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.29312338759896805
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.1394055536767745
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.20908750468106355
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.21298669595996583
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.17612726615360777
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.14983783783783783
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 'log2', 'sampling_strategy': 0.5}
        f2 score:0.24132301795727162
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.1880122127591194
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.17830609212481427
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.2048322468751869
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.10771086365038848
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.15286973390123562
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5, 'sampling_strategy': 0.7}
        f2 score:0.20303477085637056
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.11966242599823655
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.16360015174506828
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.17240523913474895
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 7, 'max_features': 0.5, 'sampling_strategy': 0.5}
        f2 score:0.1834837147887324
        params:{'n_estimators': 338, 'max_depth': 25, 'min_samples_split': 13, 'min_samples_leaf': 4, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.21102856410913282
        params:{'n_estimators': 300, 'max_depth': 5, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.08687982359426681
        params:{'n_estimators': 497, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.19177146759232913
        params:{'n_estimators': 472, 'max_depth': 9, 'min_samples_split': 27, 'min_samples_leaf': 8, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.14452271071168327
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.11463421943836725
        params:{'n_estimators': 373, 'max_depth': 16, 'min_samples_split': 9, 'min_samples_leaf': 6, 'max_features': 'sqrt', 'sampling_strategy': 0.3}
        f2 score:0.23606811145510836
        params:{'n_estimators': 257, 'max_depth': 12, 'min_samples_split': 22, 'min_samples_leaf': 10, 'max_features': 'sqrt', 'sampling_strategy': 0.5}
        f2 score:0.17157813105854983
        params:{'n_estimators': 423, 'max_depth': 14, 'min_samples_split': 28, 'min_samples_leaf': 3, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.16327367126656647
        params:{'n_estimators': 304, 'max_depth': 7, 'min_samples_split': 13, 'min_samples_leaf': 14, 'max_features': 'sqrt', 'sampling_strategy': 1.0}
        f2 score:0.1179530045509427
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.5, 'sampling_strategy': 1.0}
        f2 score:0.21546541795861546
        params:{'n_estimators': 355, 'max_depth': 11, 'min_samples_split': 24, 'min_samples_leaf': 14, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.1715119203299467
        params:{'n_estimators': 268, 'max_depth': 24, 'min_samples_split': 11, 'min_samples_leaf': 11, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.22633744855967078
        params:{'n_estimators': 505, 'max_depth': 16, 'min_samples_split': 23, 'min_samples_leaf': 5, 'max_features': 0.3, 'sampling_strategy': 0.3}
        f2 score:0.18900826911177365
        params:{'n_estimators': 185, 'max_depth': 7, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 0.3, 'sampling_strategy': 1.0}
        f2 score:0.12131715771230503
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 22, 'min_samples_leaf': 4, 'max_features': 'log2', 'sampling_strategy': 1.0}
        f2 score:0.17874445407720946
        params:{'n_estimators': 474, 'max_depth': 12, 'min_samples_split': 25, 'min_samples_leaf': 9, 'max_features': 'sqrt', 'sampling_strategy': 0.7}
        f2 score:0.16130508397016427
        params:{'n_estimators': 396, 'max_depth': 9, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'log2', 'sampling_strategy': 0.3}
        f2 score:0.15876767069135908
        params:{'n_estimators': 158, 'max_depth': 23, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.3, 'sampling_strategy': 0.5}
        f2 score:0.21405155235585266
        params:{'n_estimators': 448, 'max_depth': 15, 'min_samples_split': 12, 'min_samples_leaf': 10, 'max_features': 'log2', 'sampling_strategy': 0.7}
        f2 score:0.18168753849312255
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.2993 | fp_per_day_val(val)=9377.2969 <- choosen
        adjusted: threshold=0.7931 | F2(val)=0.4183 | fp_per_day_val(val)=2434.7699
[INFO] Best configuration found with validation: {'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt', 'sampling_strategy': 0.3} | F1(val)=0.2993
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
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w0.5s0.25_1_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\models\rf_eye_w0.5s0.25_1_and_analysis_random.joblib

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Final report
---------- eye ----------
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\pipelines\artifacts\ica_cnn_rf.py", line 275, in <module>
    print(f"\t\t F1(val)={res['val_f1']:.4f}")
                          ~~~^^^^^^^^^^
TypeError: list indices must be integers or slices, not str


#### General trained model (subset)


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
