
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def insert_First(self, new_data):
        new = Node(new_data)
        new.next = self.head
        self.head = new

    def insertByIndex(self, index, new_data):           # NOTE: this and the "insertAfterNode" methods are actually the alternative of "insert_Middle" method. ;)
        if index == 0:
            self.insert_First(new_data)
            return
        if self.head == None:
            print("\n[LinkedList is Empty]\n")
            return

        new = Node(new_data)                           # NOTE: this method's Time Complexity = O(n)
        count = 0
        current = self.head

        while count < index - 1:
            if current.next == None:
                print("\n[Invalid Index]\n")            # NOTE: just for prevent Error ;), this "if" has no core concept of LinkedList.. 8D
                return

            current = current.next
            count += 1

        temp = current.next
        current.next = new
        new.next = temp

    def insertAfterNode(self, prev_node, new_data):
        if prev_node == None:
            print("\n[Provided Previous Node must be in LinkedList]\n")
            return

        new = Node(new_data)
        temp = prev_node.next                       # NOTE: this method's Time Complexity = O(1)    [constant time]
        prev_node.next = new
        new.next = temp

    def insert_End(self, new_data):
        new = Node(new_data)
        if self.head == None:
            self.head = new
            return

        current = self.head
        while current.next != None:
            current = current.next

        current.next = new

    def deleteNode_byData(self, data):
        if self.head == None:
            print("\n[LinkedList is Empty]\n")
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next.next != None:
            current = current.next

            if current.next.data == data:
                current.next = current.next.next
                return
        else:
            print("\n[Data isn't in LinkedList]\n")

    def deleteNode_byIndex(self, index):
        if self.head == None:
            print("\n[LinkedList is Empty]\n")
            return
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        current = self.head
        
        while count < index - 1:
            current = current.next
            count += 1

        current.next = current.next.next

    def sort_LinkedList(self, head):
        if head == None:
            print("[Empty LinkedList, Can't be Sorted]")
            return
                                                                    # NOTE: remember the "Bubble Sort Algo" by Programming Hero and CISSCO 😎, here that's used.
                                                                    # NOTE: Two Nested Loops 😁😁
        current = head
        another_current = Node(None)

        while current != None:
            another_current = current.next

            while another_current != None:
                if current.data > another_current.data:
                    temp = current.data
                    current.data = another_current.data
                    another_current.data = temp

                another_current = another_current.next
            current = current.next


    def make_From_List(self, lst):
        for el in lst:
            self.insert_End(el)

    def search(self, data):
        current = self.head

        while current != None:
            if current.data == data:
                return True
            current = current.next

        return False


    def display(self):
        last = self.head 

        while last != None:
            print(last.data, end=" -> ")
            last = last.next
        print()

llist = Linked_List()
llist.make_From_List([5, 3, 6, 1, 2])
# llist.make_From_List([chr(i) for i in range(65, 71)])

print("Initial LinkedList: ", end="")
llist.display()

llist.insertByIndex(3, 10)
llist.insertAfterNode(llist.head.next.next, 4)

print("\nAfter Some Insertions: ", end="")
llist.display()


llist.deleteNode_byData("jackfdfdfruit")
llist.deleteNode_byIndex(4)

print("After Some Deletions: ", end="")
llist.display()


llist.sort_LinkedList(llist.head)
print("\nAfter Sorting LinkedList: ", end="")
llist.display()


user = int(input("\nEnter int number to search: "))

if llist.search(user):
    print("[Item Exists]")
else:
    print("[Item doesn't Exist]")
