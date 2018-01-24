# -*- coding:utf-8 -*-
__author__ = u'Heather'

if __name__ == '__main__':
    str_1 = "1234567890"
    str_2 = "abcdefABCDEF"
    str_3 = "12345abcdeABCDE"
    str_4 = "abcdef"
    str_5 = "ABCDEF"
    str_6 = "      "
    str_7 = "  sfsdf"

    #isalnum 判断字符串是否由字母或数字组成，是则返回true,否则为false
    print(str_3.isalnum())

    #isalpha 判断字符串是否都是字母，是则返回true,否则为false
    print(str_2.isalpha())

    #isnumeric 判断字符串是否都是数字，是则返回true,否则为false
    #isdigit 判断字符串是否都是数字，是则返回true,否则为false
    print(str_1.isdigit())
    print(str_1.isnumeric())

    #islower 判断字符串是否都是小写，是则返回true,否则为false
    print(str_4.islower())
    print(str_2.islower())

    #isupper 判断字符串是否都是大写，是则返回true,否则为false
    print(str_4.isupper())
    print(str_2.isupper())

    #isspace 判断字符串是否都是空格，是则返回true,否则为false
    print(str_6.isspace())
    print(str_7.isspace())