# _*_ coding : utf-8 _*_
__author__ = "Jason"
import math
import cmath
import random

if __name__ == "__main__":
    x = -100
    y = 1.5

    #数学函数
    print("常用数学函数：")
    #绝对值
    print(abs(x))
    #取最大值
    print(max(x,y))
    #取最小值
    print(min(x,y))
    #幂运算
    print(pow(x,2))
    #幂运算后再取余数
    print(pow(x,2,3))
    #平方根
    print(math.sqrt(y))
    print(cmath.sqrt(x))#结果为10j。
    print(cmath.sqrt(y))#返回的是一个复数。

    #随机数函数
    print("随机数函数：")
    a = [0,9,8,7,6,5,4,3,2,1]
    #从列表a中随机选择一个
    print(random.choice(a))
    #从指定范围内随机选择一个
    print(random.randrange(1,100))
    #指定递增范围内抽选一个
    print(random.randrange(0,100,3))#范围是1-100，按3递增。
    #随机生成一个随机数，值的范围是[0,1)
    print(random.random())
    #指定范围内随机选择一个整数，范围是[1,100]
    print(random.randint(1,100))
    #randrange和random的范围都是[min,max)左闭右开，randint是[min,max]，全闭。

    #三角函数
    #去正弦值
    print(cmath.sin(cmath.pi/2))#结果为1+0j
    print(math.sin(math.pi/2))#结果为1.0

    #常量
    print(math.pi)#返回π值，结果为3.141592653589793
    print(cmath.pi)#返回π值，结果为3.141592653589793

    #小小测试一下：
    if math.pi == cmath.pi:
        print(True)
    else:
        print(False)
    if type(math.pi) == type(cmath.pi):
        print(True)
    else:
        print(False)
    #以上2个if均返回TRUE，说明math和cmath中的π是一样的，不论是值还是类型。
