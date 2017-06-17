from sites import SitesFactory


class Orangespbru(SitesFactory):
    URL = "http://orangespb.ru/"

    @classmethod
    def get_raw_data(cls):
        return None
