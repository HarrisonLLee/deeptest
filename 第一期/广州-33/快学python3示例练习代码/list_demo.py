# coding=utf-8
# 列表运用python内置函数

if __name__ == "__main__":
    list_demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    print("内置函数处理list示例:")

    # 计算list_deom中元素个数
    print("列表中的元素个数为: %d" % len(list_demo))

    # 返回list_demo中最大值的元素
    print("列表的最大值是: %d" % max(list_demo))

    # 返回list_demo中最小值的元素
    print("列表中的最小值是: %d" % min(list_demo))

    # 将list转换成元组
    tuple1 = tuple(list_demo)
    print("将列表转换成元组:")
    print(tuple1)

    # 将元组转换成列表
    list1 = list(tuple1)
    print("将元组转换成列表:")
    print(list1)