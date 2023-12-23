from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase

import config


engine = create_engine(
    url=config.SQLALCHEMY_URL, 
    echo=config.SQLALCHEMY_ECHO
)
session = Session(
    autocommit=config.SESSION_AUTOCOMMIT,
    autoflush=config.SESSION_AUTOFLUSH,
    bind=engine
)


class Base(DeclarativeBase):
    pass


def get_db():
    db = session()

    try:
        yield db
    finally:
        db.close()
