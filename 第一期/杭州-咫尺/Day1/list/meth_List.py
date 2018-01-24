#-*- coding:utf-8 -*-
__author__ = u'Heather'
if __name__ == '__main__':
    print(u"list方法代码示例： ")
    list1 = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6]
    list2 = [7, 8, 9 , 0, 10 , 11] 

    #append
    list1.append(100)
    print(list1)

    #count
    count = list1.count(1)
    print(count)

    #extend,将list2追加到list1中
    list1.extend(list2)
    print(list1)

    #index,返回第一个3的索引
    index = list1.index(3)
    print(index)
    
    #pop，删除最后一个元素
    list1.pop()
    print(list1)

    #reserse,列表反向
    list1.reverse()
    print(list1)

    #sort对列表排序
    list1.sort()
    print(list1)

    #copy
    list3 = list1.copy()
    print(list1)
    print(list3)

    #clear
    list1.clear()
    print(list1)
    print(list3)