from sites.sites_factory import SitesFactory
from models.flower import Flower


class FlowersController:

    def __init__(self):
        pass

    def parse_all_sites(self):
        for site in SitesFactory.__subclasses__():
            print(site.get_raw_data())
            # TODO Append to database
        # TODO fill the model

    def get_goods(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration
