from fastapi import FastAPI, HTTPException
from db.db_utils import table_exists
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

DATABASE_PATH = os.getenv("DATABASE_PATH")
if not DATABASE_PATH:
    raise ValueError("DATABASE_PATH environment variable is not set. Please define it in the .env file.")


@app.get("/db-check")
def check_db_connection():
    try:
        # Try to list tables to check DB connection. This is a simple way to check the connection.
        if table_exists("fa_balance"):
            return {"status": "success", "message": "Connected to the database successfully!"}
        else:
            return {
                "status": "success",
                "message": "Connected to the database successfully, but the specified table does not exist.",
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
