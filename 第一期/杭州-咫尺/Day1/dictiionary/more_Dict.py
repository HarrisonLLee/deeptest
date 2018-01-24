#-*- coding:utf-8 -*-
__author__ = u"Heather"
if __name__ == '__main__':
    print(u"字典遍历")
    dict_demo = {u"DeepTest":u"开源优测",u"book":u"快学python3"}

    for (key,value) in dict_demo.items():
        print("%s:%s"%(key,value))
    
    for key in dict_demo:
        print("%s:%s"%(key,dict_demo[key]))

    dict_demo[u"book"] = u"second"
    print(dict_demo)

    del dict_demo[u"book"]
    print(dict_demo)

    dict_demo.clear()
    print(dict_demo)