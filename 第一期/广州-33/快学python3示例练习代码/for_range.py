# coding=utf-8
# 循环控制示例之使用for循环遍历range里的内容

if __name__ == "__main__":
    # 使用默认参数生成序列进行遍历
    for i in range(5):
        print(i, end=',')

    # 换行
    print('')

    # 指定范围内生成序列进行遍历
    for i in range(0, 10):
        print(i, end=',')

    # 换行
    print('')

    # 带步长方式生成序列进行遍历
    for i in range(0, 10, 2):
        print(i, end=',')