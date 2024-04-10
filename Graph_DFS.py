
def DFS(graph, startNode=0):
    visited = [0, 0, 0]
    exp_Stack = []

    exp_Stack.append(graph[startNode])


    while len(exp_Stack) != 0:
        node = exp_Stack.pop()

        for i in range(3):
            if node[i] == 1 and visited[i] == 0:
                print(i, end=" ")

                visited[i] = 1
                exp_Stack.append(graph[i])


graph = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

DFS(graph)