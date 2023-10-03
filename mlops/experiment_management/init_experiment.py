# experiment_management/init_experiment.py
import mlflow
import optuna
import yaml
import os

def init_mlflow():

    with open('/home/sam/github/finance-data-driven/config/mlflow_config.yaml', 'r') as f:
        mlflow_config = yaml.safe_load(f)
        
  
    mlflow.set_experiment(mlflow_config['experiment_name'])
    mlflow.set_tracking_uri(mlflow_config['artifact_location'])


# init_optuna.py
def init_optuna():
    with open("./config/optuna_config.yaml", 'r') as f:
        optuna_config = yaml.safe_load(f)
    study = optuna.create_study(
        study_name=optuna_config['study_name'],
        storage=optuna_config['storage'],
        direction="maximize",
        load_if_exists=True
    )

# You can then call these functions in your main script
if __name__ == '__main__':
    init_mlflow()
    init_optuna()
