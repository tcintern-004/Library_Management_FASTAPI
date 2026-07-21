from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db_URL = "postgresql://postgres:8149@localhost:5432/books_db"

engine = create_engine(db_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()