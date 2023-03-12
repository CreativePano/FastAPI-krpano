from fastapi import APIRouter, HTTPException

from model import User
from db import database

router = APIRouter()


@router.post("/addUser")
def add_user(user: User):
    if database.dao_get_user_by_name(user.user_name) is None:
        database.dao_add_user(user)
        return {"message": "User added"}
    else:
        raise HTTPException(status_code=400, detail="User already exists")


@router.get("/getUser/{user_id}")
def get_user(user_id: str):
    user = database.dao_get_user(user_id)
    user.pop('_id')
    if user is not None:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@router.get("/login")
def verify_user(user_name: str, user_password: str):
    user = database.dao_get_user_by_name(user_name)
    if user is not None:
        if user['user_password'] == user_password:
            user.pop('_id')
            return user
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")


@router.post("/updateUser")
def update_user(user: User):
    if database.dao_update_user(user) == 1:
        return {"message": "User updated"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
