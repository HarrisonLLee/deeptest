#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 13:13
# @Author  : caijiangchun
# @Site    : 
# @File    : guidebook1.py
# @Software: PyCharm
def guidebook():
    guide = 1
    if guide:
        print("Guidebook First Learn !")
    x = y = z = 0
    print(x, y , z)
    #复数的实部和虚部
    y = complex(1 ,3)
    print(y, y.real, y.imag)
    #类型间的转换
    a = 1999999900000000000000
    b = 9.9
    c = 1000
    print(int(b), float(c))
    print(type(b), type(c))
    g = 2e10
    f = 1.3e2
    print(g)
    print(f)

if __name__ == "__main__":
    guidebook()