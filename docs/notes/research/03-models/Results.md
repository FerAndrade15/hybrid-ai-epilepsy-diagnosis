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