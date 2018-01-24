#coding:utf-8
'''
enumerate 函数的说明：
函数原型：enumerate(sequence,[start=0])
功能：将可循环序列sequence以start开始分别列表序列数据和数据下标
即对一个可遍历的数据对象(列表，元祖，字符串),enumerate 会将该数据对象组合为一个索引序列，同时列出数据和数据下标
'''
#enumerate()使用：
#如果对一个列表，既要遍历索引又要遍历元素时，可以这样写：
list1 = ['这','是','一个','测试']

for i in range(len(list1)):
    print i,list1[i]

print ('*'*50)
#上述方法有些累赘，利用enumerate()或更加直接
list1 = ['这','是','一个','测试']

for index,item in enumerate(list1):
    print index,item

print ('*'*50)
#enumerate 还可以接受第二个参数，用于指定索引起始值,如：
list1 = ['这','是','一个','测试']

for index,item in enumerate(list1,1):
    print index,item

