from pymongo import MongoClient


class Database(object):
    __instance = None

    def __new__(cls):
        if Database.__instance is None:
            Database.__instance = object.__new__(cls)
        return Database.__instance

    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.client.drop_database("localhost")
        self.db = self.client.localhost

    def insert_one(self, name: str, dict: dict):
        self.db[name].insert_one(dict)

    def drop_by_name(self, name: str):
        self.db[name].drop()

    def collections(self):
        return self.db.collection_names(include_system_collections=False)

    def items(self, name):
        return self.db[name].find({}, {"_id": 0, "name": 1, "prices": 1})
