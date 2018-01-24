#-*- coding:utf-8 -*-
__author__ = u'Heather'
if __name__ == '__main__':
    print(u"元组运算")
    tup1 = (u"deep",u"test")
    tup2 = (1,2,3,4)

    #计算长度
    print(len(tup1))

    #元组连接
    tup3 = tup1 + tup2
    print(tup3)

    #copy
    tup4 = tup1*2
    print(tup4)

    #判断元素是否在列表
    result = 5 in tup2
    print(result)

    #遍历
    for t in tup2:
        print(t)