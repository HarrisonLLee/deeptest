
```
# __author__ ='wuwa'
# -*- coding: utf-8 -*-

'''
将X的数值转换为其他数据类型
对数学函数、随机数函数、三角函数、数学常量的练习
'''
import cmath
import math
import random

if __name__ == "__main__":
    x = 2.33
    y = 110
    m = 100
    n = -119

    # 将x转换为整型
    print(int(x))
    # 将y转换为浮点型
    print(float(y))
    # 将x转换为复数
    print(complex(x))
    # 将 x，y 转换为复数
    print(complex(x, y))

    print(u'数学函数')
    print(abs(n))

    # 返回最大值
    print(max(m, n))
    # 返回最小值
    print(min(m, n))
    # 计算n^2
    print(pow(n, 2))
    # 返回平方根
    print(math.sqrt(m))

    print(u'常用随机函数')
    a = []
    for i in range(6):
        a.append(i)

    # 从列表中随机选择一个数
    print(random.choice(a))


    print(u'常用三角函数')
    # 返回m的余弦弧度值
    print(cmath.cos(m))

    # 返回m的正弦弧度值
    print(cmath.sin(m))

    # 返回m的反余弦弧度值
    print(cmath.acos(m))

    print(u'数字常量')
    print(cmath.pi)

```
