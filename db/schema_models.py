from sqlalchemy import Column, Integer, DateTime, String
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
    
    

class LogIngestedTickers(Base):
    __tablename__ = 'log_ingested_tickers'
    
    id = Column(Integer, primary_key=True)
    ingestion_timestamp = Column(DateTime, nullable=False)
    ticker = Column(String, nullable=False)
    num_new_rows = Column(Integer, nullable=False)
    num_old_rows_diff_dates = Column(Integer, nullable=False)
    num_columns = Column(Integer, nullable=False)

# Create the table if it doesn't exist
Base.metadata.create_all(engine)