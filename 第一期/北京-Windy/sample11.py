#!/usr/bin/env  python
# -*- coding: UTF-8 -*-

class Flow:

    '''打印出100-999之间所有的水仙花数，一个三位数的各位立方和等于原数'''

    # def __init__(self, ge, shi, bai):
    #     self.ge = ge
    #     self.shi = shi
    #     self.bai = bai

    def flow(self):
        l = []
        for i in range(100, 1000):
            bai = int(i / 100)
            shi = int(i / 10 % 10)
            ge = int(i % 10)
            if i == bai ** 3 + shi ** 3 + ge ** 3:
                # print(i)
                l.append(i)
                # print(bai)
                # print(shi)
                # print(ge)
        return l


if __name__ == '__main__':
    f = Flow()
    a = f.flow()
    count = 0
    print("100-999之间的水仙花数为:", end=' ')
    for i in a:
        count += 1
        print(i, end=' ')
    print(end='\n')
    print("100-999之间的水仙花个数为%d" % count)

