from src.database import Base
from sqlalchemy import String,Boolean,Integer,Column
from .enums import DogBreed,DogStatus
from sqlalchemy.dialects.postgresql import ENUM
class Dog(Base):
    __table__name="dogs"
    id=Column(Integer,primary_key=True)

    image_url=Column(String(255),nullable=True)
    name=Column(String(255),nullable=False)
    is_chipped=Column(Boolean,default=False)
    coordinates=Column(String(255),nullable=True)
    breed=Column(
        ENUM(DogBreed, name="breeds"),
        name="breed",
        nullable=False
        )
    dog_status=Column(
        ENUM(DogStatus, name="statuses"),
        name="dog_status",
        nullable=False
    )
    
    