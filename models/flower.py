import os

from db import Database


class Flower:
    #FIELDS = ["source", "name", "wholesale"]
    wholesale = dict()

    def __init__(self, source: str, raw: dict):
        self.source = source
        self.name = raw["name"]
        for pieces, price in raw["prices"].items():
            self.wholesale[pieces] = price

    #def _get_raw(self):
    #    return {field : getattr(self, field) for field in self.FIELDS}

    def set_unit_from_pieces(self, pieces: int, unit_price: float):
        if pieces not in self.wholesale.keys():
            self.wholesale[pieces] = unit_price

    def get_wholesale_prices(self) -> dict:
        return self.wholesale

    def get_retail_price(self) -> float:
        return self.wholesale[1]

    def get_name(self) -> str:
        return self.name

    def __str__(self):
        return "{}{}{}".format(self.name, os.linesep, str(self.wholesale))