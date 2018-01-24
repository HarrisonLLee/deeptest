# -*- coding:utf-8 -*-

__author__ = "huohuo"

# first优先策略二分法查找
def first_binary_search(seq, query):
    start, end = 0, len(seq) -1

    while start <= end:
        mid = start + (end - start) // 2
        if (mid == 0 and seq[mid] == query) or (seq[mid] == query and seq[mid-1] < query):
            # 在seq中找到目标query第一次出现的位置返回对应的索引
            return mid
        elif seq[mid] < query:
            start = mid + 1
        else:
            end = mid -1
    
    return None

if __name__ == "__main__":
    print("二分法查找first示例")

    seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 7, 8, 10, 13, 15]

    print("5第一次出现的位置是：", first_binary_search(seq, 5))

    print("7第一次出现的位置是：", first_binary_search(seq, 7))

    print("15第一次出现的位置是：", first_binary_search(seq, 15))
