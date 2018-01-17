# -*- coding:utf-8 -*-

__author__= u"linan"

if __name__ == "__main__":

    #遍历元组
    tuple_1 = (1,2,3,4,5,6,7,8,9,0)
    
    print(u"遍历元组，并打印出来：")

    for t in tuple_1:
        print(t)
    
    #遍历列表
    list_1 = [u'DeepTest',u'开源优测',u'快学python3']

    print(u"遍历列表，并打印出来：")

    for text in list_1:
        print(text)

    #遍历字典
    dict_1 = {u'DeepTest':u'开源优测',u"python":u'快学python3'}

    print(u"遍历字典，并打印出来：")
    
    for (key,value) in dict_1.items():
        print("%s : %s" % (key,value))

    print("\n----------------------")

    #方式二
    print(u"方式二：")

    for key in dict_1:
        print("%s : %s" % (key,dict_1[key]))

#实例

if __name__ == "__main__":
    print(u"range for 循环实例")

    #使用默认参数生成序列进行遍历
    for i in range(5):
        print(i,end = ',')

    #换行
    print('\n----------------------------------------')

    #指定范围生成序列进行遍历
    for i in range(0,5):
        print(i,end = ',')

    #换行
    print('\n--------------------------------------')

    #带步长方式生成序列进行遍历
    for i in range(0,10,3):
        print(i,end = ',')

            
#for语句实现九九乘法表
print('\n-------------------------------------------')
if __name__ == "__main__":
    print(u"九九乘法表")

    for i in range(1, 10):
        for j in range(i, 10):
            print(u"%d * %d = %2d" % (i, j, i * j),end = " ")
        print("")


if __name__ == "__main__":
    print(u"计算0-100间所有偶数的和")

    n = 100
    index = 0
    sum = 0
    while index <= n:
        sum = sum + index
        index = index + 1
    print(u"0-100间所有偶数和 = %d" % sum)