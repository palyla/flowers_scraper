from pymongo import MongoClient

from models.flowers import Flowers
from sites.sites_factory import SitesFactory
from models.flower import Flower


class FlowersController:
    flowers = Flowers()

    def parse_all_sites(self):
        for site in SitesFactory.__subclasses__():
            raw_list = site.get_raw_data()
            if not raw_list:
                continue
            for raw in raw_list:
                self.flowers.put_raw_flower(site.URL, raw)
            # TODO Append to database

    def view_data(self, viewer):
        for flower_cursor in self.flowers:
            for flower in flower_cursor:
                viewer.view_one(flower)

