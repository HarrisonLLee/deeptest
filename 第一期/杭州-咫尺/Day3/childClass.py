#-*- coding:utf-8 -*-
__author__ = "Heather"
class DemoClass:
    def __init__(self):
        print("初始化")
    def output(self,text):
        print(text)
    def output_none(self):
        print("no param")

class ChildDemoClass(DemoClass):
    def __init__(self):
        print("我是子类")
    def output_none(self):
        print("我是子类不能传参的方法")

if __name__ == '__main__':
    demo_obj = DemoClass()
    demo_obj.output("我是参数")
    demo_obj.output_none()

    print("-----")
    child_demo_obj = ChildDemoClass()
    child_demo_obj.output("child")
    child_demo_obj.output_none()