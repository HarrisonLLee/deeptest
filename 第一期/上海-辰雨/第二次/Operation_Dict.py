#coding:utf-8
'''字典的基本操作'''
#1.为字典增加一次：
# dictName[Key]=value
students = {'203-2012-045':'John','203-2012-037':'Peter'}
students['202-2011-121']='Susan'
print students

#2.访问字典中的值
#dictName[key]返回键key对应值value
print students['202-2011-121']

#3.删除字典中的一项：
#del dictName[key]
del students['202-2011-121']
print students


#4.字典的遍历
for key in students:
    print (key+':'+str(students[key]))

#字典遍历的key\value
#遍历字典的键key
for key in students.keys():
    print key

#遍历字典的值value
for value in students.values():
    print value

#遍历字典的项
for item in students.items():
    print item

#遍历字典的key-value值：
for item,value in students.items():
    print (item,value)

#字典的标准操作符：
d1 = {'red':'41','blue':'3'}
d2 = {'blue':'3','red':'41'}
print d1 == d2
print d1 != d2

#判断一个键是否在字典中：
#in 或者not in
print '203-2012-045' in students
print '203-2015-045' in students

students = {'203-2012-045':'John','203-2012-037':'Peter'}
#keys：tuple,返回一个包含自带你所有key的列表
print tuple(students.keys())

#values:tuple 返回一个包含字典所有value的列表
print tuple(students.values())

#Items():tuple 返回一个包含所有键值的列表
print tuple(students.items())


