from fastapi import FastAPI, HTTPException, Depends
from database.db_utils import table_exists, get_periods_and_tickers, get_filtered_data
from database.db_engine import Session as SessionLocal
from dotenv import load_dotenv
import os

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

# Set up CORS
origins = [
    "http://localhost:3000",  # This is where your React app might run in development
    "http://localhost:8000",  # This is where your FastAPI backend might run
    "http://localhost:5001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

DATABASE_PATH = os.getenv("DATABASE_PATH")
if not DATABASE_PATH:
    raise ValueError(
        "DATABASE_PATH environment variable is not set. Please define it in the .env file."
    )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/db-check")
def check_db_connection():
    try:
        if table_exists("any_table_name"):
            return {
                "status": "success",
                "message": "Connected to the database successfully!",
            }
        else:
            return {
                "status": "success",
                "message": "Connected to the database successfully, but the specified table does not exist.",
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/fa-balance/options")
def get_fa_balance_options(db: SessionLocal = Depends(get_db)):
    return get_periods_and_tickers(db)


# @app.get("/fa-balance/")
# def get_fa_balance_data(period: str, ticker: str, db: SessionLocal = Depends(get_db)):
#     return get_filtered_data(db, period, ticker)


@app.get("/fa-balance/")
def get_fa_balance_data(db: SessionLocal = Depends(get_db)):
    return get_filtered_data(db)
