class Flower:
    FIELDS = ["price", "name", "wholesale"]

    def __init__(self, name, price: float):
        self.price = price
        self.name = name

        self.wholesale = {}

    def _get_raw(self):
        return {field : getattr(self, field) for field in self.FIELDS}

    def set_unit_from_pieces(self, pieces: int, unit_price: float):
        if pieces not in self.wholesale.keys():
            self.wholesale[pieces] = unit_price

    def get_wholesale_prices(self) -> dict:
        return self.wholesale

    def get_retail_price(self) -> float:
        return self.price

    def get_name(self) -> str:
        return self.name
