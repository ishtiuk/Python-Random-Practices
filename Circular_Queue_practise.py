
class Circular_Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * self.size
        self.FRONT = -1
        self.REAR = -1

    
    def enQueue(self, item):
        if (self.REAR + 1) % self.size == self.FRONT:
            print("[Overflow]\n")
            return

        elif self.FRONT == -1:
            self.FRONT = 0
            self.REAR = 0
            self.queue[self.REAR] = item

        else:
            self.REAR = (self.REAR + 1) % self.size
            self.queue[self.REAR] = item


    def deQueue(self):
        if self.FRONT == -1:
            print("[Underflow]")
            return

        elif self.FRONT == self.REAR:
            popped = self.queue[self.FRONT]
            self.FRONT = self.REAR = -1

            return popped

        else:
            popped = self.queue[self.FRONT]
            self.FRONT = (self.FRONT + 1) % self.size

            return popped


    def display(self):
        if self.FRONT <= self.REAR:
            for el in range(self.FRONT, self.REAR+1):
                print(self.queue[el], end=" ")
            print('\n')

        else:
            for el in range(self.FRONT, self.size):
                print(self.queue[el], end=" ")
            for el in range(0, self.REAR+1):
                print(self.queue[el], end=" ")
            print('\n')

    def peek(self):
        if self.FRONT == -1:
            print("[Circular Queue is Empty]")
            return
        return self.queue[self.FRONT]


my_circular_queue = Circular_Queue(5)
my_circular_queue.enQueue(5)
my_circular_queue.enQueue(8)
my_circular_queue.enQueue(9)

my_circular_queue.deQueue()

my_circular_queue.enQueue(77)
my_circular_queue.enQueue(60)
my_circular_queue.enQueue(77)

print("Queue: ", end='')
my_circular_queue.display()
