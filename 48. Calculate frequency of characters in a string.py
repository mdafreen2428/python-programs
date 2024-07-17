48. Calculate frequency of characters in a string




from collections import Counter

def character_frequency(string):
    return dict(Counter(string))

# Example usage:
print(character_frequency("hello world"))  # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
print(character_frequency("aabbcc"))       # Output: {'a': 2, 'b': 2, 'c': 2}
