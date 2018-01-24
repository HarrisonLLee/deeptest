# coding=utf-8


'''
在Python中函数定义的基本形式：


def 函数名(参数列表):

    # 代码块

    return 返回值
'''


def sum(a, b):
    c = a + b
    return c

#函数封装实现九九乘法表
def multi():
    data = []
    for i in range(1, 10):
        line = []
        for j in range(i, 10):
            line.append(u"%d * %d = %2d " % (i, j, i * j))

        data.append(line)

    return data

def sum_tuple(seq):
    sum = 0
    for s in seq:
        sum = sum + s
    return sum

def str_join(str1, str2, str3):

    return str1 + str2 + str3

if __name__ == "__main__":
    # 计算两个数的和：
    print(u"函数定义，计算和")
    # 调用函数
    c = sum(1, 2)

    print(c)

    #函数封装实现九九乘法表
    print(u"九九乘法表实例：")
    data = multi()
    for d in data:
        print(d)
        pass


    '''
    在Python中参数的传递要注意传入的是可更改的还是不可更改的对象。
    
    在python中对象从修改来讲可以分为：
    
    可更改对象
    在python中，可更改的对象有list（列表）、dict（字典）、set（集合）等等
    
    不可更改对象
    不可更改的对象有strings、tuples、numbers等等。
    
    在Python函数参数的传递，可以传入不可变或可变类的参数。
    
    不可变类型：类似C/C++中的传值参数。
    
    可变类型：类似C/C++的引用参数（即传地址方式）
    
    因为在Python中一切皆为对象，所以在Python中严格来讲我们不能跟在C/C++中一样说是值传递或引用传递，应该讲传不可变对象或可变对象。
    
    '''
    print("#元组作为参数传递")
    tuple_1 = (1, 9, 10, 2, 2, 39, 0, 11, 20)
    print(tuple_1)

    sum = sum_tuple(tuple_1)
    print(u"和为： %d" % sum)


    print(u"字符串连接实例: ")

    str1 = u"大家好，"
    str2 = u"我的公众号是："
    str3 = u"开源优测"

    str_j = str_join(str1, str2, str3)
    print(str_j)
