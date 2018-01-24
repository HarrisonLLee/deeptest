# coding=utf-8
# 元组运算示例

if __name__ == "__main__":
    print("元组运算示例:")
    tup1 = ("Hello", "World")
    tup2 = (1, 2, 3, 4)

    # 计算元组的长度
    print("元组tup1的长度: %d" %len(tup1))

    # 元组连接
    tup3 = tup1 + tup2
    print("元组连接:")
    print(tup3)

    # 元组复制
    tup4 = tup1 * 2
    print("元组复制:")
    print(tup4)

    # 判断元素是否在元组中，是则返回true，否则返回false
    result = 5 in tup2
    print("5在元组2中吗?")
    print(result)

    # 遍历元组
    for t in tup2:
        print("遍历元组2:")
        print(t)