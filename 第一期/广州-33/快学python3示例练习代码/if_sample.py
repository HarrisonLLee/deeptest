# coding=utf-8
# if控制示例

if __name__ == "__main__":
    print("if控制示例:")
    var1 = int(input("请输入一个整数:"))
    if var1 > 0 and var1 < 10:
        print("您输入了一个大于0小于10的整数")
    elif var1 >= 10:
        print("您输入了一个大于等于10的整数")
    else:
        print("您输入了一个负数")
