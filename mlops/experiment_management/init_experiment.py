# experiment_management/init_experiment.py
import mlflow
import optuna
import yaml

# Load MLFlow config
with open("../config/mlflow_config.yaml", 'r') as f:
    mlflow_config = yaml.safe_load(f)

# Initialize MLFlow experiment
mlflow.set_experiment(mlflow_config['experiment_name'])
mlflow.set_tracking_uri(mlflow_config['artifact_location'])

# Load Optuna config
with open("../config/optuna_config.yaml", 'r') as f:
    optuna_config = yaml.safe_load(f)

# Initialize Optuna study
study = optuna.create_study(
    study_name=optuna_config['study_name'],
    storage=optuna_config['storage'],
    direction="maximize",
    load_if_exists=True
)

print("MLFlow and Optuna initialized from config.")
