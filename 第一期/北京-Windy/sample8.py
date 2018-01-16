#!/usr/bin/env  python
#-*- coding: UTF-8 -*-
#
# class Sample8:
#     '''实现x*y乘法表'''
#
#     def __init__(self,cow,col):
#         self.cow = cow
#         self.col = col
#
#     def mu(self):
#         # self.col, self.cow=int(input())
#         for self.cow in range(self.col,self.cow):
#             print
#             for self.col in range(self.cow,self.cow+1):
#                 # s=self.cow*self.col
#                 return '%d*%d=%d' % self.cow,self.col,self.cow*self.col
#
#
# if __name__=='__main__':
#
#     print Sample8.mu()


for i in range(1,10):
    print
    for j in range(1,i+1):
        print '%d*%d=%d' % (i,j,i*j),

