# -*- coding:utf-8 -*-
__author__ = u'Heatherwyz'

if __name__ == "__main__":
    print(u"列表切片操作示例!")

    data_demo = [u"DeepTest", u"appium", u"testingunion.com", u"hello", u"python3"]

    #读取第二个元素
    e = data_demo[1]
    print(e)

    #读取倒数第二个元素
    e = data_demo[-2]
    print(e)

    #切片，截取第2个以后的所有元素
    e = data_demo[1:]
    print(e)

    #切片，截取第2-4个元素
    e = data_demo[1:4]
    print(e)