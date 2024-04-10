class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Circ_D_LinkedList:
    def __init__(self):
        self.head = None

    def insertFirst(self, newdata):
        new = Node(newdata)
        if self.head == None:
            self.head = new
            return

        new.next = self.head
        self.head.prev = new
        self.head = new

    def insertEnd(self, newdata):
        new = Node(newdata)
        if self.head == None:
            self.head = new
            return

        current = self.head
        while current.next != None:
            current = current.next

        new.prev = current
        current.next = new

    def insertByIndex(self, index, newdata):
        if index == 0:
            self.insertFirst(newdata)
            return
        
        current = self.head
        new = Node(newdata)
        count = 0
        while count < index - 1:
            current = current.next
            count += 1

        new.prev = current
        new.next = current.next
        current.next.prev = new
        current.next = new


    def deleteByData(self, data):
        if self.head == None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        current = self.head
        while current.next != None:
            if current.next.next == None and current.next.data == data:
                current.next = current.next.next
                return
            if current.next.data == data:
                current.next.next.prev = current
                current.next = current.next.next
                return
            current = current.next
            
    def deleteByIndex(self, index):
        if self.head == None:
            return
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        current = self.head
        while count < index - 1:
            current = current.next
            count += 1

        if current.next.next == None:
            current.next = current.next.next
            return

        current.next.next.prev = current
        current.next = current.next.next

    def print_forward(self):
        current = self.head
        while current != None:
            print(current.data, end=" -> ")
            current = current.next
        print()

    def print_backward(self):
        last = self.getLastNode()
        while last != None:
            print(last.data, end=" -> ")
            last = last.prev
        print()

    def getLastNode(self):
        current = self.head
        while current.next != None:
            current = current.next

        return current

    def sort(self):
        current = self.head                               ## Bubble Sort Algorithm

        while current != None:
            another = current.next

            while another != None:
                if current.data > another.data:
                    temp = current.data
                    current.data = another.data
                    another.data = temp
                another = another.next
            current = current.next

    def circulariFy(self):
        lastNode = self.getLastNode()
        lastNode.next = self.head

        self.head.prev = lastNode


obj = Circ_D_LinkedList()

print("[After Insertion]:")
obj.insertFirst(2)
obj.insertFirst(200)
obj.insertFirst(6)
obj.insertEnd(3)
obj.insertFirst(56)
obj.insertEnd(8)
obj.insertFirst(42)
obj.insertEnd(69)

obj.insertByIndex(0, 699)
obj.insertByIndex(5, 25)

obj.print_forward()

print("\n[After Deletion]: ")
obj.deleteByIndex(4)
obj.deleteByIndex(2)
obj.deleteByData(100)
obj.deleteByData(8)

obj.print_forward()


print("\n[After Sort]:")
obj.sort()
obj.print_forward()

print("\n[Backward Print]:")
obj.print_backward()