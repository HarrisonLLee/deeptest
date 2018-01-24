# _*_ coding : utf-8 _*_
__author__ = "Jason"
'''
语法
Python 定义函数使用 def 关键字，一般格式如下：
def 函数名（参数列表）:
    函数体
默认情况下，参数值和参数名称是按函数声明中定义的的顺序匹配起来的。
'''
#自定义最简单的加法函数，并调用
def add_test(a,b):
    return a+b
print(add_test(3,4))#结果为7
