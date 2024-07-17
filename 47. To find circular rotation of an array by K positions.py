47. To find circular rotation of an array by K positions

def circular_rotation(arr, k):
    k = k % len(arr)  # To handle rotations greater than array length
    return arr[-k:] + arr[:-k]

# Example usage:
print(circular_rotation([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
print(circular_rotation([1, 2, 3, 4, 5], 3))  # Output: [3, 4, 5, 1, 2]
