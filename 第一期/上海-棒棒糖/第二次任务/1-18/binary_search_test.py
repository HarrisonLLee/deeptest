__author__='棒棒糖'
# seq   待查序列  query 要查找的目标
def binary_search(seq,query):
    # start 为起始索引
    # end  为结束索引
    start,end=0,len(seq)-1
    while  start<=end:
        mid=start+(end-start)//2  #//整除
        val=seq[mid]
        if val==query:
        # 在seq中找到目标query返回对应的索引值
            return mid
        elif val<query:
        # 目标值大于中间值 说明目标值在mid - end之间
            start=mid+1
        else:
         # 目标值小于中间值 说明目标值在start - mid之间
            end=mid-1
    #目标值不存在于seq中，返回None
    return None

if __name__=='__main__':
    print('二分查找')
    print("二分查找只适合有序的序列")
    seq=[1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]
    print(seq)
    print('---------二分查找--------')
    print('找到：',5,'索引是',binary_search(seq,5))
    print('---------二分查找--------')
    print('找到：',1,'索引是',binary_search(seq,1))
    print('---------二分查找--------')
    print('找到：',15,'索引是',binary_search(seq,15))
    print('---------二分查找--------')
    print('找到：',25,'索引是',binary_search(seq,25))