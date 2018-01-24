# -*- coding:utf-8 -*-

__author__ = 'VV'

class Stack:
    def __init__(self, size=30):
        # initial stack size
        self.size = size

        # initial stack list
        self.stack = []

        # inistial stack default top value
        self.top = -1

    # set stack size
    def set_size(self, size):
        self.size = size

    # if stack is empty
    def is_empty(self):
        res = False
        if self.top == -1:
            res = True

        return res

    # if stack is full
    def is_full(self):
        res = False
        if self.top + 1 == self.size:
            res = True
        
        return res

    # print stack
    def show(self):
        print(self.stack)

    # push into stack
    def push(self, obj):
        for o in range(0, obj):
            if self.is_full():
                raise Exception("The stack is full!")
            else:
                self.stack.append(o)
                self.top += 1

    # pop to stack
    def pop(self, num):
        for n in range(0, num):
            if self.is_empty():
                raise Exception("The stack is empty...")
            else:
                self.stack.pop()
                self.top -= 1
                #return self.stack.pop()


if __name__ == '__main__':
    
    print("Stack demo")
    # initial stack size
    stack = Stack(5)

    # push int 1-5
    #for index in range(1, 6):
    stack.push(5)

    # print stack
    stack.show()

    # pop, data should be 5
    data = stack.pop(5)

    # print stack, it should be [1,2,3,4]
    stack.show()