# -*- coding:utf-8 -*-
__author__ = "huohuo"

# 二分法查找last优先
def last_binary_search(seq, query):
    start, end = 0, len(seq) -1

    while start <= end:
        mid = start + (end - start) // 2
        if (seq[mid] == query and mid == len(seq) - 1) or (seq[mid] == query and seq[mid + 1] > query):
            # 在seq中找到目标最后一次出现的位置
            return mid
        elif seq[mid] < query:
            start = mid + 1
        else:
            end = mid -1
            
    return None

if __name__ == "__main__":
    print("二分查找last优先")

    seq = [1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9, 10, 13]

    print("5最后一次出现的索引位置是：", last_binary_search(seq, 5))

    print("8最后一次出现的索引位置是：", last_binary_search(seq, 8))

    print("4最后一次出现的索引位置是：", last_binary_search(seq, 4))

