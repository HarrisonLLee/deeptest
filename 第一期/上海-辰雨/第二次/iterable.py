#!/usr/bin/env python
# encoding: utf-8
import sys
'''
迭代器的特性：
可以记住当前遍历的位置;
只能往前遍历，不能后退；
从序列的第一个元素开始访问，直至所有元素被访问完；
有两个基本的方法：iter()和next()
字符串/列表/或元组对象可以用于创建迭代器。
'''
seq_tuple = (1,2,3,4,5)

#创建迭代器：
seq_it = iter(seq_tuple)

#访问打印第一个元素：
print ('第一个元素:%s'%next(seq_it))

#访问打印第二个元素:
print ('第二个元素:%s'%next(seq_it))

#访问打印第三个元素：
print ('第三个元素:%s'%next(seq_it))


#使用for循环来遍历迭代器对象：
print ('\n for循环遍历迭代器对象：')
for_it = iter(seq_tuple)
for x in for_it:
	print x ,

#使用while结合next 遍历迭代器对象：
print ('\n\nwhile & next 遍历迭代器对象：')
while_it = iter(seq_tuple)
while True:
    try:
        print (next(while_it))
    except StopIteration:
        print sys.exit()


'''
生成器的特点：
与普通函数的不同的是：生成器返回的是一个迭代器的函数，只能用于迭代操作。
在调用生成器的过程中，每次遇到yield时,函数就会暂停并保存当前的运行状态，返回yield的值，并在下一次执行next()方法时从当前位置继续运行：
'''
# 下面通过使用生成器来实现斐波那契数列：

def fibonacci(n):
    # 初始化变量
    a, b, count = 0, 1, 0
    while True:
        if count > n:
            return
        yield a
        a,b = b,a+b
        count = count + 1


if __name__ == "__main__":
    f = fibonacci(10)
    while True:
        try:
            print (next(f)),
        except StopIteration:
            sys.exit(0)

