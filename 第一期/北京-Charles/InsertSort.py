# -*- coding:utf-8 -*-
#适合数据量相对较小的排序需求场景。其时间复杂度为：O（n^2），是一种稳定的排序方法。


import random
# 随机生成1-1000之间无序序列整数数据
def generator():
    random_data = []
    print(random_data)
    for i in range(0,10):  #range左闭右开
        random_data.append(random.randint(1,1000))

    return random_data
#插入顺序
def insert_sort(data_list):
    # 序列长度
    length = len(data_list)
    for i in range(1,length):
        key = data_list[i]
        j = i - 1
        while j >= 0:
            # 比较，进行插入排序
            if  data_list[j] > key:

                data_list[j+1] = data_list[j]
                data_list[j] = key
                #相当与引入了data_list[j+1]这个新的变量做过渡
            else:
                break
            j = j-1
    return data_list


if __name__ == "__main__":
    random_data = generator()
    print(random_data)

    new_list = insert_sort(random_data)
    print(new_list)