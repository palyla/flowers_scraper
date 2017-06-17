from sites import SitesFactory

class Model:
    def __init__(self):
        for site in SitesFactory.__subclasses__():
            print(site.URL)

    def get_goods(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration
