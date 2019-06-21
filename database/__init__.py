from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

DB_URL = "postgresql://postgres:postgres@localhost:5432/falcon"

def get_engine(uri):
    options = {
        "pool_recycle": 3600,
        "pool_size": 10,
        "pool_timeout": 30,
        "max_overflow": 30,
        "execution_options": True,
    }
    return create_engine(uri, **options)


db_session = scoped_session(sessionmaker())
engine = get_engine(DB_URL)


def init_session():
    db_session.configure(bind=engine)

    from app.model import Base

    Base.metadata.create_all(engine)