# coding = utf-8
# 字典方法示例

if __name__ == "__main__":
    print("字典方法应用示例")

    dict_demo = {"python":"编程语言", "ebook":"python基本教程"}
    tup1 = [1, 2, 3, 4]

    # copy复制字典
    dict_cp = dict_demo.copy()
    print(dict_demo)
    print(dict_cp)

    # fromkeys创建字典
    dict_new = dict_demo.fromkeys(tup1,"value")
    print(dict_new)

    # get获取指定key的value
    value1 = dict_demo.get("python", "我是默认值")
    value2 = dict_demo.get("python基本教程", "我是默认值")
    print(value1)
    print(value2)

    # in,判断key是否存在
    key = "python"
    result1 = key in dict_demo
    result2 = key in dict_new
    print(result1)
    print(result2)

    # items,以元组的形式返回字典所有的(key,value)
    items = dict_demo.items()
    print(items)

    # keys 以列表形式返回字典所有的key
    keys = dict_demo.keys()
    print(keys)

    # setdefault,如果key存在,则返回其对应的value,否则将该key和默认值插入到字典中,并返回默认值
    set_result1 = dict_demo.setdefault("python", "设置值")
    set_result2 = dict_demo.setdefault("我是key", "我是value")
    print(set_result1)
    print(set_result2)
    print(dict_demo)

    # update,更新字典
    dict_demo.update(dict_new)
    print(dict_demo)

    # values,返回字典中所有的value
    values = dict_demo.values()
    print(values)