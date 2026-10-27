import optuna
import torch
import gc
import os
from optuna.pruners import MedianPruner
from optuna.trial import TrialState

# 1. Configuración de persistencia y rutas
STUDY_NAME = "seizure_hybrid_model_v1"
DB_URL = f"sqlite:////workspace/ml-outputs/{STUDY_NAME}.db"
BEST_MODEL_PATH = f"/workspace/ml-outputs/seizure/models/best_{STUDY_NAME}.pth"

def objective(trial):
    # 2. Definición del espacio de búsqueda (Hiperparámetros)
    lr = trial.suggest_float("lr", 1e-5, 1e-3, log=True)
    batch_size = trial.suggest_categorical("batch_size", [16, 32, 64])
    dropout_rate = trial.suggest_float("dropout", 0.2, 0.5)
    # optimizer_name = trial.suggest_categorical("optimizer", ["Adam", "AdamW"])

    # Inicializar modelo, optimizador y dataloaders aquí con los hiperparámetros
    # model = TuModeloHibrido(dropout_rate).to('cuda')
    # optimizer = getattr(torch.optim, optimizer_name)(model.parameters(), lr=lr)
    
    best_val_loss = float("inf")

    try:
        for epoch in range(EPOCHS): # Define tu número máximo de épocas
            # --- LÓGICA DE ENTRENAMIENTO AQUÍ ---
            # train_loss = train_one_epoch(...)
            
            # --- LÓGICA DE VALIDACIÓN AQUÍ ---
            # val_loss = validate(...)
            val_loss = 0.5 # Reemplazar con tu métrica real

            # 3. Reportar a Optuna y aplicar Pruning (Poda)
            # Optuna evaluará si esta prueba va muy mal comparada con pruebas anteriores
            trial.report(val_loss, epoch)

            if trial.should_prune():
                raise optuna.exceptions.TrialPruned()

            # Guardar el checkpoint del mejor modelo de ESTA prueba específica (opcional pero recomendado)
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                # torch.save(model.state_dict(), f"/workspace/ml-outputs/seizure/sessions/trial_{trial.number}_best.pth")

        return best_val_loss

    except RuntimeError as e:
        # 4. Manejo de errores OOM (Out Of Memory) en CUDA
        if "out of memory" in str(e):
            print(f"[OOM] La prueba {trial.number} se quedó sin memoria. Liberando caché y podando prueba.")
            torch.cuda.empty_cache()
            gc.collect()
            raise optuna.exceptions.TrialPruned() # Podamos la prueba en lugar de crashear todo el script
        else:
            raise e # Si es otro error de código, sí queremos que crashee para arreglarlo

def main():
    # 5. Creación del Study con persistencia y Pruner
    os.makedirs("/workspace/ml-outputs/seizure/models", exist_ok=True)
    
    study = optuna.create_study(
        study_name=STUDY_NAME,
        storage=DB_URL,
        load_if_exists=True,             # Si se apaga el pod, al volver a correr el script continuará desde donde se quedó
        direction="minimize",            # Cambiar a "maximize" si optimizas F1-Score o Accuracy
        pruner=MedianPruner(
            n_startup_trials=5,          # Deja que 5 pruebas terminen completas antes de empezar a podar
            n_warmup_steps=3,            # Deja que cada prueba corra al menos 3 épocas antes de juzgarla
            interval_steps=1
        )
    )

    # 6. Ejecutar la optimización
    print(f"Iniciando optimización. Pruebas anteriores completadas: {len(study.trials)}")
    study.optimize(objective, n_trials=50, gc_after_trial=True) # gc_after_trial evita fugas de memoria RAM

    # 7. Resumen de resultados
    pruned_trials = study.get_trials(deepcopy=False, states=[TrialState.PRUNED])
    complete_trials = study.get_trials(deepcopy=False, states=[TrialState.COMPLETE])
    
    print("\n--- RESUMEN DE OPTUNA ---")
    print(f"Pruebas podadas: {len(pruned_trials)}")
    print(f"Pruebas completadas: {len(complete_trials)}")
    
    best_trial = study.best_trial
    print(f"Mejor valor (Loss): {best_trial.value}")
    print("Mejores hiperparámetros:")
    for key, value in best_trial.params.items():
        print(f"    {key}: {value}")

if __name__ == "__main__":
    main()