import os

os.system("cls")

import heapq


def ucs(graph, start, goal):
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            if node == goal:
                print(f"\nMinimum Cost: {cost}")
                return

            for neighbour, edge_cost in graph[node].items():
                if neighbour not in visited:
                    heapq.heappush(priority_queue, (cost + edge_cost, neighbour))

    print("Goal not found")


graph = {
    "S": {"A": 1, "G": 12},
    "A": {"B": 3, "C": 1},
    "B": {"D": 3},
    "C": {"D": 1, "G": 2},
    "D": {"G": 3},
    "G": {},
}

print("Uniform Cost Search (UCS):")
ucs(graph, "S", "G")
