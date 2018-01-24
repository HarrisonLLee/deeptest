# -*- coding:utf-8 -*-
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('Mike',30)

person('Bob',15,city='Beijing')
person('Alice',25,city='Hangzhou',gender='M')

extra = {'city':'Beijing','job':'Engineer'}
person('Jack',30,city=extra['city'],job=extra['job'])
person('Jack',30,**extra)