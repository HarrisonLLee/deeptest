# -*- coding:utf-8 -*-

__author__ = "林倩亮"
import random

class MySort():
	def __init__(self,start,end,count):
		""" 生成随机数,返回排序后的结果
		 start, end为限制随机数生成的范围
		 count为生成的随机数个数"""
		
		self.start = start
		self.end = end
		self.count = count
		self.mylist = []
		for i in range(0,self.count): 
			values = random.randint(self.start,self.end)
			self.mylist.append(values)
	def mysort(self):
		n = len(self.mylist)
		for i in range(0,n):
			for j in range(1,n-i):
				if self.mylist[j-1] > self.mylist[j]:
					self.mylist[j-1],self.mylist[j] = self.mylist[j],self.mylist[j-1]
		return self.mylist
if __name__ == "__main__":
	so = MySort(10,1000,100)
	print(so.mysort())	