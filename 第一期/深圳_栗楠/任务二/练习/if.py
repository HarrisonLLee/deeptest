# -*- coding:utf-8 -*-
__author__ = u"linan"


if __name__ == "__main__":
    var1 = int(input(u"请输入一个整数："))

    if var1 > 0 and var1 < 10:
        print(u"这个整数大于0小于10")

    elif var1 > 10:
        print(u"这个整数大于10")
    
    elif var1 == 10:
        print(u"这个整数等于10")

    else:
        print(u"这是个负数")



