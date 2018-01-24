# -*-coding:utf-8 -*-
__author__ = "huohuo"

# 二分法查找
# seq待查序列
# query要查目标
def binary_search(seq, query):
    # start为起始索引，end为结束索引
    start, end = 0, len(seq) -1

    while start <= end:
        mid = start + (end - start) // 2
        val = seq[mid]
        if val == query:
            return mid
        elif val < query:
            start = mid + 1
        else:
            end = mid - 1

    return None

if __name__ == "__main__":
    print("二分法查找示例")
    print("二分法只适合查有序序列")

    seq = [1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]
    print(seq)

    print("找到：", 5, "索引是：", binary_search(seq, 5))

    print("找到：", 4, "索引是：", binary_search(seq, 4))

    print("找到：", 25, "索引是：", binary_search(seq, 25))