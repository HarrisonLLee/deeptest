#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 16:36
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson17.py
# @Software: PyCharm
import urllib.request
import csv
import codecs


def baidu_com():
    url = "https://www.baidu.com"
    response = urllib.request.urlopen(url)
    print(response.status)
    print(response.reason)
    print(response.headers)
    print("\n")
    print(response.read().decode("utf-8"))

def doubandown():
    print(u"爬取豆瓣接口数据")
    print(u"搜索关键字python")
    url = "https://api.douban.com/v2/book/search?q=python"
    respone = urllib.request.urlopen(url)

    #将数据流bytes解码成string
    ebook_string = respone.read().decode()
    #把str转换成dict
    ebook_dict = eval(ebook_string)

    count = ebook_dict["count"]
    total = ebook_dict["total"]

    print(type(ebook_dict))
    print(ebook_dict)
    with codecs.open("books.csv", "w", "utf-8") as csvfiles:
        writers = csv.writer(csvfiles, delimiter= ",", quotechar = '|',quoting = csv.QUOTE_MINIMAL)
        writers.writerow(["书名", "作者", "描述", "出版社", "价格"])
        for book in ebook_dict["books"]:
            writers.writerow([book["title"],
            ",".join(book["author"]),
            book["summary"],
            book["publisher"],
            book["price"]])

    print("总计搜索了 %d 本书的信息" % total)




if __name__ == "__main__":
    #baidu_com()
    doubandown()
