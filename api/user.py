from fastapi import APIRouter, HTTPException

from model import User

router = APIRouter()


@router.post("/addUser", response_model=User)
def add_user(user: User):
    print(user)
    return {"message": "User added"}


@router.get("/getUser/{user_id}")
def get_user(user_id: str):
    return {"message": f"User {user_id} fetched"}


@router.get("/updateUser/{user_id}")
def update_user(user_id: str):
    return {"message": f"User {user_id} updated"}
