from fastapi import APIRouter, HTTPException

from model import Pano
from db import database

router = APIRouter()


@router.get("/paonList")
def get_pano_list():
    pano_list = database.dao_get_pano_list()
    [pano.pop('_id') for pano in pano_list]
    print(pano_list)
    if len(pano_list) > 0:
        return pano_list
    else:
        raise HTTPException(status_code=404, detail="Pano not found")


@router.post("/addPano")
def add_pano(pano: Pano):
    if database.dao_add_pano(pano):
        user = database.dao_get_user(pano.pano_publisher)
        user.pop('_id')
        user['user_publish_list'].append(pano.pano_id)
        return {"message": "Pano added"}
    else:
        raise HTTPException(status_code=400, detail="Pano already exists")


@router.get("/getPano/{pano_id}")
def get_pano(pano_id: str):
    pano = database.dao_get_pano(pano_id)
    pano.pop('_id')
    if pano is not None:
        return pano
    else:
        raise HTTPException(status_code=404, detail="Pano not found")


@router.get("/panoLike")
def pano_like(pano_id: str, user_id: str):
    pano = database.dao_get_pano(pano_id)
    pano.pop('_id')
    if pano is not None:
        if user_id in pano['pano_liker_list']:
            pano['pano_liker_list'].remove(user_id)
        else:
            pano['pano_liker_list'].append(user_id)
            publisher = database.dao_get_user(pano.pano_publisher)
            publisher.pop('_id')
            publisher['user_like_num'] += 1
            database.dao_update_user(publisher)
            liker = database.dao_get_user(user_id)
            liker.pop('_id')
            liker['user_like_list'].append(pano_id)
            database.dao_update_user(liker)
        database.dao_update_pano(pano)
        return pano
    else:
        raise HTTPException(status_code=404, detail="Pano not found")


@router.get("/panoComment")
def pano_comment(id: str, des: str, time: str, user_id: str):
    pano = database.dao_get_pano(id)
    pano.pop('_id')
    if pano is not None:
        pano['pano_comment_list'].append({'id': id, 'des': des, 'time': time, 'user_id': user_id})
        database.dao_update_pano(pano)
        return pano
    else:
        raise HTTPException(status_code=404, detail="Pano not found")
