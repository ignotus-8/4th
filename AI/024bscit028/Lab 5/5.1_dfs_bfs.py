import os

os.system("cls")

from collections import deque


def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


def bfs(graph, start, visited):
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["H"],
    "F": [],
    "G": [],
    "H": [],
}

visited_dfs = set()
print("Depth First Search:")
dfs(graph, "A", visited_dfs)

visited_bfs = set()
print(f"\nBreadth First Search:")
bfs(graph, "A", visited_bfs)
