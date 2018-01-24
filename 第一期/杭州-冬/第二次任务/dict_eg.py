#--coding:--utf-8--
#关于dict
##dict用键-值对(key-vaue)存放元素对象,通过key找到对应value,速度比较快,好比查字典
##其中key不能重复,可以是tuple str 数字,不能是list
##value 可重复,可以是任何定义的py对象

if __name__=="__main__":
    dict_1={1:"a",2:"b"}
    #内置函数:len() str()
    ##len():dict长度 即key总数
    print(len(dict_1))
    print(dict_1)
    ##str():相当于在dict前后加"",以字符串方式输出dic
    str_dict=str(dict_1)
    print(dict_1)
    print(type(str_dict))
    #dict_1[1]="a"
    #print(dict_1)

    #dict增删改
    ##通过key新增数据
    dict_1[3]="c"
    print(dict_1)
    ##通过key删除/更改数据
    dict_1.pop(3)
    del dict_1[1]
    print(dict_1)
    dict_1[2]="bb"
    print(dict_1)

    ##查
    ##get(key,d=Noe):返回key对应的value key不存在返回None或指定值
    print(dict_1.get(3,-1))
    ## in 判断key是否存在
    print(3 in dict_1)
    ## items 以tuple的形式返回 多用于for循环
    print(type(dict_1.items()))
    for i,j in dict_1.items():
        print("%s:%s" %(i,j))

    ##keys() values()，以list形式返回所有的key value
    print(type(dict_1.keys()))
    print(dict_1.values())