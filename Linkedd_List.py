
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class d_LinkedList:
    def __init__(self):
        self.head = None

    def insertFist(self):
        pass

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

    def insertByIndex(self, data, index):
        pass

    def insertAfterNode(self, prev_node, data):
        pass



    def deleteByData(self, data):
        pass

    def deleteByIndex(self, data):
        pass


    def print_Forward(self):
        current = self.head
        
        while current != None:
            print(current.data, end=" -> ")
            current = current.next
        print()


    def print_Backward(self):
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

    def makeFrom_List(self, lst):
        for item in lst:
            self.insertEnd(item)

    def Bubble_Sort(self):
        current = self.head

        while current.next != None:
            another = current.next

            while another != None:
                if current.data > another.data:
                    temp = current.data
                    current.data = another.data
                    another.data = temp

                another = another.next
            current = current.next


LLIst = d_LinkedList()

for i in range(5, -1, -1):
    LLIst.insertEnd(i)

# LLIst.makeFrom_List(["hello", "nc", "jhonny", "silverhand", "v", "judy"])

LLIst.print_Forward()

LLIst.Bubble_Sort()

LLIst.print_Forward()