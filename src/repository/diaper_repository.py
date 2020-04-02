from pymongo import MongoClient

from src.config.config import Config
from src.domain.diaper import Diaper


class DiaperRepository:
    CONNECTION = f"mongodb://{Config.DB_USER_NAME}:{Config.DB_USER_PASSWORD}@{Config.DB_SERVER}/?authSource=admin"

    def __init__(self):
        mongo_client = MongoClient(DiaperRepository.CONNECTION)
        db = mongo_client[Config.DB_NAME]
        self._collection = db["diapers"]

    def save(self, diaper: Diaper):
        if not diaper.id:
            self.insert(diaper)
        self.update(diaper)

    def find_by_sku(self, sku):
        one = self._collection.find_one({"sku": sku})
        return Diaper.create_from_dict(one) if one else None

    def insert(self, diaper):
        document = dict(diaper)
        del document["_id"]
        self._collection.insert_one(document)

    def update(self, diaper):
        myquery = {"sku": diaper.sku}
        newvalues = {"$set": {"prices": [dict(price) for price in diaper.prices]}}
        self._collection.update_one(myquery, newvalues)
