from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session

engine=create_engine("postgresql://shelter-app:shelter-app@db:5432/shelter-app")

ScopedSession=scoped_session(sessionmaker(bind=engine))



def get_session() -> Generator[scoped_session, None, None]:
    yield ScopedSession()
