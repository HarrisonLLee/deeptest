#!/usr/bin/env  python
# -*- coding: UTF-8 -*-


import math


class Prime:
    '''将一个正整数分解质因数，并将其质因数输出'''
    def __init__(self, x):
        self.x = x

    def prime(self):

        if not isinstance(self.x, int) or self.x <= 0:
            print("请输入一个正整数！")
        else:
            print("%d = " % self.x, end=' ')
            while self.x not in [1]:
                for i in range(2, self.x+1):
                        if self.x % i == 0:
                            self.x = int(self.x / i)
                            if self.x == 1:
                                print("%d " % i, end=' ')
                            else:
                                print("%d *" % i, end=' ')
                            break


if __name__ == '__main__':
    x = Prime(int(input("请输入一个正整数：")))
    x.prime()

