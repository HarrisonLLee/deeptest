# _*_coding : utf-8 _*_
__author__ = "Jason"
'''
基本概念：
1.类（class）
    简单理解为具有相同的属性和方法的对象的集合。
    定义了该集合中每个对象共有的属性和方法。
    对象是类的实例。
2.类变量
    类变量在整个实例化的对象中公用。
    定义在类中，且在函数外。类变量通常不作为实例变量使用。
3.数据成员
    类变量或实例变量，用于处理类及其实例的数据。
4.方法重写
    如果从父类继承的方法满足不了应用，对该方法进行重新实现，
    这个过程叫override（方法覆盖），也称为方法重写。
5.实例变量
    定义在方法中的变量，只作用于当前实例的类。
6.继承
    即一个派生类（derived class）继承基类（base class）的字段和方法。
    继承也允许把一个派生类的对象作为一个基类对象对待。
    例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
7.实例化
    创建一个类的实例，类的具体对象。

类定义格式：
class 类名:
    def __init__(self):
        #初始化
    def func_1(self.param):
        #方法1
    def func_2(self.param):
        #方法2
    #一个类可以有多个方法。
'''
class classExample:
    def __init__(self):
        print("初始化")

    def output(self):
        print("我是父类output")

    def output_none(self):
        print("我是父类output_none")

#类的继承
class childClass(classExample):
    def __init__(self):
        print("我是子类")

    #重写output_none方法
    def output_none(self):
        print("我是子类的output_none")

if __name__ == "__main__":
    #创建一个类的实例对象
    classDemo = classExample()#进行初始化，打印出“初始化”

    #调用方法
    classDemo.output()#打印出“我是父类output”
    classDemo.output_none()#打印出“我是父类output_none”

    #创建一个子类的实例对象
    childClassDemo = childClass()#进行初始化，打印出“我是子类”

    #调用子类方法
    childClassDemo.output_none()#打印出“我是子类的output_none”

    #调用父类方法
    childClassDemo.output()#打印出“我是父类的output”

