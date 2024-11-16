' 8 - perm'

from itertools import permutations

def generate_permutations(n):
    # Generate a list of numbers from 1 to n
    numbers = list(range(1, n + 1))
    
    # Generate all permutations
    perm = list(permutations(numbers))
    
    # Calculate the total number of permutations
    total_permutations = len(perm)
    
    return total_permutations, perm

if __name__ == "__main__":
    # Input: Positive integer n
    n = 7  

    # Generate permutations
    total, perm_list = generate_permutations(n)
    
    # Output the total number of permutations
    print(total)
    
    # Output each permutation
    for p in perm_list:
        print(' '.join(map(str, p)))
