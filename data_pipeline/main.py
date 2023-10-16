from fetch_data.fetch_equities import (
    fetch_and_store_profiles,
    fetch_and_store_financial_statements,
)
from database.database_session import SessionLocal, engine  # Centralized import
from utils.config import FMP_API_KEY  # Centralized configuration
from prometheus_client import start_http_server
import logging  # Using logging instead of print statements

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    start_http_server(8000)
    logger.info("HTTP server started on port 8000")

    try:
        fetch_and_store_profiles(engine, FMP_API_KEY, SessionLocal)
        fetch_and_store_financial_statements(engine, FMP_API_KEY, SessionLocal)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
