# -* coding:utf-8 *-
__author__ = 'nancy'

if __name__ == "__main__":
    tuple1 = (1, 2, 3, 4, 5)
    # tuple
    print(tuple1)
    for i in tuple1:
        print(i)

    # list
    list1 = [1, 2, 3, 4, 5]
    print(list1)
    for j in  list1:
        print(j)

    #dict
    dict1 = {u"key1" : u"values1", u"key2" : u"value2"}
    print(dict1)

    for key in dict1.keys():
        print(key)
    for value in  dict1.values():
        print(value)
    for (key, value) in dict1.items():
        print("%s : %s" % (key, value))
    for i in dict1:
        print("%s : %s" % (i, dict1[i]))

    # range
    for i in range(5):
        print(i, end=',')
    print('')
    for i in range(1, 10):
        print(i, end=',')
    print('')
    for i in range(1, 10, 2):
        print(i, end=',')

    #nest
    print(u"Multiplication table:")
    for i in range(1, 10):
        for j in range(i, 10):
            print("%d * %d = %2d" % (i, j, i*j), end="  ")
        print('')

    n = 1
    while n <=9:
        for m in range(n, 10):
            print("%d * %d = %2d" % (i, j, i*j), end="  ")
        print('')
        n = n + 1

    #while
    start1 = 0
    end = 100
    sum1 = 0
    while start1 <= end:
        sum1 = sum1 + start1
        start1 = start1 + 2
    print(sum1)
