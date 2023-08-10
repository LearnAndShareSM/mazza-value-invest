from fastapi import FastAPI, Depends
from .db import read_table_data, engine, Session
from .db.schema_models import FaBalance
from sqlalchemy.orm import sessionmaker

app = FastAPI()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/fa_balance/")
def read_fa_balance_data(db: Session = Depends(get_db)):
    return db.query(FaBalance).all()
