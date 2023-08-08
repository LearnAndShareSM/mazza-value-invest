from .db_engine import Session

from sqlalchemy.orm import sessionmaker
import pandas as pd
from sqlalchemy import inspect, text



def insert_data(TableClass, record):
    session = Session()
    session.add(TableClass(**record))
    session.commit()
    session.close()



def read_table_data(engine, table_name):

    Session = sessionmaker(bind=engine)
    session = Session()

    inspector = inspect(engine)
    if table_name in inspector.get_table_names():
    # Use SQLAlchemy's native methods to query the database
        query_result = session.execute(text(f"SELECT * FROM {table_name}"))

        # Get the column names directly from the CursorResult object
        column_names = query_result.keys()

        # Fetch all results into a list
        result = query_result.fetchall()

        # Convert the result to a pandas DataFrame
        df = pd.DataFrame(result, columns=column_names)
           
        session.close()
        return df
    else:
        session.close()
        
        df = pd.DataFrame()
        print(f"The table {table_name} does not exist in the database.")
    
    return df

# Usage example:
# df = read_table_data(engine, "fa_balance")
