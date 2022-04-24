graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0],
]

from collections import deque


def bfs(graph, start):
    visited = [False] * len(graph)
    Q = deque([start])
    while len(Q) > 0:
        current = Q.popleft()
        if not visited[current]:
            visited[current] = True
            print(current)
            for node in range(len(graph)):
                if graph[current][node] == 1:
                    Q.append(node)


print(bfs(graph, 0))
