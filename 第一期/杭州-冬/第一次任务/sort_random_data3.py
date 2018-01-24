#coding:--utf-8--
__author__="冬"
#生成10-100的100个数字并排序
#用冒泡排序：得出每次较小的数来实现排序（升序）
#整体结构与sort_random_data2相同,区别在以 较小的数实现排序

import random
class Msort:
    #随机生成100个10-1000的随机数,返回排序后的结果
    #start,end为限制随机数的上下限的范围
    #count为生成的随机数的个数

    def __init__(self,start,end,count):
        self.start=start
        self.end=end
        self.count=count
        self.random_data=[]

    #生成数据
    def __generate(self):
        #注意双_开头为private方法/变量,不能在class外直接调用
        self.random_data=random.sample(range(self.start,self.end),self.count)

    #对生成数据实现排序
    def sort(self):
        #通过sel去调用其它定义的方法
        self.__generate()

        #计算存放数据列表的长度
        n=len(self.random_data)
        
        #用冒泡排序,得出每次比较较小的的数来实现
        #定义x,用于计算循环开始的地方
        x=0
        while x<n-2:
            for i in range(x+1,n):
                if self.random_data[x]>self.random_data[i]:
                    self.random_data[x],self.random_data[i]=self.random_data[i],self.random_data[x]
            x=x+1
        return self.random_data
    
#使用一个例子试一试
if __name__=="__main__":    #注意是2个=
    sorted_data=Msort(10,1000,100)
    
    #排序
    data=sorted_data.sort()

    #打印
    print(data)

