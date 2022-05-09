from select import select
from sqlalchemy.orm import scoped_session
from src.enums import DogStatus

from src.models import dog as Dog
from sqlalchemy.sql.expression import select, update

class ShelterRepository:

    def change_dog_status(self, dog_id : str, dog_status : DogStatus, session:scoped_session) -> any:
        
        statement = (
            update(Dog)
            .values(dog_status = dog_status)
            .where(Dog.id == dog_id)
        )
        entry = session.execute(statement).unique().scallars().first()
        return entry


    def list_dogs_by_status(self, dog_status : DogStatus, session:scoped_session) -> any:

        statement = (
            select(Dog)
            .where(Dog.dog_status == dog_status)
        )

        entries = session.execute(statement).unique().scalars().all()

        return entries


def get_shelter_repository():
    return ShelterRepository()
