#!/usr/bin/env python
# encoding: utf-8
import random
'''
插入排序：
插入排序的操作就是将一个数据插入到已经排好序的序列中，从而获得一个新的有序序列。
适合数据量相对较小的排序需求场景。其时间复杂度为：O（n^2）.
'''
'''随机生成1-10000之间无序序列整数数据'''
def generator():
	random_data = []
	for i in range(0,10):
		random_data.append(random.randint(1,1000))
	return random_data


'''插入排序'''
def insert_sort(data_list):
	'''序列长度'''
	length = len(data_list)

	for i in range(1,length):
		key = data_list[i]
		j = i -1
		while j >= 0:
			'''比较，进行插入排序'''
			if data_list[j] > key:
				data_list[j+1] = data_list[j]
				data_list[j] = key
				print data_list
			j = j -1
	return data_list

if __name__ == '__main__':
	print ('开源优测-积微速成计划基本功提升')
	'''生成随机无序数据'''
	random_data = generator()
	'''打印无序数据'''
	print random_data
	'''插入排序'''
	sort_data = insert_sort(random_data)
	'''打印排序结果'''
	print (sort_data)


