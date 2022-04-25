from fastapi import FastAPI
from .database import SessionLocal
from sqlalchemy.orm import Session
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_model=None)
def init(db: Session=Depends(get_db)):
    return {"Hello" : "World"}

