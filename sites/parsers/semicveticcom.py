from sites import SitesFactory


class Semicveticcom(SitesFactory):
    URL = "https://semicvetic.com/"

    @classmethod
    def get_raw_data(cls):
        return None
