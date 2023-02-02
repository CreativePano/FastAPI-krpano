from fastapi import APIRouter

from api import user
from api import pano

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["user"])
# api_router.include_router(pano.router, prefix="/pano", tags=["pano"])
