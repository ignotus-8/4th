import os

os.system("cls")


def dfs(graph, node, visited):
    if node in visited:
        return

    print(node)
    visited.add(node)

    for neighbour in graph[node]:
        dfs(graph, neighbour, visited)


graph = {
    "S": {"G": 12, "A": 1},
    "A": {"C": 1, "B": 3},
    "B": {"D": 3},
    "C": {"G": 2, "D": 1},
    "D": {"G": 3},
    "G": {},
}
visited = set()
dfs(graph, "S", visited)
