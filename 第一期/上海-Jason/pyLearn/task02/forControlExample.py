# _*_ coding : utf-8 _*_
__author__ = "Jason"
'''
for 语句
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
for循环的一般格式如下：
for <variable> in <sequence>:
    <code_block>
else:
    <code_block>
'''
#循环列表
a = ["至尊宝","至尊玉","秦汉","秦祥林","臭猴子","齐天大圣"]
for x in a:
    print("星爷在《大话西游》里自称是%s"%x)
print('-'*50)
#如果是循环数字范围，可以用range，注意，range的区间也是左闭右开
for x in range(3,8):
    print(x)#分别打印3,4,5,6,7
print('-'*50)
#计算10000内有多少能被7整除
count = 0
for x in range(1,10000,7):
    count = count+1
print(count)#结果为1429
print('-'*50)
#也可以用range遍历列表，range还可以用来创建一个列表
for x in range(len(a)):
    print("大话西游星爷是%s"%a[x])#打印结果和第一个例子是一样的。
    print(list(range(len(a))))#结果为[0, 1, 2, 3, 4, 5]
print('-'*50)
#遍历元组
tuple_test = ("紫霞","青霞","白晶晶")
for x in tuple_test:
    print("至尊宝最爱的人是%s吗？"%x)
print('-'*50)
#遍历字典
dict_test = {"key1":"value1","key2":"value2"}
for (key,value) in dict_test.items():
    print("%s:%s"%(key,value))
print('-'*50)
for key in dict_test:
    print("%s:%s"%(key,dict_test[key]))