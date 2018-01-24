# -* coding:utf8 *-
__author__ = 'nancy'

if __name__ == "__main__":
    set_demo = set(u"deeptest lalalam")
    print(set_demo)

    set1 = set([1, 1, 2, 3, 4])
    set2 = set([1, 1, 2, 3, 4])

    print(u"set1: ", end="")
    print(set1)

    set1.add(9)
    set1.add(1)
    print(u"set1 add: ", end="")
    print(set1)

    set1.remove(9)
    print(u"set1 remove:", end="")
    print(set1)

    list_add = ["a", "b"]
    set1.update(list_add)
    print(u"add more than one: ", end="")
    print(set1)
'''
result is:
{' ', 't', 'd', 's', 'm', 'l', 'p', 'e', 'a'}
set1: {1, 2, 3, 4}
set1 add: {1, 2, 3, 4, 9}
set1 remove:{1, 2, 3, 4}
add more than one: {1, 2, 3, 4, 'b', 'a'}
'''