
class MyCircular_Queue:
    def __init__(self, size):
        self.arr = [None] * size
        self.size = size
        self.front = self.rear = -1

    def enQueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("[OverFlow]")
            return
        
        elif self.front == -1:
            self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.arr[self.rear] = value

        else:
            self.rear = (self.rear + 1) % self.size
            self.arr[self.rear] = value

    def deQueue(self):
        if self.front == -1:
            print("[UnderFlow]")
            return

        elif self.front == self.rear:
            popped = self.arr[self.front]
            self.front = self.rear = -1

        else:
            popped = self.arr[self.front]
            self.front = (self.front + 1) % self.size

        return popped

    def display(self):
        if self.front == -1:
            print("[Empty Circular Queue]")
            return

        if self.front <= self.rear:
            for i in range(self.front, self.rear+1):
                print(self.arr[i], end="-> ")

        elif self.front > self.rear:
            for i in range(self.front, self.size):
                print(self.arr[i], end="-> ")

            for i in range(0, self.rear + 1):
                print(self.arr[i], end="-> ")

        print()


CirQueue = MyCircular_Queue(10)

for i in range(10):
    CirQueue.enQueue(i+1)

CirQueue.display()

CirQueue.deQueue()
CirQueue.enQueue(4)
# CirQueue.display()

for i in range(10):
    CirQueue.deQueue()

CirQueue.display()

        