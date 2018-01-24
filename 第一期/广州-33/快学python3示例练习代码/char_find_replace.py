# coding=utf-8
# 字符串查找与替换

if __name__ == "__main__":
    source_str = "this is my word,please show it,ha ha ha,ye ye ye!"

    # 从左往右查找 ye
    print("从左往右查找 ye")
    print(source_str.find("ye"))
    print(source_str.index("ye"))

    # 从右往左查找 ye
    print("从右往左查找 ye")
    print(source_str.rfind("ye"))
    print(source_str.rindex("ye"))

    # 替换所有的 ye
    des_str = source_str.replace("ye","oh")
    print(des_str)

    # 替换两次 ye
    des_str =  source_str.replace("ye","oh",2)
    print(des_str)