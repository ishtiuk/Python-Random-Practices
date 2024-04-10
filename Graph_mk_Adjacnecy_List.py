
class GNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:
    def __init__(self, size):
        self.V = size
        self.arr = [None] * self.V


    def add_node(self, v1, v2):
        node = GNode(v2)
        node.next = self.arr[v1]
        self.arr[v1] = node

        node = GNode(v1)
        node.next = self.arr[v2]
        self.arr[v2] = node


    def remove_edge(self, v1, v2, again=0):
        if again == 0:
            self.remove_edge(v2, v1, again=1)

        if self.arr[v2].data == v1 and self.arr[v2].next == None:
            self.arr[v2] = None
            return

        if self.arr[v2].data == v1:
            self.arr[v2] = self.arr[v2].next
            return
                
        temp = self.arr[v2]

        while temp.next != None:
            if temp.next.data == v1 and temp.next.next == None:
                print('yes')
                temp.next = None
                return
            elif temp.next.data == v1:
                temp.next = temp.next.next

            temp = temp.next


    def print_AdjList(self):
        for i in range(self.V):
            temp = self.arr[i]

            print(i, end=": ")

            while temp != None:
                print(temp.data, end=" -> ")
                temp = temp.next
            
            print()



adj_List = Graph(4)

adj_List.add_node(0, 1)
adj_List.add_node(0, 3)
adj_List.add_node(0, 2)
adj_List.add_node(1, 3)
adj_List.add_node(1, 2)
adj_List.add_node(2, 3)

adj_List.print_AdjList()
print()

adj_List.remove_edge(1, 3)
adj_List.remove_edge(2, 3)

adj_List.print_AdjList()
