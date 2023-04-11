import requests
from fastapi import APIRouter, HTTPException

from model import Pano
from common.panoprocess import *
from db import database

router = APIRouter()

@router.post("/applyFilter/{filtername}")
def apply_filter(filtername: str, pano: Pano, index: int):
    pano_pic = base64.b64encode(requests.get(pano.pano_img_list[index]).content)
    match filtername:
        case "MovieOrange":
            return {"pano_img": filter_image_two(pano_pic)}
        case "Kameel":
            return {"pano_img": filter_image_three(pano_pic)}
        case "Aomori":
            return {"pano_img": filter_image_four(pano_pic)}
        case "SouthFrance":
            return {"pano_img": filter_image_five(pano_pic)}

@router.post("/diy")
def diy_filter(pano: Pano, index: int, brightness: int, contrast: int, saturation: int, temp: int, tint: int):
    pano_pic = base64.b64encode(requests.get(pano.pano_img_list[index]).content)
    return {"pano_img": filter_image_one(pano_pic)}
