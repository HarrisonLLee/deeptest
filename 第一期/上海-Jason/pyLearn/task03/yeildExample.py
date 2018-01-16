# _*_ coding:utf-8 _*_
__author__ = 'Jason_copy'

'''
生成器

在python中使用了yield的函数，我们称之为生成器。
与普通函数不同的是：生成器返回的是一个迭代器的函数，只能用于迭代操作，
直接理解就是：生成器 就是功能更强大的迭代器。

在调用生成器的过程中，每次遇到yield时，函数就会暂停并保存当前运行状态，返回yield的值，
并在下一次执行next()方法时从档期那位置继续运行。
'''

import sys

#生成器函数
#实现斐波那契数列
def fibonacci(n):
    #初始化变量
    a,b,count = 0,1,0
    while True:
        if count > n:
            return
        yield a
        a,b = b,a+b
        count = count+1
if __name__ == "__main__":
    #初始化生成器函数，产生一个生成器函数
    f = fibonacci(10)
    while True:
        try:
            print(next(f),'',end='')
        except StopAsyncIteration:
            sys.exit(0)