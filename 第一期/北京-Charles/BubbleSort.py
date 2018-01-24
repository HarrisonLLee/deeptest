# -*- coding:utf-8 -*-
'''
冒泡排序算法的运作如下：
1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
3.针对所有的元素重复以上的步骤，除了最后一个。
4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''
# 随机生成1-1000之间无序序列整数数据
import random
def generator():
    random_data = []
    for i in range(0, 10):
        random_data.append(random.randint(1, 1000))

    return random_data
# 冒泡排序
def bubble_sort(data_list):
    # 序列长度
    length = len(data_list)
    for i in range(0,length):
        for j in range(i+1,length):
            if data_list[i]>data_list[j]:
                data_list[i],data_list[j]=data_list[j],data_list[i]
    return  data_list

if __name__ == "__main__":
    random_data = generator()
    print(random_data)

    new_list = bubble_sort(random_data)
    print(new_list)