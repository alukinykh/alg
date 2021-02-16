# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

# my_graph = [
#     [0, 0, 1, 1, 9, 0, 0, 0],
#     [0, 0, 9, 4, 0, 0, 5, 0],
#     [0, 9, 0, 0, 3, 0, 6, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 5, 0],
#     [0, 0, 7, 0, 8, 1, 0, 0],
#     [0, 0, 0, 0, 0, 1, 2, 0]
# ]

my_graph = [
    [0, 3, 0, 0, 1, 0],
    [3, 0, 4, 0, 1, 0],
    [0, 4, 0, 1, 0, 0],
    [0, 0, 1, 0, 2, 1],
    [1, 1, 0, 2, 0, 0],
    [0, 0, 0, 1, 0, 0]
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False for _ in range(length)]
    cost = [float('inf')] * length
    paths = [[i] for i in range(length)]

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, val in enumerate(graph[start]):
            if val != 0 and not is_visited[i]:
                if cost[i] > val + cost[start]:
                    cost[i] = val + cost[start]
                    paths[i] = paths[start].copy()
                    paths[i].append(i)

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost, paths


print(dijkstra(my_graph, 0))
