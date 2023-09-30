

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

dir_path = os.path.dirname(os.path.realpath(__file__))

database_path = os.getenv("DATABASE_PATH")
if not database_path:
    raise ValueError("DATABASE_PATH environment variable is not set. Please define it in the .env file.")

engine = create_engine(f"sqlite:///{database_path}")

Session = sessionmaker(bind=engine)
