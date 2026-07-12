import os

os.system("cls")

import heapq


def greedy(graph, heuristic, start, goal):
    priority_queue = [(heuristic[start], start)]  # f,g,start
    visited = set()

    while priority_queue:
        f, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)
        print(node, end=" ")

        if node == goal:
            return

        for neighbour, edge_cost in graph[node].items():
            if neighbour not in visited:
                f_new = heuristic[neighbour]
                heapq.heappush(priority_queue, (f_new, neighbour))

    print("\nGoal not found")


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

heuristic = {"A": 46, "B": 39, "C": 41, "D": 29, "E": 38, "F": 17, "G": 6, "H": 0}

print("A* Search:")
greedy(graph, heuristic, "A", "H")
