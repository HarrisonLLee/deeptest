#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 11:13
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson3.py
# @Software: PyCharm

def tuple_one():
    '''
    元组的内置函数
    '''
    a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    print(min(a))
    print(max(a))
    print(len(a))
    b = [1, 2, 3, 4, 'a']
    c = tuple(b)
    print(c)

#元组的切片
def tuple_two():
    tupletwo = (u"deeptest", u"python3", u"World", u"Hello", u"open")
    a = tupletwo[0]
    print(a)
    b = tupletwo[1:]
    print(b)
    c = tupletwo[-1]
    print(c)
    #截取第3-4个元素
    d = tupletwo[2: 4]
    print(d)

def tuple_three():
    #合并元组
    a = (1, 3, 5, '3j')
    b = ("a", "d", "cd")
    c = a + b
    print(c)

def tuple_del():
    #删除元组
    a = (12, 32, "ek")
    print(a)
    del a
    #print(a)

def tuple_opration():
    #元组运算

    operation = (1, 2, 3, 4, 5)
    tuple1 = ("a", "b", 12)
    #元组连接
    a = operation + tuple1
    print(a)
    #元组复制
    b = operation * 2
    print(b)

    #判断元组是否含有元素
    result = 5 in operation
    print(result)

    #遍历元素
    for t in operation:
        print(t)

def tuple_list():
    #列表转元组
    list1 = [1, 2, 3, "3d", "a", "1"]
    tuple1 = tuple(list1)
    print(tuple1)

if __name__ == "__main__":
    tuple_one()
    tuple_two()
    tuple_three()
    tuple_del()
    tuple_opration()
    tuple_list()