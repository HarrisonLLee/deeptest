# coding = utf-8
# 列表运用python的切片机制

if __name__ == "__main__":
    print("列表切片的示例:")
    list1 = ["This", "is", "a", "sample", "for", "list"]

    # 读取第二个元素is，注意索引下表从0开始
    e = list1[1]
    print("列表第二个元素是:")
    print(e)

    # 读取倒数第二个for
    e = list1[-2]
    print("列表倒数第二个元素是:")
    print(e)

    # 切片,读取从第2个元素开始后的所有元素
    e = list1[1:]
    print("读取从第2个元素开始后的所有元素:")
    print(e)

    # 切片,读取第2-4个元素
    e = list1[1:4]
    print("读取第2-4个元素:")
    print(e)