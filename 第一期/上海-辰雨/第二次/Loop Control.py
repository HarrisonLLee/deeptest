#!/usr/bin/env python
# encoding: utf-8
'''在python中for循环可以遍历任何序列，例如元祖，列表，字符串，字典，集合等等'''

#for 循环对元祖进行遍历：
tuple = (1,2,3,4,5,6,7,8,9,0)
print ('遍历元祖,并打印出来：')
for t in tuple:
	print t

#for循环遍历列表：
list = ['DeepTest','开源优测','快学Python3']
print ('遍历列表,并打印出来:')
for l in list:
	print l

#for循环对字典的遍历：
dict = {u'开源优测':u'DeepTest',u'python':u'快学Python3'}
print (u'遍历字典方式一，并打印出来：')
for (key,value) in dict.items():
	print ('%s:%s'%(key,value))

print (u'遍历字典方式二，并打印出来')
for key in dict.keys():
	print ('%s:%s'%(key,dict[key]))


#range 函数的用法：
#使用默认参数生成序列进行遍历：
for i in range(5):
	print i

#换行：
print('')

#指定范围生成序列进行遍历：
for i in range(0,10):
	print i

#带步长方式生成的序列进行遍历：
for i in range(0,10,2):
	print i


#for 循环实现九九乘法表：
print (u'九九乘法表：')
line = ''
for i in range(1,10):
	for j in range(i,10):
		line = line + '%d * %d = %2d\t'%(i,j,i*j)
	print line
	line = ''


#while 循环：
print (u'计算0-100间所有偶数和')
n = 100
index = 0
sum = 0
while index <= n:
	sum = sum + index
	index = index + 2

else:
	print ('0-100间偶数的和= %d'%sum)


#while 和 for 结合实现九九乘法表：
print ('九九乘法表实例：')
n = 1
line = ''
while n <= 9:
	for m in range(n,10):
		line = line +  '%d * %d = %2d\t'%(n,m,n*m)
	print line
	line = ''
	n = n + 1
