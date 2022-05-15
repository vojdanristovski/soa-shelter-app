from typing import List, Optional
from fastapi import Depends, HTTPException, status
from src.enums import DogStatus

from src.repository.shelter import ShelterRepository, get_shelter_repository
from src.schemas import ReadDogSchema, CreateDogSchema
from src.models.dog import Dog
from src.database import ScopedSession
from sqlalchemy.exc import DatabaseError


class ShelterService:
    _return_schema = ReadDogSchema

    def __init__(self, shelter_repository: ShelterRepository):
        self.repository = shelter_repository

    def adopt_dog(self, id: str):
        return ...  # drug mikroservis

    async def change_dog_status(
        self, dog_id: str, dog_status: DogStatus
    ) -> ReadDogSchema:
        try:
            async with ScopedSession() as active_session:
                async with active_session.begin():
                    dog = await self.repository.change_dog_status(
                        dog_id, dog_status, session=active_session
                    )
                    return self._return_schema.from_orm(dog)
        except DatabaseError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="There was an error changing dog status",
            )

    async def list_dogs_by_status(
        self, dog_status: Optional[DogStatus]
    ) -> List[ReadDogSchema]:
        if dog_status is None:
            dog_status = []
        try:
            async with ScopedSession() as active_session:
                async with active_session.begin():
                    dogs = await self.repository.list_dogs_by_status(
                        dog_status, session=active_session
                    )
                    content = [self._return_schema.from_orm(dog) for dog in dogs]
                    return content

        except DatabaseError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="There was an error fetching dogs",
            )

    async def create_dog(self, dog: CreateDogSchema) -> ReadDogSchema:
        try:
            entity = Dog(**dog.dict(exclude_unset=True), dog_status=DogStatus.WAITING)
            async with ScopedSession() as active_session:
                async with active_session.begin():
                    persisted = await self.repository.insert_one(
                        entity, session=active_session
                    )
                    return ReadDogSchema.from_orm(persisted)

        except DatabaseError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="There was an error creating a dog",
            )


def get_shelter_service(
    shelter_repository: ShelterRepository = Depends(get_shelter_repository),
):
    return ShelterService(shelter_repository=shelter_repository)
