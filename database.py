from sqlalchemy import create_engine
from sqlalchemy.orm import session_maker
from sqlalchemy.ext.declarative import declarative_base

DB_NAME="birthday_test"
URL_DATABASE = f'postgresql+psycopg2://postgres:noorraghib12@localhost:5432/{DB_NAME}'





engine=create_engine(URL_DATABASE)

SessionLocal=session_maker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()