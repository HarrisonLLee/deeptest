# coding=utf-8
# 把一个为x的数值转换成各种数字的数据类型

if __name__ == "__main__":
    x = 1.68
    y = 10

    # 将x转换为整数
    print(int(x))

    print(float(y))  # 将y转换为浮点数

    print(complex(x))  # 将x转换为复数，实数部分为x，虚数部分为0

    print(complex(x, y))  # 将x，y转换为复数，实数部分为x，虚数部分为y
