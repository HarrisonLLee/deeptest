# -*- coding:utf-8 -*-
__author__ = "Heather"
class DemoClass:
    def __init__(self):
        print("初始化")

    def output(self,text):
        print(text)
    
    def output_none(self):
        print("no param")
    
if __name__ == '__main__':
    demo_obj = DemoClass()
    demo_obj.output("param")
    demo_obj.output_none()

    