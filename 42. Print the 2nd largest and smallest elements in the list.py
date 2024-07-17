42. Print the 2nd largest and smallest elements in the list

def second_largest_smallest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    if len(unique_lst) < 2:
        return None, None
    return unique_lst[-2], unique_lst[1]
