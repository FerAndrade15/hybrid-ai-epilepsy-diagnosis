# Metodología y análisis del flujo de datos

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


| **IZQUIERDOS**                                                                                                                                                                                                                                                                                       | **DERECHOS**                                                                                                                                                                                                                                                                          | **LÍNEA MEDIA**                                                                  | **AURICULARES**                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Fp1**- Frontopolar izquierdo<br><br>**F3**- Frontal izquierdo<br><br>**F7**- Temporal anterior izquierdo<br><br>**T3**- Temporal medio izquierdo<br><br>**C3**- Central izquierdo<br><br>**P3**- Parietal izquierdo<br><br>**T5**- Temporal posterior izquierdo<br><br>**O1**- Occipital izquierdo | **Fp2**- Frontopolar derecho<br><br>**F4**- Frontal derecho<br><br>**F8**- Temporal anterior derecho<br><br>**T4**- Temporal medio derecho<br><br>**C4**- Central derecho<br><br>**P4**- Parietal derecho<br><br>**T6** - Temporal posterior derecho<br><br>**O2**- Occipital derecho | **Fz**- Frontal medio<br><br>**Cz**- Central medio<br><br>**Pz**- Parietal medio | **A1**- Auricular izquierdo<br><br>**A2**- Auricular derecho |
