#-*- coding:utf-8 -*-
__author__ = u"Heather"
if __name__ == '__main__':
    
    print(u"set操作示例")

    set_source = set([1, 1, 2, 3, 4, 5, 6, 7])
    set_demo = set([1, 1, 2, 3, 4, 5, 6, 7])

    print(u"原始数据: ",end="")
    print(set_demo)

    #add
    print("add:",end="")
    set_demo.add(9)
    set_demo.add(1)
    print(set_demo)

    #remove
    print("remove:",end="")
    set_demo.remove(9)
    print(set_demo)

    #update
    list_demo = ["a","b","c"]
    print("update:",end="")
    set_demo.update(list_demo)
    print(set_demo)