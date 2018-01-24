# -*- coding:utf-8 -*-
__author__ = u"Heather"

if __name__ == "__main__":
    var1 = int(input(u"请输入一个整数："))

    if var1 >0 and var1 <10:
        print(u"你输入的数小于10大于0")

    elif var1 >=10:
        print(u"你输入的数大于等于10")
    else:
        print(u"你输入了一个负数")
