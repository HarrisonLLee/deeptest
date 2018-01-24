'''杨辉三角定义如下：
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
把每一行看做一个list，试写一个generator，不断输出下一行的list：
# -*- coding: utf-8 -*-
def triangles():
----
pass
----
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
print(t)
n = n + 1
if n == 10:
break'''
def triangel(n):
    L=[1]        #定义一个list[1]
    while True:
        yield L     #打印出该list
        L=[L[x]+L[x+1] for x in range(len(L)-1)] #计算下一行中间的值（除去两边的1）
        L.insert(0,1)         #在开头插入1
        L.append(1)           #在结尾添加1
        if len(L)>n:          #仅输出10行
            break

   e n

#生成一个generator对象，然后通过for循环迭代输出每一行
a=triangel(4)
for i in a:
    print(i)
print('*'*50)