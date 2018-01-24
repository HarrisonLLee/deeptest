# -*- coding:utf-8 -*-

__author__ = 'VV'


class Queue:
    def __init__(self, size=30):
        # initial queue size
        self.size = size

        # initial queue list
        self.queue = []

        # initial front and rear
        self.front = 0
        self.rear = -1

    # if queue is empty
    def is_empty(self):
        return self.rear == 0

    # if queue if full
    def is_full(self):
        res = False
        if (self.rear - self.front + 1) == self.size:
            res = True
        
        return res

    # push into queue
    def add(self, obj):
        for o in range(0, obj):
            if self.is_full():
                raise Exception("Queue is full!!!")
            else:
                self.queue.append(o)
                self.rear += 1

    # delete from queue
    def delete(self, num):
        for n in range(0, num):
            if self.is_empty():
                raise Exception("Queue is empty...")
            else:
                self.rear -= 1
                self.queue.pop(0)

    # the first element
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty...")
        else:
            return self.queue[self.front]
        
    # the last element
    def last(self):
        if self.is_empty():
            raise Exception("Queue is empty...")
        else:
            return self.queue[self.rear]

    # print queue
    def show(self):
        print(self.queue)


if __name__ == '__main__':
    
    print("Queue demo")

    # initial queue size
    queue = Queue(5)

    # push 5 datas to queue
    queue.add(5)

    # print queue
    queue.show()

    # print first element
    print(queue.first())

    # print last element
    print(queue.last())

    # try delete 3 datas
    queue.delete(3)

    # print to check if it deleted
    queue.show()

