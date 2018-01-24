#ccoding:--utf-8--
#关于字符串
##py3字符串都是Unicode编码


if __name__=="__main__":
    yuan=()

#字符串的连接和切割
## join 用指定字符串将元组、列表中的元素连接成一个新的字符串
tup_1=("1","a","2","b")

temp1="<".join(tup_1)
temp1_1=''.join(tup_1)
print(temp1)
print(temp1_1)  #用空字符串连接
##split 以指定的分隔符来截取字符串,返回一个list对象
temp2=temp1.split("<")
print(temp2)

#计算str长度：len()--也用于元组 列表

#字符串查找和替换
#find 无则返-1. index同find 无则抛出异常.rfind rindex为从右到左查找
str_1="you are fine" 
print(str_1.find("in",1,10))
#replace 将指定子串替换为目标字符串,可指定次数.必须是子串
str_2=str_1.replace("you are","I am")
print(str_2)

#去除字符串空格 lstrip rstrip strip

#判断str类型
str_3=str_1.replace("you are ","123youarefine")
print(str_3)
print(str_3.isalnum())