from .db_engine import Session
from sqlalchemy.orm import sessionmaker
import pandas as pd
from sqlalchemy import inspect, text


def table_exists(table_name):
    """Verifica se la tabella esiste nel database."""
    with Session() as session:
        inspector = inspect(session.bind)
        return table_name in inspector.get_table_names()


def bulk_insert_data_from_dataframe(TableClass, dataframe):
    """Inserisci tutti i record del dataframe nella tabella. Se la tabella non esiste, creala."""
    with Session() as session:
        if not table_exists(TableClass.__tablename__):
            print(f"Creating table {TableClass.__tablename__}...")
            TableClass.__table__.create(bind=session.bind)
        # Inserisci tutti i record del dataframe in bulk
        data = dataframe.to_dict(orient="records")
        session.bulk_insert_mappings(TableClass, data)
        session.commit()


def read_table_data(table_name):
    """Read all records from the specified table."""
    with Session() as session:
        inspector = inspect(session.bind)
        if table_name in inspector.get_table_names():
            query_result = session.execute(text(f"SELECT * FROM {table_name}"))
            column_names = query_result.keys()
            result = query_result.fetchall()
            return pd.DataFrame(result, columns=column_names)
        else:
            print(f"The table {table_name} does not exist in the database.")
            return pd.DataFrame()


from .schema_models import Balance


def get_periods_and_tickers(session):
    periods = session.query(Balance.period).distinct().all()
    tickers = session.query(Balance.ticker).distinct().all()
    return {"periods": [x[0] for x in periods], "tickers": [x[0] for x in tickers]}


# def get_filtered_data(session, period, ticker):
#     return session.query(Balance).filter_by(period=period, ticker=ticker).all()

def get_filtered_data(session):
    return session.query(Balance).all()