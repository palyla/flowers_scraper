import re
import xlsxwriter


class ExcelViewer:
    def __init__(self, path):
        self.document = xlsxwriter.Workbook(path)
        self.sheets_row = {}
        self.sheets = {}

    def view_one(self, flower):
        goods_source = re.sub(r"htt[a-z]+://", "", flower.get_source())
        if goods_source not in self.sheets.keys():
            self.sheets[goods_source] = self.document.add_worksheet(name=goods_source)
            self.sheets_row[goods_source] = 0

        sheet = self.sheets[goods_source]
        row = self.sheets_row[goods_source] + 1
        sheet.write(row, 0, flower.get_name())
        prices = flower.get_wholesale_prices()
        for pieces, price in prices.items():
            row += 1
            sheet.write(row, 0, "от {} шт".format(pieces))
            sheet.write(row, 1, price)

        self.sheets_row[goods_source] = row
