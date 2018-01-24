#--coding:utf-8--
#关于list

##相比tuple,list元素是可以修改的,它有许多tuple没有的方法
###如：添加--append() 删除--pop(),remove() 插入--insert() 替换--list[i]=obj
##与tuple也有着相似的一面
###如：内置函数(len() max() min() list()--tuple转list)
###如：切片--访问其中元素lisy[i],用for遍历元素 扩展--extend(seq)
##list为有序序列 可排序--sort()

if __name__=="__main__":
    list_1=["rr","ss",11,22]
    #内置函数
    print(len(list_1))
    ##不同类型间不能比较
    #print(max(list_1))
    ##list():针对tuple转list,tuple()反之
    tuple_1=(1,"a",2,"b",3,"c")
    list_2=list(tuple_1)

    #区别于tuple的增 删 改 查
    ##append(obj) 在list末尾增加 一个 元素对象
    list_3=list_1.append(33)
    print(list_1)
    ##pop([i])默认删除最后一个元素并返回该元素,可指定i
    list_4=list_1.pop(-2)
    print(list_4)
    ##remove():删除第一个匹配到的元素
    list_2.remove("a")
    print(list_2)
    ##用切片方式访问 替换元素
    print(list_2[1:])
    list_2[2]='bb'
    print(list_2)

    #list为有序序列 可排序sort()
    list_num=[33,77,11,55]
    list_num.sort()
    print(list_num)
    #扩展：可在list末尾加一个序列
    list_num.extend(tuple_1)
    print(list_num)

    ##复制--list.copy(),清空--list.clear()

    #for循环能遍历序列中的元素 包括tuple list dict等
    for i in list_num:
        print(i)