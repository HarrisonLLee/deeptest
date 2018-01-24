# -* coding:utf8 *-
__authot__ = 'nancy'

if __name__ == "__main__":
    var1 = int(input(u"please input int: "))
    if var1 > 0 and var1 < 10:
        print(u"the number >0 and <10")
    elif var1 >= 10:
        print(u"the number >=10")
    else:
        print(u"you input negative")