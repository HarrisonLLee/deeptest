# _*_ coding : utf-8 _*_
__author__ = "Jason"
'''
while 循环
Python中while语句的一般形式：
while 判断条件：
    语句
同样需要注意冒号和缩进。另外，在Python中没有do..while循环。
'''
#经典案例：计算1-100的总和
sum_100 = 0
counter = 1
while counter <= 100:
    sum_100 = sum_100 + counter
    counter = counter + 1
print(sum_100)#结果为5050
#计算奇数和
sum_100 = 0
counter = 1
while counter <= 100:
    sum_100 =sum_100 +counter
    counter = counter +2
print("100以内的奇数和是：%d"%sum_100)#结果为2500
'''
while后面也可以接else语句
'''
print('-'*50)
counter = 0
while counter <= 5:
    print("counter值为%d，小于等于5。"%counter)
    counter = counter + 1
else:
    print("counter值为%s，大于5。"%counter)
print('-'*50)
'''
while也可以接单个条件，此时相当于if
'''
nation = ["China","America","German"]
for x in range(len(nation)):
    while nation[x] == "China":
        print("我是中国人！")
        x = x + 1#如果不加这一行进行控制，就会无限循环下去
print('-'*50)