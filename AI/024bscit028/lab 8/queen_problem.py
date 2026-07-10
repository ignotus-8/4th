def isSafe(mat, row, col):
    n = len(mat)

    # Check this col on upper side
    for i in range(row):
        if mat[i][col]:
            return 0

    # Check upper diagonal on left side
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if mat[i][j]:
            return 0
        i -= 1
        j -= 1

    # Check upper diagonal on right side
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if mat[i][j]:
            return 0
        i -= 1
        j += 1

    return 1

# Recursive function to place queens
def placeQueens(row, mat, result):
    n = len(mat)

    # base case: If all queens are placed
    if row == n:
        
        # store current solution
        ans = []
        for i in range(n):
            for j in range(n):
                if mat[i][j]:
                    ans.append(j + 1)
        result.append(ans)
        return

    # Consider the row and try placing
    # queen in all columns one by one
    for i in range(n):
        
        # Check if the queen can be placed
        if isSafe(mat, row, i):
            mat[row][i] = 1
            placeQueens(row + 1, mat, result)

            # backtrack
            mat[row][i] = 0

# Function to find all solutions
def nQueen(n):
    
    # Initialize the board
    mat = [[0] * n for _ in range(n)]
    result = []

    # Place queens
    placeQueens(0, mat, result)

    return result

if __name__ == "__main__":
    n = 8
    result = nQueen(n)
    for ans in result:
        print(" ".join(map(str, ans)))