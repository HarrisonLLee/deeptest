# coding=utf-8
# 字典的遍历、修改和删除示例

if __name__ == "__main__":
    print("字典的遍历、修改和删除示例：")
    dict_demo = {"python":"编程语言", "ebook":"python基本教程"}
    # 遍历 方法1 使用items方法，以元组的形式返回字典所有的（key，value）
    for (key, value) in dict_demo.items():
        print("%s : %s" % (key, value))

    #遍历 方法2 使用key方法，以列表形式返回字典所有的key
    for key in dict_demo.keys():
        print("%s : %s" % (key, dict_demo[key]))

    # 修改
    dict_demo["编程语言"] = "修改key可以吗"
    print(dict_demo)
    dict_demo["python"] = "新手"
    print(dict_demo)

    # 删除指定元素
    del dict_demo["编程语言"]
    print(dict_demo)

    # 清空字典
    dict_demo.clear()
    print(dict_demo)