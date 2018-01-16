#!/usr/bin/env python
# encoding: utf-8
def sum(a,b):
	c = a + b
	return c

print (u'函数定义，计算和')
#调用函数
c = sum(1,2)
print c


#使用函数封装实现九九乘法表：
def muti():
	data = []
	for i in range(1,10):
		line = []
		for j in range(i,10):
			line.append('%d * %d = %2d'%(i,j,i*j))
		data.append(line)
	return data

print ('九九乘法表：')
data = muti()
for d in data:
	print d


#元祖作为参数传递，例如有一个元祖，将其传递给一个函数进行求和计算：
def sum_tumple(seq):
	sum = 0
	for s in seq:
		sum = sum + s
	return sum

print (u'元祖参数，求和实例：')
tuple = (1,2,3,4,5,6,7,8,9)
print tuple

sum = sum_tumple(tuple)
print ('和为:%d'%sum)


#将多个字符串传递给函数进行字符串连接操作：
def str_join(str1,str2,str3):
	return str1 + str2 + str3

print (u'字符串连接实例：')
str1 = u'大家好,'
str2 = u'我的公众号是：'
str3 = u'开源优测'

str_j = str_join(str1,str2,str3)
print str_j
