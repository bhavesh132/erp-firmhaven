from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os
from dotenv import load_dotenv
from typing import Generator
from contextlib import contextmanager
from urllib.parse import quote_plus

load_dotenv(".env")

DATABASE_URL = os.getenv("DATABASE_URL_PYTHON")
if not DATABASE_URL:
    raise ValueError("Database URL is not defined")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
print('attempting connection to db')
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    print('creating db session local', db)
    print('Connected Session', db)
    try: 
        print('connected to db')
        yield db
    finally: 
        db.close()


def get_engine_for_schema(schema_name: str):
    """
    Returns a SQLAlchemy engine with search_path set to the given tenant schema.
    """
    encoded_schema = quote_plus(f"-csearch_path={schema_name}")
    schema_url = f"{DATABASE_URL}?options={encoded_schema}"
    return create_engine(schema_url, pool_pre_ping=True)


@contextmanager
def get_tenant_session(schema_name: str) -> Generator[Session, None, None]:
    """
    Yields a session connected to the given tenant schema.
    """
    engine = get_engine_for_schema(schema_name)
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from fastapi import Header, Depends

def get_schema_from_header(x_tenant_id: str = Header(...)) -> str:
    return f"tenant_{x_tenant_id}"
