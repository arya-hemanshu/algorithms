
"""
Problem:
    Flatten a nested list with recursion
e.g:
    Given Input:
        [1, 2, 3, [4, 5, None, [8, 9], [10, 11], 12, 13, [14, 15, None]]]
    Output:
        [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15]
    without None
"""

TEMP = []

def flattening_list_with_recursion(list_to_flatten):
    global TEMP
    for j in list_to_flatten:
        if isinstance(j, list):
            flattening_list_with_recursion(j)
        else:
            if j is not None:
                TEMP.append(j)
    return TEMP

print(flattening_list_with_recursion([1, 2, 3, [4, 5, None, [8, 9], [10, 11], 12, 13, [14, 15, None]]]))