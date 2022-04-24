from datastructure import *

class Queue:
    maxsize = 5

    def __init__(self):
        self.items = Array(str, Queue.maxsize)
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def isEmpty(self):
        if self.size ==0:
            return True
        return False
    
    def isFull(self):
        if self.size == Queue.maxsize:
            return True
        return False
    
    def enQueue(self, item):
        if self.isFull():
            print("queue is full")
        else:
            self.rear = (self.rear+1) % Queue.maxsize
            self.items[self.rear] = item
            self.size+=1

    def deQueue(self):
        if self.isEmpty():
            print("queue is empty")
            item = None
        else:
            item = self.items[self.front]
            self.front = (self.front + 1) % Queue.maxsize
            self.size -=1
        return item
    
myQueue = Queue()

print("Dequeued", myQueue.deQueue())
myQueue.enQueue("a")
myQueue.enQueue("b")
myQueue.enQueue("c")
print("Dequeued", myQueue.deQueue())
print("Dequeued", myQueue.deQueue())
print("Dequeued", myQueue.deQueue())
print("Dequeued", myQueue.deQueue())
myQueue.enQueue("d")
myQueue.enQueue("e")
myQueue.enQueue("f")
myQueue.enQueue("g")
myQueue.enQueue("h")
myQueue.enQueue("i")
myQueue.enQueue("j")

while not myQueue.isEmpty():
  print("Dequeued", myQueue.deQueue())

print(myQueue)