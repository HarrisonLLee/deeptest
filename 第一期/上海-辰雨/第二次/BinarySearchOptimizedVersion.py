#!/usr/bin/env python
# encoding: utf-8
'''first优先策略算法实现'''
#first 二分法查找算法
#seq 待查序列
#query 要查找的目标

def first_binary_search(seq,query):
	#start 为起始索引
	#end 为结束索引
	start,end = 0,len(seq)-1
	while start <= end:
		mid = start + (end - start)//2 #//整除
		if (mid == 0 and seq[mid] == query) or (seq[mid] == query and seq[mid-1]< query):
			#这是实现first的最关键判断
			#在seq中找到目标query第一次出现的位置
			#返回对应的索引值
			return mid
		elif seq[mid]<query:
			#目标值大于中间值
			#说明目标值在mid-end 之间
			start = mid + 1
		else:
			#目标值小于中间值
			#说明目标值在start-mid之间
			end = mid - 1
		#目标值不存在与seq中，返回None
	return None

if __name__=='__main__':
	print ('二分查找first示例')
	print ('二分法查找只适合有序的序列')
	seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]
	#返回7
	print ('5第一次出现的索引的位置为:',first_binary_search(seq,5))
	#返回13
	print ('7第一次出现的索引位置为:',first_binary_search(seq,7))
	#返回15
	print ('8第一次出现的索引的位置为:',first_binary_search(seq,8))



#last二分查找算法
#seq 待查序列
#query 要查找的目标
def last_binary_search(seq,query):
	#start为起始索引
	#end 为结束索引
	start,end = 0,len(seq)-1

	while start <= end:
		mid = start + (end - start)//2 #整除
		if (seq[mid] == query and mid == len(seq)-1)or(seq[mid] == query and seq[mid+1]>query):
			#这是实现last的最关键判断
			#在seq中查找到目标query第一次出现的位置
			#返回对应的索引值
			return mid
		elif seq[mid] < query:
			#目标值大于中间值
			#说明目标值在mid-end之间
			start = mid + 1
		else:
			#目标值小于中间值
			#说明目标值在start- mid之间
			end = mid -1
	return None


if __name__=='__main__':
	print ('二分法查找last示例')
	print ('二分法查找只适合有序的序列')
	seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]
	#返回9
	print('5最后一次出现的索引位置为:',last_binary_search(seq,5))
	#返回14
	print ('7最后一次出现的索引位置为：',last_binary_search(seq,5))
	#返回5
	print ('8最后一次出现的索引位置为:',last_binary_search(seq,8))

