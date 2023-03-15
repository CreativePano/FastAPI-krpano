import pymongo

mongo = pymongo.MongoClient('mongodb://net6.takina.live:27017/')
db = mongo['krpano']


def dao_add_user(user):
    return db.userList.insert_one(user.dict()).inserted_id


def dao_get_user(user_id):
    return db.userList.find_one({'user_id': user_id})


def dao_get_user_by_name(user_name):
    return db.userList.find_one({'user_name': user_name})

def dao_update_user(user):
    return db.userList.update_one({'user_id': user['user_id']}, {'$set': user}).modified_count


def dao_get_pano_list():
    return list(db.panoList.find())


def dao_add_pano(pano):
    return db.panoList.insert_one(pano.dict()).inserted_id


def dao_get_pano(pano_id):
    return db.panoList.find_one({'pano_id': pano_id})


def dao_update_pano(pano):
    return db.panoList.update_one({'pano_id': pano['pano_id']}, {'$set': pano}).modified_count

def dao_delete_pano(pano_id):
    return db.panoList.delete_one({'pano_id': pano_id}).deleted_count
