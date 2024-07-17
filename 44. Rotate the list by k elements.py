44. Rotate the list by k elements

def rotate_list(lst, k):
    k = k % len(lst)  # To handle rotations greater than list length
    return lst[-k:] + lst[:-k]
