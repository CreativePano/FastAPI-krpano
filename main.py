from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.api import api_router

app = FastAPI(
    title="FastAPI",
    description="krpano FastAPI backend",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
