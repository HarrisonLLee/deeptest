# -*- coding:utf-8 -*-
__author__ = 'beck'

if __name__ == '__main__':
    #set是无序不可重复的，并且只有一个参数
    settest = set(u"测试使用数据TESTeesstttestTEST")
    print(settest)
    #以列表的形式存储，每个元素显示
    settestone = set([u"test","test","TEST","TEST"])
    print(settestone)

    set_source = set([u"test",1,2,3,4,5])
    set_demo = set([u"TEST",1,5,6,7,8])
    #set中添加元素-add方法
    set_source.add(9)
    set_demo.add(9)
    print(set_source)
    print(set_demo)
    #set中删除元素-remove
    set_source.remove(9)
    print(set_source)
    print(set_demo)
    #添加元素update操作
    list_demo = [1,3,8,9]
    set_demo.update(list_demo)
    print(set_demo)
    #union交集
    unionset = (set_source.union(set_demo))
    print(unionset)
    #intersection并集
    intersectionset = set_source.intersection(set_demo)
    print(intersectionset)
    #判断s1中每一个元素是否都在s2中 s1.issubset(s2)
    set_one = set([1, 5])
    set_two = set([u"TEST", 1, 5, 6, 7, 8])
    result1 = set_one.issubset(set_two)
    print(result1)
    #判断S2中每个元素是否都在S1中 s1.issuperset(s2)
    result2 = set_two.issuperset(set_one)
    print(result2)
    #返回s1中有的，s2中没有的
    myset = set_source.difference(set_demo)
    print(myset)

    #if控制语句
    var = int(input("请输入一个整数："))
    if var >=0 and var<=10:
        print("您输入的是10以内的整数")
    elif var > 10 and var <= 50:
        print("您输入的是10到50之间的整数")
    elif var > 50 and var <=100:
        print("您输入的是50到100之间的整数")
    else:
        print("您输入的是大于100的整数")

    #for控制语句练习
    #for循环控制输入元组
    tupleOne = (1,2,3,4,5,6,7,8,9,10)
    for element in tupleOne:
        print(element)
    list = ["test","one","four","three"]
    for listele in list:
        print(listele)
    dict_test = {"key1":"testone","key2":"testtwo","key3":"testthree"}
    for dictele in dict_test:
        print("%s %s"%(dictele,dict_test[dictele]))
    for (key,value) in dict_test.items():
        print("%s %s"%(key,value))

    #利用range生成示例
    print("range函数的运用：")
    for i in range(5):
        print(i,end=',')
    print('')
    for j in range(1,10):
        print(j,end=',')
    print('')
    for index in  range(10,100,10):
        print(index,end=',')
    print('')

    #利用for循环生成9*9的乘法口诀表
    for i in range(1,10):
        for j in range(i,10):
                print("%d*%d=%2d"%(i,j,i*j),end=' ')
        print('')
    #使用while循环来累计100以内所有偶数之和d
    n=100
    index = 0
    sum = 0
    while(index <= n):
        sum = sum + index
        index = index + 2
    print("100以内所有偶数和为%d"%sum)
    #使用for和while实现9*9乘法表
    i = 1
    while i<=9:
        for j in range(i,10):
            print("%d*%d=%2d" % (i, j, i * j), end=' ')
        print('')
        i = i+1;
    #break为结束循环体
    for x in  range(1,10):
        if x == 5:
            break
        print(x,end=',')
    print('')
    #continue为结束本次循环
    for x in range(1,10):
        if x == 5 :
            continue
        print(x,end=',')
    print('')

    #函数定义
    #简单的求和运算
    def sum(a,b):
        c = a +b
        return  c
    frist =float(input("请输入第一个数："))
    print('')
    second =float(input("请输入第二个数："))
    sumnum = sum(frist, second)
    print("输入的2个数的之和%s："%sumnum)
    #实现乘法运算
    def multi(a,b):
        data = []
        for i in  range(a,b):
            line = []
            for j in range(i,b):
                line.append("%d*%d=%2d"%(i,j,i*j))
            data.append(line)
        return  data

    datatest = multi(1,10)
    for d in  datatest:
        print(d)
    #实现元组的传递
    def sum_tuple(seq):
        sum = 0
        for i in seq:
            sum = sum +i
        return  sum
    tuple_1 = (1,2,3,4,5,6,7,8,9,10,11)
    print(tuple_1)
    dataone = sum_tuple(tuple_1)
    print(u"求和结果为： %d"%dataone)
    #定义字符串连接
    def str_join(str1,str2,str3):
        return str1+' ' + str2+' ' + str3
    str1 = "I"
    str2 = 'Love'
    str3 = 'Testing'
    new_str = str_join(str1,str2,str3)
    print(new_str)







