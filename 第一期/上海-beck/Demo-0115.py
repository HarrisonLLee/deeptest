# -*- coding:utf-8 -*-
import sys
import support

__author__ = 'beck'

class Demo_class:
    def __init__(self):
        print("函数初始化")
    def output(self,text):
        print(text)
    def output_deom(self):
        print("我是没有参数的")

if __name__ == '__main__':
        demo_test = Demo_class()
        demo_test.output("我是测试函数!!!!@@@@")
        demo_test.output_deom()

class democlass_one:
    def __init__(self):
        print("父类函数初始化操作")
    def output(self,text):
        print(text)
    def output_one(self):
        print("父类函数的没有参数的方法")

class child_democlass(democlass_one):
    def __init__(self):
        print("子类函数继续初始化操作")
    def output_one(self):
        print("子类函数的没有参数的方法")

if __name__ == '__main__':
        demo_test_one = democlass_one()
        demo_test_one.output("继承相关函数的示例，父类打印")
        demo_test_one.output_one()

        child_test = child_democlass()
        child_test.output("TEST！！！")
        child_test.output_one()

#定义一个员工类
class Employee:
    empCount = 0
    def __init__(self,nameone,salary):
        self.nameone = nameone
        self.salary = salary
        Employee.empCount +=1
    # def dispalyCount(self):
    #     print("Total Employee %d"%Employee.empCount)
    def dispalyemployee(self):
        print("Name: %s"%self.nameone,",Salary :%s"%self.salary)

if __name__ == '__main__':
    e1 = Employee("testone",2000)
    e2 = Employee("testtwo",3000)
    e1.dispalyemployee()
    e2.dispalyemployee()
    print("Total Employee %d"%Employee.empCount)

#函数模块的导入和使用
if __name__ == '__main__':
    support.print_func("Test Python")
    print(sys.path)

    support.fib(1000)
    support.fib2(1000)

#迭代器
if __name__ == '__main__':
    test_tuple = (1,2,3,4,5,6,7,8,9)
    seq_it = iter(test_tuple)
    print("第一个元素：%s" %next(seq_it))
    print("第二个元素：%s" %next(seq_it))
    print("第三个元素：%s" %next(seq_it))

    tuple_list = iter(test_tuple)
    for element in  tuple_list:
        print(element,end=',')

    print("\nwhile & next遍历迭代器对象： ")
    while_it = iter(test_tuple)
    while True:
        try:
            print(next(while_it))
        except StopAsyncIteration:
            sys.exit()

#生产器，使用yield
def fibonacci(n):
    a,b,count = 0,1,0
    while True:
        if count > n:
            return
        yield a
        a,b =  b,a+b
        count = count + 1

if __name__ == '__main__':
    f1 = fibonacci(10)
    while True:
        try:
            print(next(f1),end=' ')
        except StopAsyncIteration:
            sys.exit(0)

def yield_test(n):
    for i in range(n):
        yield  call(i)
        print("test for i=",i)
    print(u"yield_test 运行结束！！！")

def call(i):
    return i*2

if __name__ == '__main__':
    for j in  yield_test(5):
        print(j,'test')

def byLineReader(file_path):
    try:
        f = open(file_path,"r")
        #sizehint = 104857600 #读取100M
        sizehint = 1 #读取1个字节
        line = f.readline(sizehint)
        while line:
            yield line
            line = f.readline(sizehint)
    finally:
         f.close()

if __name__ == '__main__':
    file_path='test.txt'
    for line in byLineReader(file_path):
        print(line)








