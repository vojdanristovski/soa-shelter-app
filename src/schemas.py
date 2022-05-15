from typing import Optional
from pydantic import BaseModel, Field, BaseConfig
from src.enums import DogBreed, DogStatus
from datetime import datetime


class BaseDbSchema(BaseModel):
    id_: int = Field(alias="id")
    created_at: datetime
    updated_at: Optional[datetime]

    class Config(BaseConfig):
        allow_population_by_field_name: bool = True


class ReadDogSchema(BaseDbSchema):
    name: str
    breed: DogBreed
    dog_status: DogStatus
    coordinates: Optional[str]
    is_chipped: bool
    image_url: Optional[str]

    class Config:
        orm_mode = True


class CreateDogSchema(BaseModel):
    name: str
    image_url: Optional[str]
    is_chipped: Optional[bool]
    coordinates: Optional[str]
    breed: DogBreed
