#coding:utf-8
import random

#随机生成1-1000之间的无序序列的整数数据
def generator():
    random_data = []
    for i in range(0,10):
        random_data.append(random.randint(1,1000))
    return random_data

#冒泡排序：
def bubble_sort(data_list):
    #序列的长度
    length = len(data_list)

    for i in range(0,length):
        for j in range(i+1,length):
            if data_list[i] > data_list[j]:
                data_list[i],data_list[j]=data_list[j],data_list[i]

    return data_list

if __name__ == "__main__":
    print ('开源优测')

    #生成随机数字
    random_data = generator()

    #打印无序序列：
    print random_data

    #冒泡排序：
    data_list = bubble_sort(random_data)

    #打印排序好的序列：
    print data_list