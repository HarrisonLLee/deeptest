# coding=utf-8
# 循环控制示例之使用for循环遍历字典，使用两种方式，一种是以元组的方式遍历出来，一种是以列表的方式遍历出来

if __name__ == "__main__":
    dict_demo = {"python":"编程语言", "ebook":"python基础教程"}
    print("使用元组的方式遍历出来:")
    for (key, value) in dict_demo.items():
        print("%s : %s" % (key, value))

    print("使用列表的方式遍历出来:")
    for key in dict_demo.keys():
        print("%s : %s" % (key, dict_demo[key]))