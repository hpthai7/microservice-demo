from .config import Config
from .utils.helper import Helper
from bson.objectid import ObjectId
import pymongo

class MongoHandler(object):

    def __init__(self):
        self._mongo_client = pymongo.MongoClient(host=Config.DB_HOST,
                                                 port=Config.DB_PORT, # necessary
                                                 username=Config.DB_USERNAME,
                                                 password=Config.DB_PASSWORD,
                                                 authSource=Config.DB_NAME,
                                                 authMechanism=Config.DB_AUTH)

    def _talk_collection(self):
        return self._mongo_client[Config.DB_NAME][Config.DB_COLLECTION_TALKS]

    def persist_talk(self, talk):
        if 'talk_id' not in talk:
            talk['talk_id'] = Helper.make_id()
        talk['_id'] = talk['talk_id']
        insert_one_result = self._talk_collection().insert_one(talk)
        return insert_one_result.inserted_id

    def get_talks(self):
        return list(self._talk_collection().find())
        
    def get_talk(self, id):
        return list(self._talk_collection().find(id))