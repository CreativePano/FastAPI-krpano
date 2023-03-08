from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    user_avatar: str
    user_name: str
    user_phone: str
    user_like_num: int
    user_like_list: list
    user_publish_list: list
    user_collection_list: list


class pano(BaseModel):
    pano_id: str
    pano_name: str
    pano_publish_time: str
    pano_publisher: str
    pano_address: str
    pano_img_list: list
    pano_liker_list: list
    pano_comment_list: list


class img(BaseModel):
    img: str
    name: str


class comment(BaseModel):
    id: str
    des: str
    time: str
    user_id: str
