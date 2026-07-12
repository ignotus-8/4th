import os

os.system("cls")


def dls(graph, node, goal, depth, limit, visited, path):
    visited.add(node)
    path.append(node)

    print(node, end=" ")

    if node == goal:
        print("\nGoal found")
        return True

    if depth == limit:
        visited.remove(node)
        path.pop()
        return False

    for neighbour in graph[node]:
        if neighbour not in visited:
            if dls(graph, neighbour, goal, depth + 1, limit, visited, path):
                return True

    visited.remove(node)
    path.pop()
    return False


graph = {
    "A": {"B": 22, "D": 30, "E": 25},
    "B": {"A": 22, "C": 20, "D": 11},
    "C": {"B": 20},
    "D": {"A": 30, "B": 11, "F": 10},
    "E": {"A": 25, "F": 25, "G": 40},
    "F": {"D": 10, "E": 25, "G": 12},
    "G": {"E": 40, "F": 12, "H": 6},
    "H": {"G": 6},
}

visited = set()
path = []
if dls(graph, "A", "F", 0, 2, visited, path):
    print("Path:"," -> ".join(path))
else:
    print("Goal not found")
