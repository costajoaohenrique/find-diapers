from pymongo import MongoClient

from src.config.config import Config
from src.domain.diaper import Diaper


class DiaperRepository:

    def __init__(self):
        mongo_client = MongoClient(Config.DB_URI)
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
