import os

os.system("cls")

# Tree stored as a dictionary
tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [5, 6],
    "E": [7, 4],
    "F": [3, 2],
    "G": [8, 1]
}


def minimax(node, is_max):

    # Base case: leaf node
    if isinstance(node, int):
        return node, []

    left_child, right_child = tree[node]

    left_value, left_path = minimax(left_child, not is_max)
    right_value, right_path = minimax(right_child, not is_max)

    if is_max:
        if left_value >= right_value:
            return left_value, [left_child] + left_path
        else:
            return right_value, [right_child] + right_path

    else:
        if left_value <= right_value:
            return left_value, [left_child] + left_path
        else:
            return right_value, [right_child] + right_path


value, path = minimax("A", True)

print("Optimal Value :", value)
print("Optimal Path  : A ->", " -> ".join(map(str, path)))