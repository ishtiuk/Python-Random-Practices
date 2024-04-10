
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class D_Linked_List:
    def __init__(self):
        self.head = None

    def insertFirst(self, new_data):
        new = Node(new_data)

        if self.head == None:
            self.head = new 
            return

        new.next = self.head
        self.head.prev = new
        self.head = new

    def insertByIndex(self, index, new_data):
        if index > self.getsize():
            print('[Invalid Index]')
            return
        if index == 0:
            self.insertFirst(new_data)
            return

        i = 0
        current = self.head
        new = Node(new_data)
        while i < index - 1:  
            i += 1
            current = current.next

        new.next = current.next
        new.prev = current
        current.next = new

        
    
    def insertEnd(self, new_data):
        new = Node(new_data)

        if self.head == None:
            self.head = new
            return

        current = self.head
        while current.next != None:
            current = current.next

        current.next = new
        new.prev = current

    def printForward(self):
        current = self.head

        while current != None:
            print(current.data, end=" -> ")
            current = current.next
        print()

    def printBackward(self):
        last = self.getLastNode()

        while last != None:
            print(last.data, end=" -> ")
            last = last.prev
        print()


    def getLastNode(self):
        last = self.head

        while last.next != None:
            last = last.next

        return last

    def getsize(self):
        size = 0
        current = self.head

        while current != None:
            size += 1
            current = current.next

        return size

    def sort(self):
        current = self.head

        # while i <= self.getsize():
        while current != None:
            another = current.next

            while another != None:
                if current.data > another.data:
                    temp = current.data
                    current.data = another.data
                    another.data = temp
                another = another.next
            
            current = current.next
            # i += 1



LList = D_Linked_List()
LList.insertFirst(5)
LList.insertFirst(2)
LList.insertFirst(77)
LList.insertFirst(7)
LList.insertFirst(30)
LList.insertFirst(1)
LList.insertEnd(6)
LList.insertEnd(600)

print("Foward Display: ", end='')
LList.printForward()

print("Backward Display: ", end='')
LList.printBackward()

print("\nD_LList size:", LList.getsize())

print("Sorted: ", end='')
LList.sort()
LList.printForward()


LList.insertByIndex(9, 66)
LList.printForward()
LList.printBackward()