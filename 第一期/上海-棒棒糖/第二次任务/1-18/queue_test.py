__author__='棒棒糖'
class Queue(object):
    def __init__(self,size=30):
        #初始化队列长度
        self.size=size
        #c初始化队列列表
        self.queue=[]
        #初始化队列前后、后端位置
        self.front=0
        self.rear=-1
    #判断队列是否为空
    def is_empty(self):
        return self.rear==0
    #判断队列是否满了
    def is_full(self):
        res=False
        if (self.rear-self.front+1)==self.size:
            res=True
        return res

    #入队
    def add(self,obj):
        if self.is_full():
            raise Exception('队列是满的')
        else:
            self.queue.append(obj)
            self.rear+=1
    #出队
    def delete(self):
        if self.is_empty():
            raise Exception('队列是空的')
        else:
            self.rear-=1
            self.queue.pop(0)
    #队列头元素
    def first(self):
        if self.is_empty():
            raise Exception('队列是空的')
        else:
            return self.queue[self.front]
    #队列尾元素
    def last(self):
        if self.is_empty():
            raise Exception('队列是空的')
        else:
            return self.queue[self.rear]
    #打印队列
    def show(self):
        print(self.queue)

if __name__=='__main__':
    print('队列例子')
    #初始化长度为5的队列
    queue=Queue(5)
    #先把1-5的数据入队
    for index in range(1,6):
        queue.add(index)
    #打印队列
    queue.show()
    #打印下队列头
    print(queue.first())
    #打印下队列尾
    print(queue.last())
    #出个队列
    queue.delete()
    # 打印队列
    queue.show()
    #再出个队列
    queue.delete()
    # 打印队列
    queue.show()