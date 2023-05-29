import requests
from fastapi import APIRouter, HTTPException

from model import Pano
from db import database
from model import Pano
from common.panoprocess import *
from db import database
# 在 common 文件夹中导入 upload 函数
from common.upload import upload

router = APIRouter()

@router.post("/applyFilter/{filtername}")
def apply_filter(filtername: str, pano: Pano, index: int):
    pano_url = "https://oss.jetlab.live" + pano.pano_img_list[index]
    pano_pic = base64.b64encode(requests.get(pano_url).content)
    if filtername == "MovieOrange":
        res=upload(filter_image_two(pano_pic))
        print(res[0]['url'])
        print(pano.pano_id)
        modified_pano_id = pano.pano_id
        # update pano 
        pano = database.dao_get_pano(pano.pano_id)
        if pano is not None:
            # 将 res 替换 pano.pano_img_list[index] 中的 url
            pano['pano_img_list'][index] = res[0]['url']
            database.dao_update_pano(pano)
        else:
            raise HTTPException(status_code=404, detail="Pano not found")
        findpano = database.dao_get_pano(modified_pano_id)
        findpano.pop('_id')
        return findpano
    elif filtername == "Kameel":
        res=upload(filter_image_three(pano_pic))
        print(res[0]['url'])
        print(pano.pano_id)
        modified_pano_id = pano.pano_id
        # update pano 
        pano = database.dao_get_pano(pano.pano_id)
        if pano is not None:
            # 将 res 替换 pano.pano_img_list[index] 中的 url
            pano['pano_img_list'][index] = res[0]['url']
            database.dao_update_pano(pano)
        else:
            raise HTTPException(status_code=404, detail="Pano not found")
        findpano = database.dao_get_pano(modified_pano_id)
        findpano.pop('_id')
        return findpano
    elif filtername == "Aomori":
        res=upload(filter_image_four(pano_pic))
        print(res[0]['url'])
        print(pano.pano_id)
        modified_pano_id = pano.pano_id
        # update pano 
        pano = database.dao_get_pano(pano.pano_id)
        if pano is not None:
            # 将 res 替换 pano.pano_img_list[index] 中的 url
            pano['pano_img_list'][index] = res[0]['url']
            database.dao_update_pano(pano)
        else:
            raise HTTPException(status_code=404, detail="Pano not found")
        findpano = database.dao_get_pano(modified_pano_id)
        findpano.pop('_id')
        return findpano
    elif filtername == "SouthFrance":
        res=upload(filter_image_five(pano_pic))
        print(res[0]['url'])
        print(pano.pano_id)
        modified_pano_id = pano.pano_id
        # update pano 
        pano = database.dao_get_pano(pano.pano_id)
        if pano is not None:
            # 将 res 替换 pano.pano_img_list[index] 中的 url
            pano['pano_img_list'][index] = res[0]['url']
            database.dao_update_pano(pano)
        else:
            raise HTTPException(status_code=404, detail="Pano not found")
        findpano = database.dao_get_pano(modified_pano_id)
        findpano.pop('_id')
        return findpano

@router.post("/diy")
def diy_filter(pano: Pano, index: int, brightness: int, saturation: int, temp: int, tint: int):
    pano_url = "https://oss.jetlab.live" + pano.pano_img_list[index]
    pano_pic = base64.b64encode(requests.get(pano_url).content)
    # return {"pano_img": filter_image_one(pano_pic, brightness, saturation, temp, tint)}
    res=upload(filter_image_one(pano_pic, brightness, saturation, temp, tint))
    print(res[0]['url'])
    print(pano.pano_id)
    modified_pano_id = pano.pano_id
    # update pano 
    pano = database.dao_get_pano(pano.pano_id)
    if pano is not None:
        # 将 res 替换 pano.pano_img_list[index] 中的 url
        pano['pano_img_list'][index] = res[0]['url']
        database.dao_update_pano(pano)
    else:
        raise HTTPException(status_code=404, detail="Pano not found")
    findpano = database.dao_get_pano(modified_pano_id)
    findpano.pop('_id')
    return findpano
