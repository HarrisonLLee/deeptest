# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Description :
   Author :       Young
   Change Activity: 2018/1/16:
-------------------------------------------------
"""
__author__ = 'Young'

#元组，使用小括号()来标识，其特点是：元组中的元素不可修改


if __name__ == "__main__":

    """
    

    Python中常用的内置函数有：
    
    len
    用于计算元组元素的个数
    
    max
    返回元组中元素最大值
    
    min
    返回元组中元素最小值
    
    tuple
    将列表转换成元组


    """
    tuple_demo = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

    # 计算tuple_demo中元素个数
    print(len(tuple_demo))
    print(tuple_demo.__len__())

    # 返回tuple_demo中最大值的元素
    print(max(tuple_demo))
    # print(tuple_demo.__gt__())

    # 返回tuple_demo中最小值的元素
    print(min(tuple_demo))

    # 将list转换成元组
    list_demo = [1, 2, 3, 4, 5, 6]
    tuple1 = tuple(list_demo)

    # 打印转换后的元组
    print(tuple1)

    print("--------------切片------------------")
    print(u"元组切片操作示例!")

    data_demo = (u"DeepTest", u"appium", u"testingunion.com", u"hello", u"python3")

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

    #元组可以通过下标索引的方式来读取元素
    #元组可以通过负数下标索引的方式反向读取元素
    #元组可以通过 起始:终止 方式截取一段元素

    '''
    元组的元素的特性：不可修改。但我们可以对元组进行合并或是连接生成新的元组，：
    '''
    print(u"-----------元组合并或连接操作示例!-----------")
    tup1 = (u"DeepTest", u"appium")
    tup2 = (u"testingunion.com", u"hello", u"python3")

    # 合并成新的元组
    tup3 = tup1 + tup2

    # 打印看看效果
    print(tup1)
    print(tup2)
    print(tup3)
    '''
    元组的元素的特性：不可修改。意味着我们不可以删除单个元素，但可以把元组给删除，示例如下：
    '''
    print(u"----------元组合并或连接操作示例!----------")
    tup1 = (u"DeepTest", u"appium")
    print(tup1)

    # 删除元组
    del tup1
    #print(tup1)

    '''
    元组和字符串一样可以使用+或*进行运算，经过运算后可以生成一个新的元组。
    '''
    print(u"------------元组运算示例------------")
    tup1 = (u"DeepTest", u"开源优测")
    tup2 = (1, 2, 3, 4)

    # 计算元组长度
    print(len(tup1))

    #  元组连接
    tup3 = tup1 + tup2
    print(tup3)

    # 元组复制
    tup4 = tup1 * 2
    print(tup4)

    # 判断元素是否在元组中, 是则返回True, 否则返回
    result = 5 in tup2
    print(result)

    # 遍历元组
    for t in tup2:
        print(t)

    print("使用内置函数tuple将list转换成元组，代码示例如下：")
    list_demo = [1, 2, 3, 4, 5, 6]
    tuple1 = tuple(list_demo)

    # 打印转换后的元组
    print(tuple1)
    print("使用内置函数list将tuple转换成元组，代码示例如下：")
    #元组转换为列表
    tuple_demo = (1, 2, 3, 4, 5, 6)
    print(list(tuple_demo))