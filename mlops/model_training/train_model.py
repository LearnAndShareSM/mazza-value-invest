# model_training/train_model.py
from sklearn.datasets import make_classification
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from model_validation import CombPurgedKFoldCV
from sklearn.model_selection import KFold, StratifiedKFold

import mlflow
import yaml

# Function to train XGBoost
def train_xgboost(params, X, y):
    clf = XGBClassifier(
        learning_rate=params['learning_rate'],
        max_depth=params['max_depth'],
        n_estimators=params['n_estimators']
    )
    clf.fit(X, y)
    mlflow.log_params(params)
    mlflow.sklearn.log_model(clf, "xgboost_model")

# Function to train Random Forest
def train_random_forest(params, X, y):
    clf = RandomForestClassifier(
        n_estimators=params['n_estimators'],
        max_depth=params['max_depth'],
        min_samples_split=params['min_samples_split']
    )
    clf.fit(X, y)
    mlflow.log_params(params)
    mlflow.sklearn.log_model(clf, "random_forest_model")

# Load training config
with open("../config/train_config.yaml", 'r') as f:
    train_config = yaml.safe_load(f)

# Sample dataset
X, y = make_classification()

# Start an MLFlow run and log everything
with mlflow.start_run() as run:
    # Check if xgboost is in config and train
    if 'xgboost' in train_config:
        train_xgboost(train_config['xgboost'], X, y)

    # Check if random_forest is in config and train
    if 'random_forest' in train_config:
        train_random_forest(train_config['random_forest'], X, y)

print("Models trained and logged with MLFlow based on config.")
