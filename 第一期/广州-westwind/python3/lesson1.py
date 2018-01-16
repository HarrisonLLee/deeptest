#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 22:08
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson1.py
# @Software: PyCharm
#计算1到99的和
def sum100():
    sum0 = 0
    for index in range(0, 100):
        sum0 = sum0 + index
    print("1-99的和为：%d" % sum0)

#输入
def input1():
    data = input("请输入字符串：")
    print("你输入了： %s" % data)

if __name__ == "__main__":
    sum100()
    input1()