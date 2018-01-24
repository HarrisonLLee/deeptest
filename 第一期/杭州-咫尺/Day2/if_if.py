# -*- coding:utf-8 -*-
__author__ = "Heather"
if __name__ == '__main__':
    print (u"乘法表")
    for i in range (0, 10):
        for j in range (i, 10):
            print (u"%d*%d=%d" % (i, j, i * j), end=" ")
        print ("")

    n = 100
    index = 0
    sum = 0
    while index <= n:
        sum = sum + index
        index = index + 2
    print (u"偶数和=%d" % (sum))

    x = 1
    while x <= 9:
        for y in range (x, 10):
            print (u"%d * %d = %2d" % (x, y, x * y),end="  ")
        print("")
        x = x + 1
