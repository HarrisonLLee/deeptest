#coding:utf-8
#自定义异常：
class Getoutofloop(Exception):
    print ('hello python')

try:
    for i in range(5):
        for j in range(5):
            if i == j == 2:
                raise Getoutofloop()  #raise　引发异常，后面的语句不再执行，然后跳转到except部分
            else:
                print i,'-------',j
except Getoutofloop:
    print ('测试结束')


#封装为函数：
def test():
    for i in range(5):
        for j in range(5):
            if i == j == 2:
                return '测试'   #return 后面的语句不再执行
            else:
                print i,'----',j

print test()


#for...else...跳出指定循坏层
for i in range(5):
    for j in range(5):
        for k in range(5):
            if i == j == k == 3:
                break
            else:
                print i,'---',j,'---',k
        else:
            continue
        break
    else:
        continue
    break


#案例用户名登陆三次不成功将被锁定账户：
for i in range (1,4):
    name = raw_input('please enter you name:')
    with open(r'C:\Users\Administrator\Desktop\python\lockname.txt') as f:
        name_list = f.read()
        if name in name_list:
            print ('the username is locked,please enter another name:')
            break  #外层循环,若执行时直接跳出整个程序：
        else:
            with open(r'C:\Users\Administrator\Desktop\python\username.txt') as fp:
                read_line = fp.readlines()   #这样的读取出来的是一个read_line 列表
            for u in read_line:
                (username,password)=u.strip().split(' ')
                if username == name:
                    for k in range(1,4):
                        pwd = raw_input('please enter your password:')
                        if password == pwd:
                            print ('congratulation ! welcome to login system!')
                            break
                        else:
                            continue
                    else:
                        print ("you have input three time, so can't input the password ")
                    break
            else:
                print ('the username need to register')
            break  #如果break是从for循环跳出来的话，则for...else也是不再执行的

