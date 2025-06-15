#this will handle the database connection

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL) #this engine makes the connection with the database

SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine) #this will helps talk with the database

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# try: #this is a postgres driver which helps in connecting with the database but we are now using sqlachemy driver
#     conn = psycopg2.connect(host='localhost', dbname='fastapi', user='postgres', 
#                             password = 'Abhay1998', cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("Database connection was successful")
# except Exception as error:
#     print("Connection to the database failed")
#     print("Erorr: ", error)
