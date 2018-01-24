# -*- coding:utf-8 -*-

__author__ = u'Heatherwyz'

if __name__ == "__main__":
    dict_demo = {u"DeepTest": u"开源优测", u"book": u"快学Python3"}
    tup1 = [1, 2, 3, 4] 

    #copy
    dict_cp = dict_demo.copy()
    print(dict_demo)
    print(dict_cp)

    #fromkeys 创建字典
    dict_new = dict.fromkeys(tup1,u"value")
    print(dict_new)

    #get获取指定key的value
    value1 = dict_demo.get(u"Deeptest",u"默认")
    value2 = dict_demo.get(u"Python3",u"默认")

    print(value1)
    print(value2)
    
    #in判断key是否存在
    key = u"DeepTest"
    result1 = key in dict_demo
    result2 = key in dict_new
    print(result1)
    print(result2)
    
    #items ,以元组形式返回字典所有的（key,value）
    items = dict_demo.items()
    print(items)

    #keys 以列表形式返回字典所有的key
    keys = dict_demo.keys()
    print(keys)

    #setdefault 如果key存在 ，则返回对应的value，
    #否则将该key和默认值插入到字典中，并返回默认值
    set_result1 = dict_demo.setdefault(u"DeepTest",u"设置值")
    set_result2 = dict_demo.setdefault(u"我是key",u"我是value")
    print(set_result1)
    print(set_result2)

    #update
    dict_demo.update(dict_new)
    print(dict_demo)

    #values
    values = dict_demo.values()
    print(values)