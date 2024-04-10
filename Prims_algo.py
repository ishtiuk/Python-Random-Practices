
def Prims_Algo(graph, V):
    no_edges = 0
    visited = [0 for i in range(V)]
    INF = 99999999

    visited[0] = 1


    while no_edges < V - 1:
        x = 0
        y = 0
        minimum = INF

        for i in range(V):
            if visited[i] == 1:

                for j in range(V):
                    if visited[j] == 0 and graph[i][j] > 0:

                        if graph[i][j] < minimum:
                            minimum = graph[i][j]

                            x = i
                            y = j

        visited[y] = 1
        no_edges += 1
        print(x, "-", y, ": ", graph[x][y])



# graph = [
#     [0, 2, 3],
#     [2, 0, 1],
#     [3, 1, 0]
# ]

graph = [
    [0, 0, 8, 0, 13, 17, 0],
    [0, 0, 20, 0, 0, 0, 6],
    [8, 20, 0, 11, 0, 0, 0],
    [0, 0, 11, 0, 12, 0, 0],
    [0, 0, 0, 12, 0, 15, 0],
    [0, 0, 0, 0, 15, 0, 18],
    [0, 6, 0, 0, 0, 18, 0]
]

print("MST: ")
# Prims_Algo(graph, 3)

Prims_Algo(graph, 7)
