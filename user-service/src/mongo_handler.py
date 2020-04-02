from .config import Config
import pymongo


class MongoHandler(object):

    def __init__(self):
        self._mongo_client = pymongo.MongoClient(Config.DB_HOST,
                                                 username=Config.DB_USERNAME,
                                                 password=Config.DB_PASSWORD,
                                                 authSource=Config.DB_NAME,
                                                 authMechanism=Config.DB_AUTH)

    def _user_collection(self):
        return self._mongo_client[Config.DB_NAME][Config.DB_COLLECTION_USERS]

    def persist_user(self, user):
        self._user_collection(self).insert_one(user)

    def get_users(self):
        self._user_collection(self).find()