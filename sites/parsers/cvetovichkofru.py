from sites import SitesFactory


class Cvetovichkofru(SitesFactory):
    URL = "https://cvetovichkof.ru/"

    @classmethod
    def get_raw_data(cls):
        return None
