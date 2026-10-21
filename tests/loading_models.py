import torch
import os
from epileptic_eeg_analysis_toolbox.backend.ml_service.seizure_transformer import SeizureTransformer

def test_model():
    print("1. Instanciando el modelo...")
    model = SeizureTransformer() 
    model.eval()

    print("2. Cargando los pesos")
    current_path = os.path.dirname(os.path.abspath(__file__))
    weights_path = os.path.abspath(os.path.join(current_path, "..", "epileptic_eeg_analysis_toolbox", "models_weights", "seizure_transformer.pth"))
    state = torch.load(weights_path, map_location=torch.device('cpu'))
    model.load_state_dict(state)

    print("3. Generando ventana de EEG simulada (Batch=1, Canales=19, Tiempo=15390)...")
    sintetic_tensor = torch.randn(1, 19, 15360)
    
    print("4. Ejecutando inferencia...")
    with torch.no_grad():
        output = model(sintetic_tensor)
        
    print(f"¡Éxito! El modelo funcionó sin errores de dimensiones.")
    print(f"Forma del tensor de salida: {output.shape}")

if __name__ == "__main__":
    test_model()