# -*_ coding:utf-8 -*-
__author__ = "Lakisha"

import urllib.request

from openpyxl import Workbook

if __name__ == "__main__":
    print("爬取豆瓣网书记数据写入Excel")

    #通过豆瓣搜索API，搜索Python关键字，采集书籍数据
    # 本示例只采集第一页的数据
    url = "https://api.douban.com/v2/book/search?q=python"
    response = urllib.request.urlopen(url)

    #将bytes数据流解码城string
    ebook_str = response.read().decode()

    #将string转换成dict
    ebook_dict = eval(ebook_str)

    #构建一个wookbook对象
    wb = Workbook()
    ws = wb.active
    ws.append(["书名", "作者", "描述", "出版社", "价格"])

    #写入书信息
    for book in ebook_dict["books"]:
        ws.append([book["title"],
                   ",".join(book["author"]),
                   book["summary"],
                   book["publisher"],
                   book["price"]
                   ])
    wb.save("ebook.xlsx")