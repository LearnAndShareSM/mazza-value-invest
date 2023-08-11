# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# import yaml
# import os

# dir_path = os.path.dirname(os.path.realpath(__file__))

# credentials_path = os.path.join(dir_path, "..", "credentials.yaml")
# with open(credentials_path, "r") as file:
#     config = yaml.safe_load(file)

# # Check if we are in TEST_MODE
# if os.environ.get("TEST_MODE") == "true":
#     database_path = os.path.join(dir_path, "..", "test_value_invest.db")
# else:
#     database_path = os.path.join(dir_path, "..", config["database"]["file"])

# engine = create_engine(f"sqlite:///{database_path}")

# Session = sessionmaker(bind=engine)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

dir_path = os.path.dirname(os.path.realpath(__file__))

# Fetch the database path from environment variable
database_path = os.getenv("DATABASE_PATH")
if not database_path:
    raise ValueError("DATABASE_PATH environment variable is not set. Please define it in the .env file.")

engine = create_engine(f"sqlite:///{database_path}")

Session = sessionmaker(bind=engine)
