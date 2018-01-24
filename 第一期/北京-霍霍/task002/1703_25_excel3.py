# -*- coding:utf-8 -*-
__author__ = "huohuo"

import urllib.request
from openpyxl import Workbook

if __name__ == "__main__":
    print("爬取豆瓣网书籍数据写入excel示例")

    # 通过豆瓣网搜索API，搜索python关键字，采集书籍数据
    # 只采集第一页数据
    url = "https://api.douban.com/v2/book/search?=python"
    response = urllib.request.urlopen(url)

    # 将byte数据流解码成string
    ebook_str = response.read().decode()

    # 将string转换成dict
    ebook_dict = eval(ebook_str)

    # 构建一个Workbook对象
    # 激活第一个sheet
    wb = Workbook()
    # 写入表头
    ws = wb.active
    ws.append("书名", "作者", "描述", "出版社", "价格")

    # 写入书信息
    for book in ebook_dict["books"]:
        ws.append([book["title"],
            ",".join(book["author"]),
            book["summary"],
            book["piblisher"],
            book["price"]])

    wb.save("ebook.xlsx")
