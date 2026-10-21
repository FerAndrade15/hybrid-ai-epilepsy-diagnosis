# Métodos de XAI en Deep Learning
## Modelos de XAI aplicados a modelos convolucionales
- GradCAM
- GradCAM++
- ScoreCAM

## Modelos recurrentes
- SHAP GradientExplainer: Explica la importancia temporal
- Integrated Gradientes: Generalmente aplicados a los LSTM
- Attention Weigths: Para modelos con atención
- LIME
# X-AI methods

- Grad-CAM
- Permutation Features importance (PFI)
- Partial Dependence Plots (PDP) 
- Neuro-XAI


|Saliency|IG|Occlusion|
|---|---|---|
|Idea|pendiente local|suma de pendientes a lo largo del camino|intervención (borrar)|
|Unidad|Δp por unidad de señal|probabilidad|probabilidad|
|Signo|no (abs)|sí|sí|
|Falla con saturación|sí|no|no|
|Coste|1 pasada|`n_steps` pasadas|1 pasada por trozo|
- **B** = _batch_: cuántas ventanas hay
- **T** = _time_: cuántos puntos de tiempo tiene cada ventana
- **C** = _channels_: cuántos canales de EEG hay
tensor `(B, T, C)`


Y por eso `occlusion` usa `axis`:

- En `(B, T, C)` (Sanchez), los canales son `axis=2` y el tiempo es `axis=1`.
- En `(B, C, T)` (UNet), los canales son `axis=1` y el tiempo es `axis=2`.

El eje 0 siempre es el batch, y `occlusion` no te deja usarlo.