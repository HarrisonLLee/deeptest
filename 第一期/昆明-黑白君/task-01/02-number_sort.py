#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: denggl
import random


class MySort:
    # 生成随机数,返回排序后的结果
    # start, end为限制随机数生成的范围
    # count为生成的随机数个数
    def __init__(self, start, end, count):
        self.start = int(start)
        self.end = int(end)
        self.count = int(count)
        self.__mysort__()

    # 实现排序，内部函数
    def __mysort__(self):
        # step1: 获取指定区间的100个随机数
        list = []
        count = self.count
        while count > 0:
            random_number = random.randint(self.start, self.end)
            if random_number not in list:
                list.append(random_number) #获取指定区间中的一个随机数
                count = count - 1
            else:  #去掉重复的随机数
                continue
        # step2: 对list进行排序,一次选出一个最小的值，冒泡法
        for i in range(len(list)):
            for j in range(i+1, len(list)):
                if list[i] > list[j]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
        # 结果输出显示：
        k = 1
        print("当前参与排序的数字共有：%s 个，结果如下：" % self.count)
        for item in list:
            print('第 %s 个数是： %s' % (k, item))
            k = k + 1


# 使用示例
if __name__ == "__main__":
    # 获取区间范围，随机数个数
    print("请输入区间范围，请使用如“10-100”的格式：")
    start, end = input().strip().split('-')
    print("请输入随机获取的数字个数：")
    count = input()
    # 进行排序
    sorted_data = MySort(start, end, count)
    # 打印排序后的结果
    print(sorted_data)
