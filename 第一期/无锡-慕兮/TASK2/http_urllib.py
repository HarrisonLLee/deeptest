# -*- coding:utf-8 -*-
#__author__ == "Lakisha"

import urllib.request
import csv
import codecs


if __name__ == "__main__":

    print("urllib爬取豆瓣网")
    print("搜索关键字：Python")

    url = "https://api.douban.com/v2/book/search?q=Python"
    response = urllib.request.urlopen(url)

    #将bytes数据流解码成string
    ebook_str = response.read().decode()

    #将string转成dict
    ebook_dict = eval(ebook_str)

    #print(ebook_dict)
    #print(type(ebook_dict))
    count = ebook_dict["count"]
    total = ebook_dict["total"]

    with codecs.open('book.csv', 'w', 'utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["书名", "作者", "描述", "出版社", "价格"])
        #写书信息
        for book in ebook_dict["books"]:
            spamwriter.writerow([book["title"],
                                ",".join(book["author"]),
                                book["summary"],
                                book["publisher"],
                                book["price"]]
                                )
'''
        #从第二页开始，获取其他书籍信息
        for start in range(1, int(total/count)+1):
            url = "https://api.douban.com/v2/book/search?q=Python&start=%d" %start
            try:
                reponse = urllib.request.urlopen(url)
            except:
                print("别老爬别人的数据，要爬也别太快，会被封IP的")
                break

        #将bytes数据流解码成string
        ebook_str = response.read().decode()
        ebook_dict = dict(ebook_str)

        for book in ebook_dict["books"]:
            spamwriter.writenow(book["title"],
                                ",".join(book["author"]),
                                book["summary"],
                                book["publisher"],
                                book["price"]
                                )
        print("总计搜索了 %d 本书的信息"% total)
'''
'''
if __name__ == "__main__":
    print("urllib基本示例")

    url = "http://www.baidu.com"

    response = urllib.request.urlopen(url)

    print(response.status)

    print(response.reason)

    print(response.headers)

    print(response.read().decode("utf-8"))
'''