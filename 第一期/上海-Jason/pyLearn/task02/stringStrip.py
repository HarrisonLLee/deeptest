# _*_ coding : utf-8 _*_
__author__ = "Jason_copy"

if __name__ == "__main__":
    # 去字符串空格示例
    demo_str = "  我的前  后 和 中 间  都有空格  "
    print(demo_str)

    # 去除前面的空格
    lstr = demo_str.lstrip()
    print(lstr)#结果为“我的前  后 和 中 间  都有空格  ”

    # 去除后面的空格
    rstr = demo_str.rstrip()
    print(rstr)#结果为“  我的前  后 和 中 间  都有空格”

    # 去除前后的空格
    str = demo_str.strip()
    print(str)#结果为“我的前  后 和 中 间  都有空格”