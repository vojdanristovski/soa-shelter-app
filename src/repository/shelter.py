from typing import List
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select, update

from src.models.dog import Dog
from src.enums import DogStatus


class ShelterRepository:
    async def change_dog_status(
        self, dog_id: str, dog_status: DogStatus, session: AsyncSession
    ) -> Dog:
        statement = update(Dog).values(dog_status=dog_status).where(Dog.id == dog_id)
        result = await session.execute(statement)
        return result.unique().scallars().first()

    async def list_dogs_by_status(
        self, dog_status: DogStatus, session: AsyncSession
    ) -> List[Dog]:
        statement = select(Dog).where(Dog.dog_status == dog_status)
        result = await session.execute(statement)
        return result.unique().scalars().all()

    async def create_dog(self, dog: Dog, session: AsyncSession) -> Dog:
        session.add(dog)
        await session.flush()
        await session.refresh(dog)
        return dog


def get_shelter_repository():
    return ShelterRepository()
