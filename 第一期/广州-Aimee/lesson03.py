#coding = utf-8


__author__ = 'Aimee'

#循环控制

print('range for 循环：')

for i in range(5):
    print(i,end=',')

print('\n')  #换行

#指定范围生成系列进行遍历

for i in range(0,10,2):
    print(i,end=',')


#嵌套
# 一次外循环后内循环，然后再继续
print('九九乘法表：')

for i in range(1,10):
    for j in range(i,10):
        print("%d * %d =%d" %(i,j,i*j),end=" ")

    print("\n")


print("计算0-100之间所有偶数和")


n = 100
index = 0
sum = 0
while index <= n:
    sum =sum +index
    index = index +2

print("0-100间偶数和= %d" %sum)


n = 100
sum = 0
counter =1
while counter <= n:
    sum = sum + counter
    counter +=1    #    counter每次加1


print("1-100之间所有数之和：%d" %sum)


#while 和 for综合使用   %d 整型格式化

print("九九乘法表：")

n = 1
while n <=9:
    for m in range(n,10):
        print("%d * %d = %d" %(n,m,n*m),end="  ")
    print("\n")
    n = n +1
