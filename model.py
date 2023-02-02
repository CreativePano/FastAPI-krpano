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


class UserLike(BaseModel):
    user_id: str            # 外键合并主键
    pano_id: list           # 外键合并主键


class UserPublish(BaseModel):
    user_id: str            # 外键合并主键
    pano_id: list           # 外键合并主键


class UserCollection(BaseModel):
    user_id: str            # 外键合并主键
    pano_id: list           # 外键合并主键
