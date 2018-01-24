#-*- coding:utf-8 -*-
__author__ = "Heather"
import sys
def fibonacci(n):
    a,b,count = 0,1,0
    while True:
        if count > n:
            return
        yield a
        a,b=b,a+b
        count = count + 1

if __name__ == '__main__':
    f = fibonacci(10)
    while True:
        try:
            print(next(f),end=' ')
        except StopAsyncIteration:
            sys.exit(0)
    