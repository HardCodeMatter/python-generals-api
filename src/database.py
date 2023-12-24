from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

import config


engine = create_engine(
    url=config.SQLALCHEMY_URL, 
    echo=config.SQLALCHEMY_ECHO
)
Session = sessionmaker(
    autocommit=config.SESSION_AUTOCOMMIT,
    autoflush=config.SESSION_AUTOFLUSH,
    bind=engine
)


class Base(DeclarativeBase):
    pass


def get_db():
    db = Session()

    try:
        yield db
    finally:
        db.close()
