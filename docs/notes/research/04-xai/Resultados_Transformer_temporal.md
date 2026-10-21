# Aplicación de explicabilidad al modelo del trasnformador temporal - UVG

## Análisis
### Features reportadas

|Nombre en tu gráfica|Significado probable|Qué describe|
|---|---|---|
|`bp_rel_theta`|Potencia relativa en theta|Fracción de la potencia espectral correspondiente a theta|
|`rms_eeg`|Valor RMS del EEG|Magnitud cuadrática media de la señal|
|`bp_rel_alpha`|Potencia relativa en alfa|Fracción de potencia correspondiente a alfa|
|`hjorth_mobility`|Movilidad de Hjorth|Variación de la señal respecto a su amplitud; relacionada con su contenido frecuencial|
|`beta_alpha_ratio`|Cociente de potencias beta/alfa|Predominio relativo de beta frente a alfa|
|`theta_alpha_ratio`|Cociente de potencias theta/alfa|Predominio relativo de theta frente a alfa|
|`bp_rel_delta`|Potencia relativa en delta|Fracción de potencia correspondiente a delta|
|`tkeo_mean`|Media del operador de energía Teager–Kaiser|Descriptor que combina información de amplitud y variación oscilatoria|
|`std_eeg`|Desviación estándar del EEG|Dispersión de la amplitud respecto a su media|
|`hjorth_complexity`|Complejidad de Hjorth|Relación entre la movilidad de la derivada y la movilidad de la señal|
|`line_length`|Longitud de línea|Variación acumulada —o media, según implementación— entre muestras consecutivas|
|`bp_rel_gamma`|Potencia relativa en gamma|Fracción de potencia correspondiente a gamma|
|`hjorth_activity`|Actividad de Hjorth|Habitualmente, varianza de la señal|
|`spectral_entropy`|Entropía espectral|Qué tan concentrada o distribuida está la potencia entre frecuencias|
|`bp_rel_beta`|Potencia relativa en beta|Fracción de potencia correspondiente a beta|
|`sef95`|Frecuencia de borde espectral al 95 %|Frecuencia por debajo de la cual se acumula el 95 % de la potencia del espectro considerado|
- Verdadero negativo:
![[saliency_window_0.pdf]]

- Falso negativo:
![[saliency_window_127.pdf]]

- Falso positivo:
![[saliency_window_165.pdf]]

- Verdadero positivo:
![[saliency_window_415.pdf]]


| Caso                 | Distribución temporal y magnitud                                                                                                                                                                                                   | Features con mayor sensibilidad                                       | Canales con mayor sensibilidad media temporal |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------- |
| **VN — ventana 0**   | Sensibilidad extendida a lo largo del tiempo en determinados canales, con variaciones rápidas. Los valores absolutos son muy pequeños: el mapa alcanza aproximadamente \(1.9\times10^{-11}\).                                      | Desviación estándar; potencia relativa **alfa**; cociente beta/alfa.  | T5-O1, C4-T4, T4-A2, FP2-F4, C4-P4 y FP1-F3.  |
| **FN — ventana 127** | Algunos canales mantienen sensibilidad durante gran parte de la ventana, con variaciones locales. Presenta máximos mayores que el VN seleccionado, aunque sigue en el orden de \(10^{-11}\).                                       | Potencia relativa alfa; desviación estándar; cociente theta/alfa.     | C4-P4, T3-T5, FP2-F4, T5-O1, FP1-F3 y P4-O2.  |
| **FP — ventana 165** | Sensibilidad relativamente concentrada en intervalos breves, separados por regiones de menor intensidad. El máximo del mapa es aproximadamente \(1.7\times10^{-6}\): **mayor que en VN y FN**, pese a que el mapa luce más oscuro. | RMS; potencia relativa theta; movilidad de Hjorth.                    | V F3-C3 y C3-CZ.                              |
| **VP — ventana 415** | Sensibilidad temporal más extendida que en el FP seleccionado, con máximos locales destacados. El máximo del mapa alcanza aproximadamente \(6.6\times10^{-6}\).                                                                    | Potencia relativa alfa; cociente beta/alfa; desviación estándar; RMS. | F8-T4, CZ-C4, FP1-F7 y C4-T4.                 |

