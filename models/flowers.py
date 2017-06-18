from db import Database
from flower import Flower


class Flowers:
    def __init__(self):
        self.db = Database()

    def __iter__(self):
        return self

    # TODO iterator over flowers
    def __next__(self):
        for collection in self.db.collections():
            for item in self.db.items(collection):
                flower = Flower(collection, item)
                yield flower
        raise StopIteration

    def put_raw_flower(self, source, raw):
        self.db.insert_one(source, raw)
