# _*_ coding : utf-8 _*_
__author__ = "Jason_copy"

'''
根据字符串数据来判断其类型，需要用到以下函数：
函数            说明
isalnum         判断字符串是否由字母或数字组成，是则返回true,否则为false
isalpha         判断字符串是否都是字母，是则返回true,否则为false
isdigit         判断字符串是否都是数字，是则返回true,否则为false
islower         判断字符串是否都是小写，是则返回true,否则为false
isnumeric       判断字符串是否都是数字，是则返回true,否则为false
isspace         判断字符串是否都是空格，是则返回true,否则为false
isupper         判断字符串是否都是大写，是则返回true,否则为false
'''
if __name__ == "__main__":
    str_1 = "1234567890"
    str_2 = "abcdefABCDEF"
    str_3 = "12345abcdeABCDE"
    str_4 = "abcdef"
    str_5 = "ABCDEF"
    str_6 = "    "
    str_7 = " sfsdf "

    # isalnum
    print(str_3.isalnum())#结果为TRUE
    print(str_1.isalnum())#结果为TRUE
    print(str_2.isalnum())#结果为TRUE

    # isalpha
    print(str_2.isalpha())#结果为TRUE
    print(str_2.isnumeric())#结果为FALSE

    # isdigit
    print(str_1.isdigit())#结果为TRUE
    print(str_1.isnumeric())#结果为TRUE

    # islower
    print(str_4.islower())#结果为TRUE
    print(str_2.islower())#结果为FALSE

    # isupper
    print(str_4.isupper())#结果为FALSE
    print(str_2.isupper())#结果为FALSE

    # isspace
    print(str_6.isspace())#结果为TRUE
    print(str_7.isspace())#结果为FALSE

    '''
    python3中str函数isdigit、isdecimal、isnumeric的区别：
    isdigit()
    True: Unicode数字，byte数字（单字节），全角数字（双字节）
    False: 罗马数字，汉字数字
    Error: 无
    
    isdecimal()
    True: Unicode数字，，全角数字（双字节）
    False: 罗马数字，汉字数字
    Error: byte数字（单字节）
    
    isnumeric()
    True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
    False: 无
    Error: byte数字（单字节）
    '''
    print('-'*100)
    num = "1"  #unicode
    print(num.isdigit())   # True
    print(num.isdecimal()) # True
    print(num.isnumeric()) # True

    print('-'*50)
    num = "1" # 全角
    print(num.isdigit())   # True
    print(num.isdecimal()) # True
    print(num.isnumeric()) # True

    print('-'*50)
    num = b"1"# byte
    print(num.isdigit())   # True
    #print(num.isdecimal())# AttributeError 'bytes' object has no attribute 'isdecimal'
    #print(num.isnumeric())# AttributeError 'bytes' object has no attribute 'isnumeric'

    print('-'*50)
    num = "Ⅳ" # 罗马数字
    print(num.isdigit())   # False
    print(num.isdecimal()) # False
    print(num.isnumeric()) # True

    print('-'*50)
    num = "四" # 汉字
    print(num.isdigit())   # False
    print(num.isdecimal()) # False
    print(num.isnumeric()) # True
