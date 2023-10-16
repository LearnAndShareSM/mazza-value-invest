from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker


@contextmanager
def session_scope(SessionLocal):
    """Provide a transactional scope around a series of operations."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
