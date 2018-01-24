# -*- coding:utf-8 -*-

__author__ = "nicole"

import sys

class calc:
     # 初始化
     def __init__(self,a,b):
         self.a = int(a)
         self.b =int(b)
         
     # 加法
     def add(self):
         return self.a + self.b 
         

     # 减法
     def sub(self):
         return self.a - self.b
          


     # 乘法
     def mul(self):
        return self.a * self.b
         


     # 除法
     def div(self):
         return self.a / self.b
         

if __name__ == "__main__":
    print 'please input two integar:'

    a = int(input("a:"))
    b =int(input("b:"))
    y = calc(a,b)
    print y.add()
    print y.sub()
    print y.mul()
    print y.div()