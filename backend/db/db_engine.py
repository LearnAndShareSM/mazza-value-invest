from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import yaml
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
credentials_path = os.path.join(dir_path, '..', 'credentials.yaml')


with open(credentials_path, 'r') as file:
    config = yaml.safe_load(file)


engine = create_engine(f"sqlite:///{config['database']['file']}")


Session = sessionmaker(bind=engine)
