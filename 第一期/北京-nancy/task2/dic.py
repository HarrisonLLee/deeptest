# -* coding:utf-8 *-
__author__ = 'nancy'

if __name__ == "__main__":
    dict1 = {u"key1" : u"value1", u"key2" : u"value2"}
    tuple1 = (1, 2, 3, 4)

    print(dict1)
    print(len(dict1))
    dict_str = str(dict1)
    print(dict_str)
    print(type(dict_str))
    print(type(dict1))

    dict_copy = dict1.copy()
    print(dict_copy)

    dict_new = dict.fromkeys(tuple1, u"value")
    print(dict_new)

    # get value
    value1 = dict1.get(u"key1", u"test")
    value2 = dict1.get(u"123", u"no value")
    print(value1)
    print(value2)

    # if in
    key1 = u"key1"
    key2 = u"lala"
    result1 = key1 in dict1
    result2 = key2 in dict1
    print(result1)
    print(result2)

    # return keys
    print(dict1.keys())
    # return values
    dict_value = dict1.values()
    print(dict_value)
    # return items
    print(dict1.items())

    # if key exist,return value
    # if not,insert new key:value and return default
    dict_setdefault1 = dict1.setdefault(u"key1", u"set value")
    dict_setdefault2 = dict1.setdefault(u"new", u"new")
    print(dict_setdefault1)
    print(dict_setdefault2)
    print(dict1)

    # update
    dict1.update(dict_new)
    print(dict1)

    dict1 = dict_copy.copy()
    print(dict1)

    # print
    for (key, value) in dict1.items():
        print("%s : %s" % (key, value))

    for key in dict1.keys():
        print("key is : %s" % key)

    for value in dict1.values():
        print("value is : %s" % value)

    dict1[u"key1"] = u"update"
    print(dict1)

    del dict1[u"key1"]
    print(dict1)

    dict1.clear()
    print(dict1)

'''
{'key1': 'value1', 'key2': 'value2'}
2
{'key1': 'value1', 'key2': 'value2'}
<class 'str'>
<class 'dict'>
{'key1': 'value1', 'key2': 'value2'}
{1: 'value', 2: 'value', 3: 'value', 4: 'value'}
value1
no value
True
False
dict_keys(['key1', 'key2'])
dict_values(['value1', 'value2'])
dict_items([('key1', 'value1'), ('key2', 'value2')])
value1
new
{'key1': 'value1', 'key2': 'value2', 'new': 'new'}
{'key1': 'value1', 'key2': 'value2', 'new': 'new', 1: 'value', 2: 'value', 3: 'value', 4: 'value'}
{'key1': 'value1', 'key2': 'value2'}
key1 : value1
key2 : value2
key is : key1
key is : key2
value is : value1
value is : value2
{'key1': 'update', 'key2': 'value2'}
{'key2': 'value2'}
{}
'''