
visited = [0, 0, 0]

def DFS(graph, startNode=0):

    for i in range(3):
        if graph[startNode][i] == 1 and visited[i] == 0:
            visited[i] = 1
            DFS(graph, i)

            print(i, end=" ")


graph = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

DFS(graph)