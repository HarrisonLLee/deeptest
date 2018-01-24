# coding=utf-8

import threading
import time

'''
场景一：小编（主）先吃完了，xiaoming(客)和xiaowang(客)还没吃完，这种场景会导致结账的人先走了，剩下两个小伙伴傻眼了。。

场景二：小编（主）先吃完了，xiaoming和xiaowang还没吃饱，一起结账走人。


场景三：小编（主）先等xiaoming和xiaowang吃饱了，小编最后结账一起走人。
'''


def chiHuoGuo(people):
    print("%s 吃火锅-羊肉A %s" % (time.ctime(), people))
    time.sleep(1)
    print("%s 吃火锅-鱼丸B %s" % (time.ctime(), people))


class myThread(threading.Thread):
    def __init__(self, people, name):
        threading.Thread.__init__(self)
        self.threadName = name
        self.people = people

    def run(self):
        print("开始线程 : " + self.threadName)
        chiHuoGuo(self.people)  # start task
        print("结束线程 : " + self.threadName)


print("-------开始主线程-------")
print("YOU YOU 请大伙儿吃火锅")

thread1 = myThread("Xiao Ming", "Thread --1111")
thread2 = myThread("Xiao Wang", "Thread --2222")

# 第二种
# thread2.setDaemon(True)
# thread1.setDaemon(True)

# 第一种
thread1.start()
thread2.start()

# 第三种
# thread1.join()
# thread2.join()

time.sleep(0.5)
print("-------结束主线程-------")
