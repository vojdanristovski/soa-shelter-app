from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from src.api.api import router
from src import models
from src.database import SessionLocal,engine


models.Base.metadata.create_all(bind=engine)


app=FastAPI()

app.include_router(router, prefix="/api/v1")
