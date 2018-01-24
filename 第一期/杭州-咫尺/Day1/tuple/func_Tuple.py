# -*- coding:utf-8 -*-
__author__ = u'Heather'

if __name__ == '__main__':
    tuple_demo = (1,2,3,4,5,6,7,8,9,0)

    #计算tuple_demo中元素个数
    print(len(tuple_demo))

    #返回tuple_demo中最大值的元素
    print(max(tuple_demo))

    #返回tuple_demo中最小值的元素
    print(min(tuple_demo))

    #将list转换成元组
    list_demo = [1,2,3,4,5,6]
    tuple1 = tuple(list_demo)

    #打印转换后的元组
    print(tuple1)