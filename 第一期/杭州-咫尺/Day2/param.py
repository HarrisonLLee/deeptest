# -*- coding:utf-8 -*-
__author__ = "Heather"
def sum_tuple(seq):
    sum = 0
    for s in seq:
        sum = sum + s
    return  sum

if __name__ == '__main__':
    tuple1 = (1,9,10,2,2,39,0,11,200)
    print(tuple1)

    sum = sum_tuple(tuple1)
    print(u"和=%d"%sum)

def str_join(str1,str2,str3):
    return str1+str2+str3

str_1 = "a"
str_2 = "b"
str_3 = "c"
str_j = str_join(str_1,str_2,str_3)
if __name__ == '__main__':
    print(str_j)