# -*- coding:utf-8 -*-
__author__ = "Heather"
if __name__ == '__main__':
    #for元组遍历
    tuple_1 = (1,2,3,4,5,6,7,8,9,0)
    print(u"遍历元组并打印")
    for t in tuple_1:
        print(t)

if __name__ == '__main__':
    #遍历列表
    list_1 = [u'Deeptest',u'开源优测',u'快学python3']
    print(u"遍历列表")
    for text in list_1:
        print(text)

if __name__ == '__main__':
    #遍历字典
    dict_1 = {u"开源":u"deeptest",u"python":u"python3"}
    print(u"字典遍历")
    for (key,value) in dict_1.items():
        print("%s:%s"%(key,value))

    print("\n------------")

    for key in dict_1:
        print("%s:%s"%(key,dict_1[key]))