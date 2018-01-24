#!/usr/bin/env python
# encoding: utf-8
import random
'''
一趟快速排序的算法：
1.设置两个变量i,j,排序开始的时候：i=0,j=N-1
2.以第一个数组元素作为关键数据，赋值给key,即key=A[0]
3.从j开始向前搜索，即由后开始向前搜索(j--),找到第一个小于key的值A[j]，将A[j]和A[i]互换；
4.从i开始向后搜索，即由前开始向后搜索（i++），找到第一个大于key的A[i],将A[i]与A[j]
5.重复第三四步，直到i=j,(3,4步中，没有找打符合条件的值，即3中A[j]不小于key,4中A[i]不大于key
的时候改变j,i的值，使得j=j-1,i=i-1,直至找到为止，找到符合条件的值，进行交换的时候i,j 指针位置不变，
另外，i==j这一过程一定正好是i+或j-完成的时候，此时令循环结束)
'''
'''随机生成1-1000之间无序序列整数数据'''
def generator():
	random_data = []
	for i in range(0,10):
		random_data.append(random.randint(1,1000))
	return random_data

'''快速排序'''
def quick_sort(data_list,start,end):
	'''判断是否需要进行排序'''
	if start >= end:
		return data_list
	'''设置排序基准值，这里我们设置为第一个元素值'''
	base = data_list[start]
	left = start
	right = end
	while left < right:
		'''对data_list从右往左找第一个比base小的数的索引位置'''
		while left < right and data_list[right] >= base:
			right = right - 1

		'''对data_list从左往右找第一个比base大的数的索引位置'''
		while left < right and data_list[left] <= base:
			left = left + 1

		'''交换数据初步排序'''
		data_list[left],data_list[right] = data_list[right],data_list[left]
		print data_list

	'''把找打比base小的数据与base交换位置'''
	data_list[start],data_list[left] = data_list[left],data_list[start]

	'''进入下一轮排序'''
	quick_sort(data_list,start,left-1)

	quick_sort(data_list,right+1,end)

	return data_list

if __name__=='__main__':
	print ('开源优测-积微速成计划基本功')

	'''生成所以无序数据'''
	random_data = generator()

	'''打印无序数据'''
	print random_data

	'''插入排序'''
	length = len(random_data)
	sorted_data = quick_sort(random_data,0,length-1)

	'''打印排序结果'''
	print sorted_data
