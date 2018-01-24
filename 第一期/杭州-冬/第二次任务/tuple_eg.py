#coding:--utf-8--
#本文是关于元组

#tuple为不可变对象(如dict中的key),其元素不可修改删除
#内置函数有 len() max()--返回最大值 min() tuple()--list传tuple
tuple_1=(1,"a",2,"b",3,"c")
print(len(tuple_1))
#不能在不同类型间比较
#print(max(tuple_1))

list_1=[1,"a",2,"b"]
tuple_2=tuple(list_1)
print(tuple_2)

#tuple的合并 + 与复制 *
tuple_3=tuple_1+tuple_2
print(tuple_3)
tuple_4=tuple_2*2
print(tuple_4)

#tuple作为序列也可用切片的方式访问
tuple_part=tuple_3[1:]
print(tuple_part)

#判断tuple是否有某个元素
print(8 in tuple_1)

#遍历tuple中的元素
for i in tuple_1:
    print(i)