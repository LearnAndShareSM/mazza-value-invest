from database.models.financial_statements import Base, Profile, CashFlow
from fetch_data.fetch_equities import (
    fetch_and_store_profiles,
    fetch_and_store_financial_statements,
)

from utils.context_manager import session_scope
from utils.config import DATABASE_URL, FMP_API_KEY
from sqlalchemy import create_engine
from prometheus_client import start_http_server
from sqlalchemy.orm import sessionmaker

# Initialize SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize database
Base.metadata.clear()
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    start_http_server(8000)

    fetch_and_store_profiles(engine, FMP_API_KEY, SessionLocal)
    fetch_and_store_financial_statements(engine, FMP_API_KEY, SessionLocal)

    Base.metadata.clear()
