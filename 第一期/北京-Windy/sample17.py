#!/usr/bin/env  python
# -*- coding: UTF-8 -*-


from sys import stdout
'''
猴子吃桃，第一天吃了总量的一半加1，第二天又吃了第一年剩下的一半加1，以后每天都吃了前一天剩下的一半加1，到第十天再次时发现只剩一个了，
求猴子开始摘了多少个桃子
'''

x2 = 1;
for day in range(9, 0, -1):
    x1 = (x2 + 1) * 2
    x2 = x1
print(x1)

'''
两队比赛，一队队员分别为a，b，c，另一队队员为x，y，z。
其中a不和x比，c不和x，z比。求比赛对手名单
'''

for i in range(ord('x'), ord('z')+1):
    for j in range(ord('x'), ord('z')+1):
        if i != j:
            for k in range(ord('x'), ord('z')+1):
                if(i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print("order is a VS %s\t b VS % s\t c VS %s" % (chr(i), chr(j), chr(k)))


'''打印出菱形'''

for i in range(4):
    for j in range(2 - i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print()

for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print()


'''
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''

a = 2.0
b = 1.0
s = 0
for n in range(1, 21):
    s += a / b
    t = a
    a = a + b
    b = t
print(s)

'''
求1+2！+3!+...+20!=?
'''
n = 0
s = 0
t = 1
for n in range(1, 21):
    t *= n
    s += t
print('1+2！+3!+...+20! = %d' % s)


'''
利用递归函数求5！
'''


def fact(j):
    su = 0
    if j == 0:
        su = 1
    else:
        su = j * fact(j - 1)
    return su


for i in range(6):
    print('%d! = %d' % (i, fact(i)))

'''
利用递归函数调用方式，将输入的一个字符串反向打印出来
'''


def output(s):
    if len(s) > 0:
        print(s[-1], end=' ')
        output(s[0:-1])



s = input('请输入一个字符串：')
output(s)


'''
有5个人坐在一起，问第五个人多少岁？他说比第4个人大
2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人
，又说比第2人大两岁。问第2个人，说比第一个人大两岁。
最后问第一个人，他说是10岁。请问第五个人多大？
'''


def age(n):
    if n == 1:
        c = 10
    else:
        c = age(n - 1) + 2
    return c


print('\n')
print('第五个人的年龄为：', age(5))


'''
输入一个正整数，判断它是几位数，并将各位的数字输出
'''


x = int(input('请输入一个正整数：\n'))
if not isinstance(x, int) or x <= 0:
    print("请输入一个正整数！")
a = int(x / 10000)
b = int(x % 10000 / 1000)
c = int(x % 1000 / 100)
d = int(x % 100 / 10)
e = int(x % 10)

if a != 0:
    print('这是一个五位数,各位倒序输出为：', e, d, c, b, a)
elif b != 0:
    print('这是一个四位数,各位倒序输出为：', e, d, c, b)
elif c != 0:
    print('这是一个三位数,各位倒序输出为：', e, d, c)
elif d != 0:
    print('这是一个二位数,各位倒序输出为：', e, d)
else:
    print('这是一个一位数,各位倒序输出为：', e)