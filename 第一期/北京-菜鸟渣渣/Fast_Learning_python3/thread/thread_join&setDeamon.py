# coding=utf-8
'''
- 场景一：小编（主）先吃完了，xiaoming(客)和xiaowang(客)还没吃完，这种场景会导致结账的人先走了，剩下两个小伙伴傻眼了。。。

- 场景二：小编（主）先吃完了，xiaoming和xiaowang还没吃饱，一起结账走人。

- 场景三：小编（主）先等xiaoming和xiaowang吃饱了，小编最后结账一起走人。

'''

# 场景一：主线程已经结束了，子线程还在跑
# 1.我们把thread1.start()和thread2.start()称为两个子线程，写在外面的代码就是主线程了。
import threading
import time

'''
def chiHuoGuo(people):
    print("%s 吃火锅的小伙伴-羊肉：%s" % (time.ctime(), people))
    time.sleep(1)
    print("%s 吃火锅的小伙伴-鱼丸：%s" % (time.ctime(), people))


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, people, name):
        '''
# 重写threading.Thread初始化内容
'''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        '''
# 重写run方法
'''
        print("开始线程: " + self.threadName)

        chiHuoGuo(self.people)  # 执行任务
        print("qq交流群：226296743")
        print("结束线程: " + self.name)


print("yoyo请小伙伴开始吃火锅：！！！")

# 创建新线程
thread1 = myThread("xiaoming", "Thread-1")
thread2 = myThread("xiaowang", "Thread-2")

# 开启线程
thread1.start()
thread2.start()

time.sleep(0.1)
print("退出主线程：吃火锅结束，结账走人")
'''
'''
场景二：主线程结束了，子线程必须也跟着结束

1.主线程中，创建了子线程thread1和thread2，并且在主线程中调用了thread.setDaemon(),这个的意思是，把主线程设置为守护线程，这时候，要是主线程执行结束了，就不管子线程是否完成,一并和主线程退出.
（敲黑板：必须在start()方法调用之前设置，如果不设置为守护线程，程序会被无限挂起。）

2.线程有一个布尔属性叫做daemon。表示线程是否是守护线程，默认取否。当程序中的线程全部是守护线程时，程序才会退出。只要还存在一个非守护线程，程序就不会退出。
主线程是非守护线程。

3.setDaemon(True)此方法里面参数设置为True才会生效

'''
'''

def chiHuoGuo(people):
    print("%s 吃火锅的小伙伴-羊肉：%s" % (time.ctime(), people))
    time.sleep(1)
    print("%s 吃火锅的小伙伴-鱼丸：%s" % (time.ctime(), people))


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, people, name):
        # 重写threading.Thread初始化内容
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        # 重写run方法
        print("开始线程: " + self.threadName)

        chiHuoGuo(self.people)  # 执行任务
        print("qq交流群：226296743")
        print("结束线程: " + self.name)


print("yoyo请小伙伴开始吃火锅：！！！")

# 创建新线程
thread1 = myThread("xiaoming", "Thread-1")
thread2 = myThread("xiaowang", "Thread-2")

# 守护线程setDaemon(True)
thread1.setDaemon(True)  # 必须在start之前
thread2.setDaemon(True)

# 开启线程
thread1.start()
thread2.start()

time.sleep(0.1)
print("退出主线程：吃火锅结束，结账走人")
'''

'''
1.如果想让主线程等待子线程结束后再运行的话，就需要用到join(),此方法是在start之后（与setDaemon相反）

2.join(timeout)此方法有个timeout参数，是线程超时时间设置。

'''


def chiHuoGuo(people):
    print("%s 吃火锅的小伙伴-羊肉：%s" % (time.ctime(), people))
    time.sleep(1)
    print("%s 吃火锅的小伙伴-鱼丸：%s" % (time.ctime(), people))


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, people, name):
        '''重写threading.Thread初始化内容'''
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        '''重写run方法'''
        print("开始线程: " + self.threadName)

        chiHuoGuo(self.people)  # 执行任务
        print("qq交流群：226296743")
        print("结束线程: " + self.name)


print("yoyo请小伙伴开始吃火锅：！！！")

# 创建新线程
thread1 = myThread("xiaoming", "Thread-1")
thread2 = myThread("xiaowang", "Thread-2")

# 开启线程
thread1.start()
thread2.start()

# 阻塞主线程，等子线程结束
thread1.join()
thread2.join()

time.sleep(0.1)
print("退出主线程：吃火锅结束，结账走人")
