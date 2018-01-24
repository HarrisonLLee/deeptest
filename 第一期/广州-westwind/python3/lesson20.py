#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/20 16:53
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson20.py
# @Software: PyCharm
import urllib.request
from openpyxl import Workbook


def download_data():

    #通过豆瓣的API，搜索python关键字，采集书籍的数据
    url = "https://api.douban.com/v2/book/search?q=python"
    responese = urllib.request.urlopen(url)

    #将bytes数据流解码成string
    ebook_str = responese.read().decode()

    #将string转换成dict
    ebook_dict = eval(ebook_str)

    #创建一个Workbook对象
    wb = Workbook()
    ws = wb.active
    #写入表头
    ws.append(["书名","作者","描述","出版社","价格"])

    #写入书的信息
    for book in ebook_dict['books']:
        ws.append([book["title"],
                  ",".join("author"),
                  book["summary"],
                  book["publisher"],
                  book["price"]])

    #保存
    wb.save("ebook.xlsx")

if __name__ == "__main__":

    download_data()