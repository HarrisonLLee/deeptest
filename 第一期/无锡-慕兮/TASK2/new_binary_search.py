
# -*- coding:utf-8 -*-

__author__ = 'Lakisha'

def first_binary_search(seq, query):
    # 
    # :param seq: 待查序列 
    # :param query: 要查找的目标
    # :return: 
    # 
    start, end = 0, len(seq) - 1

    while start <= end:
        mid = start +(end - start)//2
        if seq[mid] == query:
            if mid == 0:
                return mid
            elif seq[mid -1] < query:
                return mid
            else:
                end = end -2
            # 这是实现first的最关键判断
            # 在seq中找到目标query第一次出现的位置
            # 返回对应的索引值
            return mid
        elif seq[mid] < query:
            # 目标值大于中间值
            # 说明目标值在mid - end之间
            start = mid + 1
        else:
            end = mid - 1
    #目标值不存在于seq中，返回None
    return None

if __name__ == "__main__":
    print("二分查找first示例")
    print("二分查找只适合有序的序列")

    seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15, 15, 15]

    #返回5
    print("5 第一次出现的索引位置为：", first_binary_search(seq, 5))

    #返回7
    print("7 第一次出现的索引位置为：", first_binary_search(seq, 7))

    #返回13
    print("8 第一次出现的索引位置为：", first_binary_search(seq, 13))
'''


# -*- coding:utf-8 -*-

__author__ = 'Lakisha'

def last_binary_search(seq, query):

# :param
# seq: 待查序列
# :param
# query: 要查找的目标
# :return
    start, end = 0, len(seq) - 1

    while start <= end:
        mid = start +(end - start)//2
        if seq[mid] == query:
            # (seq[mid] == query and ):
            if mid == len(seq) - 1:
                return mid
            elif seq[mid + 1] > query:
                return mid
            else:
                end = end + 2
            # 这是实现first的最关键判断
            # 在seq中找到目标query第一次出现的位置
            # 返回对应的索引值
        elif seq[mid] < query:
            # 目标值大于中间值
            # 说明目标值在mid - end之间
            start = mid + 1
        elif seq[mid] > query:
            end = mid -1

        # else:
            # mid = mid -1
    #目标值不存在于seq中，返回None
    return None

if __name__ == "__main__":
    print("二分查找first示例")
    print("二分查找只适合有序的序列")

    seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]

    #返回5
    print("4 最后一次出现的索引位置为：", last_binary_search(seq, 4))

    #返回7
    print("6 最后一次出现的索引位置为：", last_binary_search(seq, 6))

    #返回13
    print("1 最后一次出现的索引位置为：", last_binary_search(seq, 1))
'''

