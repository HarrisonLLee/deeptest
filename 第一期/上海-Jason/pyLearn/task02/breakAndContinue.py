# _*_ coding : utf-8 _*_
__author__ = "Jason"
'''
break和continue语句及循环中的else子句

break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。

continue语句被 用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
'''
#for语句的break和continue

#break
for counter in range(0,10):
    print("counter值为%d"%counter)
    if counter == 1:
        print("测试break中断if语句")
        print("counter值为%d"%counter)
        print("break中断前")#可打印
        break
        print("break中断后")#不打印，且counter值最大为1，即循环到1时就终止循环
    print()
print('-'*50)
#continue
for i in range(0,3):
    print("测试continue跳出if语句")
    print("i值为%d"%i)
    print("continue跳出前")#可打印
    continue
    print("continue跳出后")#不打印
print('-'*50)

#while语句的break和continue

#break
i = 0
while i <= 3:
    print("i值为%d"%i)
    if i > 1:
        print("break前")
        break
        print("break后")#i大于1后不循环
    i = i +1
print('-'*50)
#continue
i = 0
while i <= 3:
    print("i值为%d"%i)
    i = i + 1
    if i > 1:
        print("continue前")
        continue
        print("continue后")#大于1后循环继续，不打印
    #i = i + 1  如果自增放在这里，会无限循环