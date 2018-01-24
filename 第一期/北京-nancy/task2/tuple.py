# -* coding:utf-8 *-
__author__ = 'nancy'

if __name__ == "__main__":
    # base
    tuple_demo = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    print(len(tuple_demo))
    print(max(tuple_demo))
    print(min(tuple_demo))

    list_demo = [1, 2, 3, 4, 5, 6, 7]
    print(tuple(list_demo))

    # split
    data_demo = (u"deepteset", u"appium", u"test.com", u"hello", u"python3")
    appium = data_demo[1]
    print(appium)
    hello = data_demo[-2]
    print(hello)
    appium_end = data_demo[1:]
    print(appium_end)
    appium_hello = data_demo[1:3]
    print(appium_hello)

    # join
    tup1 = (u"test", u"test1")
    tup2 = (u"2test", u"2test1")
    tup3 = tup1 + tup2
    print(tup1)
    print(tup2)
    print(tup3)

    # delete
    ## del tup1
    ## print(tup1)   # NameError: name 'tup1' is not defined

    # calc
    copy_tup = tup2 * 2
    print(copy_tup)
    ifintup = "2test" in tup2
    print(ifintup)

    for i in tup2:
        print(i)


'''
result is:
10
9
0
(1, 2, 3, 4, 5, 6, 7)
appium
hello
('appium', 'test.com', 'hello', 'python3')
('appium', 'test.com')
('test', 'test1')
('2test', '2test1')
('test', 'test1', '2test', '2test1')
('2test', '2test1', '2test', '2test1')
True
2test
2test1
'''#
