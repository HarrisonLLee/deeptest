# -*- coding:utf-8 -*-
import math
import random
import cmath
'''
if __name__ == "__main__":

    x = 1.68
    y =10

    print(int(x))
    print(float(y))
    print(complex(x))
    print(complex(x,y))
    print(complex(y,x))

    a = -100
    b = 1.9
    c=100

    print('常用数学函数')
    print(abs(a))
    print(max(a,b,x,y))
    print(min(a,x,y,b))
    print('*****')

    print(pow(a,2))
    print(int(math.sqrt(c)))

    print("常用随机函数")
    ran = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(random.choice(ran))
    print(random.randrange(1,100,5))

    print(random.random())

    print("常用三角函数")
    q = 100

    # 返回x的反余弦弧度值
    print(cmath.acos(q))

    # 返回x的正弦弧度值
    print(cmath.sin(q))

    # 返回x的余弦弧度值
    print(cmath.cos(q))

    print(u"数学常量")
    print(cmath.pi)

    #join 合并一个新的字符串
    t = ('1', '2', '3', '4', '5', 'a', 'b', "efg")
    str_demo = ')'.join(t)
    print(str_demo)

    str_set = str_demo.split(')')
    print(str_set)

    str1=''.join(t)
    print(str1)

    #字符串查找啊等等，面试也很重要
    source_str = "it's my book, please show it, wa ka ka, yo yo yo!"
    print('从左往右查找yo')
    print(source_str.find('yo'))
    print(source_str.rindex('yo'))
    #replace all
    des_str = source_str.replace("yo","quan")
    print(des_str)
    #replace one
    des_str1 = source_str.replace("yo", "luo", 1)
    print(des_str1)

    demo_str = "  我的前  后 和 中 间  都有空格  "
    print(demo_str)


    lstr = demo_str.lstrip()
    print(lstr)


    rstr = demo_str.rstrip()
    print(rstr)

    str = demo_str.strip()
    print(str)
'''
if __name__ == '__main__':
    t1= (1,2,3,4,-5,6,7,8,999,0)

    print(len(t1))
    print(max(t1))
    print(min(t1))

    l1=[2,3,3,3,1,24,13]
    print(tuple(l1))
    #切片
    t2=('a','b','c',1,2,3,4)
    print(t2[2])
    print(t2[2:])
    print(t2[1:5]) #从第二个元素到第五个元素

    t3 = t1 + t2
    print(t3)
    result = 4 in t2
    print(result)

    for i in t1:
        print(i)

    list1 = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6]
    list2 = [7, 8, 9, 0, 10, 11]

    #print(type(list1.append(886)))
    list1.append(886)
    print(list1)
    #统计出现个数
    print(list1.count(886))
    #extend 加入合并新的list
    list2.extend(list1)
    print(list2)
    #返回第一数字"2"的索引数！！！！
    index = list2.index(2)
    print(index)
    list1.insert(0, 200)
    print(list1)
    # pop, 删除最后一个元素
    list1.pop()
    print(list1)
    # reverse, 把列表反向一下
    list1.reverse()
    print(list1)
    list1.sort()
    print(list1)
    print('----')
    list3 = list1.copy()
    print(list1)
    print(list3)
    # clear 清空列表
    list1.clear()
    print(list1)
    print(list3)

