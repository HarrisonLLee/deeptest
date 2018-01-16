# -*- coding:utf-8 -*-
from os import replace

__author__ = 'beck'
if __name__ == '__main__':
    a=u'测试使用字符串'
    b=u"查询使用字符串test"
    c=u'''测试使用字符串
    测试使用字符串
    测试使用字符串test'''
    print(a,b,c)
    #字符串的分割和连接
    mystring =('2','3','7','fd','4','90','jkf89s')
    #join进行拼接
    str_list='_'.join(mystring)
    print(str_list)
    #split用来分开字符串，返回为一个list
    str_demo = str_list.split('_')
    print(str_demo)

    new_str =''.join(str_demo)
    print(new_str)

    #字符串的查找和替换
    source_str=u'this is a test string for python,ha ha ha'
    #从左往右查找
    print(source_str.find('str'))
    #指定了范围查找
    print("===="+ str(source_str.find('str',10,20)))
    print(source_str.index("tes"))
    # 指定了范围查找
    print("++++++"+ str(source_str.index('tes',10,60))) #使用str来将int转换为str
    #从右往左进行查找
    print(source_str.rfind('is'))
    print(source_str.rindex('p'))
    #替换字符串中字符
    des_str = source_str.replace('ha','yo')
    print(des_str)
    dest_str = source_str.replace('ha','yo',2)
    print(dest_str)

    #去掉字符串中空格
    demo_str = "    都是 空格 还是空格 空格 "
    print(demo_str)

    listone = demo_str.lstrip()
    print(listone)
    listtwo = demo_str.rstrip()
    print(listtwo)
    listthree = demo_str.strip()
    print(listthree)

    str_1 =u"123456789"
    str_2 = "abcdefABCDEF"
    str_3 = "12345abcdeABCDE"
    str_4 = "abcdef"
    str_5 = "ABCDEF"
    str_6 = "    "
    str_7 = " sfsdf "
    str_8 ='四'

    #判断是否都是数字或字母组成
    print(str_3.isalnum())
    #判断是否都是字母组成
    print(str_2.isalpha())
    #判断是否都是数字
    print(str_1.isdigit())
    print(str_1.isnumeric())
    print(str_8.isdigit())
    print(str_8.isnumeric())
    print(str_8.isdecimal())
    print(str_1.isdecimal())

    #判断是否都是小写
    print(str_2.islower())
    print(str_4.islower())
    #判断是否都是大写
    print(str_2.isupper())
    print(str_5.isupper())

    #判断是否都是空格
    print(str_6.isspace())
    print(str_7.isspace())
