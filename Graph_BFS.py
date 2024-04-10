
print("BFS", end=": ")

def BFS(graph, startNode = 0):
    # cities = ["Dhaka", "Feni", "Chittagong"]
    visited_List = [0 for i in range(len(graph[0]))]
    explo_Queue = []

    explo_Queue.append(graph[startNode])

    while len(explo_Queue) != 0:
        node = explo_Queue.pop(0)

        for i in range(3):
            if node[i] == 1 and visited_List[i] == 0:
                print(i, end=" ")
                # print(cities[i], end=" ")

                visited_List[i] = 1
                explo_Queue.append(graph[i])



graph = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

BFS(graph)