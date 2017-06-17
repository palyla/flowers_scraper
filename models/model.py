from sites import SitesFactory


class Model:
    def __init__(self):
        for site in SitesFactory.__subclasses__():
            if "https://cvetovik.com" in site.URL:
                print(site.get_raw_data())
                # TODO Append to database

    def get_goods(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration
