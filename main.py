from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import uvicorn
from src.api.api import router
from src import models
from src.database import engine


models.Base.metadata.create_all(bind=engine)


app=FastAPI()

app.include_router(router, prefix="/api/v1")

if __name__ == '__main__':
    uvicorn.run(app, port=8003, host='localhost')
