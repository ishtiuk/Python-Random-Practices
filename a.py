class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def addlast(self, node, cycle=None):
        if self.head == None:
            self.head = node
            return
        
        current = self.head
        while current.next != None:
            current = current.next
        current.next = node

        if cycle:
            current.next.prev = current
            
            
    def p(self):
        current = self.head
        while current != None:
            print(f"{current.data}: ||{current.next} : {current.prev} ||", end=" -> ")
            current = current.next
        print("\n")

def detectCycle(head):
    current = head.head

    while current != None:
        if current.prev:
            return current.prev.data
        current = current.next
       

for i in range(int(input())):
    llist = LinkedList()
    n = int(input())
    lst = list(map(int, input().split()))
    cycle = int(input())
    
    for j in range(n):
        if cycle == j:
            llist.addlast(Node(lst[j]), cycle)
        else:
            llist.addlast(Node(lst[j]))
    # print(llist.idxs, lst)
    # llist.p()
    
    print(detectCycle(llist))