from datetime import datetime
from loguru import logger
from fetch_data.fetch_equities import (
    fetch_and_store_profiles,
    fetch_and_store_financial_statements,
)
from database.database_session import SessionLocal, engine
from common.config import FMP_API_KEY

# Initialize Loguru with file logging, rotation, and level
logger.add("data_pipeline_{time}.log", rotation="1 week", level="INFO", serialize=True)

if __name__ == "__main__":
    run_id = (
        datetime.now().isoformat()
    )  # Generate run_id based on current date and time
    try:
        logger.bind(run_id=run_id).info("Starting data pipeline")

        fetch_and_store_profiles(engine, FMP_API_KEY, SessionLocal, run_id)
        fetch_and_store_financial_statements(engine, FMP_API_KEY, SessionLocal, run_id)

    except Exception as e:
        logger.bind(run_id=run_id).exception("An error occurred: {}", e)
