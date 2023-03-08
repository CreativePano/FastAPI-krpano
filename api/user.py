from fastapi import APIRouter, HTTPException

from model import User
from db import database

router = APIRouter()

@router.post("/addUser")
def add_user(user: User):
    if database.dao_add_user(user):
        return {"message": "User added"}
    else:
        raise HTTPException(status_code=400, detail="User already exists")


@router.get("/getUser/{user_id}")
def get_user(user_id: str):
    user = database.dao_get_user(user_id)
    user.pop('_id')
    if user is not None:
        print(user)
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@router.post("/updateUser")
def update_user(user: User):
    if database.dao_update_user(user) == 1:
        return {"message": "User updated"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
