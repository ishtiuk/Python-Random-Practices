
class Min_Heap:
    def __init__(self):
        self.arr = []
        self.size = 0


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


    def insertNode(self, item):
        if self.size == 0:
            self.arr.append(item)

        else:
            self.arr.append(item)

            for i in range(((self.size) // 2) - 1, -1, -1):
                self.heapify(self.size, i)

        self.size += 1


    def deleteNode(self, num):
        for i in range(self.size):
            if num == self.arr[i]:
                break

        temp = self.arr[i]
        self.arr[i] = self.arr[self.size - 1]
        self.arr[self.size - 1] = temp

        del self.arr[self.size - 1]
        self.size -= 1

        for i in range(self.size):
            self.heapify(self.size, i)



obj = Min_Heap()

obj.insertNode(55)
obj.insertNode(14)
obj.insertNode(7)

obj.insertNode(55)
obj.insertNode(10)
obj.insertNode(9)
obj.insertNode(21)
obj.insertNode(25)

print(obj.arr, obj.size)

obj.deleteNode(14)
obj.deleteNode(7)

print(obj.arr, obj.size)


obj2 = Min_Heap()

obj2.insertNode("B")
obj2.insertNode("D")
obj2.insertNode("C")
obj2.insertNode("F")
obj2.insertNode("A")
obj2.insertNode("E")

print(obj2.arr, obj2.size)

obj2.deleteNode("C")
obj2.deleteNode("B")

print(obj2.arr, obj2.size)