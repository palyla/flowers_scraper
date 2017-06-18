from db import Database
from models.flower import Flower
from itertools import chain


class Flowers:
    def __init__(self):
        self.db = Database()

    def __iter__(self):
        result = (((Flower(collection, flower)) for flower in self.db.items(collection)) for collection in
                  self.db.collections())
        return chain(*result)

    def put_raw_flower(self, source, raw):
        self.db.insert_one(source, raw)
