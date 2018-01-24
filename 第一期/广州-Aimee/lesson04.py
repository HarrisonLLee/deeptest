#coding = utf-8
__author__ = 'Aimee'

#函数
# def sum(a,b):
#     c = a+b
#     return c
#
#
# if __name__ == "__main__":
#     c =(1,3)
#     print(c)



#九九乘法表

def muli():
    data = []
    for i in range(1,10):
        line = []
        for j in range(i,10):
            line.append("%d *%d = %d" %(i,j,i*j))
        data.append(line)

    return data


if __name__ =="__main__":
    data = muli()
    for d in data:
        print(d)



