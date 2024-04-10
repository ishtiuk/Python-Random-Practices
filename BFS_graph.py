
def BFS(graph, V, startNode=0):
    exp_queue = []
    visited = [0 for i in range(V)]


    exp_queue.append(graph[startNode])
    visited[startNode] = 1

    print(startNode, end=" ")

    while len(exp_queue) != 0:
        node = exp_queue.pop(0)


        for i in range(V ):
            
            if node[i] > 0 and visited[i] == 0:
                print(i, end=" ")
                
                
                visited[i] = 1
                exp_queue.append(graph[i])


graph = [
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
]

print("BFS: ", end=" ")

BFS(graph, 7, startNode=0)