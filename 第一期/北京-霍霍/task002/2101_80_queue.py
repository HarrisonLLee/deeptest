# -*- coding:utf-8 -*-

__author__ = "huohuo"

class Queue:
    def __init__(self, size=30):
        # 初始化队列长度
        self.size = size

        # 初始化队列列表
        self.queue =[ ]

        # 初始化队列前后端位置
        self.front = 0
        self.rear = -1

    # 判断队列是否为空
    def is_empty(self):
        return self.rear == 0

    # 判断队列是否满了
    def is_full(self):
        res = False
        if (self.rear - self.front + 1 ) == self.size:
            res = True
        
        return res
    # 入队
    def add(self, obj):
        if self.is_full():
            raise Exception("队列满了。")
        else:
            self.queue.append(obj)
            self.rear += 1

    # 出队
    def delete(self):
        if self.is_empty():
            raise Exception("队列是空的")
        else:
            self.rear -= 1
            self.queue.pop(0)

    # 队列头元素
    def first(self):
        if self.is_empty():
            raise Exception("队列为空")
        else:
            return self.queue[self.front]

    # 队列尾元素
    def last(self):
        if self.is_empty():
            raise Exception("队列为空")
        else:
            return self.queue[self.rear]
    
    # 打印队列
    def show(self):
        print(self.queue)

if __name__ == "__main__":
    print("队列实现示例")

    # 初始化长度为5的队列
    queue = Queue(5)

    # 入队
    for index in range (1, 6):
        queue.add(index)

    # 打印队列数据
    queue.show()

    # 打印队列头
    print(queue.first())

    # 打印队列尾
    print(queue.last())

    # 出队
    queue.delete()

    # 打印
    queue.show()