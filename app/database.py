from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:npg_A8GD5TWBUENy@ep-misty-shadow-b4rki4im-pooler.c-6.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require" # this is the connection string to connect to the database. The format is: dialect+driver://username:password@host:port/database

engine = create_engine(SQLALCHEMY_DATABASE_URL) # this is the engine that will be used to connect to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # this is the session that will be used to connect to the database
Base = declarative_base() # this is the base class that will be used to define the models


def get_db():
    db = SessionLocal()
    try:
        yield db # this will yield the database session to the path operation function
    finally:
        db.close() # this will close the database session after the path operation function is done