# coding = utf-8
__author__ = 'Aimee'

#迭代器是一个可以记住遍历的位置的对象。
#迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
# 迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
# 字符串，列表或元组对象都可用于创建迭代器

# import sys
#
# if __name__ == "__main__":
#
#     tuple = (1,2,3,4,5,6)
#     #创建迭代器
#     it = iter(tuple)
#     #打印第一个元素
#     print("第一个元素: %s" % next(it))
#     #打印第二个元素
#     print("第二个元素: %s" % next(it))
#
#     #使用for循环来遍历迭代器对象
#     it_for = iter(tuple)
#     print("for 循环遍历迭代器：")
#     for i in it_for:
#         print(i,end=",")
#
#     print("\n")
#
#     #while 结合next遍历迭代器
#     print("while 循环遍历迭代器：")
#     it_while = iter(tuple)
#     while True:
#         try:
#             print(next(it_while))
#         except:
#             sys.exit()
#


#s生成器返回的是一个迭代器的函数

import sys

def fibonacci(n):

    # 初始化变量
    a,b,count = 0,1,0
    while True:
        if count > n:
            return
        yield a

        a,b = b,a+b
        print("%d,%d" %(a,b))
        count = count +1


if __name__ == "__main__":
    f = fibonacci(10)  #f是一个迭代器，由生成器返回生成

    while True:
        try:
            print(next(f),end=",")

        except:
            sys.exit()













