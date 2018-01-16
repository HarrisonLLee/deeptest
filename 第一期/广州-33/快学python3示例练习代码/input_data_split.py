# coding=utf-8
# 通过空格来切割键盘输入的数据，输出

if __name__ == "__main__":
    # 读取键盘任意输入
    data = input("请输入任意字符:")

    # 以空格切割输入的字符串
    list_data = data.split(' ')

    # 打印切割后的列表数据
    print(list_data)
