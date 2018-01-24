# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Description :
   Author :       Young
   Change Activity: 2018/1/17:
-------------------------------------------------
"""
__author__ = 'Young'
'''
类(Class)
简单理解为具有相同的属性和方法的对象的集合。定义了该集合中每个对象共有的属性和方法，对象是类的实例。

类变量
类变量在整个实例化的对象中公用。定义在类中且在函数体外。（少用）

数据成员
类变量或实例变量，用于处理类及其实例的数据

方法重写

如果从父类继承的方法满足不了应用，对该方法进行重新实现，这个过程叫override（方法覆盖），也称为方法重写。

实例变量
定义在方法中的变量，只作用于当前实例。

继承
想想你跟你爸的关系就懂什么是继承了。

实例化
创建一个类的实例，即类的具体对象

'''


#定义一个简单的类，并创建该类的对象
class DemoClass:
    def __init__(self):
        print("初始化")

    def output(self, text):
        # 输出text到console
        print(text)

    def output_none(self):
        # 不带参数的方法
        print("我不能传入参数")


#继承的特性
class ChildDemoClass(DemoClass):
    def __init__(self):
        DemoClass.__init__(self)
        print("我是子类")

        # 重写output_none

    def output_none(self):
        print("我是子类不能传参的方法")

if __name__ == "__main__":
    # 创建一个类对象
    demo_obj = DemoClass()

    # 调用output
    demo_obj.output("我是参数")

    # 调用output_none
    demo_obj.output_none()
    print("----------------继承 - 对基础示例扩展--------------------")
    # 创建子类的对象
    child_demo_obj = ChildDemoClass()

    # 调用output, 调用的是父类的方法
    child_demo_obj.output("我是参数")

    # 调用output_none, 调用的是自己的方法，即重写后的方法
    child_demo_obj.output_none()

'''

类是可以继承的
子类可以重写父类的方法
子类可以直接调用父类的方法
在python中类通过class这个关键字来定义
类可以看作资源的集合：变量、方法
类要实例化成对象，通过对象来调用其方法

'''