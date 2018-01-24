#!/usr/bin/env  python
# -*- coding: UTF-8 -*-

from functools import reduce


class SumList:
    '''对一个列表的所有数据进行求和，s=2+22+222+2222，求s的值'''
    def __init__(self, a, n):
        self.a = a
        self.n = n

    def __add__(self):
        Sn = []
        Tn = 0
        for i in range(self.n):
            Tn = Tn + self.a
            self.a = self.a * 10
            Sn.append(Tn)
            print(Tn)
        Sn = reduce(lambda x, y: x + y, Sn)
        return Sn


if __name__ == '__main__':
    S = SumList(int(input("请输入要累加的次数：")), int(input("请输入累加项：")))
    Sn = S.__add__()
    print(Sn)