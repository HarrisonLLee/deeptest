#!/usr/bin/env python
# encoding: utf-8
#list列表基本用法：
list = ['Michael','Bob','Tracy']

print ('打印出列表的值：')
print list

print ('打印出列表的长度')
print (len(list))

print ('用索引来访问list中每一个位置的元素，记得索引是0开始的')
print (list[0])
print (list[1])
print (list[2])
print (list[:-1])

print ('列表末尾追加元素：')
print (list.append('Admin'))

print ('列表指定位置插入元素:')
print (list.insert(1,'JACK'))


print ('删除list末尾的元素')
print (list.pop())

print ('删除指定位置的元素')
print (list.pop(1))

print ('修改列表中指定的元素')
list[1]='hello'
print list

print ('删除列表中指定元素')
# print list.remove('hello')

print ('列表数值进行排序')
print list.sort()
print list

#列表中的strip() 函数的用法：
#strip()用于裁剪字符串首尾的某些字符：
a = '  abc '

#strip()不带任何参数，可以删除首尾的空格
print a.strip()

#但是strip() 无法删除位于字符串中间的空格
a = ' a a a '
print a.strip()

#除了删除首尾空格，任何不显示的字符都会被删除
a = '\na a a \t'
print a.strip()

#如果我们要想删除位于首尾的其他字符，我们可以使用参数strip(strip),它将删除所有包含在string中的字符，当时只是删除位于首尾的字符
a = 'asdfasdfasdfalkkkk'
print a.strip('ak')

