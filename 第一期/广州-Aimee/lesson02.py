#coding = utf-8


__author__ = 'Aimee'

# if __name__ == "__main__":
#     x = 1.68
#     y = 10
#     #转换参数类型
#     print(int(x))
#     print(float(y))
#     print(complex(x))
#     print(complex(x,y))


    #常用函数，数学函数math，随机函数random，三角函数cmath，数学常量pi

import math
import random
import  cmath


# x = -100
# y = 1.9
# print("常用数学函数")
# print(abs(x))   #取绝对值
#
# #取最大值
# print(max(x,y))
#
# #取最小值
# print(min(x,y))
#
# #计算平方
# print(pow(3,5))

#返回平方根
# print(math.sqrt(9))

# from math import  sqrt   #导入具体的函数就直接引用 如果没有就带上模块函数
# print(sqrt(9))

a = [1,2,4,3,5,6,7,8,9,0]

print(random.choice(a))  #随机选择一个

print(random.randrange(2,100,5))  #2到100直接 按照5递增 的数集随便选择一个

print(random.random())    #0-1直接随机生成一个数

print(cmath.e)
print(cmath.pi)








