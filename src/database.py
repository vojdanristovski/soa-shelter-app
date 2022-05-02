from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import get_config

engine=create_engine(get_config().database_url)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
