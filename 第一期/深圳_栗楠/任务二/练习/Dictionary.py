#-*- coding:utf-8 -*-
__author__ = u'linan'

if __name__ == "__main__":

    #字典基本示例
    dict = {u"DeepTest":u"开源优测",u"book":u"快学python3"}

    #计算字典的长度
    print(len(dict))

    #以字符方式输出字典，即讲字典转换成字符串
    str_d = str(dict)
    print(str_d)
    print(dict)

    #判断类型
    print(type(dict))
    print(type(str_d))

#字典方法
if __name__ == "__main__":
    print(u"字典方法应用示例")

    dict_demo = {u"DeepTest":u"开源优测",u"book":u"快学Python3"}
    tup1 = [1,2,3,4]

    #复制字典
    dict_cp = dict_demo.copy()
    print(dict_cp)
    print(dict_demo)

    #fromkeys创建字典
    dict_new = dict_demo.fromkeys(tup1,u"value")
    print(dict_new)

    #get获取指定key的value
    value1 = dict_demo.get(u"DeepTest",u"默认值")
    value2 = dict_demo.get(u"Python3",u"默认值")
    print(value1)
    print(value2)

    #in,判断key是否存在
    key = u"DeepTest"
    result1 = key in dict_demo
    result2 = key in dict_new
    print(result1)
    print(result2)

    #items,以元组形式返回字典所有的(key,value)
    items = dict_demo.items()
    print(items)

    #kyes,以列表形式返回字典所有的key
    keys = dict_demo.keys()
    print(keys)

    #setdefault,如果key存在，则返回其对应的value
    #否则将该key和默认值插入字典中，并返回默认值
    set_result1 = dict_demo.setdefault(u"Deeptest",u"快学Python3")
    set_result2 = dict_demo.setdefault(u"我是key",u"value")
    print(set_result1)
    print(set_result2)
    print(dict_demo)

    #update,更新字典
    dict_demo.update(dict_new)
    print(dict_demo)

    #values,返回字典中所有的value
    values = dict_demo.values()
    print(values)

    #遍历，修改，删除
    if __name__ == "__main__":
        print(u"字典遍历、修改、删除示例")
        dict_demo = {u"DeepTest": u"开源优测", u"ebook": u"快学Python3"}

        #遍历 方法1
        for (key,value) in dict_demo.items():
            print("%s : %s" % (key,value))

        #遍历 方法2
        for key in dict_demo.keys():
            print("%s : %s" % (key,dict_demo[key]))

        #修改
        dict_demo[u"ebook"] = u"哎哟我去"
        print(dict_demo)

        #删除指定元素
        del dict_demo[u"ebook"]
        print(dict_demo)

        #清空字典
        dict_demo.clear()
        print(dict_demo)