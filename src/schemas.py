from typing import Optional
from pydantic import BaseModel
from .enums import DogBreed, DogStatus


class ReadDogSchema(BaseModel):
    name: str
    breed: DogBreed
    status: DogStatus
    coordinates: Optional[str]
    is_chipped: bool
    image_url: Optional[str]

    class Config:
        orm_mode = True


class CreateDogSchema(BaseModel):
    name: str
    breed: DogBreed
    coordinates: Optional[str]
    is_chipped: Optional[bool]
    image_url: Optional[str]

    class Config:
        orm_mode = True
