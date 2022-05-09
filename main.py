from fastapi import FastAPI
import uvicorn
from src.api.api import router



app=FastAPI()



app.include_router(router, prefix="/api/v1")



if __name__ == '__main__':
    uvicorn.run(app, port=8003, host='localhost')
