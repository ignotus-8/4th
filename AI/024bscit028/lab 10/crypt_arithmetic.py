import os

os.system("cls")


from itertools import permutations

# Input the puzzle
word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
result = input("Enter result word: ").upper()

# Find unique letters
letters = list(set(word1 + word2 + result))

# Check if more than 10 unique letters
if len(letters) > 10:
    print("No solution possible (more than 10 unique letters).")
    exit()

# Try all possible digit assignments
for perm in permutations(range(10), len(letters)):

    mapping = dict(zip(letters, perm))

    # First letter of a word cannot be zero
    if mapping[word1[0]] == 0 or mapping[word2[0]] == 0 or mapping[result[0]] == 0:
        continue

    # Convert words to numbers
    n1 = int("".join(str(mapping[ch]) for ch in word1))
    n2 = int("".join(str(mapping[ch]) for ch in word2))
    res = int("".join(str(mapping[ch]) for ch in result))

    # Check the equation
    if n1 + n2 == res:
        print("\nSolution Found!")
        print(word1, "=", n1)
        print(word2, "=", n2)
        print(result, "=", res)
        break
else:
    print("No solution exists.")
