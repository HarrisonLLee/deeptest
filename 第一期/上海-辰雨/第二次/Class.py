#!/usr/bin/env python
# encoding: utf-8
'''
几个基本概念：
类变量：类变量在整个实例化的对象中公用，定义在类中且在函数体外。
数据成员：类变量或实例变量，用于处理类以及实例的数据；
方法重写：如果从父类继承的方法满足不了应用，对该方法进行重新实现，这个过程叫做override(方法覆盖)，也成为方法重写；
实例变量：定义在方法中的变量，只作用于当前的实例；
继承：子类可以调用父类中的方法；
实例化:创建一个类的实例，即类的具体对象；
'''
class DemoClass(object):
	def __init__(self):
		print ('实例化对象时，执行该方法')

	def output(self,text):
		#输出text 到console
		print (text)

	def output_none(self):
		#不带参数的方法：
		print ('不带传入参数')

#继承DemoClass
class ChildDemoClass(DemoClass):
	def __init__(self):
		print ('我是子类')

	#重写output_none
	def output_none(self):
		print ('我是子类不能传参的方法')


#创建一个类对象：
demo_obj = DemoClass()

#调用output
demo_obj.output('我是参数')

#调用output_none
demo_obj.output_none()

print ('************************')
#创建子类的对象
child_demo_obj = ChildDemoClass()

#调用output,调用的是父类的方法，因为子类没有该方法：
child_demo_obj.output('子类调用父类的方法体')

#调用output_none，调用的是自己的方法，即重写的方法
child_demo_obj.output_none()
