from urllib import request

import io
from bs4 import BeautifulSoup
import pdfminer
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine

from sites import SitesFactory


class Cvetovichkofru(SitesFactory):
    URL = "https://cvetovichkof.ru/"

    @classmethod
    def get_raw_data(cls):
        pdf = PDFParser(cls.get_pdf())
        doc = PDFDocument()
        pdf.set_document(doc)
        doc.set_parser(pdf)
        doc.initialize('')

        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for lt_obj in layout:
                if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                    print(lt_obj.get_text())

        return None

    @classmethod
    def get_pdf(cls):
        return request.urlopen("https://cvetovichkof.ru/images/prays_opt.pdf")

    @classmethod
    def get_page(cls, url):
        print("GET  {}".format(url))
        page = request.urlopen(url)
        soup = BeautifulSoup(page, "html.parser")
        return soup
