# -*- coding:utf-8 -*-
__author = u'linan'

def sum(a,b):
    c = a + b
    return c

if __name__ == "__main__":
    print(u"函数定义，计算和")

    #调用函数
    c = sum(1,2)
    print(c)

#乘法表示例

def multi():
    data = []
    for i in range(1, 10):
        line= []
        for j in range(i, 10):
            line.append(u"%d * %d = %2d" % (i, j, i*j))
        data.append(line)
    return data
if __name__ == "__main__":
    print(u"九九乘法表示例")
    data = multi()  
    for d in data:
        print(d)
    

#参数传递
#元组传递
def sum_tuple(seq):
    sum = 0
    for s in seq:
        sum = sum + s
    return sum

if __name__ == "__main__":
    print(u"元组传参，求和实例")
    tuple_1 = (1,9,10,2,2,0,11,20)
    print(tuple_1)

    sum = sum_tuple(tuple_1)
    print(u"和为：  %d" % sum)

#字符串传递
def str_join(str1,str2,str3):
    return str1 + str2 +str3
if __name__ == "__main__":
    print(u"字符串连接实例：")
    str1 = u"大家好!"
    str2 = u"我是栗楠,"
    str3 = u"是测试工程师。"
    str_j = str_join(str1,str2,str3)
    print(str_j)