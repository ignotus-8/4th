import os

os.system("cls")


N = 8


def is_safe(board, row, col):

    # Check same column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve(board, row):

    # Base case
    if row == N:
        return True

    # Try every column
    for col in range(N):

        if is_safe(board, row, col):

            board[row][col] = "Q"

            if solve(board, row + 1):
                return True

            # Backtracking
            board[row][col] = "."

    return False


board = [["." for _ in range(N)] for _ in range(N)]

if solve(board, 0):

    print("Solution Found")

    for row in board:
        print(" ".join(row))

    print("\nQueen Positions (Row, Column):")

    for row in range(N):
        for col in range(N):
            if board[row][col] == "Q":
                print(f"({row}, {col})")

else:
    print("No Solution")
