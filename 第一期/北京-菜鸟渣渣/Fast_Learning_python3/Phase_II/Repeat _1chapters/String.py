# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Description :
   Author :       Young
   Change Activity: 2018/1/16:
-------------------------------------------------
"""
__author__ = 'Young'
'''
字符串是Python中最常用的数据类型，通常我们使用引号(单引' 或 双引" 或 三引号""")来创建字符串。

在python3中，所有的字符串都是Unicode编码。

对于编程而言，大部分时间都是在做字符的处理，例如字符串连接、切割、转换、格式化等等。
'''

if __name__ == "__main__":
    print("字符连接和切割")
    t = ('1', '2', '3', '4', '5', 'a', 'b', "efg")

    # 用 - 将t中元素合并成一个新的字符串
    str_demo = '-'.join(t)
    print(str_demo)

    # 将str_demo以-进行切割
    str_set = str_demo.split('-')
    print(str_set)

    # 将t中元素合并成一个新的字符串
    str_demo = ''.join(t)
    print(str_demo)


    '''
    find
    find(str, beg=0, end=len(string)),查找str是否包含在字符串中，若指定了beg和end，则在beg和end范围中查找，若找到则返回开始的索引值，否则返回-1
    
    index
    同find方法，不同的是，index若未查找到，抛出一个异常信息，而不是返回-1
    
    rfind
    同find方法，不过rfind是从右边往左边查找。
    
    rindex
    同index方法，不过rindex是从右边往左边查找。
    
    repalce
    将字符串中指定的子串替换成目标字符串，如果指定了替换次数，则替换不超过指定的次数
    '''
    print("字符串查找和替换")
    source_str = u"it's my book, please show it, wa ka ka, yo yo yo!"

    # 从左往右查找yo
    print(u"从左往右查找 yo")
    print(source_str.find("yo"))
    print(source_str.index("yo"))

    # 从右往左查找yo
    print(u"从右往左查找 yo")
    print(source_str.find("yo"))
    print(source_str.rindex("yo"))

    # 替换所有的 yo
    des_str = source_str.replace("yo", "ha")
    print(des_str)

    # 替换两次 yo
    des_str = source_str.replace("yo", "ha", 2)
    print(des_str)


    '''
    lstrip
    去除字符串左边的空格
    
    rstrip
    去除字符串右边的空格
    
    strip
    去除字符串左右两边的空格，即把lstrip和rstrip都执行一遍
    '''
    print("去字符串前后空格")
    demo_str = "  我的前  后 和 中 间  都有空格  "
    print(demo_str)

    # 去除前面的空格
    lstr = demo_str.lstrip()
    print(lstr)

    # 去除后面的空格
    rstr = demo_str.rstrip()
    print(rstr)

    # 去除前后的空格
    str = demo_str.strip()
    print(str)


    '''
    isalnum
    判断字符串是否由字母或数字组成，是则返回true,否则为false
    
    isalpha
    判断字符串是否都是字母，是则返回true,否则为false
    
    isdigit 判断字符串是否都是数字，是则返回true,否则为false
    
    islower 判断字符串是否都是小写，是则返回true,否则为false
    
    isnumeric 判断字符串是否都是数字，是则返回true,否则为false
    
    isspace 判断字符串是否都是空格，是则返回true,否则为false
    
    isupper 判断字符串是否都是大写，是则返回true,否则为false
    '''
    print("判断字符串类型")
    str_1 = "1234567890"
    str_2 = "abcdefABCDEF"
    str_3 = "12345abcdeABCDE"
    str_4 = "abcdef"
    str_5 = "ABCDEF"
    str_6 = "    "
    str_7 = " sfsdf "

    # isalnum
    print(str_3.isalnum())

    # isalpha
    print(str_2.isalpha())

    # isdigit
    print(str_1.isdigit())

    # islower
    print(str_4.islower())
    print(str_2.islower())

    # isupper
    print(str_4.isupper())
    print(str_2.isupper())

    # isspace
    print(str_6.isspace())
    print(str_7.isspace())