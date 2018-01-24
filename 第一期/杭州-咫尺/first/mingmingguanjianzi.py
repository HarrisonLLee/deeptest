# -*- coding:utf-8 -*-
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)

person('Jack',30,city='Beijing',addr='Chaoyang',zipcode=123456)

def person1(name,age,*,city,job):
    print(name,age,city,job)

person1('Jack',30,city='Beijing',job='Chaoyang')