from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import yaml

# Load the database and API credentials
with open('credentials.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Connect to the database
engine = create_engine(f"sqlite:///{config['database']['file']}")

# Create a new session
Session = sessionmaker(bind=engine)
