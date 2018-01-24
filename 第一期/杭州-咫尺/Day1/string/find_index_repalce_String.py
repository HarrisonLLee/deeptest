# -*- coding:utf-8 -*-
__author__ = u'Heather'

if __name__ == '__main__':
    source_str = u"it's my book,please show it,wa ka ka,yo yo yo!"

    #从左往右找yo
    print(u"从左往右查找yo")
    print(source_str.find("yo"))
    print(source_str.index("yo"))

    #从右往左找yo
    print(u"从右往左查找yo")
    print(source_str.find("yo"))
    print(source_str.rindex("yo"))

    #替换所有的yo
    des_str = source_str.replace("yo","ha")
    print(des_str)

    #替换两次yo
    des_str = source_str.replace("yo","hi",2)
    print(des_str)