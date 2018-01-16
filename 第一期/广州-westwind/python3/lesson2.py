#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/13 22:36
# @Author  : caijiangchun
# @Site    : 
# @File    : lesson2.py
# @Software: PyCharm
#字符串的内置函数之连接和切割(join and split)
def string1():
    t = ('1','2', '3', '9', '39', 'study')
    print(t)
    #用-将t中的元素合并成新的字符串
    string_demo = "_".join(t)
    print(string_demo)
    #把string_demo进行以-进行切割
    str_list = string_demo.split('_')
    print(str_list)
    #将t中的元素合并成一个新的字符串
    strtwo = "".join(t)
    print(strtwo)

#查找和替换（find index rfing rindex replace)
def find_replac():
    source_str = u"it's my book, please show it, Welcom to Python book!"
    print(u"从左往右查找")
    print(source_str.find("bo"))
    print(source_str.index("bo"))
    print(u"从右往左查")
    print(source_str.rfind("com"))
    print(source_str.rindex("com"))

    #替换所有的boo
    replace_str = source_str.replace("boo", "kkk")
    print(replace_str)

#去字符串前后的空格
def strip1():
    demo = u" 我的前 后 左 右 中间  都有空格"
    print(demo)

    lstrip1 = demo.lstrip()
    print(lstrip1)

    rstrip1 = demo.rstrip()
    print(rstrip1)

    strip2 = demo.strip()
    print(strip2)

#判断字符串的类型
def str_type():
    str_one = u"12345499580"
    str_two = u"adkjclkjKFJALL"
    str_three = u"ads1122jDJKFJ"
    str_four = u"adsskk"
    str_five = u" BADKK"
    str_six = u"    "
    str_seven = u" sa1k 123 "

    #isalnum是否都是字母和数字
    print(str_three.isalnum())
    #isalpha字母
    print(str_two.isalpha())
    #isdigit数字
    print(str_one.isdigit())
    print(str_seven.isdigit())

    #islower小写
    print(str_four.islower())
    #isupper大写
    print(str_two.isupper())
    print(str_five.isupper())

    #isspace都是空格
    print(str_six.isspace())
    print(str_seven.isspace())

if __name__ == "__main__":
    string1()
    find_replac()
    strip1()
    str_type()