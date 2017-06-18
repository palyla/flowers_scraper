import re
from urllib import request
from bs4 import BeautifulSoup

from sites import SitesFactory


class Cvetovikcom(SitesFactory):
    URL = "https://cvetovik.com"

    @classmethod
    def get_raw_data(cls) -> list:
        page = cls.get_page(cls.URL + "/catalog/tsveti/")
        pages_num = str(page.find("div", class_="pages")).count("</a>")

        goods_links = []
        for page_num in range(1, pages_num + 1):
            page = cls.get_page("{}{}{}".format(cls.URL, "/catalog/tsveti/?page=", page_num))
            raw_goods = page.findAll("div", class_="catalog-good-item")
            goods_links.extend(cls.parse_goods_links(raw_goods))

        raw_data = []
        for link in goods_links:
            raw_data.append(cls.parse_one_goods(link))

        return raw_data

    @classmethod
    def parse_one_goods(cls, url):
        page = cls.get_page(url)
        one_goods = page.findAll("div", class_="col-sm-7 show-good-extra")

        one_goods_name = None
        one_goods_price = None
        one_goods_wholesale = {}
        for tag in one_goods:
            for name in tag.select("h1"):
                one_goods_name = name.text.strip()
            for price in tag.select("span.goodprice1"):
                one_goods_price = price.text.strip()
            for whole_sale in tag.select("div.well.well-sm"):
                for match in re.finditer("от.([0-9]+).шт:.<strong>([0-9]+)</strong>", str(whole_sale)):
                    # match.group(1) # amount
                    # match.group(2) # price
                    one_goods_wholesale[match.group(1).strip()] = match.group(2).strip()
        one_goods_wholesale["1"] = one_goods_price.strip()

        return {"name": one_goods_name, "prices": one_goods_wholesale}

    @classmethod
    def parse_goods_links(cls, goods_tags) -> list:
        links = []
        for tag in goods_tags:
            for link in tag.select("a"):
                links.append("{}{}".format(cls.URL, link['href']))
                break
        return links

    @classmethod
    def get_page(cls, url):
        print("GET  {}".format(url))
        page = request.urlopen(url)
        soup = BeautifulSoup(page, "html.parser")
        return soup
