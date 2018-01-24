# coding=utf-8

# 在Python中for循环可以遍历任何序列，例如元组、列表、字符串、字典、集合等等。


if __name__ == "__main__":
    #  for元组遍历
    print("----------for循环如何进行元组遍历输出：-------------")
    tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

    print(u"遍历元组，并打印出来： ")
    for t in tuple_1:
        print(t)

    print("----------for循环如何进行列表遍历输出：-------------")
    list_1 = [u'DeepTest', u'开源优测', u'快学Python3']

    print(u"遍历列表，并打印出来： ")
    for text in list_1:
        print(text)

    #遍历字典的两种方式：

    print("--------for字典遍历--------------")
    dict_1 = {u"开源优测": u"DeepTest", u"python": u"快学Python3"}
    print(dict_1.items())
    print(u"遍历字典方式一，并打印出来： ")
    for (key, value) in dict_1.items():
        print("%s : %s " % (key, value))

    print("\n-----------------------------")

    print(u"遍历字典方式二，并打印出来： ")
    for key in dict_1:
        print("%s : %s " % (key, dict_1[key]))


    '''
    结合range()函数使用 本节说明下如何结合range函数来使用。
    range(start, end, step)
    功能说明：以指定步长生成一个指定范围的数值序列
    参数说明： start: 数值序列的起始数值（默认为0） end： 数值序列的终止数值 step ： 数值序列中数值的间距（默认为1）
    
    '''
    print(u"range for循环实例")

    # 使用默认参数生成序列进行遍历
    for i in range(5):
        print(i, end=',')

        # 换行
    print('')

    # 指定范围生成序列进行遍历
    for i in range(0, 10):
        print(i, end=',')

        # 换行
    print('')

    # 带步长方式生成序列进行遍历
    for i in range(0, 10, 2):
        print(i,end="  ")

    #嵌套

    #两个for语句实现九九乘法表：

    for i in range(1, 10):
        for j in range(i, 10):
            print(u"%d * %d = %2d" % (i, j, i * j), end="  ")

        print("")

    #while循环语句来计算0-100所有的偶数和：
    print(u"计算0-100间所有偶数和")

    n = 100
    index = 0
    sum = 0
    while index <= n:
        sum = sum + index
        index = index + 2

    print(u"0-100间偶数和= %d " % sum)

    #while和for综合使用
    print(u"九九乘法表实例：")
    n = 1

    while n <= 9:
        for m in range(n, 10):
            print(u"%d * %d = %2d" % (n, m, n * m), end="  ")

        print("")
        n = n + 1

'''
break&continue

break
break语句用于控制跳出for或while循环体

continue
continue语句用于跳出当前循环块中剩余的代码语句，继续下一次循环执行。

'''