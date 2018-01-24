# coding=utf-8
# 函数示例，使用函数实现九九乘法表输出


# 九九乘法表
def mult9():
    data = []
    for i in range(1, 10):
        line = []
        for j in range(i, 10):
            line.append("%d * %d = %2d" % (i, j, i*j))
        data.append(line)
    return data


if __name__ == "__main__":
    print("使用函数实现九九乘法表输出:")
    data = mult9()
    for d in data:
        print(d)