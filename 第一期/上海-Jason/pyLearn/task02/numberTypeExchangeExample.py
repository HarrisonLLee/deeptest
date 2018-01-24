# _*_ coding : utf-8 _*_
__author__ = "Jason_copy"
'''
类型转换：
'''
import math
if __name__ == "__main__":
    x = 1.68
    y = 10

    #将x转换成整数
    print(int(x))#结果为1，取整
    print(math.floor(x))#结果为1，取小于等于x的最大整数
    print(math.ceil(x))#结果为2，大于等于x的最小整数

    #将y转换成浮点型
    print(float(y))#结果为10.0

    #将x转换成复数型
    print(complex(x))#结果为1.68+0j

    #将x、y转换成复数，x为实数部分，y为虚数部分
    print(complex(x,y))#结果为1.68+10j