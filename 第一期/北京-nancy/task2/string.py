# -* coding:utf-8 *-
__author__ = 'nancy'

if __name__ == "__main__":
    a = u'this is string'
    b = u"this is string"
    c = """
    this is string
    this is still string
    """

    old_tuple = ('1', '2', '3', '4', '5', 'a', 'b', "egg")

    # use '-' join old_tuple to be a new string
    join_str = '-'.join(old_tuple)
    print(join_str)

    # use '-' split string
    split_list = join_str.split('-')
    print(split_list)

    new_str = ''.join(old_tuple)
    print(new_str)

    source_str = u"this is a test this is a test this is a test"
    print(u"find test from left to right")
    print(source_str.find("test"))
    print(source_str.index("test"))
    # print(source_str.find("aaa"))     # return -1
    # print(source_str.index("aaa"))    # throwing an exception

    print(u"find test from right to left")
    print(source_str.rfind("test"))
    print(source_str.rindex("test"))

    print(u"replace all test")
    replace_str = source_str.replace("test", "replace")
    print(replace_str)

    print(u"replace twice")
    replace2_str = source_str.replace("test", "replace", 2)
    print(replace2_str)

    space_str = u"   There's a space in the middle and my front and back   "
    print(space_str)

    # remove the front space
    l_str = space_str.lstrip()
    print(l_str)

    # remove the space behind
    r_str = space_str.rstrip()
    print(r_str)

    # remove the space before and after
    s_str = space_str.strip()
    print(s_str)

    # judge the type of string
    str_num = "0123456789"
    str_abc = "adcdABCD"
    str_all = "123asdASDF"
    str_sa = "adsg"
    str_ba = "ASDF"
    str_space = "     "
    str_aspace = " adsf "

    print(str_all.isalnum())  # letter and num
    print(str_abc.isalpha())  # letter
    print(str_num.isdigit())  # num
    print(str_abc.islower())  # lowercase letters
    print(str_sa.islower())
    print(str_abc.isupper())  # upper letters
    print(str_ba.isupper())
    print(str_space.isspace())
    print(str_aspace.isspace())

'''
result is:
1-2-3-4-5-a-b-egg
['1', '2', '3', '4', '5', 'a', 'b', 'egg']
12345abegg
find test from left to right
10
10
find test from right to left
40
40
replace all test
this is a replace this is a replace this is a replace
replace twice
this is a replace this is a replace this is a test
   There's a space in the middle and my front and back
There's a space in the middle and my front and back
   There's a space in the middle and my front and back
There's a space in the middle and my front and back
True
True
True
False
True
False
True
True
False
'''