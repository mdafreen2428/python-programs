45. Automorphic number

def is_automorphic(num):
    square = num ** 2
    return str(square).endswith(str(num))

# Example usage:
print(is_automorphic(5))  # Output: True, because 5^2 = 25
print(is_automorphic(6))  # Output: True, because 6^2 = 36
print(is_automorphic(25))  # Output: True, because 25^2 = 625
