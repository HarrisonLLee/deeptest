#!/usr/bin/env  python
# -*- coding: UTF-8 -*-


import time
import datetime

class Grand:
    '''根据分数输出对应等级'''
    '''输出指定格式的时间'''
    '''输入一行字符串，并统计其中英文字母、空格、数字以及其他格式的字符个数'''
    def __init__(self, score, stri=[]):
        self.score = score
        self.stri = stri

    def grand(self):
        if self.score >= 90:
            print("%d"%self.score, "属于", 'A')
        elif 60 <= self.score < 89:
            print("%d" % self.score, "属于", 'B')
        elif self.score < 60:
            print("%d" % self.score, "属于", 'C')

    def count(self):
        length = len(self.stri)
        print(self.stri)
        ying, shu, kong, qita = 0
        for i in range(0, length):
            if 'a' <= self.stri[i] <= 'z' or 'A' <= self.stri[i] <= 'Z':
                ying += 1
            elif '0' <= self.stri[i] <='9':
                shu += 1
            elif self.stri[i] == ' ':
                kong += 1
            else:
                qita += 1
            # print(i)
        print("英文字母的个数为%d" % ying)
        print("数字的个数为%d" % shu)
        print("空格个数为%d" % kong)
        print("其他字符的个数为%d" % qita)


if __name__ == '__main__':

    g = Grand(int(input("请输入分数：")), input("输入一串字符串: "))
    g.grand()
    g.count()

    print(time.localtime())
    print(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()))
    print(time.asctime())
    print(time.time())

    print(datetime.date(1941, 1, 5))
    print(datetime.date.today().strftime('%d-%m-%Y'))
    print(datetime.date.today())
