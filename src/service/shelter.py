
from fastapi import Depends, HTTPException, status
from src.enums import DogStatus

from src.repository.shelter import ShelterRepository, get_shelter_repository
from src.schemas import ReadDogSchema
from src.database import ScopedSession
from sqlalchemy.exc import DatabaseError


class ShelterService:
    _return_schema = ReadDogSchema

    def __init__(self, shelter_repository: ShelterRepository):
        self.repository = shelter_repository

    def adopt_dog(self, id: str):
        return ...  # drug mikroservis

    def change_dog_status(self, dog_id: str, dog_status: DogStatus) -> ReadDogSchema:
        try:
            with ScopedSession() as active_session:
                with active_session.begin():
                    dog = self.repository.change_dog_status(
                        dog_id, dog_status, session=active_session)
                    return self._return_schema.from_orm(dog)
        except DatabaseError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="There was an error updating a reason",
            )


def get_sheler_service(shelter_repository: ShelterRepository = Depends(get_shelter_repository)):
    return ShelterService(shelter_repository=shelter_repository)
