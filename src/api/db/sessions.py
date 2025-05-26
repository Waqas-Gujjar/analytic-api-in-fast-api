from .configs import DATABASE_URL
from sqlmodel import SQLModel,Session
import sqlmodel



if DATABASE_URL == "":
    raise NotImplemented("DATABASE NEED TO SET ")


engin = sqlmodel.create_engine(DATABASE_URL)


def init_db():
    print("create database")
    SQLModel.metadata.create_all(engin)

def get_session():
    with Session(engin) as session:
        yield session


