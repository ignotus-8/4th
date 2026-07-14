import os

os.system("cls")

# no 1
print("Graph 1:")
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": ["G"], "E": ["H"],
         "F":[""],"G":[""]}

for vertex in graph:
    print(f"{vertex} — {graph[vertex]}")

# no 2
print("Graph 2:")

graph2 = {
    "S": {"A": 1, "G": 12},
    "A": {"B": 3, "C": 1},
    "B": {"D": 3},
    "C": {"D": 1, "G": 2},
    "D": {"G": 3},
    "G": {}
}
 
for node in graph2:
    print(f"{node}->{graph2[node]}")

#no 3
print("Graph 3:")

graph3 = {
    "A": {"B": 22, "D": 30, "E": 25},
    "B": {"A": 22, "C": 20, "D": 11},
    "C": {"B": 20},
    "D": {"A": 30, "B": 11, "F": 10},
    "E": {"A": 25, "F": 25, "G": 40},
    "F": {"D": 10, "E": 25, "G": 12},
    "G": {"E": 40, "F": 12, "H": 6},
    "H": {"G": 6}
}
for node in graph3:
    print(f"{node} — {graph3[node]}")