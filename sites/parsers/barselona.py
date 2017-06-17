from sites import SitesFactory


class Barselona(SitesFactory):
    URL = "http://9046065.ru/"

    @classmethod
    def get_raw_data(cls):
        return None
