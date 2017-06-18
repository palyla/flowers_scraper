from db import Database
from models.flower import Flower


class Flowers:
    def __init__(self):
        self.db = Database()

    def __iter__(self):
        for collection in self.db.collections():
            for flower in self.db.items(collection):
                yield Flower(collection, flower)

        raise StopIteration

    def put_raw_flower(self, source, raw):
        self.db.insert_one(source, raw)
