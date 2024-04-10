
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    
class D_LLIst:
    def __init__(self):
        self.head = None

    def insertEnd(self, data):
        new = Node(data)

        if self.head == None:
            self.head = new
            return

        current = self.head
        while current.next != None:
            current = current.next

        new.prev = current
        current.next = new

    
    def displayForward(self):
        current = self.head
        
        while current != None:
            print(current.data, end=" -> ")
            current = current.next
        print()

    def displayBackward(self):
        last = self.getLastNode()

        while last != None:
            print(last.data, end=" -> ")
            last = last.prev
        print()
    

    def getLastNode(self):
        if self.head == None:
            return

        last = self.head

        while last.next != None:
            last = last.next
        return last


    def getSize(self):
        size = 0
        current = self.head

        while current != None:
            size += 1
            current = current.next

        return size


    def sort(self):
        current = self.head

        while current != None:
            another = current.next

            while another != None:
                if current.data > another.data:
                    temp = current.data
                    current.data = another.data
                    another.data = temp
                another = another.next
            current = current.next


    # def sort(self):
    #     size = self.getSize()
    #     i = 0

    #     while i <= size:
    #         current = self.head

    #         while current.next != None:
    #             if current.data > current.next.data:
    #                 temp = current.data
    #                 current.data = current.next.data
    #                 current.next.data = temp

    #             current = current.next
    #         i += 1



llist = D_LLIst()

for i in range(100, 90, -1):
    llist.insertEnd(i)

print("Forward: ", end="")
llist.displayForward()

print("Backward: ", end="")
llist.displayBackward()

llist.sort()
print("Sorted: ", end="")
llist.displayForward()