from fastapi import FastAPI, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from .db import db_engine, schema_models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # Cambia questo per limitare i domini
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Lista di campi validi per filtrare e ordinare
# VALID_FIELDS = [column.name for column in schema_models.Balance.__table__.columns]


@app.get("/db_check/")
def check_db_connection(db: Session = Depends(db_engine.Session)):
    try:
        # Esegui una query semplice per verificare la connessione
        db.execute("SELECT 1")
        return {"status": "Database connection is OK"}
    except Exception as e:
        return {"status": "Database connection failed", "error": str(e)}

# @app.get("/fa_balance/")
# def get_fa_balance(
#     db: Session = Depends(db_engine.Session),
#     filter_field: str = Query(None, description="Campo da filtrare"),
#     filter_value: str = Query(None, description="Valore del filtro"),
#     order_field: str = Query(None, description="Campo per ordinare"),
# ):
#     query = db.query(schema_models.Balance)

#     if filter_field:
#         if filter_field not in VALID_FIELDS:
#             raise HTTPException(status_code=400, detail=f"Campo {filter_field} non valido.")
#         query = query.filter(getattr(schema_models.Balance, filter_field) == filter_value)
    
#     if order_field:
#         if order_field not in VALID_FIELDS:
#             raise HTTPException(status_code=400, detail=f"Campo {order_field} non valido.")
#         query = query.order_by(getattr(schema_models.Balance, order_field))

#     # Implementazione base della paginazione
#     results = query.limit(50).all()

#     return results


# @app.get("/available_tickers/")
# def get_available_tickers(db: Session = Depends(db_engine.Session)):
#     # Esegui una query per ottenere tutti i ticker univoci
#     tickers = db.query(schema_models.Balance.ticker).distinct().all()

#     print(tickers)
#     # Converti i risultati in una lista semplice
#     ticker_list = [ticker[0] for ticker in tickers]

#     return ticker_list
