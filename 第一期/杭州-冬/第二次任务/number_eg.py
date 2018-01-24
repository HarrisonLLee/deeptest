#coding:--utf-8--
#各种数学函数定义在math中
#随机数定义在random中
#三角函数定义在cmath中
#py内置定义了一些数学常量
import random
import math
 
if __name__=="__main__":
    # int在计算机存储是精确的 float不是
    x=1.68
    y=10

    print(float(y))
    print(int(x))
    """
    #return 一个指定范围的数据
    r1=random.randrange(2,10,2) 
    #相当于random.chioce(range(2,10,2)),但是不生成一个range对象--序列
    print(r1)
    #从一个非空序列中选取一个数
    r2=random.choice(range(2,10,2))
    print(r2)

    #生成一个指定长度和范围的随机数列表
    r3=random.sample(range(2,10),3)
    print(r3)

    #生成一个0-1的随机浮点数
    r4=random.random()
    print(r4)

    #生成一个指定范围的随机浮点数,是否含边界？
    r5=random.uniform(2,5.7)
    print(r5)
    """
    #关于除法
    ##  /即是真除法 结果总是float
    c1=3
    c2=1
    c3=1.2

    s1=c1/c2
    print(s1)
    ## //有float则返回float,去除小数部分 得到比不大于真正商的整数部分
    ##等同math.floor()
    s2=c1//c3
    print(s2)

    c4,c5=8,-3
    s3=c4//c5
    print(s3)

    #关于取整
    ##int（）直接去除小数部分
    ##math.floor() 得到一个最接近原数同时小于原数的整数
    ##round()得到最接近原数的整数

    ##向上取整：向正无穷方向 取最接近原数的整数.向下取整反之
    print('int(2.1): %s' %int(2.1))
    print('int(-2.9): %s' %int(-2.9))

    print('math.floor(2.1): %s ' %math.floor(2.1))
    print('math.floor(2.9): %s ' %math.floor(2.9))
    print('math.floor(-2.1): %s ' %math.floor(-2.1))
    
    print('round(2.9): %s ' %round(2.9))
    print('round(2.1): %s ' %round(2.1))
    print('round(-2.1): %s ' %round(-2.1))