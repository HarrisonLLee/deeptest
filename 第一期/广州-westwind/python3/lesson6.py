#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 22:28
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson6.py
# @Software: PyCharm

def set_one():
    '''集合的元素是无序，不可重复'''
    set_a = {"a", 1, "b", "10"}
    print(set_a)

    set_b = set()
    print(set_b)

    set_source = set([1, 2, 3, 4, 5, 6, 7, 8])
    set_demo = set((1, 2, 3, 4, 5, 6, 7, 8))
    print(set_demo)
    print(set_source)

    #add
    set_demo.add(9)
    print(set_demo)

    set_demo.remove(9)
    print(set_demo)

if __name__ == "__main__":
    set_one()