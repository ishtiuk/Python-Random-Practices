
class Graph:
    def __init__(self, size):
        self.V = size
        self.matrix = [[0 for i in range(self.V)] for j in range(self.V)]


    def add_edge(self, v1, v2):
        if v1 == v2:
            print("[Same Nodes %d and %d]" % (v1, v2))

        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1


    def remove_edge(self, v1, v2):
        if self.matrix[v1][v2] == 0 or self.matrix[v2][v1] == 0:
            print("[No Connected %d and %d]" % (v1, v2))
            return

        self.matrix[v1][v2] = 0
        self.matrix[v2][v1] = 0


    def print_Graph(self):
        for i in range(self.V):
            print(i, end=": ")

            for j in range(self.V):
                print(self.matrix[i][j], end=" ")
            print()


adj_Mtrx = Graph(4)

adj_Mtrx.add_edge(0, 1)
adj_Mtrx.add_edge(0, 2)
adj_Mtrx.add_edge(0, 3)
adj_Mtrx.add_edge(1, 2)
adj_Mtrx.add_edge(1, 3)
adj_Mtrx.add_edge(2, 3)

adj_Mtrx.print_Graph()
print()

adj_Mtrx.remove_edge(0, 1)

adj_Mtrx.print_Graph()

