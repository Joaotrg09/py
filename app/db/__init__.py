from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from app.config import DATABASE_URL

from contextlib import contextmanager

Base = declarative_base()

engine = create_engine(DATABASE_URL, pool_recycle=10, pool_size=25, max_overflow=15)

SessionLocal = scoped_session(
    sessionmaker(bind=engine, autocommit=False, autoflush=False)
)


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
