#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/14 14:26
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson5.py
# @Software: PyCharm
#字典是无序的
def dict_one():
    #字典的内置函数
    dict1 = {
        "one": 1,
        2: "two"
    }
    print(dict1)
    print(len(dict1))

    #以字符的形式输出字典,即字典转换成字符串
    str_dict = str(dict1)
    print(str_dict)
    print(dict1)

    print(type(dict1))
    print(type(str_dict))

def dict_two():
    #字典的方法
    dict1 = {"name": "apple", "type": "friut", "how": "eat"}
    tup1 = (1, 2, 3, 4)
    print(dict1)

    #复制
    dict_cp = dict1.copy()
    print(dict_cp)

    #fromkeys创建字典
    dict_new = dict1.fromkeys(tup1, u"value")
    print(dict_new)

    #get获取对应key的value值
    value1 = dict1.get("name")
    value2 = dict1.get("type")
    print(value1)
    print(value2)

    #in, 判断key是否存在
    key = "name"
    result1 = key in dict1
    result2 = key in dict_new
    print(result1)
    print(result2)

    #item,以元组形式返回字典所有的（key,value)
    tuple_dict = tuple(dict1.items())
    print(tuple_dict)

    #keys ,返回字典所有关键字组成的无序列表
    keys = list(dict1.keys())
    print(keys)
    #sorted有序时,返回字典所有关键字组成的有序列表
    keyss = sorted(dict1.keys())
    print(keyss)

    #setdefault,如果key存在，则返回对应的value值
    #如key不存在， 则把key和value插入到字典中，并且返回对应的value
    set_result = dict1.setdefault(u"name", u"我是默认值")
    set_results = dict1.setdefault(u"key", u"value")
    print(set_result)
    print(set_results)
    print(dict1)

    #update,更新字典
    dict_new.update(dict1)
    print(dict_new)

    #values,返回字典中所有的value
    value3 = list(dict1.values())
    print(value3)

def dict_four():
    #字典遍历，修改，删除
    dict_d = {"python": "3", "java": "1.8", "c": "2015", "php": "7"}

    #字典推导式
    dict_a = {x : x**2 for x in (1, 2, 4, 8)}
    print(dict_a)

    #遍历1
    for (key, value) in dict_d.items():
        print("%s: %s" % (key, value))

    #遍历2
    for key in dict_d.keys():
        print((key, dict_d[key]))

    #修改
    dict_d["python"] = '2'
    print(dict_d)

    #删除指定元素
    del dict_d["python"]
    print(dict_d)

    #清空
    dict_a.clear()
    print(dict_a)

if __name__ == "__main__":
    dict_one()
    dict_two()
    dict_four()
