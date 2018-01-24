# coding=utf-8
# 元组切片示例

if __name__ == "__main__":
    print("元组切片示例：")

    data_demo = ("This", "is", "a", "sample", "for", "tuple")

    # 读取第二个元素is，注意索引下标从0开始
    e = data_demo[1]
    print(e)

    # 读取倒数第三个sample
    e = data_demo[-3]
    print(e)

    # 切片，读取从第2个元素开始后的所有元素
    e =  data_demo[1:]
    print(e)

    # 切片，读取第2-4个元素
    e = data_demo[1:4]
    print(e)