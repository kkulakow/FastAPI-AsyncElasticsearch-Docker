"""
DB setiings.
"""
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
import os


db_path = os.path.join(os.path.dirname(__file__), 'posts.db')
SQLALCHEMY_DATABASE_URL = 'sqlite:///{}'.format(db_path)
engine = create_engine(
     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
 )


SessionLocal = sessionmaker(bind=engine, autocommit=False,autoflush=False)

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()