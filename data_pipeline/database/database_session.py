from sqlalchemy.orm import sessionmaker
from models.financial_statements import Base
from config.settings import DATABASE_URL
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

Base.metadata.create_all(bind=engine)
