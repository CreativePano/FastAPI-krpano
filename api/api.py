from fastapi import APIRouter

from api import user
from api import pano
from api import filter

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(pano.router, prefix="/pano", tags=["pano"])
api_router.include_router(filter.router, prefix="/filter", tags=["filter"])
