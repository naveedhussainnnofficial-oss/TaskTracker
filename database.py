
from sqlmodel import SQLModel,Session , create_engine 


engine=create_engine("sqlite:///database.db",connect_args={"check_same_thread":False})


def create_table():
    SQLModel.metadata.create_all(engine)


def create_session():
    with Session(engine) as session :
        yield session

