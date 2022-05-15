from fastapi import APIRouter
from src.api import shelter


router = APIRouter()


router.include_router(shelter.router)
