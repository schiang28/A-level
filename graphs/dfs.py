# graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
# visited = set()  # Set to keep track of visited nodes.
# def dfs(visited, graph, node):
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)

# # Driver Code
# dfs(visited, graph, "A")

graph = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0],
]


def dfs(graph, start):
    visited = [False] * len(graph)
    stack = [start]
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            print(current)
            for node in range(len(graph)):
                if graph[node][current] == 1:
                    stack.append(node)


dfs(graph, 0)
