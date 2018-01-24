# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Description :
   Author :       Young
   Change Activity: 2018/1/17:
-------------------------------------------------
"""
__author__ = 'Young'

'''
迭代是Python最强大的功能特色，是遍历访问序列元素的一种方式。

迭代器的特性是：

可以记住当前遍历位置
只能往前遍历，不能后退
从序列的第一个元素开始访问，直至所有元素被访问完
有两个基本方法: iter() 和 next()
字符串、列表或元组对象可以用于创建迭代器

'''
import sys

# 生成器函数
# 实现斐波那契数列
def fibonacci(n):
    # 初始化变量
    a, b, count = 0, 1, 0

    while True:
        if count > n:
            return

        yield a

        a, b = b, a + b
        count = count + 1



if __name__ == "__main__":
    # 初始化生成器函数,产生一个生成器函数
    f = fibonacci(10)

    while True:
        try:
            print(next(f), end=' ')
        except StopAsyncIteration:
            sys.exit(0)



    seq_tuple = (1, 2, 3, 4, 5)

    # 创建迭代器
    seq_it = iter(seq_tuple)

    # 访问打印第一个元素
    print("第一个元素：%s" % next(seq_it))

    # 访问打印第二个元素
    print("第二个元素：%s" % next(seq_it))

    # 访问打印第三个元素
    print("第三个元素：%s" % next(seq_it))

    # 使用for循环来遍历迭代器对象
    print("\nfor循环遍历迭代器对象： ")
    for_it = iter(seq_tuple)
    for x in for_it:
        print(x, end=' ')


        # 使用while结合next遍历迭代器对象
    print("\n\nwhile & next遍历迭代器对象： ")
    while_it = iter(seq_tuple)
    while True:
        try:
            print(next(while_it))
        except StopAsyncIteration:
            sys.exit()
            pass