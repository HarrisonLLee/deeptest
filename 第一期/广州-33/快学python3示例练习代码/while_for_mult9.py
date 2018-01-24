# coding=utf-8
# 循环控制示例之，使用while和for完成九九乘法表

if __name__ == "__main__":
    print("使用while和for循环完成九九乘法表:")
    a = 1
    while a <= 9:
        for b in range(a, 10):
            print("%d * %d = %2d" % (a, b, a * b), end= "  ")
        print("")
        a = a + 1