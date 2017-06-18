from db import Database
from models.flower import Flower


class Flowers:
    def __init__(self):
        self.db = Database()

    def __iter__(self):
        result = (((Flower(collection, flower)) for flower in self.db.items(collection)) for collection in self.db.collections())
        return result

    def put_raw_flower(self, source, raw):
        self.db.insert_one(source, raw)
