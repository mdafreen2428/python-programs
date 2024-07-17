46. Permutation 

import math

def permutation(n, r):
    return math.factorial(n) // math.factorial(n - r)

# Example usage:
print(permutation(5, 3))  # Output: 60
print(permutation(6, 2))  # Output: 30
