from typing import Annotated

from fastapi import Depends
from sqlmodel import Field, Session, SQLModel

from app.src.db import engine


class Hero(SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
