from sqlalchemy import create_engine #creates a connection to the db
from sqlalchemy.ext.declarative import declarative_base #define the base class for the model(table)
from sqlalchemy.orm import sessionmaker #helps create db sessions


#Here we are using an in-memory database
#SQLALCHEMY is the ORM, SQLITE is the database
#Stores the database in the same directory as scripts (in blog.db)
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'


#Establishing a connection to the database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}
    )
#SQLite is single threaded by default, {"check_same_thread":False} allows multiple threads to access the database (asynchronous)


#Creating a db session
#autocommit=False: Any transaction must be explicitly committed
#autoflush=False: Changes are not automatically written to the db until committed
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


#A base class for defining SQLAlchemy models(tables)
#All ORM models inherit from Base
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()
