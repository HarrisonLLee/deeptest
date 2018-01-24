# coding=utf-8
# 判断字符串类型

if __name__ == "__main__":
    str1 = "abc123"
    str2 = "abc"
    str3 = "123"
    str4 = "abcABC"
    str5 = "  "
    str6 = " abc"
    str7 = "ABC"

    # isalnmu 判断字符串是否由字母或数字组成
    print(str1.isalnum())
    print(str2.isalnum())

    # isalpha 判断字符串是否都是字母
    print(str1.isalpha())
    print(str2.isalpha())

    # isdigit 判断字符串是否都是数字
    print(str1.isdigit())
    print(str3.isdigit())

    # islower 判断字符串是否都是小写
    print(str2.islower())
    print(str4.islower())

    # isnumric 判断字符串是否都是数字
    print(str1.isnumeric())
    print(str3.isnumeric())

    # isspace 判断字符串是否都是空格
    print(str5.isspace())
    print(str6.isspace())

    # isupper 判断字符串是否都是大写
    print(str7.isupper())
    print(str4.isupper())