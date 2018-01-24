# coding=utf-8
# 去字符串前后空格

if __name__ == "__main__":
    # 去字符串空格示例
    demo_str = " 这个字符串 前 中 后都有空格 "
    print(demo_str)

    # 去除前面的空格
    lstr = demo_str.lstrip()
    print(lstr)

    # 去除后面的空格
    rstr = demo_str.rstrip()
    print(rstr)

    # 去除前后的空格
    str = demo_str.strip()
    print(str)