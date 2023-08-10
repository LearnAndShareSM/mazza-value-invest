from .db_engine import Session

from sqlalchemy.orm import sessionmaker
import pandas as pd
from sqlalchemy import inspect, text

from sqlalchemy import inspect, create_engine
from sqlalchemy.orm import sessionmaker
import yaml
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
credentials_path = os.path.join(dir_path, "..", "credentials.yaml")

with open(credentials_path, "r") as file:
    config = yaml.safe_load(file)

engine = create_engine(f"sqlite:///{config['database']['file']}")
Session = sessionmaker(bind=engine)


def table_exists(table_name):
    """Verifica se la tabella esiste nel database."""
    inspector = inspect(engine)
    return table_name in inspector.get_table_names()


def bulk_insert_data_from_dataframe(TableClass, dataframe):
    """Inserisci tutti i record del dataframe nella tabella. Se la tabella non esiste, creala."""
    with Session() as session:
        if not table_exists(TableClass.__tablename__):
            print(f"Creating table {TableClass.__tablename__}...")
            TableClass.__table__.create(bind=engine)
        
        # Inserisci tutti i record del dataframe in bulk
        data = dataframe.to_dict(orient='records')
        session.bulk_insert_mappings(TableClass, data)
        session.commit()



def read_table_data(engine, table_name):
    with Session() as session:
        inspector = inspect(engine)
        if table_name in inspector.get_table_names():
            query_result = session.execute(text(f"SELECT * FROM {table_name}"))
            column_names = query_result.keys()
            result = query_result.fetchall()
            return pd.DataFrame(result, columns=column_names)
        else:
            print(f"The table {table_name} does not exist in the database.")
            return pd.DataFrame()

