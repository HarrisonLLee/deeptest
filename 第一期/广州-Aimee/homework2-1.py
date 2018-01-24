#coding = utf-8

__author__ = 'Aimee'

y = [1,4,2,9,45,36,27]
y.sort()
print(y)


import random
#导入random package Python分为自带和外部包，如果引入外部包需要先pip安装，内部的直接引用

class Mysort:

    # 生成随机数，返回排序后的结果
    # start,end为限制随机数生成的范围
    # count为生成的随机数个数
    def __init__(self,start,end,count):

        self.start = start
        self.end = end
        self.count = count
        self.random_data = []

    #生成数据
    def generator(self):

        for i in range(0,self.count):
            self.random_data.append(random.randint(self.start,self.end))

        return self.random_data


if __name__ == "__main__":
    #数据排序 sort
    data = Mysort(10,1000,100)
    y = data.generator()
    y.sort()
    print(y)
