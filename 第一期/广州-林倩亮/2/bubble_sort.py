
import random

#随机生成1-1000之间无序序列整数数据
def genetator():
	random_data = []
	for i in range(0,10)
		random_data.append(random,randint(1,1000))
	return random_data
	
#冒泡排序
def bubble_sort(data_list):
	# 序列长度
	lenght = len(data_list)
	
	for i in range(0,lenght):
		for j in range(i+1,lenght):
			if data_list[i] > data_list[j]:
				data_list[i],data_list[j] = data_list[j],data_list[i]
	return data_list
	
if __name__ == "__main__":
	print("开源优测 - 积微速成计划基本功提升")
	
	#随机生成无序数据
	random_data = genetator()
	
	#打印无序数据
	print(random_data)
	
	#插入排序
	sorted_data = bubble_sort(random_data)
	
	#打印排序结果
	print(sorted_data)