# -*- coding:utf-8 -*-

__author__ = "Lakisha"

import random

'''
公众号：开源优测
'''


# 随机生成1-1000之间无需序列整数数据
def generator():
    random_data = []
    for i in range(1, 10):
        random_data.append(random.randint(1, 1000))
    return random_data


# 快速排序
def quick_sort(data_list, start, end):
    # 判断是否需要进行排序
    if start >= end:
        return data_list
        # 设置排序基准值，这里我们设置为第一个元素值
    while start < end:
        base = data_list[start]
        left = start
        right = end
        while left < right:
            # 对data_list从右往左找第一个比base小的数的索引位置
            while data_list[right] >= base:
                right = right - 1

            # 对data_list从左往右找第一个比base大的数的索引位置
            while data_list[left] <= base:
                left = left + 1

            # 交换数据初步排序
            data_list[left], data_list[right] = data_list[right], data_list[left]

    # 把找到比base小的数据与base交换位置
    data_list[start], data_list[left] = data_list[left], data_list[start]

    # 进入下一轮排序
    quick_sort(data_list, start, left - 1)
    quick_sort(data_list, right + 1, end)
    return data_list


if __name__ == "__main__":
    print("开源优测-积微速成计划基本功")

    # 生成随机无需数据
    random_data = generator()

    # 打印无序数据
    print(random_data)

    # 插入排序
    lenth = len(random_data)
    sorted_data = quick_sort(random_data, 0, lenth - 1)

    # 打印排序结果
    print(sorted_data)
