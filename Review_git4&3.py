from itertools import combinations, permutations

# Define the lists
A = [1, 2, 3]
B = ['a', 'b', 'c']
C = [True, False]
D = [3.14, 2.71]
E = ['x', 'y']

all_lists = [A, B, C, D, E]

# Function to compute and print combinations
def print_combinations(lst, name):
    print(f"Combinations for list {name}:")
    for r in range(1, len(lst) + 1):
        combs = list(combinations(lst, r))
        print(f"  {r}-combinations: {combs}")

# Function to compute and print permutations
def print_permutations(lst, name):
    print(f"Permutations for list {name}:")
    perms = list(permutations(lst))
    print(f"  {perms}")

# Computing combinations and permutations for each list
for name, lst in zip(['A', 'B', 'C', 'D', 'E'], all_lists):
    print_combinations(lst, name)
    print_permutations(lst, name)
    print()