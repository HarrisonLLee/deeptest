# -*- coding:utf-8 -*-

if __name__ == '__main__':
    d1 = {'id':1,'sku':'apple','city':'beijing'}
    d2 = {"id":2,'sku':'grape','city':'xiamen'}
    print(len(d1))
    print(d2)

    str_d1=str(d1)
    print(type(str_d1))
    print(str_d1)

    d2.clear()
    print(d2)