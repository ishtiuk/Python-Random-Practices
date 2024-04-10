
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * self.size
        self.FRONT = -1
        self.REAR = -1

    def enQueue(self, item):
        if (self.REAR + 1) % self.size == self.FRONT:
            print("[Overflow..! Circular Queue is Full]")

        elif self.REAR == -1:                   # or "elif self.FRONT == -1"
            self.FRONT = 0
            self.REAR = 0                       # NOTE: if Queue is Empty, then setting the first element...
            self.queue[self.REAR] = item

        else:
            self.REAR = (self.REAR + 1) % self.size       # NOTE: if Queue isn't Empty, then continuing "EnQueue" according to "Circular Increment" of self.REAR 😎
            self.queue[self.REAR] = item

    def deQueue(self):
        if self.REAR == -1:
            print("[Cicular Queue is Empty]")

        elif self.FRONT == self.REAR:
            popped = self.queue[self.FRONT]
            self.FRONT = -1
            self.REAR = -1

            return popped

        else:
            popped = self.queue[self.FRONT]
            self.FRONT = (self.FRONT + 1) % self.size

            return popped

    def display(self):
        if self.FRONT <= self.REAR:
            for el in range(self.FRONT, self.REAR + 1):
                print(self.queue[el], end=" ")
            print()

        else:
            for el in range(self.FRONT, self.size):
                print(self.queue[el], end=" ")

            for el in range(0, self.REAR + 1):
                print(self.queue[el], end=" ")
            print()



circular_Q_obj = CircularQueue(size=5)

circular_Q_obj.enQueue(5)
circular_Q_obj.enQueue(9)
circular_Q_obj.enQueue(7)

circular_Q_obj.display()

circular_Q_obj.deQueue()
circular_Q_obj.deQueue()

circular_Q_obj.display()

circular_Q_obj.enQueue(75)
circular_Q_obj.enQueue(12)
circular_Q_obj.enQueue(25)
circular_Q_obj.enQueue(36)

circular_Q_obj.display()
print(circular_Q_obj.queue)