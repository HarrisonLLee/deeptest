#!/usr/bin/env  python
# -*- coding: UTF-8 -*-
class Sample5:
    '''输入三个数字，按从各大到小的书序排列输出'''
    def sor(self):
        l=[]
        for i in range(3):
            x=int(input())
            l.append(x)

        l.sort()
        return l

if __name__=='__main__':
    print("请输入三个数字：")
    sam=Sample5()
    mySam=sam.sor()

    for i in mySam:
        print(i)
        i+=1