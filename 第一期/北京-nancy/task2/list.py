# -* coding:utf-8 *-
__author__ = 'nancy'

if __name__ == "__main__":
    list_demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    list2 = [11, 12, 13]

    print(len(list_demo))
    print(max(list_demo))
    print(min(list_demo))

    list_tuple = (1, 2, 3)
    print(list(list_tuple))

    list2.append(2)
    print(list2)

    list_demo.extend(list2)
    print(list_demo)

    num = list_demo.count(2)
    print(num)

    list_index = list_demo.index(2)
    print(list_index)

    list_demo.insert(0, 200)
    print(list_demo)

    a = list_demo.pop()
    print(list_demo)
    print(a)

    list_demo.reverse()
    print(list_demo)

    list_demo.sort()
    print(list_demo)

    list_copy = list_demo.copy()
    print(list_copy)

    list_copy.clear()
    print(list_copy)
    print(list_demo)

    # split
    print(list_demo[0])
    print(list_demo[-1])
    print(list_demo[1:])
    print(list_demo[1:4])

    print(list_demo)
    list_demo[0] = u"test"
    print(list_demo)
'''
result is:
10
9
0
[1, 2, 3]
[11, 12, 13, 2]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 2]
2
1
[200, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 2]
[200, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13]
2
[13, 12, 11, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 200]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 200]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 200]
[]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 200]
0
200
[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 200]
[1, 2, 3]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 200]
['test', 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 200]
'''