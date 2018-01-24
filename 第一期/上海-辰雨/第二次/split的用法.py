#!/usr/bin/env python
# encoding: utf-8
'''
split()：拆分字符串，通过制定分隔符对字符串进行切片，并返回分割后的字符串列表
os.path.list():按照路径将文件名和路径分割
'''
print ('字符串分割')
string = 'www.gziscas.com.cn'

#1.以'.'为分隔符
print (string.split('.'))

#2.分割2次
print (string.split('.',2))

#3.分割两次，并取序列为1的项：
print (string.split('.',2)[1])

#4.分割两次，并把分割后的三个部分保存到三个文件中
u1,u2,u3 = string.split('.',2)
print (u1)
print (u2)
print (u3)


print ('分离文件名和路径：')
import os
print (os.path.split('/dodo/soft/python/test.txt'))

#实例
str="hello boy<[www.baidu.com]>byebye"
print (str.split('[')[1].split(']')[0])
