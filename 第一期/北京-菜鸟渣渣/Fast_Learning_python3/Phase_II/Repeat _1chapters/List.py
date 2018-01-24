# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Description :
   Author :       Young
   Change Activity: 2018/1/16:
-------------------------------------------------
"""
__author__ = 'Young'

#List（列表）是Python最常用的数据类型，它使用方括号[]来标识

'''
Python中常用的内置函数有：

len
用于计算列表元素的个数

max
返回列表中元素最大值

min
返回列表中元素最小值

list
将元组转换成列表
'''

if __name__ == "__main__":
    list_demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    print(u"内置函数处理list示例： ")

    # 计算list_demo中元素个数
    print(len(list_demo))

    # 返回list_demo中最大值的元素
    print(max(list_demo))

    # 返回list_demo中最小值的元素
    print(min(list_demo))

    # 将list转换成元组
    list_demo = (1, 2, 3, 4, 5, 6)
    list1 = list(list_demo)

    # 打印转换后的列表
    print(list1)

    '''
    在python中，有大量的方法用于list的处理,下面我们看看示例：
    
    append(obj)
    在列表末尾添加新的对象
    count(obj)
    统计列表中某个元素出现的次数
    extend(seq)
    在列表末尾追加另外一个序列（即列表扩展）
    index(obj)
    返回列表中第一个匹配到的元素的索引
    insert(index, obj)
    将在列表指定位置插入一个对象
    pop(obj=list[-1])
    移除列表中的一个元素（默认最后一个），并返回该元素
    remove(obj)
    删除列表中第一个匹配到的元素
    reverse()
    将列表中元素反向
    sort([func])
    对列表中元素进行排序
    clear()
    清空列表中元素
    copy()
    复制列表
    
    '''
    print(u"list方法代码示例： ")
    list1 = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6]
    list2 = [7, 8, 9, 0, 10, 11]

    # append，追加一个元素
    list1.append(100)
    print(list1)

    # count, 统计1出现的次数
    count = list1.count(1)
    print(count)

    # extend, 将list2追加到list1中
    list1.extend(list2)
    print(list1)

    # index, 返回第一个2的索引
    index = list1.index(2)
    print(index)

    # insert, 在列表第一个位置插入200
    list1.insert(0, 200)
    print(list1)

    # pop, 删除最后一个元素
    list1.pop()
    print(list1)

    # reverse, 把列表反向一下
    list1.reverse()
    print(list1)

    # sort,对列表进行排序
    list1.sort()
    print(list1)

    # copy，列表拷贝
    list3 = list1.copy()
    print(list1)
    print(list3)

    # clear 清空列表
    list1.clear()
    print(list1)
    print(list3)


    #列表也是一个序列，所以我们可以使用Python的切片机制来访问元组中指定位置的元素
    print(u"列表切片操作示例!")

    data_demo = [u"DeepTest", u"appium", u"testingunion.com", u"hello", u"python3"]

    # 读取第二个元素appium, 注意索引下标从0开始
    e = data_demo[1]
    print(e)

    # 读取倒数第二个hello
    e = data_demo[-2]
    print(e)

    # 切片，截取从第2个元素开始后的所有元素
    e = data_demo[1:]
    print(e)

    # 切片，截取第2-4个元素
    e = data_demo[1:4]
    print(e)

    #更新
    #列表不同于元组，列表中的元素是可以进行修改或更新的，除了前提到的append、insert方法新增外，我们还可以对列表中原来的数据进行修改。
    print(u"列表更新操作示例!")
    data_demo = [u"DeepTest", u"appium", u"testingunion.com", u"hello", u"python3"]
    print(data_demo)

    # 把hello改为hello word
    data_demo[3] = u"hello word"
    print(data_demo)
