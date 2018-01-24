#coding:utf-8
'''
1.set 顾名思义，就是个集合，集合的元素是唯一的，无序的，一个{}里面放一些元素就构成了一个集合，set
里面可以是多种的数据类型,但不能是列表，集合，字典，可以是元祖。
2.集合石一个无序不重复的元素的值；
3.大括号或set()函数可以用来创建集合，注意：想要创建空集合，你必须使用set()而不是{}。{}用于创建空字典：
'''
#add(增加元素)
name = set(['Tom','Lucy','Ben'])
name.add('Juny')
print name

#clear(清空所有元素)
name = set(['Tom','Lucy','Ben'])
name.clear()
print(name)

#copy(拷贝set集合)
name = set(['Tom','Lucy','Ben'])
new_name = name.copy()
print new_name

#difference(返回两个或多个集合中不同的元素，并生成新的集合)
A = set([2,3,4,5])
B = set([3,4])
C = set([2])
n = A.difference(B,C)  #返回A集合里面，在B和C集合中没有的元素，并生成新的集合
print n

#difference_update(删除A集合里面，在B集合中存在的元素)
A = set([2,3,4,5])
B = set([4,5])
A.difference_update(B)
print A


#discard(移除元素)
n = set([2,3,4])
n.discard(3)
print (n)

#intersection(取交集，并生成新的集合)
n1 = set([2,3,4,5])
n2 = set([4,5,6,7])
n = n1.intersection(n2)
print n


#intersection_update(取交集，修改原来的集合)
n1 = set([2,3,4,5])
n2 = set([4,5,6,7])
n1.intersection_update(n2)
print n1


#pop(随机移除一个元素)
n = set([2,3,4,5])
n1 = n.pop()
print (n,n1)

#remove(移除指定元素)
n = set([2,3,4,5])
n.remove(2)
print n

#symmetric_difference(取交集，并生成新的集合)
A = set([2,3,4,5])
B = set([4,5,6,7])
print A.symmetric_difference(B)


#symmetric_difference_update(取交集，改变原来的集合)
A = set([2,3,4,5])
B = set([4,5,6,7])
A.symmetric_difference_update(B)
print A

#union(取并集，并生成新的集合)
A = set([2,3,4,5])
B = set([4,5,6,7])
print A.union(B)

#update(取并集，改变原来的集合)
A = set([2,3,4,5])
B = set([4,5,6,7])
A.update(B)
print A
