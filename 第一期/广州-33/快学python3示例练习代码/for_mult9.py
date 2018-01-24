# coding=utf-8
# 循环控制示例之，使用两层for嵌套循环实现九九乘法表

if __name__ == "__main__":
    print("九九乘法表:")
    for i in range(1, 10):
        for j in range(i, 10):
            print("%d * %d = %2d" % (i, j, i*j), end="  ")
        print("")