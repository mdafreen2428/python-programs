python program to swap first and last elements of a list


def swap_first_last(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Test the function
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
print("Swapped list:", swap_first_last(my_list))