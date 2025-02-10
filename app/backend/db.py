from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engin = create_engine('sqlite:///taskmanager.db', echo= True)

SessionLocal = sessionmaker(bind=engin)

class Base(DeclarativeBase):
    pass

