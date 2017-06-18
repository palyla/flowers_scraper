from pymongo import MongoClient

from flowers import Flowers
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
                print(raw)
                self.flowers.put_raw_flower(site.URL, raw)
            #print(raw)
            # TODO Append to database

    def view_data(self, viewer):
        for flower in self.flowers:
            viewer.view_one(flower)

