import re
from urllib import request
from bs4 import BeautifulSoup

from sites import SitesFactory

class Cvetopttorgspbru(SitesFactory):
    URL = "http://www.cvetopttorg.spb.ru"

    @classmethod
    def get_raw_data(cls) -> list:
        page = cls.get_page(cls.URL)
        goods_section = page.find("table", class_="views-view-grid cols-3")

        links = []
        for goods_link in goods_section.select("a"):
            links.append("{}{}".format(cls.URL, goods_link["href"]))
        print(links)

        raw_data = []
        for link in links:
            one_goods = cls.parse_one_goods(link)
            raw_data.append(one_goods)

        return raw_data

    @classmethod
    def parse_one_goods(cls, url):
        page = cls.get_page(url)
        goods_section = page.find("section", class_="clearfix", id="main")

        one_goods_name = None
        one_goods_wholesale = {}
        for title in goods_section.select("h1"):
            one_goods_name = title.text.strip()

        tag = page.findAll("div", {"class":"field field-name-field-optprice field-type-number-float field-label-inline clearfix"})
        match = re.search(r">([0-9]+).руб.", str(tag))
        opt_price = match.group(1)
        tag = page.findAll("div", {"class":"field field-name-field-lot field-type-number-integer field-label-inline clearfix"})
        match = re.search(r">([0-9]+)", str(tag))
        amount_per_opt = match.group(1)
        one_goods_wholesale[amount_per_opt] = opt_price

        tag = page.findAll("div", {"class": "field field-name-field-price field-type-number-float field-label-inline clearfix"})
        match = re.search(r">([0-9]+).руб.", str(tag))
        one_goods_wholesale["1"] = match.group(1)

        return {"name": one_goods_name, "prices": one_goods_wholesale}

    @classmethod
    def get_page(cls, url):
        print("GET  {}".format(url))
        page = request.urlopen(url)
        soup = BeautifulSoup(page, "html.parser")
        return soup
