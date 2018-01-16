# -*- coding:utf-8 -*-

__author__ = "liqi"

import sys

#生成器函数
#实现斐波那契数列

def fibonacci(n):
    #初始化变量
    a, b, count = 0, 1, 0
    while True:
        if count > n:
            return
        yield a

        a, b =b, a + b
        count +=1

# 实现杨辉三角
def yanghuisj(n):
#     初始化变量
    li = [1]
    while len(li) <= n:
        yield li
        li.append(0)
        #生成列表推导式
        li = [li[i - 1] + li[i] for i in range(len(li))]


if __name__ == "__main__":
    # 初始化生成器函数，产生一个生成器函数
    # f = fibonacci(10)
    #
    # while True:
    #     try:
    #         print(next(f),end =" " )
    #     except StopAsyncIteration:
    #         sys.exit(0)

    #打印杨辉三角
    li = yanghuisj(10)
    for i in li:
        print(i)

    #关于列表推导式
    # [expression for item in iterable]

    # 创建一个整数列表
    # 等同于 number_list = list(range(1, 5))
    number_list = [number for number in range(1, 5)]
    print (number_list)

    # 创建一个整数平方列表
    number_list1 = [number * number for number in range(1, 5)]
    print(number_list1)

    # 创建一个带if 的列表推倒式
    number_list2 = [number * (number -1) for number in range(1, 10) if number % 2 ==0]
    print(number_list2)


