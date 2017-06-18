from pymongo import MongoClient
from utils.config import Configuration


class Database(object):
    __instance = None

    def __new__(cls):
        if Database.__instance is None:
            Database.__instance = object.__new__(cls)
        return Database.__instance

    def __init__(self):
        conf = Configuration()
        db_addr = conf.get('database', 'address', fallback='127.0.0.1')
        db_port = conf.getint('database', 'port', fallback=27017)
        db_name = conf.get('database', 'name', fallback='flowers')
        clean_database = conf.getboolean('database', 'clean', fallback=True)

        self.client = MongoClient(host=db_addr, port=db_port, connect=True)

        if clean_database:
            self.client.drop_database(db_name)

        self.db = self.client.get_database(db_name)

    def insert_one(self, name: str, dict: dict):
        return self.db.get_collection(name).insert_one(dict)

    def drop_by_name(self, name: str):
        return self.db.get_collection(name).drop()

    def collections(self):
        return self.db.collection_names(include_system_collections=False)

    def items(self, name):
        return self.db[name].find({}, {"_id": 0})
