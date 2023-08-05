from .db_engine import Session

def insert_data(TableClass, record):
    session = Session()
    session.add(TableClass(**record))
    session.commit()
    session.close()
