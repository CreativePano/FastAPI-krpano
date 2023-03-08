import pymongo

mongo = pymongo.MongoClient('mongodb://localhost:27017/')
db = mongo['krpano']

def dao_add_user(user):
    return db.userList.insert_one(user.dict()).inserted_id


def dao_get_user(user_id):
    return db.userList.find_one({'user_id': user_id})


def dao_update_user(user):
    return db.userList.update_one({'user_id': user.user_id}, {'$set': user.dict()}).modified_count