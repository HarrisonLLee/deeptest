__author__='棒棒糖'
import random
#随机生成1-1000之间无序序列整数数据
def data():
    random_data=[]
    for i in range(0,10):
        random_data.append(random.randint(1,1000))
    return random_data
#插入排序(把小的数字不断往前移)
def insert_sort(data_list):
    #序列长度：
    lenght=len(data_list)
    for i in range(1,lenght):
        key=data_list[i]
        j=i-1
        while j >=0:
        #比较，进行插入排序
            if data_list[j]>key:
                data_list[j+1]=data_list[j]
                data_list[j]=key
            j=j-1
    return data_list
if __name__=='__main__':
    print('棒棒糖碰一个')
    #生成随机无序数据
    random_data=data()
    print(random_data)
    #插入排序
    sorted_data=insert_sort(random_data)
    print(sorted_data)
