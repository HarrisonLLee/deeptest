#!/usr/bin/env python
# encoding: utf-8
import random
'''
选择排序的基本过程：
n 个记录的文件的直接选择排序可经过n-1趟直接选择排序得到的有序结果：
1.在未排序序列中找到最下元素，存在到排序序列的起始位置。
2.在从剩余未排序元素中继续查找最下【大】元素，然后放到已排序序列的末尾；
3.以此类推，直到所有元素均排序完成。
'''
'''随机生成1-1000之间的无序序列整数数据'''
def generator():
	random_data = []
	for i in range(0,10):
		random_data.append(random.randint(1,1000))
	return random_data

'''选择排序'''
def select_sort(data_list):
	length = len(data_list)

	for i in range(0,length):
		min = i
		'''查找最小元素'''
		for j in range(i+1,length):
			if data_list[j] < data_list[min]:
				'''找到最下元素'''
				min = j

		'''交换位置'''
		data_list[min],data_list[i] = data_list[i],data_list[min]

	return data_list

if __name__=='__main__':
	print ('开源优测')

	'''生成随机无序数据'''
	random_data = generator()

	'''打印无序数据'''
	print (random_data)

	'''插入排序'''
	length = len(random_data)
	sorted_data = select_sort(random_data)

	'''打印排序结果'''
	print (sorted_data)

