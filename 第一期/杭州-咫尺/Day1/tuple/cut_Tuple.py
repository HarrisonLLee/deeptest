# -*- coding:utf-8 -*-
__author__ =u'Heather'

if __name__ == '__main__':
    print(u"元组切片操作示例")

    data_demo = (u"Deeptest",u"appium",u"testingunion.com",u"hello",u"python3")

    #读取第二个元素
    e = data_demo[1]
    print(e)

    #读取倒数第二个元素
    e = data_demo[-2]
    print(e)

    #切片，截取从第2个蒜素开始后的所有元素
    e = data_demo[1:]
    print(e)

    #切片，截取第2-4个元素
    e = data_demo[1:4]
    print(e)