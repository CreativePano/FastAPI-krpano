from fastapi import APIRouter, HTTPException, File, UploadFile

from model import Pano
from db import database

router = APIRouter()


@router.get("/paonList")
def get_pano_list():
    pano_list = database.dao_get_pano_list()
    [pano.pop('_id') for pano in pano_list]
    if len(pano_list) > 0:
        return pano_list
    else:
        raise HTTPException(status_code=404, detail="Pano not found")


@router.post("/addPano")
def add_pano(pano: Pano):
    if database.dao_get_pano(pano.pano_id) is None:
        user = database.dao_get_user(pano.pano_publisher)
        if user is not None:
            user.pop('_id')
            user['user_publish_list'].append(pano.pano_id)
            database.dao_add_pano(pano)
        else:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "Pano added"}
    else:
        raise HTTPException(status_code=400, detail="Pano already exists")


@router.get("/getPano/{pano_id}")
def get_pano(pano_id: str):
    pano = database.dao_get_pano(pano_id)
    if pano is not None:
        pano.pop('_id')
        return pano
    else:
        raise HTTPException(status_code=404, detail="Pano not found")


@router.get("/panoLike")
def pano_like(pano_id: str, user_id: str):
    pano = database.dao_get_pano(pano_id)
    if pano is not None:
        pano.pop('_id')
        publisher = database.dao_get_user(pano['pano_publisher'])
        publisher.pop('_id')
        liker = database.dao_get_user(user_id)
        liker.pop('_id')
        if user_id in pano['pano_liker_list']:
            pano['pano_liker_list'].remove(user_id)
            publisher['user_like_num'] -= 1
            database.dao_update_user(publisher)
            liker['user_like_list'].remove(pano_id)
            database.dao_update_user(liker)
        else:
            pano['pano_liker_list'].append(user_id)
            publisher['user_like_num'] += 1
            database.dao_update_user(publisher)
            liker['user_like_list'].append(pano_id)
            database.dao_update_user(liker)
        database.dao_update_pano(pano)
        return pano
    else:
        raise HTTPException(status_code=404, detail="Pano not found")


@router.get("/panoComment")
def pano_comment(id: str, des: str, time: str, user_id: str):
    pano = database.dao_get_pano(id)
    if pano is not None:
        pano.pop('_id')
        pano['pano_comment_list'].append({'id': id, 'des': des, 'time': time, 'user_id': user_id})
        database.dao_update_pano(pano)
        return pano
    else:
        raise HTTPException(status_code=404, detail="Pano not found")

@router.get("/deletePano")
def delete_pano(pano_id: str, user_id: str):
    pano = database.dao_get_pano(pano_id)
    if pano is not None:
        pano.pop('_id')
        if pano['pano_publisher'] == user_id:
            database.dao_delete_pano(pano_id)
            return {"message": "Pano deleted"}
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")
    else:
        raise HTTPException(status_code=404, detail="Pano not found")

@router.get("/search")
def search_pano(find: str):
    pano_list = database.dao_search_pano(find)
    [pano.pop('_id') for pano in pano_list]
    if len(pano_list) > 0:
        return pano_list
    else:
        raise HTTPException(status_code=404, detail="Pano not found")


@router.post("/hotspots")
def rebuild_hotspots(pano_id: str, hotspots: list):
    pano = database.dao_get_pano(pano_id)
    if pano is not None:
        pano.pop('_id')
        pano['pano_hotspots'] = hotspots
        database.dao_update_pano(pano)
        return pano
    else:
        raise HTTPException(status_code=404, detail="Pano not found")
