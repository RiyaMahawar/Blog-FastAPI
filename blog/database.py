from sqlalchemy import create_engine #creates a connection to the db
from sqlalchemy.ext.declarative import declarative_base #define the base class for the model(table)
from sqlalchemy.orm import sessionmaker #helps create db sessions

SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()
