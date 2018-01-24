# coding=utf-8
# 集合使用方法的示例

if __name__ == "__main__":
    print("set示例:")
    set_source = set([11, 11, 12, 13, 14, 15, 16, 17])
    set_demo = set([1, 1, 2, 3, 4, 5, 6, 7])
    print("原始数据:", end="")
    print(set_demo)

    # add方法，新增元素
    print("add后:", end="")
    set_demo.add(9)
    set_demo.add(1)  # 添加重复的没效果
    print(set_demo)

    # remove 删除元素
    print("remove后:", end="")
    set_demo.remove(9)
    print(set_demo)

    # update 新增多个元素值
    list_demo = ["a", "b", "c"]
    set_demo.update(list_demo)
    print("update后:", end="")
    print(set_demo)

    # clear 清空set集合
    print("清空前:", end="")
    print(set_source)
    set_source.clear()
    print("清空后:", end="")
    print(set_source)

    # issubset s1.issubset(s2), 判断s1中的每个元素是否都在s2中，即s1≤s2
    s1 = set(["apple", "pear"])
    s2 = set(["apple", "pear", "banana"])
    result = s1.issubset(s2)
    print(result)

    # issuperset s1.issuperset(s2), 判断s2中的每个元素是否都在s1中,即s1>=s2
    result = s1.issuperset(s2)
    print(result)

    # union 返回两个集合的并集
    s3 = s1.union(s2)
    print(s3)

    # intersection 返回两个集合的交集
    s3 = s1.intersection(s2)
    print(s3)

    # difference s1.difference(s2)， 返回s1中有s2中没的元素
    s3 = s2.difference(s1)
    print(s3)
