#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: denggl

class Calc:
    # 初始化
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    # 加法
    def __add__(self):
        return self.a + self.b

    # 减法
    def __sub__(self):
        return self.a - self.b

    # 乘法
    def mul(self):
        return self.a * self.b

    # 除法
    def div(self):
        if self.b == 0:
            return '除数不能为0'
        return self.a / self.b


print("请依次输入a 和 b，中间用空格分开:")
a, b = input().strip().split()
print("计算结果将默认保留两位小数：\n")
print("a - b 的结果为：%.2f" % Calc(a, b).__sub__())
print("a + b 的结果为：%.2f" % Calc(a, b).__add__())
print("a * b 的结果为：%.2f" % Calc(a, b).mul())
print("a / b 的结果为：%.2f" % Calc(a, b).div())