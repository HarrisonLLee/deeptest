#!/usr/bin/env python
# encoding: utf-8
'''
二分法查找基本概念：
二分法称为折半查找，优点是比较次数少，查找速度快，平均性能也好；
缺点：
要求待查表为有序列表，且插入删除困难，因此，折半查找方法适用于不经常变动而查找频繁的有序列表
二分查找的基本思想为：将n个元素分成大致相等的两部分，取a[n/2]与x做比较
如果x = a[n/2]，则找打x,算法中止；
如果x<a[n/2],则只要在数组a的左半部分继续搜索x;
如果x>a[n/2]，则只要在数组a的右半部分搜索x;
时间复杂度无非就是while的循环次数；
'''
#二分查找算法：
#seq 待查序列
#query 要查找的目标

def binary_search(seq,query):
	#start 为起始索引
	# #end 为结束索引
	start,end = 0,len(seq)-1

	while start<=end:
		mid = start + (end-start)//2  #整除
		val = seq[mid]
		if val == query:
			#在seq中段找到目标query
			#返回对应的索引值
			return mid
		elif val < query:
			#目标值大于中间值
			#说明目标值在mid-end之间
			start = mid+1
		else:
			#目标值小于中间值
			#说明目标值在start-mid之间
			end = mid-1
	return None

if __name__=='__main__':
	print ('二分法查找示例')
	print ('二分法只适合有序的序列')
	seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]
	print (seq)
	print ('---------二分法查找---------')
	print (u'找到:',5,u'索引是:',binary_search(seq,5))
	print ('---------二分法查找---------')
	print (u'找到:', 4, u'索引是:', binary_search(seq, 4))
	print ('---------二分法查找---------')
	print (u'找到:', 13, u'索引是:', binary_search(seq, 13))
	print ('---------二分法查找---------')
	print (u'找到:', 1, u'索引是:', binary_search(seq, 1))
	print ('---------二分法查找---------')
	print (u'找到:', 25, u'索引是:', binary_search(seq, 25))

