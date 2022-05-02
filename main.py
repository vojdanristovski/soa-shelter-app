from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()


class Item(BaseModel):
    id : Optional[int] = 2 #ako nema id ke bide 2 sekogas
    name : str


@app.get("/")
def index():
    return {"message" : "Hello World"}

@app.get("/greet/{name}")
def greet(name : str):
    return {"Hello" : name}

@app.post("/item")
def add_new_item(item:Item):
    return {'name' : item.name, "id" : item.id}