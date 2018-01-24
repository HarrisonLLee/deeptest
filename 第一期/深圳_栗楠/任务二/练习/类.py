# -*- coding:utf-8 -*-
__author__ = u"linan"

class DemoClass:
    def __init__(self):
        print('初始化')

    def output(self,text):
        #输出text到console
        print(text)

    def output_none(self):
        #不带参数的方法
        print("我不能传入参数")

        if __name__ == "__main__":
    #创建一个类对象
    demo_obj = DemoClass()

    #调用output
    demo_obj.output("参数")
    #调用output_none
    demo_obj.output_none



#定义一个基本类
class DemoClass:
    def __init__(self):
        print("初始化")

    def output(self,text):
        #输出text到console
        print(text)

    def output_none(self):
        #不带参数的方法
        print("我不能传入参数")

#集成DemoClass
class ChildDemoClass(DemoClass):
    def __init__(self):
        print("子类")

    #重写output_none
    def output_none(self):
        
        print("我是子类不能传参的方法")

if __name__ == "__mina__":
    #创建一个类的对象
    demo_obj = DemoClass()

    #调用output
    demo_obj.output("我是参数")

    #调用output_none
    demo_obj.output_none()
    print("--------------------------------")
    
    #创建子类的对象
    child_demo_obj = ChildDemoClass()

    #调用output调用的是父类的方法
    child_demo_obj.optput("我是参数")

    #调用output_none 调用的是自己的方法，即重写后的方法
    child_demo_obj.output_none()
