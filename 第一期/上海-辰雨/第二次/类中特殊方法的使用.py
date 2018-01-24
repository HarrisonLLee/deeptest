#!/usr/bin/env python
# encoding: utf-8
'''
__init__ 方法负责对象的初始化，系统执行该方法前，其实该对象已经存在了
'''
class A(object):
	def __init__(self):
		print ('__init__')
		super(A,self).__init__()

	def __new__(cls):
		print ('__new__')
		return super(A,cls).__new__(cls)

	def __call__(self):
		print ('__call__')

A()
#从输出结果来看，__new__方法先被调用，返回一个实例对象，接着__init__被调用。

class A(object):
	def __init__(self):
		print ('__init__')
		print (self)
		super(A, self).__init__()

	def __new__(cls):
		print ('__new__')
		self = super(A, cls).__new__(cls)
		print (self)
		return self

A()


#从输出结果看来，__new__方法的返回值就是类的实例对象，这个实例对象会传递给__init__方法中定义的self参数，以便实例对象可以被正确的初始化
#如果__new__方法不返回值(或者说返回None)那么__init__将不会得到调用。

#__call__方法：
#如果在类中实现了__call__方法，那么实例对象也将成为一个可调用的对象
class Counter(object):
	def __init__(self,func):
		self.func = func
		self.count = 0

	def __call__(self,*args,**kwargs):
		self.count += 1
		return self.func(*args,**kwargs)


@Counter
def foo():
	pass

for i in range(10):
	foo()

print (foo.count)



