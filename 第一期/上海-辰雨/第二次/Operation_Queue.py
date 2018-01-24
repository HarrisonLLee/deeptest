#coding:utf-8
import collections

#双向队列
aa = collections.deque()
#往左边添加
aa.append("1")
#在左边添加
aa.appendleft('10')
aa.appendleft('1')
#统计制定字符出现的字数
bb = aa.count('1')
print aa
print bb
#清空队列，返回None
print (aa.clear())
#向右扩展
aa.extend(['rr','hh','kk'])
aa.extendleft(['rlr','h1h','kk1'])
print (aa)
#不加参数默认删除最后一个
print aa.pop()
#不加参数默认移除最左边一个
print aa.popleft()
#移除指定值：
aa.remove('rr')
print aa
#队列翻转：
aa.reverse()
print aa
#把后面的几个移到前面去
aa.rotate(1)
print aa

print('*'*50)
print ('单向队列')
import Queue

Q = Queue.Queue()
#加入队列
Q.put('123')
Q.put('345')
#计算队列中数据的个数
print(Q.qsize())
#取队列数据(先进先出)
print(Q.get())





