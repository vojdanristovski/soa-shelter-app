

from typing import Optional
from fastapi import APIRouter, Depends, Query

from src.schemas import ReadDogSchema

from src.enums import DogStatus
from src.service.shelter import ShelterService, get_sheler_service


router = APIRouter(prefix="/shelter", tags=["Shelter"])


# @router.post("/adopt/{dog_id}", response_model=any)
# def adopt_dog(dog_id: str):
#     return ...
@router.get("/list_dogs_by_status")
async def list_dogs_by_status(status:Optional[DogStatus]=Query(None),shelter_service: ShelterService = Depends(get_sheler_service)):
    return shelter_service.list_dogs_by_status(status)

@router.post("/change_dog_status/{dog_id}", response_model=ReadDogSchema)
async def change_dog_status(dog_id: str, status: DogStatus, shelter_service: ShelterService = Depends(get_sheler_service)):
    return shelter_service.change_dog_status(dog_id, status)
