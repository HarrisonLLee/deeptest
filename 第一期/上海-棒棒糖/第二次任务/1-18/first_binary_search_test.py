__author__='棒棒糖'

# first二分查找算法
# seq   待查序列
# query 要查找的目标
def first_binary_search(seq,query):
    start,end=0,len(seq)-1
    while start<=end:
        mid=start+(end-start)//2
        if (mid==0 and seq[mid]==query) or (seq[mid]==query and seq[mid-1]<query):
    # 在seq中找到目标query第一次出现的位置
    # 返回对应的索引值
            return mid
        elif seq[mid]<query:
            start=mid+1
        else:
            end=mid-1
    return None
if __name__=='__main__':
    print("二分查找first示例")
    print("二分查找只适合有序的序列")

    seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]

    # 返回7
    print("5第一次出现的索引位置为： ", first_binary_search(seq, 5))

    # 返回13
    print("7第一次出现的索引位置为： ", first_binary_search(seq, 7))

    # 返回15
    print("8第一次出现的索引位置为： ", first_binary_search(seq, 8))
