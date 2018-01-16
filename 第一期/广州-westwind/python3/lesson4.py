#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 13:07
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson4.py
# @Software: PyCharm
def list_one():
    #列表的内置函数
    list1 = [1, 2, 3, 4, 5]
    print(len(list1))
    print(max(list1))
    print(min(list1))
    tuple1 = ("2", "a", "2d")
    print(list(tuple1))
def list_two():
    #list的方法
    list_first = [1, 2, 3, 0, 2]
    list_second = ["a", "c", "d"]
    list_first.append(4)#增加一个元素
    print(list_first)
    print(list_first.count(2))#出现2的次数

    list_first.extend(list_second)#将list_second追加到list_first中
    print(list_first)

    index1 = list_first.index(2)#返回列表中第一个2的索引
    print(index1)

    list_second.insert(2, "b")#在第3的位置插入“b”
    print(list_second)

    list_first.pop()#删除最后一个元素
    print(list_first)

    list_first.reverse()#列表反向
    print(list_first)

    list_second.sort()#列表排序
    print(list_second)

    list_third = list_second.copy()#复制列表
    print(list_second)
    print(list_third)

    list_second.clear()
    print(list_second)
    print(list_third)

def list_three():
    #切片
    list1 = [u"opensouce", 12, u"python3", 0, u"test"]
    print(list1)

    print(list1[0])
    print(list1[1:3])
    print(list1[3:])
    print(list1[-2])

def list_update():
    listone = [1, 3, 2, 4, 5, 6]
    print(listone)
    listone[2] = 9
    print(listone)

if __name__ == "__main__":
    list_one()
    list_two()
    list_three()
    list_update()