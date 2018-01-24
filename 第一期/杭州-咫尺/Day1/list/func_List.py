#-*- coding:utf-8 -*-
__author__ = u'Heather'
if __name__ == '__main__':
    list_demo = [1,2,3,4,5,6,7,8,9,0]
    print(u"内置函数处理list")

    #计算个数
    print(len(list_demo))
    #找最大值
    print(max(list_demo))
    #最小值
    print(min(list_demo))
    #把tuple换成list
    tuple_demo = (1,2,3,4,5,6)
    list1 = list(tuple_demo)
    print(list1)