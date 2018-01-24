# _*_ coding : utf-8 _*_
__author__ = "Jason"
'''
经典案例：99乘法表
'''
if __name__ == "__main__":
    print(u"99乘法表：")
    for i in range(1,10):
        for j in range(i,10):
            print(u"%d*%d = %2d"%(i,j,i*j),end="    ")
        print("")
    print('-'*50)
    #打印正常版的乘法表
    print(u"正常版本的99乘法表：")
    for i in range(1,10):
        for j in range(1,i+1):
            print(u"%d*%d = %2d"%(j,i,i*j),end="    ")
        print()
    print('-'*50)
    #for、while均使用
    m = 1
    while m <= 9:
        if m == 1:
            print(u"%d*%d = %2d"%(1,m,m),end='    ')
        else:
            for n in range(1,m):
                print(u"%d*%d = %2d"%(n,m,m*n),end='    ')
        m = m + 1
        print()