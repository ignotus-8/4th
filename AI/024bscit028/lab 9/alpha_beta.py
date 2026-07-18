import os

os.system("cls")

tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [5, 6],
    "E": [7, 4],
    "F": [3, 2],
    "G": [8, 1],
}


def alpha_beta(node, is_max, alpha, beta):

    # Leaf node
    if isinstance(node, int):
        return node, []

    left_child, right_child = tree[node]

    if is_max:

        best_value = float("-inf")
        best_path = []

        for child in [left_child, right_child]:

            value, path = alpha_beta(child, False, alpha, beta)

            if value > best_value:
                best_value = value
                best_path = [child] + path

            alpha = max(alpha, best_value)

            if alpha >= beta:
                print(f"Beta Pruning at {node}")
                break

        return best_value, best_path

    else:

        best_value = float("inf")
        best_path = []

        for child in [left_child, right_child]:

            value, path = alpha_beta(child, True, alpha, beta)

            if value < best_value:
                best_value = value
                best_path = [child] + path

            beta = min(beta, best_value)

            if beta <= alpha:
                print(f"Alpha Pruning at {node}")
                break

        return best_value, best_path


value, path = alpha_beta("A", True, float("-inf"), float("inf"))

print("\nOptimal Value :", value)
print("Optimal Path  : A ->", " -> ".join(map(str, path)))
