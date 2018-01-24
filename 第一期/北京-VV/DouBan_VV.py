# -*- coding:utf-8 -*-

__author__ = 'VV'

import urllib.request
from openpyxl import Workbook

if __name__ == '__main__':
    print("Get Ukulele books info from Douban")

    url = "https://api.douban.com/v2/book/search?q=ukulele"
    response = urllib.request.urlopen(url)

    # turn bytes to string
    ebook_str = response.read().decode()

    # turn string to Dict
    ebook_dict = eval(ebook_str)

    # create a Workbook object
    wb = Workbook()

    # active first sheet
    ws = wb.active

    # write table title
    ws.append(["ID", "Title", "Subtitle", "Author", "Summary", "Pubdate", "Publisher", "Price", "Binding", "Catalog"])

    # write book info
    for book in ebook_dict["books"]:
        ws.append([book["id"],
            book["title"],
            book["subtitle"],
            ",".join(book["author"]),
            book["summary"],
            book["pubdate"],
            book["publisher"],
            book["price"],
            book["binding"],
            book["catalog"]])

    # Save
    wb.save("Ubook.xlsx")