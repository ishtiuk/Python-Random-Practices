
class Priority_Queue:
    def __init__(self):
        self.arr = []
        self.size = 0

    def insertNode(self, item):
        if self.size == 0:
            self.arr.append(item)

        else:
            self.arr.append(item)
            for i in range((self.size // 2) - 1, -1, -1):
                self.heapify(self.size, i)

        self.size += 1

    def deleteNode(self, item):
        for i in range(self.size):
            if item == self.arr[i]:
                break

        temp = self.arr[i]
        self.arr[i] = self.arr[self.size - 1]
        self.arr[self.size - 1] = temp

        del self.arr[self.size - 1]
        self.size -= 1

        for i in range((self.size // 2) - 1, -1, -1):
            self.heapify(self.size, i)


    def heapify(self, size, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < size and self.arr[i] > self.arr[left]:
            smallest = left
        if right < size and self.arr[i] > self.arr[right]:
            smallest = right

        if smallest != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[smallest]
            self.arr[smallest] = temp

            self.heapify(size, smallest)



my_P_Queue = Priority_Queue()
my_P_Queue.insertNode(7)
my_P_Queue.insertNode(6)
my_P_Queue.insertNode(4)
my_P_Queue.insertNode(2)
my_P_Queue.insertNode(5)
my_P_Queue.insertNode(10)

print(my_P_Queue.arr)

my_P_Queue.deleteNode(5)
print(my_P_Queue.arr)