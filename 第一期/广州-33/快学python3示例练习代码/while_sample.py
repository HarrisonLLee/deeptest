# coding=utf-8
# 循环控制示例之，使用while循环计算0-100所有偶数的和

if __name__ == "__main__":
    index = 0
    n = 100
    sum = 0

    while index <= 100:
        sum = sum + index
        index = index + 2

    print("0-100间偶数之和为: %d" % sum)