from typing import Generator
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
from .config import get_config

engine=create_engine(get_config().database_url)

Base=declarative_base()

ScopedSession=scoped_session(sessionmaker(bind=engine))



def get_session() -> Generator[scoped_session, None, None]:
    yield ScopedSession()
