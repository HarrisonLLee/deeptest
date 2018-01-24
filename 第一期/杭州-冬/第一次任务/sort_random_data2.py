#coding:--utf-8--
#用冒泡排序,得出每次最大的数来实现排序
#对具体冒泡的写法进行了优化,使之更简洁
import random
class Mysort:
    #随机生成100个10-1000的随机数,返回排序后的结果
    #start,end为限制随机数的上下限的范围
    #count为生成的随机数的个数
    def __init__(self,start,end,count):
        self.start=start
        self.end=end
        self.count=count
        self.random_data=[]

    #生成数据
    def __generate(self):#双_开头为private方法/变量,不能在类体外直接调用
        self.random_data=random.sample(range(self.start,self.end),self.count)

    #实现排序
    def sort(self):
        self.__generate()
        #计算存放数据的列表长度
        n=len(self.random_data)

        #用冒泡对列表数据进行排序,得出每次较大的数来实现排序
        while n>=1:
            for i in range(n-1):
                if self.random_data[i]<self.random_data[i+1]:
                    self.random_data[i],self.random_data[i+1]=self.random_data[i+1],self.random_data[i]
            n=n-1
        return self.random_data

#使用示例
if __name__=="__main__":
    sorted_data=Mysort(10,1000,10)

    #排序
    data=sorted_data.sort()

    #打印排序后的结果,逐个打印出来
    for e in data:
        print(e)




