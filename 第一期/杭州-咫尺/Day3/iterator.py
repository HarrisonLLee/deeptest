# -*- coding:utf-8 -*-
__author__ = "Heather"
import sys
if __name__ == '__main__':
    seq_tuple = (1,2,3,4,5)
    seq_it = iter(seq_tuple)
    print("第一个元素：%s"%next(seq_it))
    print("第二个元素：%s"%next(seq_it))
    print("第三个元素：%s"%next(seq_it))

    #for
    print("\nfor循环遍历迭代器对象")
    for_it = iter(seq_tuple)
    for x in for_it:
        print(x,end=' ')

    #while
    print("\nwhile&next遍历迭代器")
    while_it = iter(seq_tuple)
    while True:
        try:
            print(next(while_it))
        except StopAsyncIteration:
            sys.exit()