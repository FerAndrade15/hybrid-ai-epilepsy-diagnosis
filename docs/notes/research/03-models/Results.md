# Artifacts

## ICA+ICLabel + RF
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> uv run python -m implementation.models.rf_model

Loading 25 artifact patients, 1 sessions per patient for testing...
  channel  start_time  stop_time label  confidence   Patient  ... Section    Montage NoChannels  Duration                                                EDF                                                CSV
0  FP1-F7     22.9737    30.0688  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7    136.7987   140.1117  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7    145.0133   148.0498  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3     22.9737    30.0688  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3    136.7987   140.1117  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

[5 rows x 13 columns]

--------------------------------------------------
ARTIFACT: eye | windows: 20s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_eye.parquet
[INFO] Split distribution:  split
train    10231
test      2395
val       2287
Name: count, dtype: int64

Starting training of Random Forest (eye)

============================================================
Modelo: rf_eye
Train: 10231 (pos=303) | Val: 2287 (pos = 29) | Test: 2395 (pos=24)
[DEBUG] y_val dist (rf_eye): {0: 2258, 1: 29}
[DEBUG] y_val hash (rf_eye): 11912536868275785955
[DEBUG] X_val hash (rf_eye): 11445343832670305202
        params:{'max_depth': None, 'n_estimators': 200}
        f1 score:0.5853658536585366
        params:{'max_depth': None, 'n_estimators': 400}
        f1 score:0.6190476190476191
        params:{'max_depth': 20, 'n_estimators': 200}
        f1 score:0.6363636363636364
        params:{'max_depth': 20, 'n_estimators': 400}
        f1 score:0.6222222222222222
[INFO] Threshold óptimo (val): 0.2890 | F1(val) con threshold=0.7077 (vs 0.5 -> 0.6364)
[INFO] Comparation between threshold=0.5 and adjusted threshold
              sensitivity  specificity  precision  f1_score  fp_per_day
model
rf_eye_thr05         0.75       0.9992     0.9000    0.8182        3.61
rf_eye               1.00       0.9941     0.6316    0.7742       25.25
Best configuration found with validation: {'max_depth': 20, 'n_estimators': 200} | F1(val)=0.6364
Final report
              precision    recall  f1-score   support

   no_rf_eye       1.00      0.99      1.00      2371
      rf_eye       0.63      1.00      0.77        24

    accuracy                           0.99      2395
   macro avg       0.82      1.00      0.89      2395
weighted avg       1.00      0.99      0.99      2395

Confusion matrix
[[2357   14]
 [   0   24]]
General metrics
model                 rf_eye
sensitivity              1.0
specificity           0.9941
precision             0.6316
accuracy              0.9942
f1_score              0.7742
auc_roc               0.9992
false_alar_rate       0.0059
fp_per_day             25.25
TP                        24
FP                        14
TN                      2357
FN                         0
n_test_windows          2395
covered_test_hours     13.31
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_eye_grid.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_eye_and_analysis_grid.joblib

--------------------------------------------------
ARTIFACT: muscle | windows: 5s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_muscle.parquet
[INFO] Split distribution:  split
train    43130
test     10590
val       9703
Name: count, dtype: int64

Starting training of Random Forest (muscle)

============================================================
Modelo: rf_muscle
Train: 43130 (pos=1525) | Val: 9703 (pos = 245) | Test: 10590 (pos=392)
[DEBUG] y_val dist (rf_muscle): {0: 9458, 1: 245}
[DEBUG] y_val hash (rf_muscle): 15688256561422212987
[DEBUG] X_val hash (rf_muscle): 12322128536613835801
        params:{'max_depth': None, 'n_estimators': 200}
        f1 score:0.13620071684587814
        params:{'max_depth': None, 'n_estimators': 400}
        f1 score:0.15492957746478872
        params:{'max_depth': 20, 'n_estimators': 200}
        f1 score:0.42701525054466233
        params:{'max_depth': 20, 'n_estimators': 400}
        f1 score:0.4217391304347826
[INFO] Threshold óptimo (val): 0.4727 | F1(val) con threshold=0.4646 (vs 0.5 -> 0.4270)
[INFO] Comparation between threshold=0.5 and adjusted threshold
                 sensitivity  specificity  precision  f1_score  fp_per_day
model
rf_muscle_thr05       0.1709       0.9911     0.4241    0.2436      148.49
rf_muscle             0.2066       0.9896     0.4332    0.2798      172.96
Best configuration found with validation: {'max_depth': 20, 'n_estimators': 200} | F1(val)=0.4270
Final report
              precision    recall  f1-score   support

no_rf_muscle       0.97      0.99      0.98     10198
   rf_muscle       0.43      0.21      0.28       392

    accuracy                           0.96     10590
   macro avg       0.70      0.60      0.63     10590
weighted avg       0.95      0.96      0.95     10590

Confusion matrix
[[10092   106]
 [  311    81]]
General metrics
model                 rf_muscle
sensitivity              0.2066
specificity              0.9896
precision                0.4332
accuracy                 0.9606
f1_score                 0.2798
auc_roc                  0.9736
false_alar_rate          0.0104
fp_per_day               172.96
TP                           81
FP                          106
TN                        10092
FN                          311
n_test_windows            10590
covered_test_hours        14.71
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_muscle_grid.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_muscle_and_analysis_grid.joblib

--------------------------------------------------
ARTIFACT: non_physiological | windows: 1s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_non_physiological.parquet
[INFO] Split distribution:  split
train    238861
val       48026
test      35070
Name: count, dtype: int64

Starting training of Random Forest (non_physiological)

============================================================
Modelo: rf_non_physiological
Train: 238861 (pos=11914) | Val: 48026 (pos = 212) | Test: 35070 (pos=353)
[DEBUG] y_val dist (rf_non_physiological): {0: 47814, 1: 212}
[DEBUG] y_val hash (rf_non_physiological): 3087459260785746475
[DEBUG] X_val hash (rf_non_physiological): 2152757767067955685
        params:{'max_depth': None, 'n_estimators': 200}
        f1 score:0.0
        params:{'max_depth': None, 'n_estimators': 400}
        f1 score:0.0
        params:{'max_depth': 20, 'n_estimators': 200}
        f1 score:0.40898876404494383
        params:{'max_depth': 20, 'n_estimators': 400}
        f1 score:0.42701525054466233
[INFO] Threshold óptimo (val): 0.4564 | F1(val) con threshold=0.4649 (vs 0.5 -> 0.4270)
[INFO] Comparation between threshold=0.5 and adjusted threshold
                            sensitivity  specificity  precision  f1_score  fp_per_day
model
rf_non_physiological_thr05       0.0198       0.9826     0.0115    0.0145     1488.04
rf_non_physiological             0.0198       0.9671     0.0061    0.0093     2815.95
Best configuration found with validation: {'max_depth': 20, 'n_estimators': 400} | F1(val)=0.4270
Final report
                         precision    recall  f1-score   support

no_rf_non_physiological       0.99      0.97      0.98     34717
   rf_non_physiological       0.01      0.02      0.01       353

               accuracy                           0.96     35070
              macro avg       0.50      0.49      0.49     35070
           weighted avg       0.98      0.96      0.97     35070

Confusion matrix
[[33574  1143]
 [  346     7]]
General metrics
model                 rf_non_physiological
sensitivity                         0.0198
specificity                         0.9671
precision                           0.0061
accuracy                            0.9575
f1_score                            0.0093
auc_roc                             0.7221
false_alar_rate                     0.0329
fp_per_day                         2815.95
TP                                       7
FP                                    1143
TN                                   33574
FN                                     346
n_test_windows                       35070
covered_test_hours                    9.74
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_non_physiological_grid.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_non_physiological_and_analysis_grid.joblib

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Final report
---------- eye ----------
                 F1(val)=0.6364
                 best_params={'max_depth': 20, 'n_estimators': 200}
                 Confusion matrix: [[2357   14]
 [   0   24]]
                 Metrics results: {'model': 'rf_eye', 'sensitivity': 1.0, 'specificity': np.float64(0.9941), 'precision': 0.6316, 'accuracy': 0.9942, 'f1_score': 0.7742, 'auc_roc': 0.9992, 'false_alar_rate': np.float64(0.0059), 'fp_per_day': np.float64(25.25), 'TP': 24, 'FP': 14, 'TN': 2357, 'FN': 0, 'n_test_windows': 2395, 'covered_test_hours': 13.31}
---------- muscle ----------
                 F1(val)=0.4270
                 best_params={'max_depth': 20, 'n_estimators': 200}
                 Confusion matrix: [[10092   106]
 [  311    81]]
                 Metrics results: {'model': 'rf_muscle', 'sensitivity': 0.2066, 'specificity': np.float64(0.9896), 'precision': 0.4332, 'accuracy': 0.9606, 'f1_score': 0.2798, 'auc_roc': 0.9736, 'false_alar_rate': np.float64(0.0104), 'fp_per_day': np.float64(172.96), 'TP': 81, 'FP': 106, 'TN': 10092, 'FN': 311, 'n_test_windows': 10590, 'covered_test_hours': 14.71}
---------- non_physiological ----------
                 F1(val)=0.4270
                 best_params={'max_depth': 20, 'n_estimators': 400}
                 Confusion matrix: [[33574  1143]
 [  346     7]]
                 Metrics results: {'model': 'rf_non_physiological', 'sensitivity': 0.0198, 'specificity': np.float64(0.9671), 'precision': 0.0061, 'accuracy': 0.9575, 'f1_score': 0.0093, 'auc_roc': 0.7221, 'false_alar_rate': np.float64(0.0329), 'fp_per_day': np.float64(2815.95), 'TP': 7, 'FP': 1143, 'TN': 33574, 'FN': 346, 'n_test_windows': 35070, 'covered_test_hours': 9.74}
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis>

#### Balanced 
Loading 25 artifact patients, 1 sessions per patient for testing...
  channel  start_time  stop_time label  confidence   Patient  ... Section    Montage NoChannels  Duration                                                EDF                                                CSV
0  FP1-F7     22.9737    30.0688  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7    136.7987   140.1117  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7    145.0133   148.0498  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3     22.9737    30.0688  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3    136.7987   140.1117  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

[5 rows x 13 columns]

--------------------------------------------------
ARTIFACT: eye | windows: 20s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_eye.parquet
[INFO] Split distribution:  split
train    10231
test      2395
val       2287
Name: count, dtype: int64

Starting training of Random Forest (eye)

============================================================
Modelo: rf_eye
Train: 10231 (pos=303) | Val: 2287 (pos = 29) | Test: 2395 (pos=24)
[DEBUG] y_val dist (rf_eye): {0: 2258, 1: 29}
[DEBUG] y_val hash (rf_eye): 11912536868275785955
[DEBUG] X_val hash (rf_eye): 11445343832670305202
        params:{'max_depth': None, 'n_estimators': 200}
        f1 score:0.23829787234042554
        params:{'max_depth': None, 'n_estimators': 400}
        f1 score:0.23829787234042554
        params:{'max_depth': 20, 'n_estimators': 200}
        f1 score:0.2222222222222222
        params:{'max_depth': 20, 'n_estimators': 400}
        f1 score:0.22134387351778656
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.4321 | fp_per_day_val(val)=340.0087
        adjusted: threshold=0.8250 | F2(val)=0.5128 | fp_per_day_val(val)=45.3345 <- choosen
[INFO] Best configuration found with validation: {'max_depth': None, 'n_estimators': 200} | F1(val)=0.2383
Final report -------------------------
              precision    recall  f1-score   support

   no_rf_eye       0.99      0.99      0.99      2371
      rf_eye       0.38      0.33      0.36        24

    accuracy                           0.99      2395
   macro avg       0.69      0.66      0.67      2395
weighted avg       0.99      0.99      0.99      2395

Confusion matrix -------------------------
[[2358   13]
 [  16    8]]
General metrics -------------------------
model                 rf_eye
sensitivity           0.3333
specificity           0.9945
precision              0.381
accuracy              0.9879
f1_score              0.3556
auc_roc               0.9578
false_alar_rate       0.0055
fp_per_day             23.45
TP                         8
FP                        13
TN                      2358
FN                        16
n_test_windows          2395
covered_test_hours     13.31
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_eye_grid.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_eye_and_analysis_grid.joblib

--------------------------------------------------
ARTIFACT: muscle | windows: 5s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_muscle.parquet
[INFO] Split distribution:  split
train    43130
test     10590
val       9703
Name: count, dtype: int64

Starting training of Random Forest (muscle)

============================================================
Modelo: rf_muscle
Train: 43130 (pos=1525) | Val: 9703 (pos = 245) | Test: 10590 (pos=392)
[DEBUG] y_val dist (rf_muscle): {0: 9458, 1: 245}
[DEBUG] y_val hash (rf_muscle): 15688256561422212987
[DEBUG] X_val hash (rf_muscle): 12322128536613835801
        params:{'max_depth': None, 'n_estimators': 200}
        f1 score:0.27011494252873564
        params:{'max_depth': None, 'n_estimators': 400}
        f1 score:0.2603978300180832
        params:{'max_depth': 20, 'n_estimators': 200}
        f1 score:0.18910675381263617
        params:{'max_depth': 20, 'n_estimators': 400}
        f1 score:0.18482407799915218
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.3959 | fp_per_day_val(val)=1216.3496 <- choosen
        adjusted: threshold=0.5200 | F2(val)=0.4082 | fp_per_day_val(val)=1059.6310
[INFO] Best configuration found with validation: {'max_depth': None, 'n_estimators': 200} | F1(val)=0.2701
Final report -------------------------
              precision    recall  f1-score   support

no_rf_muscle       0.99      0.95      0.97     10198
   rf_muscle       0.42      0.87      0.57       392

    accuracy                           0.95     10590
   macro avg       0.71      0.91      0.77     10590
weighted avg       0.97      0.95      0.96     10590

Confusion matrix -------------------------
[[9732  466]
 [  51  341]]
General metrics -------------------------
model                 rf_muscle
sensitivity              0.8699
specificity              0.9543
precision                0.4226
accuracy                 0.9512
f1_score                 0.5688
auc_roc                  0.9706
false_alar_rate          0.0457
fp_per_day               760.39
TP                          341
FP                          466
TN                         9732
FN                           51
n_test_windows            10590
covered_test_hours        14.71
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_muscle_grid.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_muscle_and_analysis_grid.joblib

--------------------------------------------------
ARTIFACT: non_physiological | windows: 1s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_non_physiological.parquet
[INFO] Split distribution:  split
train    238861
val       48026
test      35070
Name: count, dtype: int64

Starting training of Random Forest (non_physiological)

============================================================
Modelo: rf_non_physiological
Train: 238861 (pos=11914) | Val: 48026 (pos = 212) | Test: 35070 (pos=353)
[DEBUG] y_val dist (rf_non_physiological): {0: 47814, 1: 212}
[DEBUG] y_val hash (rf_non_physiological): 3087459260785746475
[DEBUG] X_val hash (rf_non_physiological): 2152757767067955685
        params:{'max_depth': None, 'n_estimators': 200}
        f1 score:0.0
        params:{'max_depth': None, 'n_estimators': 400}
        f1 score:0.0
        params:{'max_depth': 20, 'n_estimators': 200}
        f1 score:0.0846201358863496
        params:{'max_depth': 20, 'n_estimators': 400}
        f1 score:0.08330817989737398
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.1768 | fp_per_day_val(val)=5197.3847 <- choosen
        adjusted: threshold=0.7353 | F2(val)=0.3819 | fp_per_day_val(val)=1324.0828
[INFO] Best configuration found with validation: {'max_depth': 20, 'n_estimators': 200} | F1(val)=0.0846
Final report -------------------------
                         precision    recall  f1-score   support

no_rf_non_physiological       1.00      0.75      0.85     34717
   rf_non_physiological       0.03      0.76      0.06       353

               accuracy                           0.75     35070
              macro avg       0.51      0.75      0.45     35070
           weighted avg       0.99      0.75      0.85     35070

Confusion matrix -------------------------
[[25888  8829]
 [   86   267]]
General metrics -------------------------
model                 rf_non_physiological
sensitivity                         0.7564
specificity                         0.7457
precision                           0.0294
accuracy                            0.7458
f1_score                            0.0565
auc_roc                             0.7767
false_alar_rate                     0.2543
fp_per_day                        21751.51
TP                                     267
FP                                    8829
TN                                   25888
FN                                      86
n_test_windows                       35070
covered_test_hours                    9.74
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_non_physiological_grid.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_non_physiological_and_analysis_grid.joblib

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Final report
---------- eye ----------
                 F1(val)=0.2383
                 best_params={'max_depth': None, 'n_estimators': 200}
                 Confusion matrix: [[2358   13]
 [  16    8]]
                 Metrics results: {'model': 'rf_eye', 'sensitivity': 0.3333, 'specificity': np.float64(0.9945), 'precision': 0.381, 'accuracy': 0.9879, 'f1_score': 0.3556, 'auc_roc': 0.9578, 'false_alar_rate': np.float64(0.0055), 'fp_per_day': np.float64(23.45), 'TP': 8, 'FP': 13, 'TN': 2358, 'FN': 16, 'n_test_windows': 2395, 'covered_test_hours': 13.31}
---------- muscle ----------
                 F1(val)=0.2701
                 best_params={'max_depth': None, 'n_estimators': 200}
                 Confusion matrix: [[9732  466]
 [  51  341]]
                 Metrics results: {'model': 'rf_muscle', 'sensitivity': 0.8699, 'specificity': np.float64(0.9543), 'precision': 0.4226, 'accuracy': 0.9512, 'f1_score': 0.5688, 'auc_roc': 0.9706, 'false_alar_rate': np.float64(0.0457), 'fp_per_day': np.float64(760.39), 'TP': 341, 'FP': 466, 'TN': 9732, 'FN': 51, 'n_test_windows': 10590, 'covered_test_hours': 14.71}
---------- non_physiological ----------
                 F1(val)=0.0846
                 best_params={'max_depth': 20, 'n_estimators': 200}
                 Confusion matrix: [[25888  8829]
 [   86   267]]
                 Metrics results: {'model': 'rf_non_physiological', 'sensitivity': 0.7564, 'specificity': np.float64(0.7457), 'precision': 0.0294, 'accuracy': 0.7458, 'f1_score': 0.0565, 'auc_roc': 0.7767, 'false_alar_rate': np.float64(0.2543), 'fp_per_day': np.float64(21751.51), 'TP': 267, 'FP': 8829, 'TN': 25888, 'FN': 86, 'n_test_windows': 35070, 'covered_test_hours': 9.74}
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> 


#### Resultados random search
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> uv run python -m implementation.models.rf_model

Loading 25 artifact patients, 1 sessions per patient for testing...
  channel  start_time  stop_time label  confidence   Patient  ... Section    Montage NoChannels  Duration                                                EDF                                                CSV
0  FP1-F7     22.9737    30.0688  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7    136.7987   140.1117  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7    145.0133   148.0498  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3     22.9737    30.0688  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3    136.7987   140.1117  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

[5 rows x 13 columns]

--------------------------------------------------
ARTIFACT: eye | windows: 20s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_eye.parquet
[INFO] Split distribution:  split
train    10231
test      2395
val       2287
Name: count, dtype: int64

Starting training of Random Forest (eye)

============================================================
Modelo: rf_eye
Train: 10231 (pos=303) | Val: 2287 (pos = 29) | Test: 2395 (pos=24)
[DEBUG] y_val dist (rf_eye): {0: 2258, 1: 29}
[DEBUG] y_val hash (rf_eye): 11912536868275785955
[DEBUG] X_val hash (rf_eye): 11445343832670305202
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.6164383561643836
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.7333333333333333
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 0.3}
        f2 score:0.7386363636363636
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'log2'}
        f2 score:0.7046979865771812
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.75
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.695364238410596
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.7333333333333333
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.5755395683453237
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5}
        f2 score:0.5555555555555556
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.6506849315068494
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.684931506849315
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'sqrt'}
        f2 score:0.7046979865771812
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.5797101449275363
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.5597014925373134
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.7361963190184049
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.7333333333333333
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.6012658227848101
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.5797101449275363
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.6145251396648045
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.3}
        f2 score:0.6441717791411042
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.7333333333333333
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.5797101449275363
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 0.5}
        f2 score:0.5921052631578947
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.6081081081081081
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.5714285714285714
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.7419354838709677
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 'log2'}
        f2 score:0.6802721088435374
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 0.3}
        f2 score:0.6081081081081081
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 'sqrt'}
        f2 score:0.6711409395973155
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.75
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.5782312925170068
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.7333333333333333
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.3}
        f2 score:0.5704697986577181
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.625
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 0.3}
        f2 score:0.625
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.7236842105263158
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5}
        f2 score:0.5755395683453237
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.6756756756756757
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.5}
        f2 score:0.5792682926829268
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.7189542483660131
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.7500 | fp_per_day_val(val)=37.7787 <- choosen
        adjusted: threshold=0.5229 | F2(val)=0.7500 | fp_per_day_val(val)=37.7787
[INFO] Best configuration found with validation: {'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 'log2'} | F1(val)=0.7500
Final report -------------------------
              precision    recall  f1-score   support

   no_rf_eye       1.00      1.00      1.00      2371
      rf_eye       0.71      1.00      0.83        24

    accuracy                           1.00      2395
   macro avg       0.85      1.00      0.91      2395
weighted avg       1.00      1.00      1.00      2395

Confusion matrix -------------------------
[[2361   10]
 [   0   24]]
General metrics -------------------------
model                 rf_eye
sensitivity              1.0
specificity           0.9958
precision             0.7059
accuracy              0.9958
f1_score              0.8276
auc_roc               0.9994
false_alar_rate       0.0042
fp_per_day             18.04
TP                        24
FP                        10
TN                      2361
FN                         0
n_test_windows          2395
covered_test_hours     13.31
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_eye_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_eye_and_analysis_random.joblib

--------------------------------------------------
ARTIFACT: muscle | windows: 5s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_muscle.parquet
[INFO] Split distribution:  split
train    43130
test     10590
val       9703
Name: count, dtype: int64

Starting training of Random Forest (muscle)

============================================================
Modelo: rf_muscle
Train: 43130 (pos=1525) | Val: 9703 (pos = 245) | Test: 10590 (pos=392)
[DEBUG] y_val dist (rf_muscle): {0: 9458, 1: 245}
[DEBUG] y_val hash (rf_muscle): 15688256561422212987
[DEBUG] X_val hash (rf_muscle): 12322128536613835801
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.5332829046898638
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.5571740713765477
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 0.3}
        f2 score:0.546875
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'log2'}
        f2 score:0.5651274982770503
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.5760485093481557
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.604153555695406
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.5611150822015726
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.5527817403708987
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5}
        f2 score:0.3796095444685466
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.5326965466568699
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.5161787365177196
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'sqrt'}
        f2 score:0.5677785663591199
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.4600484261501211
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.5339805825242718
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.5725971370143149
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.5880376344086021
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.48094940662086194
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.557541100786276
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.537867824409069
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.3}
        f2 score:0.5973451327433629
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.6072607260726073
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.4838709677419355
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 0.5}
        f2 score:0.3951367781155015
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.5409836065573771
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.3952569169960474
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.5818278427205101
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 'log2'}
        f2 score:0.5614783226723525
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 0.3}
        f2 score:0.49888309754281457
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 'sqrt'}
        f2 score:0.5696636925188744
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.5868295273499734
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.3819709702062643
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.549645390070922
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.3}
        f2 score:0.4799107142857143
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.4538690476190476
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 0.3}
        f2 score:0.46701112877583467
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.6062322946175638
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5}
        f2 score:0.3456998313659359
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.5110132158590308
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.5}
        f2 score:0.5214541120381406
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.5612594113620808
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.6073 | fp_per_day_val(val)=625.0933 <- choosen
        adjusted: threshold=0.4874 | F2(val)=0.6048 | fp_per_day_val(val)=674.9583
[INFO] Best configuration found with validation: {'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 'sqrt'} | F1(val)=0.6073
Final report -------------------------
              precision    recall  f1-score   support

no_rf_muscle       0.98      0.98      0.98     10198
   rf_muscle       0.44      0.38      0.41       392

    accuracy                           0.96     10590
   macro avg       0.71      0.68      0.69     10590
weighted avg       0.96      0.96      0.96     10590

Confusion matrix -------------------------
[[10008   190]
 [  243   149]]
General metrics -------------------------
model                 rf_muscle
sensitivity              0.3801
specificity              0.9814
precision                0.4395
accuracy                 0.9591
f1_score                 0.4077
auc_roc                  0.9732
false_alar_rate          0.0186
fp_per_day               310.03
TP                          149
FP                          190
TN                        10008
FN                          243
n_test_windows            10590
covered_test_hours        14.71
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_muscle_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_muscle_and_analysis_random.joblib

--------------------------------------------------
ARTIFACT: non_physiological | windows: 1s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_non_physiological.parquet
[INFO] Split distribution:  split
train    238861
val       48026
test      35070
Name: count, dtype: int64

Starting training of Random Forest (non_physiological)

============================================================
Modelo: rf_non_physiological
Train: 238861 (pos=11914) | Val: 48026 (pos = 212) | Test: 35070 (pos=353)
[DEBUG] y_val dist (rf_non_physiological): {0: 47814, 1: 212}
[DEBUG] y_val hash (rf_non_physiological): 3087459260785746475
[DEBUG] X_val hash (rf_non_physiological): 2152757767067955685
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.4969217238346526
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.5085470085470085
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 0.3}
        f2 score:0.43348916277093075
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'log2'}
        f2 score:0.4601899196493791
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.5455537370430987
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.5978934324659232
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.49058084772370486
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.46360153256704983
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5}
        f2 score:0.4571026722925457
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.4934747145187602
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.45004500450045004
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'sqrt'}
        f2 score:0.48621745788667686
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.46354635463546356
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.4804421768707483
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.5488803932277444
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.5021367521367521
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.4375
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.4708171206225681
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.2564102564102564
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.3}
        f2 score:0.4834761321909425
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.4715622750179986
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.40111940298507465
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 0.5}
        f2 score:0.471976401179941
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.4647887323943662
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.4702194357366771
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.5641025641025641
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 'log2'}
        f2 score:0.4836193447737909
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 0.3}
        f2 score:0.483271375464684
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 'sqrt'}
        f2 score:0.4606741573033708
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.5489130434782609
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.4584527220630373
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.4661016949152542
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.3}
        f2 score:0.46943231441048033
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.4706734250543085
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 0.3}
        f2 score:0.2719112988384372
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.5862898376428142
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5}
        f2 score:0.5071315372424723
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.4714352066883418
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.5}
        f2 score:0.42426147077309867
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.47919762258543835
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.5979 | fp_per_day_val(val)=1030.8416 <- choosen
        adjusted: threshold=0.5467 | F2(val)=0.6258 | fp_per_day_val(val)=825.7527
[INFO] Best configuration found with validation: {'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'} | F1(val)=0.5979
Final report -------------------------
                         precision    recall  f1-score   support

no_rf_non_physiological       0.99      0.89      0.94     34717
   rf_non_physiological       0.01      0.13      0.02       353

               accuracy                           0.88     35070
              macro avg       0.50      0.51      0.48     35070
           weighted avg       0.98      0.88      0.93     35070

Confusion matrix -------------------------
[[30800  3917]
 [  308    45]]
General metrics -------------------------
model                 rf_non_physiological
sensitivity                         0.1275
specificity                         0.8872
precision                           0.0114
accuracy                            0.8795
f1_score                            0.0209
auc_roc                              0.733
false_alar_rate                     0.1128
fp_per_day                         9650.09
TP                                      45
FP                                    3917
TN                                   30800
FN                                     308
n_test_windows                       35070
covered_test_hours                    9.74
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_non_physiological_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_non_physiological_and_analysis_random.joblib

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Final report
---------- eye ----------
                 F1(val)=0.7500
                 best_params={'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 'log2'}
                 Confusion matrix: [[2361   10]
 [   0   24]]
                 Metrics results: {'model': 'rf_eye', 'sensitivity': 1.0, 'specificity': np.float64(0.9958), 'precision': 0.7059, 'accuracy': 0.9958, 'f1_score': 0.8276, 'auc_roc': 0.9994, 'false_alar_rate': np.float64(0.0042), 'fp_per_day': np.float64(18.04), 'TP': 24, 'FP': 10, 'TN': 2361, 'FN': 0, 'n_test_windows': 2395, 'covered_test_hours': 13.31}
---------- muscle ----------
                 F1(val)=0.6073
                 best_params={'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
                 Confusion matrix: [[10008   190]
 [  243   149]]
                 Metrics results: {'model': 'rf_muscle', 'sensitivity': 0.3801, 'specificity': np.float64(0.9814), 'precision': 0.4395, 'accuracy': 0.9591, 'f1_score': 0.4077, 'auc_roc': 0.9732, 'false_alar_rate': np.float64(0.0186), 'fp_per_day': np.float64(310.03), 'TP': 149, 'FP': 190, 'TN': 10008, 'FN': 243, 'n_test_windows': 10590, 'covered_test_hours': 14.71}
---------- non_physiological ----------
                 F1(val)=0.5979
                 best_params={'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'}
                 Confusion matrix: [[30800  3917]
 [  308    45]]
                 Metrics results: {'model': 'rf_non_physiological', 'sensitivity': 0.1275, 'specificity': np.float64(0.8872), 'precision': 0.0114, 'accuracy': 0.8795, 'f1_score': 0.0209, 'auc_roc': 0.733, 'false_alar_rate': np.float64(0.1128), 'fp_per_day': np.float64(9650.09), 'TP': 45, 'FP': 3917, 'TN': 30800, 'FN': 308, 'n_test_windows': 35070, 'covered_test_hours': 9.74}
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> 


#### Random Search - Standard RF
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> uv run python -m implementation.models.rf_model

Loading 25 artifact patients, 1 sessions per patient for testing...
  channel  start_time  stop_time label  confidence   Patient  ... Section    Montage NoChannels  Duration                                                EDF                                                CSV
0  FP1-F7     22.9737    30.0688  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7    136.7987   140.1117  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7    145.0133   148.0498  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3     22.9737    30.0688  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3    136.7987   140.1117  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

[5 rows x 13 columns]

--------------------------------------------------
ARTIFACT: eye | windows: 20s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_eye.parquet
[INFO] Split distribution:  split
train    10231
test      2395
val       2287
Name: count, dtype: int64

Starting training of Random Forest (eye)

============================================================
Modelo: rf_eye
Train: 10231 (pos=303) | Val: 2287 (pos = 29) | Test: 2395 (pos=24)
[DEBUG] y_val dist (rf_eye): {0: 2258, 1: 29}
[DEBUG] y_val hash (rf_eye): 11912536868275785955
[DEBUG] X_val hash (rf_eye): 11445343832670305202
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.6164383561643836
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.7333333333333333
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 0.3}
        f2 score:0.7386363636363636
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'log2'}
        f2 score:0.7046979865771812
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.75
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.695364238410596
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.7333333333333333
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.5755395683453237
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5}
        f2 score:0.5555555555555556
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.6506849315068494
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.684931506849315
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'sqrt'}
        f2 score:0.7046979865771812
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.5797101449275363
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.5597014925373134
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.7361963190184049
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.7333333333333333
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.6012658227848101
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.5797101449275363
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.6145251396648045
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.3}
        f2 score:0.6441717791411042
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.7333333333333333
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.5797101449275363
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 0.5}
        f2 score:0.5921052631578947
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.6081081081081081
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.5714285714285714
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.7419354838709677
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 'log2'}
        f2 score:0.6802721088435374
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 0.3}
        f2 score:0.6081081081081081
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 'sqrt'}
        f2 score:0.6711409395973155
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.75
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.5782312925170068
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.7333333333333333
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.3}
        f2 score:0.5704697986577181
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.625
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 0.3}
        f2 score:0.625
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.7236842105263158
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5}
        f2 score:0.5755395683453237
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.6756756756756757
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.5}
        f2 score:0.5792682926829268
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.7189542483660131
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.7500 | fp_per_day_val(val)=37.7787 <- choosen
        adjusted: threshold=0.5229 | F2(val)=0.7500 | fp_per_day_val(val)=37.7787
[INFO] Best configuration found with validation: {'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 'log2'} | F1(val)=0.7500
Final report -------------------------
              precision    recall  f1-score   support

   no_rf_eye       1.00      1.00      1.00      2371
      rf_eye       0.71      1.00      0.83        24

    accuracy                           1.00      2395
   macro avg       0.85      1.00      0.91      2395
weighted avg       1.00      1.00      1.00      2395

Confusion matrix -------------------------
[[2361   10]
 [   0   24]]
General metrics -------------------------
model                 rf_eye
sensitivity              1.0
specificity           0.9958
precision             0.7059
accuracy              0.9958
f1_score              0.8276
auc_roc               0.9994
false_alar_rate       0.0042
fp_per_day             18.04
TP                        24
FP                        10
TN                      2361
FN                         0
n_test_windows          2395
covered_test_hours     13.31
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_eye_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_eye_and_analysis_random.joblib

--------------------------------------------------
ARTIFACT: muscle | windows: 5s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_muscle.parquet
[INFO] Split distribution:  split
train    43130
test     10590
val       9703
Name: count, dtype: int64

Starting training of Random Forest (muscle)

============================================================
Modelo: rf_muscle
Train: 43130 (pos=1525) | Val: 9703 (pos = 245) | Test: 10590 (pos=392)
[DEBUG] y_val dist (rf_muscle): {0: 9458, 1: 245}
[DEBUG] y_val hash (rf_muscle): 15688256561422212987
[DEBUG] X_val hash (rf_muscle): 12322128536613835801
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.5332829046898638
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.5571740713765477
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 0.3}
        f2 score:0.546875
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'log2'}
        f2 score:0.5651274982770503
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.5760485093481557
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.604153555695406
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.5611150822015726
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.5527817403708987
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5}
        f2 score:0.3796095444685466
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.5326965466568699
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.5161787365177196
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'sqrt'}
        f2 score:0.5677785663591199
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.4600484261501211
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.5339805825242718
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.5725971370143149
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.5880376344086021
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.48094940662086194
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.557541100786276
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.537867824409069
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.3}
        f2 score:0.5973451327433629
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.6072607260726073
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.4838709677419355
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 0.5}
        f2 score:0.3951367781155015
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.5409836065573771
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.3952569169960474
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.5818278427205101
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 'log2'}
        f2 score:0.5614783226723525
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 0.3}
        f2 score:0.49888309754281457
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 'sqrt'}
        f2 score:0.5696636925188744
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.5868295273499734
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.3819709702062643
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.549645390070922
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.3}
        f2 score:0.4799107142857143
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.4538690476190476
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 0.3}
        f2 score:0.46701112877583467
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.6062322946175638
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5}
        f2 score:0.3456998313659359
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.5110132158590308
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.5}
        f2 score:0.5214541120381406
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.5612594113620808
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.6073 | fp_per_day_val(val)=625.0933 <- choosen
        adjusted: threshold=0.4874 | F2(val)=0.6048 | fp_per_day_val(val)=674.9583
[INFO] Best configuration found with validation: {'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 'sqrt'} | F1(val)=0.6073
Final report -------------------------
              precision    recall  f1-score   support

no_rf_muscle       0.98      0.98      0.98     10198
   rf_muscle       0.44      0.38      0.41       392

    accuracy                           0.96     10590
   macro avg       0.71      0.68      0.69     10590
weighted avg       0.96      0.96      0.96     10590

Confusion matrix -------------------------
[[10008   190]
 [  243   149]]
General metrics -------------------------
model                 rf_muscle
sensitivity              0.3801
specificity              0.9814
precision                0.4395
accuracy                 0.9591
f1_score                 0.4077
auc_roc                  0.9732
false_alar_rate          0.0186
fp_per_day               310.03
TP                          149
FP                          190
TN                        10008
FN                          243
n_test_windows            10590
covered_test_hours        14.71
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_muscle_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_muscle_and_analysis_random.joblib

--------------------------------------------------
ARTIFACT: non_physiological | windows: 1s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_non_physiological.parquet
[INFO] Split distribution:  split
train    238861
val       48026
test      35070
Name: count, dtype: int64

Starting training of Random Forest (non_physiological)

============================================================
Modelo: rf_non_physiological
Train: 238861 (pos=11914) | Val: 48026 (pos = 212) | Test: 35070 (pos=353)
[DEBUG] y_val dist (rf_non_physiological): {0: 47814, 1: 212}
[DEBUG] y_val hash (rf_non_physiological): 3087459260785746475
[DEBUG] X_val hash (rf_non_physiological): 2152757767067955685
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.4969217238346526
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.5085470085470085
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 0.3}
        f2 score:0.43348916277093075
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'log2'}
        f2 score:0.4601899196493791
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.5455537370430987
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.5978934324659232
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.49058084772370486
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.46360153256704983
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5}
        f2 score:0.4571026722925457
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.4934747145187602
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.45004500450045004
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'sqrt'}
        f2 score:0.48621745788667686
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.46354635463546356
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.4804421768707483
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.5488803932277444
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.5021367521367521
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.4375
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.4708171206225681
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.2564102564102564
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.3}
        f2 score:0.4834761321909425
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.4715622750179986
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.40111940298507465
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 0.5}
        f2 score:0.471976401179941
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.4647887323943662
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.4702194357366771
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.5641025641025641
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 'log2'}
        f2 score:0.4836193447737909
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 0.3}
        f2 score:0.483271375464684
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 'sqrt'}
        f2 score:0.4606741573033708
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.5489130434782609
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.4584527220630373
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.4661016949152542
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.3}
        f2 score:0.46943231441048033
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.4706734250543085
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 0.3}
        f2 score:0.2719112988384372
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.5862898376428142
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5}
        f2 score:0.5071315372424723
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.4714352066883418
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.5}
        f2 score:0.42426147077309867
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.47919762258543835
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.5979 | fp_per_day_val(val)=1030.8416 <- choosen
        adjusted: threshold=0.5467 | F2(val)=0.6258 | fp_per_day_val(val)=825.7527
[INFO] Best configuration found with validation: {'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'} | F1(val)=0.5979
Final report -------------------------
                         precision    recall  f1-score   support

no_rf_non_physiological       0.99      0.89      0.94     34717
   rf_non_physiological       0.01      0.13      0.02       353

               accuracy                           0.88     35070
              macro avg       0.50      0.51      0.48     35070
           weighted avg       0.98      0.88      0.93     35070

Confusion matrix -------------------------
[[30800  3917]
 [  308    45]]
General metrics -------------------------
model                 rf_non_physiological
sensitivity                         0.1275
specificity                         0.8872
precision                           0.0114
accuracy                            0.8795
f1_score                            0.0209
auc_roc                              0.733
false_alar_rate                     0.1128
fp_per_day                         9650.09
TP                                      45
FP                                    3917
TN                                   30800
FN                                     308
n_test_windows                       35070
covered_test_hours                    9.74
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_non_physiological_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_non_physiological_and_analysis_random.joblib

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Final report
---------- eye ----------
                 F1(val)=0.7500
                 best_params={'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 'log2'}
                 Confusion matrix: [[2361   10]
 [   0   24]]
                 Metrics results: {'model': 'rf_eye', 'sensitivity': 1.0, 'specificity': np.float64(0.9958), 'precision': 0.7059, 'accuracy': 0.9958, 'f1_score': 0.8276, 'auc_roc': 0.9994, 'false_alar_rate': np.float64(0.0042), 'fp_per_day': np.float64(18.04), 'TP': 24, 'FP': 10, 'TN': 2361, 'FN': 0, 'n_test_windows': 2395, 'covered_test_hours': 13.31}
---------- muscle ----------
                 F1(val)=0.6073
                 best_params={'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
                 Confusion matrix: [[10008   190]
 [  243   149]]
                 Metrics results: {'model': 'rf_muscle', 'sensitivity': 0.3801, 'specificity': np.float64(0.9814), 'precision': 0.4395, 'accuracy': 0.9591, 'f1_score': 0.4077, 'auc_roc': 0.9732, 'false_alar_rate': np.float64(0.0186), 'fp_per_day': np.float64(310.03), 'TP': 149, 'FP': 190, 'TN': 10008, 'FN': 243, 'n_test_windows': 10590, 'covered_test_hours': 14.71}
---------- non_physiological ----------
                 F1(val)=0.5979
                 best_params={'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'}
                 Confusion matrix: [[30800  3917]
 [  308    45]]
                 Metrics results: {'model': 'rf_non_physiological', 'sensitivity': 0.1275, 'specificity': np.float64(0.8872), 'precision': 0.0114, 'accuracy': 0.8795, 'f1_score': 0.0209, 'auc_roc': 0.733, 'false_alar_rate': np.float64(0.1128), 'fp_per_day': np.float64(9650.09), 'TP': 45, 'FP': 3917, 'TN': 30800, 'FN': 308, 'n_test_windows': 35070, 'covered_test_hours': 9.74}
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> CTra

#### Random Search - 
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> uv run python -m implementation.models.rf_model

Loading 25 artifact patients, 1 sessions per patient for testing...
  channel  start_time  stop_time label  confidence   Patient  ... Section    Montage NoChannels  Duration                                                EDF                                                CSV
0  FP1-F7     22.9737    30.0688  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7    136.7987   140.1117  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7    145.0133   148.0498  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3     22.9737    30.0688  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3    136.7987   140.1117  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

[5 rows x 13 columns]

--------------------------------------------------
ARTIFACT: eye | windows: 20s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_eye.parquet
[INFO] Split distribution:  split
train    10231
test      2395
val       2287
Name: count, dtype: int64

Starting training of Random Forest (eye)

============================================================
Modelo: rf_eye
Train: 10231 (pos=303) | Val: 2287 (pos = 29) | Test: 2395 (pos=24)
[DEBUG] y_val dist (rf_eye): {0: 2258, 1: 29}
[DEBUG] y_val hash (rf_eye): 11912536868275785955
[DEBUG] X_val hash (rf_eye): 11445343832670305202
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.6164383561643836
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.7333333333333333
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 0.3}
        f2 score:0.7386363636363636
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'log2'}
        f2 score:0.7046979865771812
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.75
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.695364238410596
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.7333333333333333
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.5755395683453237
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5}
        f2 score:0.5555555555555556
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.6506849315068494
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.684931506849315
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'sqrt'}
        f2 score:0.7046979865771812
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.5797101449275363
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.5597014925373134
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.7361963190184049
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.7333333333333333
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.6012658227848101
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.5797101449275363
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.6145251396648045
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.3}
        f2 score:0.6441717791411042
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.7333333333333333
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.5797101449275363
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 0.5}
        f2 score:0.5921052631578947
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.6081081081081081
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.5714285714285714
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.7419354838709677
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 'log2'}
        f2 score:0.6802721088435374
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 0.3}
        f2 score:0.6081081081081081
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 'sqrt'}
        f2 score:0.6711409395973155
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.75
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.5782312925170068
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.7333333333333333
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.3}
        f2 score:0.5704697986577181
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.625
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 0.3}
        f2 score:0.625
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.7236842105263158
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5}
        f2 score:0.5755395683453237
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.6756756756756757
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.5}
        f2 score:0.5792682926829268
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.7189542483660131
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.7500 | fp_per_day_val(val)=37.7787 <- choosen
        adjusted: threshold=0.5229 | F2(val)=0.7500 | fp_per_day_val(val)=37.7787
[INFO] Best configuration found with validation: {'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 'log2'} | F1(val)=0.7500
Final report -------------------------
              precision    recall  f1-score   support

   no_rf_eye       1.00      1.00      1.00      2371
      rf_eye       0.71      1.00      0.83        24

    accuracy                           1.00      2395
   macro avg       0.85      1.00      0.91      2395
weighted avg       1.00      1.00      1.00      2395

Confusion matrix -------------------------
[[2361   10]
 [   0   24]]
General metrics -------------------------
model                 rf_eye
sensitivity              1.0
specificity           0.9958
precision             0.7059
accuracy              0.9958
f1_score              0.8276
auc_roc               0.9994
false_alar_rate       0.0042
fp_per_day             18.04
TP                        24
FP                        10
TN                      2361
FN                         0
n_test_windows          2395
covered_test_hours     13.31
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_eye_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_eye_and_analysis_random.joblib

--------------------------------------------------
ARTIFACT: muscle | windows: 5s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_muscle.parquet
[INFO] Split distribution:  split
train    43130
test     10590
val       9703
Name: count, dtype: int64

Starting training of Random Forest (muscle)

============================================================
Modelo: rf_muscle
Train: 43130 (pos=1525) | Val: 9703 (pos = 245) | Test: 10590 (pos=392)
[DEBUG] y_val dist (rf_muscle): {0: 9458, 1: 245}
[DEBUG] y_val hash (rf_muscle): 15688256561422212987
[DEBUG] X_val hash (rf_muscle): 12322128536613835801
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.5332829046898638
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.5571740713765477
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 0.3}
        f2 score:0.546875
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'log2'}
        f2 score:0.5651274982770503
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.5760485093481557
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.604153555695406
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.5611150822015726
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.5527817403708987
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5}
        f2 score:0.3796095444685466
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.5326965466568699
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.5161787365177196
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'sqrt'}
        f2 score:0.5677785663591199
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.4600484261501211
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.5339805825242718
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.5725971370143149
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.5880376344086021
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.48094940662086194
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.557541100786276
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.537867824409069
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.3}
        f2 score:0.5973451327433629
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.6072607260726073
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.4838709677419355
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 0.5}
        f2 score:0.3951367781155015
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.5409836065573771
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.3952569169960474
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.5818278427205101
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 'log2'}
        f2 score:0.5614783226723525
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 0.3}
        f2 score:0.49888309754281457
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 'sqrt'}
        f2 score:0.5696636925188744
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.5868295273499734
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.3819709702062643
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.549645390070922
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.3}
        f2 score:0.4799107142857143
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.4538690476190476
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 0.3}
        f2 score:0.46701112877583467
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.6062322946175638
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5}
        f2 score:0.3456998313659359
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.5110132158590308
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.5}
        f2 score:0.5214541120381406
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.5612594113620808
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.6073 | fp_per_day_val(val)=625.0933 <- choosen
        adjusted: threshold=0.4874 | F2(val)=0.6048 | fp_per_day_val(val)=674.9583
[INFO] Best configuration found with validation: {'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 'sqrt'} | F1(val)=0.6073
Final report -------------------------
              precision    recall  f1-score   support

no_rf_muscle       0.98      0.98      0.98     10198
   rf_muscle       0.44      0.38      0.41       392

    accuracy                           0.96     10590
   macro avg       0.71      0.68      0.69     10590
weighted avg       0.96      0.96      0.96     10590

Confusion matrix -------------------------
[[10008   190]
 [  243   149]]
General metrics -------------------------
model                 rf_muscle
sensitivity              0.3801
specificity              0.9814
precision                0.4395
accuracy                 0.9591
f1_score                 0.4077
auc_roc                  0.9732
false_alar_rate          0.0186
fp_per_day               310.03
TP                          149
FP                          190
TN                        10008
FN                          243
n_test_windows            10590
covered_test_hours        14.71
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_muscle_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_muscle_and_analysis_random.joblib

--------------------------------------------------
ARTIFACT: non_physiological | windows: 1s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_non_physiological.parquet
[INFO] Split distribution:  split
train    238861
val       48026
test      35070
Name: count, dtype: int64

Starting training of Random Forest (non_physiological)

============================================================
Modelo: rf_non_physiological
Train: 238861 (pos=11914) | Val: 48026 (pos = 212) | Test: 35070 (pos=353)
[DEBUG] y_val dist (rf_non_physiological): {0: 47814, 1: 212}
[DEBUG] y_val hash (rf_non_physiological): 3087459260785746475
[DEBUG] X_val hash (rf_non_physiological): 2152757767067955685
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.4969217238346526
        params:{'n_estimators': 344, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.5085470085470085
        params:{'n_estimators': 240, 'max_depth': 7, 'min_samples_split': 18, 'min_samples_leaf': 14, 'max_features': 0.3}
        f2 score:0.43348916277093075
        params:{'n_estimators': 481, 'max_depth': 24, 'min_samples_split': 22, 'min_samples_leaf': 12, 'max_features': 'log2'}
        f2 score:0.4601899196493791
        params:{'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.5455537370430987
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.5978934324659232
        params:{'n_estimators': 501, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.49058084772370486
        params:{'n_estimators': 395, 'max_depth': 16, 'min_samples_split': 16, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.46360153256704983
        params:{'n_estimators': 191, 'max_depth': 18, 'min_samples_split': 27, 'min_samples_leaf': 2, 'max_features': 0.5}
        f2 score:0.4571026722925457
        params:{'n_estimators': 536, 'max_depth': 25, 'min_samples_split': 11, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.4934747145187602
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.45004500450045004
        params:{'n_estimators': 180, 'max_depth': 29, 'min_samples_split': 16, 'min_samples_leaf': 13, 'max_features': 'sqrt'}
        f2 score:0.48621745788667686
        params:{'n_estimators': 455, 'max_depth': 24, 'min_samples_split': 23, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.46354635463546356
        params:{'n_estimators': 313, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.4804421768707483
        params:{'n_estimators': 395, 'max_depth': 8, 'min_samples_split': 23, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.5488803932277444
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.5021367521367521
        params:{'n_estimators': 334, 'max_depth': 13, 'min_samples_split': 27, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.4375
        params:{'n_estimators': 184, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.4708171206225681
        params:{'n_estimators': 358, 'max_depth': 8, 'min_samples_split': 22, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.2564102564102564
        params:{'n_estimators': 298, 'max_depth': 10, 'min_samples_split': 19, 'min_samples_leaf': 10, 'max_features': 0.3}
        f2 score:0.4834761321909425
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.4715622750179986
        params:{'n_estimators': 433, 'max_depth': 22, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.40111940298507465
        params:{'n_estimators': 495, 'max_depth': 25, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 0.5}
        f2 score:0.471976401179941
        params:{'n_estimators': 528, 'max_depth': 14, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.4647887323943662
        params:{'n_estimators': 257, 'max_depth': 22, 'min_samples_split': 20, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.4702194357366771
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.5641025641025641
        params:{'n_estimators': 508, 'max_depth': 24, 'min_samples_split': 24, 'min_samples_leaf': 10, 'max_features': 'log2'}
        f2 score:0.4836193447737909
        params:{'n_estimators': 362, 'max_depth': 22, 'min_samples_split': 11, 'min_samples_leaf': 12, 'max_features': 0.3}
        f2 score:0.483271375464684
        params:{'n_estimators': 400, 'max_depth': 16, 'min_samples_split': 17, 'min_samples_leaf': 9, 'max_features': 'sqrt'}
        f2 score:0.4606741573033708
        params:{'n_estimators': 166, 'max_depth': 8, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.5489130434782609
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 0.5}
        f2 score:0.4584527220630373
        params:{'n_estimators': 534, 'max_depth': 19, 'min_samples_split': 6, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.4661016949152542
        params:{'n_estimators': 408, 'max_depth': 20, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 0.3}
        f2 score:0.46943231441048033
        params:{'n_estimators': 190, 'max_depth': 18, 'min_samples_split': 24, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.4706734250543085
        params:{'n_estimators': 421, 'max_depth': 5, 'min_samples_split': 13, 'min_samples_leaf': 7, 'max_features': 0.3}
        f2 score:0.2719112988384372
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.5862898376428142
        params:{'n_estimators': 596, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 5, 'max_features': 0.5}
        f2 score:0.5071315372424723
        params:{'n_estimators': 519, 'max_depth': 6, 'min_samples_split': 26, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.4714352066883418
        params:{'n_estimators': 562, 'max_depth': 12, 'min_samples_split': 15, 'min_samples_leaf': 10, 'max_features': 0.5}
        f2 score:0.42426147077309867
        params:{'n_estimators': 206, 'max_depth': 18, 'min_samples_split': 17, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.47919762258543835
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.5979 | fp_per_day_val(val)=1030.8416 <- choosen
        adjusted: threshold=0.5467 | F2(val)=0.6258 | fp_per_day_val(val)=825.7527
[INFO] Best configuration found with validation: {'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'} | F1(val)=0.5979
Final report -------------------------
                         precision    recall  f1-score   support

no_rf_non_physiological       0.99      0.89      0.94     34717
   rf_non_physiological       0.01      0.13      0.02       353

               accuracy                           0.88     35070
              macro avg       0.50      0.51      0.48     35070
           weighted avg       0.98      0.88      0.93     35070

Confusion matrix -------------------------
[[30800  3917]
 [  308    45]]
General metrics -------------------------
model                 rf_non_physiological
sensitivity                         0.1275
specificity                         0.8872
precision                           0.0114
accuracy                            0.8795
f1_score                            0.0209
auc_roc                              0.733
false_alar_rate                     0.1128
fp_per_day                         9650.09
TP                                      45
FP                                    3917
TN                                   30800
FN                                     308
n_test_windows                       35070
covered_test_hours                    9.74
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_non_physiological_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_non_physiological_and_analysis_random.joblib

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Final report
---------- eye ----------
                 F1(val)=0.7500
                 best_params={'n_estimators': 380, 'max_depth': 8, 'min_samples_split': 25, 'min_samples_leaf': 7, 'max_features': 'log2'}
                 Confusion matrix: [[2361   10]
 [   0   24]]
                 Metrics results: {'model': 'rf_eye', 'sensitivity': 1.0, 'specificity': np.float64(0.9958), 'precision': 0.7059, 'accuracy': 0.9958, 'f1_score': 0.8276, 'auc_roc': 0.9994, 'false_alar_rate': np.float64(0.0042), 'fp_per_day': np.float64(18.04), 'TP': 24, 'FP': 10, 'TN': 2361, 'FN': 0, 'n_test_windows': 2395, 'covered_test_hours': 13.31}
---------- muscle ----------
                 F1(val)=0.6073
                 best_params={'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
                 Confusion matrix: [[10008   190]
 [  243   149]]
                 Metrics results: {'model': 'rf_muscle', 'sensitivity': 0.3801, 'specificity': np.float64(0.9814), 'precision': 0.4395, 'accuracy': 0.9591, 'f1_score': 0.4077, 'auc_roc': 0.9732, 'false_alar_rate': np.float64(0.0186), 'fp_per_day': np.float64(310.03), 'TP': 149, 'FP': 190, 'TN': 10008, 'FN': 243, 'n_test_windows': 10590, 'covered_test_hours': 14.71}
---------- non_physiological ----------
                 F1(val)=0.5979
                 best_params={'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'}
                 Confusion matrix: [[30800  3917]
 [  308    45]]
                 Metrics results: {'model': 'rf_non_physiological', 'sensitivity': 0.1275, 'specificity': np.float64(0.8872), 'precision': 0.0114, 'accuracy': 0.8795, 'f1_score': 0.0209, 'auc_roc': 0.733, 'false_alar_rate': np.float64(0.1128), 'fp_per_day': np.float64(9650.09), 'TP': 45, 'FP': 3917, 'TN': 30800, 'FN': 308, 'n_test_windows': 35070, 'covered_test_hours': 9.74}
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> 


#### a

TypeError: imblearn.ensemble._forest.BalancedRandomForestClassifier() got multiple values for keyword argument 'sampling_strategy'
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis> uv run python -m implementation.models.rf_model

Loading 25 artifact patients, 1 sessions per patient for testing...
  channel  start_time  stop_time label  confidence   Patient  ... Section    Montage NoChannels  Duration                                                EDF                                                CSV
0  FP1-F7     22.9737    30.0688  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
1  FP1-F7    136.7987   140.1117  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
2  FP1-F7    145.0133   148.0498  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
3   F7-T3     22.9737    30.0688  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...
4   F7-T3    136.7987   140.1117  eyem         1.0  aaaaaaju  ...    t000  01_tcp_ar         36  1441.996  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...  D:\Users\disenoeinnovacion\Datasets\DATA_EEG_T...

[5 rows x 13 columns]

--------------------------------------------------
ARTIFACT: eye | windows: 20s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_eye.parquet
[INFO] Split distribution:  split
train    10231
test      2395
val       2287
Name: count, dtype: int64

Starting training of Random Forest (eye)

============================================================
Modelo: rf_eye
Train: 10231 (pos=303) | Val: 2287 (pos = 29) | Test: 2395 (pos=24)
[DEBUG] y_val dist (rf_eye): {0: 2258, 1: 29}
[DEBUG] y_val hash (rf_eye): 11912536868275785955
[DEBUG] X_val hash (rf_eye): 11445343832670305202
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.36175710594315247
        params:{'n_estimators': 536, 'max_depth': 7, 'min_samples_split': 22, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.27204502814258913
        params:{'n_estimators': 386, 'max_depth': 29, 'min_samples_split': 23, 'min_samples_leaf': 11, 'max_features': 0.3}
        f2 score:0.25
        params:{'n_estimators': 503, 'max_depth': 17, 'min_samples_split': 8, 'min_samples_leaf': 12, 'max_features': 'log2'}
        f2 score:0.26119402985074625
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 9, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.12697022767075306
        params:{'n_estimators': 439, 'max_depth': 15, 'min_samples_split': 25, 'min_samples_leaf': 9, 'max_features': 'log2'}
        f2 score:0.2966101694915254
        params:{'n_estimators': 352, 'max_depth': 10, 'min_samples_split': 7, 'min_samples_leaf': 9, 'max_features': 'sqrt'}
        f2 score:0.2116788321167883
        params:{'n_estimators': 178, 'max_depth': 26, 'min_samples_split': 25, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.3160270880361174
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 22, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.352112676056338
        params:{'n_estimators': 586, 'max_depth': 16, 'min_samples_split': 27, 'min_samples_leaf': 10, 'max_features': 'sqrt'}
        f2 score:0.19515477792732167
        params:{'n_estimators': 491, 'max_depth': 9, 'min_samples_split': 14, 'min_samples_leaf': 8, 'max_features': 'sqrt'}
        f2 score:0.280561122244489
        params:{'n_estimators': 169, 'max_depth': 18, 'min_samples_split': 8, 'min_samples_leaf': 11, 'max_features': 'sqrt'}
        f2 score:0.2365415986949429
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 14, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.2369281045751634
        params:{'n_estimators': 296, 'max_depth': 27, 'min_samples_split': 14, 'min_samples_leaf': 2, 'max_features': 'log2'}
        f2 score:0.42042042042042044
        params:{'n_estimators': 508, 'max_depth': 9, 'min_samples_split': 16, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.25925925925925924
        params:{'n_estimators': 364, 'max_depth': 13, 'min_samples_split': 10, 'min_samples_leaf': 9, 'max_features': 'log2'}
        f2 score:0.22727272727272727
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 9, 'min_samples_leaf': 12, 'max_features': 0.5}
        f2 score:0.19205298013245034
        params:{'n_estimators': 465, 'max_depth': 7, 'min_samples_split': 12, 'min_samples_leaf': 11, 'max_features': 'log2'}
        f2 score:0.14285714285714285
        params:{'n_estimators': 345, 'max_depth': 25, 'min_samples_split': 26, 'min_samples_leaf': 7, 'max_features': 0.5}
        f2 score:0.20743919885550788
        params:{'n_estimators': 279, 'max_depth': 10, 'min_samples_split': 22, 'min_samples_leaf': 10, 'max_features': 0.3}
        f2 score:0.3448275862068966
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 25, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.22727272727272727
        params:{'n_estimators': 504, 'max_depth': 24, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 'log2'}
        f2 score:0.25089605734767023
        params:{'n_estimators': 274, 'max_depth': 24, 'min_samples_split': 18, 'min_samples_leaf': 7, 'max_features': 0.5}
        f2 score:0.25089605734767023
        params:{'n_estimators': 405, 'max_depth': 5, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.2396694214876033
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 0.3}
        f2 score:0.20833333333333334
        params:{'n_estimators': 404, 'max_depth': 6, 'min_samples_split': 24, 'min_samples_leaf': 9, 'max_features': 'log2'}
        f2 score:0.14979338842975207
        params:{'n_estimators': 404, 'max_depth': 18, 'min_samples_split': 7, 'min_samples_leaf': 9, 'max_features': 'log2'}
        f2 score:0.1746987951807229
        params:{'n_estimators': 286, 'max_depth': 20, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.37433155080213903
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 11, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.2230769230769231
        params:{'n_estimators': 534, 'max_depth': 5, 'min_samples_split': 10, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.17791411042944785
        params:{'n_estimators': 535, 'max_depth': 12, 'min_samples_split': 27, 'min_samples_leaf': 5, 'max_features': 0.5}
        f2 score:0.2928870292887029
        params:{'n_estimators': 447, 'max_depth': 8, 'min_samples_split': 18, 'min_samples_leaf': 8, 'max_features': 'sqrt'}
        f2 score:0.2059659090909091
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 7, 'max_features': 0.3}
        f2 score:0.35714285714285715
        params:{'n_estimators': 516, 'max_depth': 13, 'min_samples_split': 9, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.3977272727272727
        params:{'n_estimators': 197, 'max_depth': 7, 'min_samples_split': 24, 'min_samples_leaf': 11, 'max_features': 0.3}
        f2 score:0.24207011686143573
        params:{'n_estimators': 357, 'max_depth': 22, 'min_samples_split': 9, 'min_samples_leaf': 13, 'max_features': 'sqrt'}
        f2 score:0.2241112828438949
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.5}
        f2 score:0.23648648648648649
        params:{'n_estimators': 350, 'max_depth': 9, 'min_samples_split': 14, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.2928870292887029
        params:{'n_estimators': 457, 'max_depth': 20, 'min_samples_split': 20, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.23387096774193547
        params:{'n_estimators': 189, 'max_depth': 13, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.2570921985815603
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 17, 'min_samples_leaf': 11, 'max_features': 0.3}
        f2 score:0.2857142857142857
        params:{'n_estimators': 269, 'max_depth': 24, 'min_samples_split': 29, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.2730696798493409
        params:{'n_estimators': 267, 'max_depth': 22, 'min_samples_split': 24, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.2676864244741874
        params:{'n_estimators': 272, 'max_depth': 6, 'min_samples_split': 7, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.1695906432748538
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 22, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.3349282296650718
        params:{'n_estimators': 287, 'max_depth': 25, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 'log2'}
        f2 score:0.39215686274509803
        params:{'n_estimators': 358, 'max_depth': 26, 'min_samples_split': 5, 'min_samples_leaf': 11, 'max_features': 0.3}
        f2 score:0.2839756592292089
        params:{'n_estimators': 473, 'max_depth': 21, 'min_samples_split': 15, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.3181818181818182
        params:{'n_estimators': 213, 'max_depth': 19, 'min_samples_split': 7, 'min_samples_leaf': 10, 'max_features': 'log2'}
        f2 score:0.22727272727272727
        params:{'n_estimators': 187, 'max_depth': 23, 'min_samples_split': 15, 'min_samples_leaf': 12, 'max_features': 'sqrt'}
        f2 score:0.37037037037037035
        params:{'n_estimators': 230, 'max_depth': 17, 'min_samples_split': 9, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.27184466019417475
        params:{'n_estimators': 215, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 4, 'max_features': 0.3}
        f2 score:0.3804347826086957
        params:{'n_estimators': 507, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 14, 'max_features': 0.5}
        f2 score:0.15104166666666666
        params:{'n_estimators': 411, 'max_depth': 16, 'min_samples_split': 13, 'min_samples_leaf': 9, 'max_features': 0.3}
        f2 score:0.2730696798493409
        params:{'n_estimators': 282, 'max_depth': 5, 'min_samples_split': 8, 'min_samples_leaf': 14, 'max_features': 'log2'}
        f2 score:0.12619669277632725
        params:{'n_estimators': 367, 'max_depth': 16, 'min_samples_split': 24, 'min_samples_leaf': 2, 'max_features': 0.3}
        f2 score:0.33045977011494254
        params:{'n_estimators': 274, 'max_depth': 17, 'min_samples_split': 21, 'min_samples_leaf': 8, 'max_features': 0.3}
        f2 score:0.32634032634032634
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 19, 'min_samples_leaf': 9, 'max_features': 'log2'}
        f2 score:0.2279874213836478
        params:{'n_estimators': 513, 'max_depth': 11, 'min_samples_split': 28, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.29045643153526973
        params:{'n_estimators': 384, 'max_depth': 26, 'min_samples_split': 15, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.425531914893617
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.4255 | fp_per_day_val(val)=349.4534
        adjusted: threshold=0.8892 | F2(val)=0.5344 | fp_per_day_val(val)=1.8889 <- choosen
[INFO] Best configuration found with validation: {'n_estimators': 384, 'max_depth': 26, 'min_samples_split': 15, 'min_samples_leaf': 5, 'max_features': 'sqrt'} | F1(val)=0.4255
Final report -------------------------
              precision    recall  f1-score   support

   no_rf_eye       0.99      1.00      1.00      2371
      rf_eye       0.80      0.33      0.47        24

    accuracy                           0.99      2395
   macro avg       0.90      0.67      0.73      2395
weighted avg       0.99      0.99      0.99      2395

Confusion matrix -------------------------
[[2369    2]
 [  16    8]]
General metrics -------------------------
model                 rf_eye
sensitivity           0.3333
specificity           0.9992
precision                0.8
accuracy              0.9925
f1_score              0.4706
auc_roc                0.971
false_alar_rate       0.0008
fp_per_day              3.61
TP                         8
FP                         2
TN                      2369
FN                        16
n_test_windows          2395
covered_test_hours     13.31
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_eye_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_eye_and_analysis_random.joblib

--------------------------------------------------
ARTIFACT: muscle | windows: 5s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_muscle.parquet
[INFO] Split distribution:  split
train    43130
test     10590
val       9703
Name: count, dtype: int64

Starting training of Random Forest (muscle)

============================================================
Modelo: rf_muscle
Train: 43130 (pos=1525) | Val: 9703 (pos = 245) | Test: 10590 (pos=392)
[DEBUG] y_val dist (rf_muscle): {0: 9458, 1: 245}
[DEBUG] y_val hash (rf_muscle): 15688256561422212987
[DEBUG] X_val hash (rf_muscle): 12322128536613835801
        params:{'n_estimators': 190, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.41164658634538154
        params:{'n_estimators': 536, 'max_depth': 7, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.349313066354867
        params:{'n_estimators': 386, 'max_depth': 29, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.3805774278215223
        params:{'n_estimators': 503, 'max_depth': 17, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.41143654114365413
        params:{'n_estimators': 375, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.31994645247657294
        params:{'n_estimators': 439, 'max_depth': 15, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.39469264360094053
        params:{'n_estimators': 352, 'max_depth': 10, 'min_samples_split': 3, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.24885464389837567
        params:{'n_estimators': 178, 'max_depth': 26, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.33559577677224733
        params:{'n_estimators': 224, 'max_depth': 23, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.313823642664613
        params:{'n_estimators': 586, 'max_depth': 16, 'min_samples_split': 13, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.33876500857632935
        params:{'n_estimators': 491, 'max_depth': 9, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.3424068767908309
        params:{'n_estimators': 169, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.3890537421694692
        params:{'n_estimators': 565, 'max_depth': 23, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.4528158295281583
        params:{'n_estimators': 296, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 1, 'max_features': 'log2'}
        f2 score:0.3972545757071547
        params:{'n_estimators': 508, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'sqrt'}
        f2 score:0.28976721629485935
        params:{'n_estimators': 364, 'max_depth': 13, 'min_samples_split': 4, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.34557547715442455
        params:{'n_estimators': 573, 'max_depth': 15, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.30717225161669603
        params:{'n_estimators': 465, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.18288112726727626
        params:{'n_estimators': 345, 'max_depth': 25, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.2790843524615867
        params:{'n_estimators': 279, 'max_depth': 10, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.39080459770114945
        params:{'n_estimators': 524, 'max_depth': 9, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 'sqrt'}
        f2 score:0.2180259076810801
        params:{'n_estimators': 504, 'max_depth': 24, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.4361904761904762
        params:{'n_estimators': 274, 'max_depth': 24, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5}
        f2 score:0.3191107923987092
        params:{'n_estimators': 405, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 2, 'max_features': 0.3}
        f2 score:0.3412256267409471
        params:{'n_estimators': 347, 'max_depth': 21, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.3}
        f2 score:0.30210558437595364
        params:{'n_estimators': 404, 'max_depth': 6, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'log2'}
        f2 score:0.180865200059058
        params:{'n_estimators': 404, 'max_depth': 18, 'min_samples_split': 3, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.36490683229813664
        params:{'n_estimators': 286, 'max_depth': 20, 'min_samples_split': 2, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.30687830687830686
        params:{'n_estimators': 592, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.23583974738504046
        params:{'n_estimators': 534, 'max_depth': 5, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.2688774367017701
        params:{'n_estimators': 535, 'max_depth': 12, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.35691523263224983
        params:{'n_estimators': 447, 'max_depth': 8, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.19923307769256418
        params:{'n_estimators': 598, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.30796460176991153
        params:{'n_estimators': 516, 'max_depth': 13, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.38841567291311757
        params:{'n_estimators': 197, 'max_depth': 7, 'min_samples_split': 12, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.24502768095140456
        params:{'n_estimators': 357, 'max_depth': 22, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.4083044982698962
        params:{'n_estimators': 572, 'max_depth': 8, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5}
        f2 score:0.3441820276497696
        params:{'n_estimators': 350, 'max_depth': 9, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.3343592613318411
        params:{'n_estimators': 457, 'max_depth': 20, 'min_samples_split': 9, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.25709468951952796
        params:{'n_estimators': 189, 'max_depth': 13, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.3073132780082988
        params:{'n_estimators': 314, 'max_depth': 27, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.37537537537537535
        params:{'n_estimators': 269, 'max_depth': 24, 'min_samples_split': 14, 'min_samples_leaf': 2, 'max_features': 0.3}
        f2 score:0.27505532722099274
        params:{'n_estimators': 267, 'max_depth': 22, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.41742617572001456
        params:{'n_estimators': 272, 'max_depth': 6, 'min_samples_split': 3, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.17888563049853373
        params:{'n_estimators': 207, 'max_depth': 16, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.3517432891082999
        params:{'n_estimators': 287, 'max_depth': 25, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.5299653293709757
        params:{'n_estimators': 358, 'max_depth': 26, 'min_samples_split': 2, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.373792524149517
        params:{'n_estimators': 473, 'max_depth': 21, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.3882809742322626
        params:{'n_estimators': 213, 'max_depth': 19, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 'log2'}
        f2 score:0.4090438384535727
        params:{'n_estimators': 187, 'max_depth': 23, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.48417132216014896
        params:{'n_estimators': 230, 'max_depth': 17, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.28818897637795277
        params:{'n_estimators': 215, 'max_depth': 21, 'min_samples_split': 3, 'min_samples_leaf': 2, 'max_features': 0.3}
        f2 score:0.2934232715008432
        params:{'n_estimators': 507, 'max_depth': 9, 'min_samples_split': 5, 'min_samples_leaf': 7, 'max_features': 0.5}
        f2 score:0.1765536723163842
        params:{'n_estimators': 411, 'max_depth': 16, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.3120149022042844
        params:{'n_estimators': 282, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.1801205705043376
        params:{'n_estimators': 367, 'max_depth': 16, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.3}
        f2 score:0.3286384976525822
        params:{'n_estimators': 274, 'max_depth': 17, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.3}
        f2 score:0.312392722279437
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.30894519131334025
        params:{'n_estimators': 513, 'max_depth': 11, 'min_samples_split': 14, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.3189771197846568
        params:{'n_estimators': 384, 'max_depth': 26, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.41743119266055045
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.5300 | fp_per_day_val(val)=1469.2363 <- choosen
        adjusted: threshold=0.5491 | F2(val)=0.5397 | fp_per_day_val(val)=1154.0183
[INFO] Best configuration found with validation: {'n_estimators': 287, 'max_depth': 25, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'log2'} | F1(val)=0.5300
Final report -------------------------
              precision    recall  f1-score   support

no_rf_muscle       0.99      0.95      0.97     10198
   rf_muscle       0.38      0.87      0.53       392

    accuracy                           0.94     10590
   macro avg       0.69      0.91      0.75     10590
weighted avg       0.97      0.94      0.95     10590

Confusion matrix -------------------------
[[9653  545]
 [  52  340]]
General metrics -------------------------
model                 rf_muscle
sensitivity              0.8673
specificity              0.9466
precision                0.3842
accuracy                 0.9436
f1_score                 0.5325
auc_roc                  0.9699
false_alar_rate          0.0534
fp_per_day               889.29
TP                          340
FP                          545
TN                         9653
FN                           52
n_test_windows            10590
covered_test_hours        14.71
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_muscle_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_muscle_and_analysis_random.joblib

--------------------------------------------------
ARTIFACT: non_physiological | windows: 1s

--------------------------------------------------
[INFO] Existing dataset, loading: C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\features\rf_dataset_non_physiological.parquet
[INFO] Split distribution:  split
train    238861
val       48026
test      35070
Name: count, dtype: int64

Starting training of Random Forest (non_physiological)

============================================================
Modelo: rf_non_physiological
Train: 238861 (pos=11914) | Val: 48026 (pos = 212) | Test: 35070 (pos=353)
[DEBUG] y_val dist (rf_non_physiological): {0: 47814, 1: 212}
[DEBUG] y_val hash (rf_non_physiological): 3087459260785746475
[DEBUG] X_val hash (rf_non_physiological): 2152757767067955685
        params:{'n_estimators': 190, 'max_depth': 28, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.402975821450713
        params:{'n_estimators': 536, 'max_depth': 7, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.14121195503153278
        params:{'n_estimators': 386, 'max_depth': 34, 'min_samples_split': 11, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.21532615579480685
        params:{'n_estimators': 503, 'max_depth': 20, 'min_samples_split': 3, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.497997997997998
        params:{'n_estimators': 375, 'max_depth': 16, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.19903381642512077
        params:{'n_estimators': 439, 'max_depth': 17, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.4210305823209049
        params:{'n_estimators': 352, 'max_depth': 11, 'min_samples_split': 3, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.10134476710192945
        params:{'n_estimators': 178, 'max_depth': 30, 'min_samples_split': 12, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.3744493392070485
        params:{'n_estimators': 224, 'max_depth': 27, 'min_samples_split': 11, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.21608832807570977
        params:{'n_estimators': 586, 'max_depth': 18, 'min_samples_split': 13, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
        f2 score:0.21575198994553832
        params:{'n_estimators': 491, 'max_depth': 10, 'min_samples_split': 6, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.191734921816828
        params:{'n_estimators': 169, 'max_depth': 21, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.38938395970554046
        params:{'n_estimators': 565, 'max_depth': 27, 'min_samples_split': 6, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.5187695516162669
        params:{'n_estimators': 296, 'max_depth': 32, 'min_samples_split': 6, 'min_samples_leaf': 1, 'max_features': 'log2'}
        f2 score:0.3298774740810556
        params:{'n_estimators': 508, 'max_depth': 10, 'min_samples_split': 8, 'min_samples_leaf': 1, 'max_features': 'sqrt'}
        f2 score:0.1378529568460309
        params:{'n_estimators': 364, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.2544466403162055
        params:{'n_estimators': 573, 'max_depth': 18, 'min_samples_split': 4, 'min_samples_leaf': 6, 'max_features': 0.5}
        f2 score:0.13577023498694518
        params:{'n_estimators': 465, 'max_depth': 7, 'min_samples_split': 6, 'min_samples_leaf': 6, 'max_features': 'log2'}
        f2 score:0.05293118945371018
        params:{'n_estimators': 345, 'max_depth': 29, 'min_samples_split': 12, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.10947763528307788
        params:{'n_estimators': 279, 'max_depth': 12, 'min_samples_split': 10, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.21598497495826377
        params:{'n_estimators': 524, 'max_depth': 10, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 'sqrt'}
        f2 score:0.09454545454545454
        params:{'n_estimators': 504, 'max_depth': 28, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.5165180912427897
        params:{'n_estimators': 274, 'max_depth': 28, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 0.5}
        f2 score:0.11685728493286922
        params:{'n_estimators': 405, 'max_depth': 6, 'min_samples_split': 3, 'min_samples_leaf': 2, 'max_features': 0.3}
        f2 score:0.08600631543958784
        params:{'n_estimators': 347, 'max_depth': 25, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.3}
        f2 score:0.1106687898089172
        params:{'n_estimators': 404, 'max_depth': 7, 'min_samples_split': 11, 'min_samples_leaf': 5, 'max_features': 'log2'}
        f2 score:0.06642089874785483
        params:{'n_estimators': 404, 'max_depth': 21, 'min_samples_split': 3, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.32605203983295855
        params:{'n_estimators': 286, 'max_depth': 23, 'min_samples_split': 2, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.17471091000502764
        params:{'n_estimators': 592, 'max_depth': 11, 'min_samples_split': 5, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.10332434860736747
        params:{'n_estimators': 534, 'max_depth': 6, 'min_samples_split': 5, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.10323605320627358
        params:{'n_estimators': 535, 'max_depth': 13, 'min_samples_split': 13, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.09603841536614646
        params:{'n_estimators': 447, 'max_depth': 8, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.07800253788161529
        params:{'n_estimators': 598, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.18831877729257643
        params:{'n_estimators': 516, 'max_depth': 14, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.25949367088607594
        params:{'n_estimators': 197, 'max_depth': 7, 'min_samples_split': 12, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.07376409674444996
        params:{'n_estimators': 357, 'max_depth': 26, 'min_samples_split': 4, 'min_samples_leaf': 7, 'max_features': 'sqrt'}
        f2 score:0.42535091450446616
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.5}
        f2 score:0.07902135096117316
        params:{'n_estimators': 350, 'max_depth': 9, 'min_samples_split': 6, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.15629742033383914
        params:{'n_estimators': 457, 'max_depth': 23, 'min_samples_split': 9, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.15323926566530116
        params:{'n_estimators': 189, 'max_depth': 15, 'min_samples_split': 3, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.1550794126460893
        params:{'n_estimators': 314, 'max_depth': 32, 'min_samples_split': 8, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.26453957996768984
        params:{'n_estimators': 269, 'max_depth': 27, 'min_samples_split': 14, 'min_samples_leaf': 2, 'max_features': 0.3}
        f2 score:0.11399048712481548
        params:{'n_estimators': 267, 'max_depth': 26, 'min_samples_split': 12, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.4875061244487996
        params:{'n_estimators': 272, 'max_depth': 7, 'min_samples_split': 3, 'min_samples_leaf': 4, 'max_features': 'sqrt'}
        f2 score:0.0682362072310976
        params:{'n_estimators': 207, 'max_depth': 18, 'min_samples_split': 11, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.3233513857916534
        params:{'n_estimators': 287, 'max_depth': 29, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.5938951559389516
        params:{'n_estimators': 358, 'max_depth': 30, 'min_samples_split': 2, 'min_samples_leaf': 6, 'max_features': 0.3}
        f2 score:0.24120420747188973
        params:{'n_estimators': 473, 'max_depth': 24, 'min_samples_split': 7, 'min_samples_leaf': 3, 'max_features': 'sqrt'}
        f2 score:0.30513176144244103
        params:{'n_estimators': 213, 'max_depth': 22, 'min_samples_split': 3, 'min_samples_leaf': 5, 'max_features': 'log2'}
        f2 score:0.45937211449676824
        params:{'n_estimators': 187, 'max_depth': 27, 'min_samples_split': 7, 'min_samples_leaf': 6, 'max_features': 'sqrt'}
        f2 score:0.5134957208689928
        params:{'n_estimators': 230, 'max_depth': 19, 'min_samples_split': 4, 'min_samples_leaf': 3, 'max_features': 0.5}
        f2 score:0.15193981413187785
        params:{'n_estimators': 215, 'max_depth': 25, 'min_samples_split': 3, 'min_samples_leaf': 2, 'max_features': 0.3}
        f2 score:0.139502207948615
        params:{'n_estimators': 507, 'max_depth': 10, 'min_samples_split': 5, 'min_samples_leaf': 7, 'max_features': 0.5}
        f2 score:0.09094865100087032
        params:{'n_estimators': 411, 'max_depth': 18, 'min_samples_split': 6, 'min_samples_leaf': 5, 'max_features': 0.3}
        f2 score:0.12269207861822513
        params:{'n_estimators': 282, 'max_depth': 5, 'min_samples_split': 3, 'min_samples_leaf': 7, 'max_features': 'log2'}
        f2 score:0.050080317490314656
        params:{'n_estimators': 367, 'max_depth': 19, 'min_samples_split': 12, 'min_samples_leaf': 1, 'max_features': 0.3}
        f2 score:0.24381498745069918
        params:{'n_estimators': 274, 'max_depth': 19, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 0.3}
        f2 score:0.1540310246886607
        params:{'n_estimators': 572, 'max_depth': 9, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'log2'}
        f2 score:0.1389261744966443
        params:{'n_estimators': 513, 'max_depth': 13, 'min_samples_split': 14, 'min_samples_leaf': 3, 'max_features': 0.3}
        f2 score:0.0978075978075978
        params:{'n_estimators': 384, 'max_depth': 30, 'min_samples_split': 7, 'min_samples_leaf': 2, 'max_features': 'sqrt'}
        f2 score:0.2465897166841553
[INFO] Threshold decision based on validation:
        thr05: threshold=0.5000 | F2(val)=0.5939 | fp_per_day_val(val)=863.5323
        adjusted: threshold=0.4711 | F2(val)=0.6113 | fp_per_day_val(val)=928.2972 <- choosen
[INFO] Best configuration found with validation: {'n_estimators': 287, 'max_depth': 29, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'log2'} | F1(val)=0.5939
Final report -------------------------
                         precision    recall  f1-score   support

no_rf_non_physiological       0.99      0.84      0.91     34717
   rf_non_physiological       0.02      0.30      0.04       353

               accuracy                           0.84     35070
              macro avg       0.51      0.57      0.47     35070
           weighted avg       0.98      0.84      0.90     35070

Confusion matrix -------------------------
[[29194  5523]
 [  246   107]]
General metrics -------------------------
model                 rf_non_physiological
sensitivity                         0.3031
specificity                         0.8409
precision                            0.019
accuracy                            0.8355
f1_score                            0.0358
auc_roc                             0.7569
false_alar_rate                     0.1591
fp_per_day                        13606.71
TP                                     107
FP                                    5523
TN                                   29194
FN                                     246
n_test_windows                       35070
covered_test_hours                    9.74
Model saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_non_physiological_random.joblib
Model with metrics saved in C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis\outputs\artifact\individual_tests\models\rf_rf_non_physiological_and_analysis_random.joblib

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Final report
---------- eye ----------
                 F1(val)=0.4255
                 best_params={'n_estimators': 384, 'max_depth': 26, 'min_samples_split': 15, 'min_samples_leaf': 5, 'max_features': 'sqrt'}
                 Confusion matrix: [[2369    2]
 [  16    8]]
                 Metrics results: {'model': 'rf_eye', 'sensitivity': 0.3333, 'specificity': np.float64(0.9992), 'precision': 0.8, 'accuracy': 0.9925, 'f1_score': 0.4706, 'auc_roc': 0.971, 'false_alar_rate': np.float64(0.0008), 'fp_per_day': np.float64(3.61), 'TP': 8, 'FP': 2, 'TN': 2369, 'FN': 16, 'n_test_windows': 2395, 'covered_test_hours': 13.31}
---------- muscle ----------
                 F1(val)=0.5300
                 best_params={'n_estimators': 287, 'max_depth': 25, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'log2'}
                 Confusion matrix: [[9653  545]
 [  52  340]]
                 Metrics results: {'model': 'rf_muscle', 'sensitivity': 0.8673, 'specificity': np.float64(0.9466), 'precision': 0.3842, 'accuracy': 0.9436, 'f1_score': 0.5325, 'auc_roc': 0.9699, 'false_alar_rate': np.float64(0.0534), 'fp_per_day': np.float64(889.29), 'TP': 340, 'FP': 545, 'TN': 9653, 'FN': 52, 'n_test_windows': 10590, 'covered_test_hours': 14.71}
---------- non_physiological ----------
                 F1(val)=0.5939
                 best_params={'n_estimators': 287, 'max_depth': 29, 'min_samples_split': 9, 'min_samples_leaf': 4, 'max_features': 'log2'}
                 Confusion matrix: [[29194  5523]
 [  246   107]]
                 Metrics results: {'model': 'rf_non_physiological', 'sensitivity': 0.3031, 'specificity': np.float64(0.8409), 'precision': 0.019, 'accuracy': 0.8355, 'f1_score': 0.0358, 'auc_roc': 0.7569, 'false_alar_rate': np.float64(0.1591), 'fp_per_day': np.float64(13606.71), 'TP': 107, 'FP': 5523, 'TN': 29194, 'FN': 246, 'n_test_windows': 35070, 'covered_test_hours': 9.74}
PS C:\Users\diseñoeinnovacion\Documents\MariaAndrade\hybrid-ai-epilepsy-diagnosis>





## Uso
En qué situación necesito esto.

## Comandos / Código
```bash
# comando aquí
```

## Errores comunes 
- Error: descripción → Solución: cómo lo resolví

## Referencias
- Fuente, link, paper, o conversación de donde salió esto o para el que es base para usar después

## Fecha
**Creación**: YYYY-MM-DD
**Última actualización**: YYYY-MM-DD