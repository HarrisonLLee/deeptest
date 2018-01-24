# _*_ coding : utf-8 _*_
__author__ = 'Jason_copy'

'''
在python提供了以下函数来实现查找与替换功能。

find
    find(str, beg=0, end=len(string)),查找str是否包含在字符串中，
    若指定了beg和end，则在beg和end范围中查找，若找到则返回开始的索引值，否则返回-1
index
    同find方法，不同的是，index若未查找到，抛出一个异常信息，而不是返回-1
rfind
    同find方法，不过rfind是从右边往左边查找。
rindex
    同index方法，不过rindex是从右边往左边查找。
repalce
    将字符串中指定的子串替换成目标字符串，如果指定了替换次数，则替换不超过指定的次数
'''
if __name__ == "__main__":
    source_str = u"it's my book, please show it, wa ka ka, yo yo yo!"

    #从左往右查找“yo”
    print("从左往右查找yo")
    print(source_str.find("yo"))#结果为40
    print(source_str.index("yo"))#结果为40

    #从右往左找“yo”
    print("从右往左查找yo")
    print(source_str.find("yo"))#结果为40
    print(source_str.rfind("yo"))#结果为46

    #替换所有的“yo”
    des_str = source_str.replace("yo","ha")
    print(des_str)#结果为it's my book, please show it, wa ka ka, ha ha ha!

    #替换2次“yo”
    des_str = source_str.replace("yo","ha",2)
    print(des_str)#结果为it's my book, please show it, wa ka ka, ha ha yo!