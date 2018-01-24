#!/usr/bin/env  python
# -*- coding: UTF-8 -*-


class Perfect:
    '''输出1-1000之内所有的完数'''

    def perf(self):

        for i in range(1, 1001):
            count = 0
            for j in range(1, i):
                if i % j == 0:
                    count += j
            print('%d +' % j, end='')
            if i == count:
                print('%d =' % i, end=' ')


if __name__ == '__main__':
    p = Perfect()
    p.perf()
