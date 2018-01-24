# coding = utf-8
# 列表的方法

if __name__ == "__main__":
    print("列表方法示例:")
    list1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    list2 = [5, 6, 7, 8]
    list3 = [5, 1, 3, 7, 0]

    # append,追加一个元素
    list1.append(9999)
    print(list1)

    # count,统计2出现的次数
    print("统计在列表1出现2的次数: %d" % list1.count(2))

    # extend, 将list2追加到list1中
    list1.extend(list2)
    print(list1)

    # index,返回第一个2的索引
    print("列表1中第一个2的索引是: %d" % list1.index(2))

    # insert,在列表1第三个位置输入 666
    list1.insert(2, 666)
    print(list1)

    # pop,删除最后一个元素，默认最后一个(-1)，可以指定
    list1.pop()
    print(list1)

    # pop,删除第3个元素
    list1.pop(2)
    print(list1)

    # reverse,把列表反向一下
    list1.reverse()
    print(list1)

    # sort,对列表进行排序
    list3.sort()
    print(list3)

    # copy,列表拷贝
    list4 = list1.copy()
    print(list1)
    print(list4)

    # clear,清空列表
    list1.clear()
    print(list1)
    print(list4)