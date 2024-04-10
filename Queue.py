class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * self.size
        self.front = 0
        self.rear = -1

    
    def enQueue(self, item):
        if self.isFull():
            print("[Overflow..! Simple Queue is Full]")
            return 

        self.rear += 1
        self.queue[self.rear] = item


    def deQueue(self):
        if self.isEmpty():
            print("[Simple Queue is Empty]")
            return

        self.front += 1
        popped = self.queue[self.front]
        return popped


    def isFull(self):
        return self.rear + 1 == self.size

    def isEmpty(self):
        return self.front == self.rear


    def display(self):

        for el in range(self.front, self.rear+1):
            print(self.queue[el], end=' ')
        print()


my_Queue = Queue(3)

my_Queue.enQueue(5)
my_Queue.enQueue(10)
my_Queue.enQueue(5)
my_Queue.enQueue(5)

my_Queue.display()
