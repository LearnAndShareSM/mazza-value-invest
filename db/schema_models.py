from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from .db_engine import engine

Base = declarative_base()

# Define the table with a name, columns, and constraints
class LogAvailableTickers(Base):
    __tablename__ = 'log_available_tickers'
    
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    num_companies = Column(Integer, nullable=False)
    num_tickers = Column(Integer, nullable=False)

# Create the table if it doesn't exist
Base.metadata.create_all(engine)