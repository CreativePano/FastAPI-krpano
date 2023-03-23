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

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True,
                ssl_keyfile="./maxin.key", ssl_certfile="./maxinfull.crt")
