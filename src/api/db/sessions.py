from .configs import DATABASE_URL
from sqlmodel import SQLModel, Session, create_engine

if DATABASE_URL == "":
    raise NotImplementedError("DATABASE_URL needs to be set")

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


