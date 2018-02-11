
"""
A python implementation of merge sort,
complexity of merge sort is O(NlogN)

Args:
    unsorted array of numbers or letters
Output:
    sorted array of number or letters

How to use:
    python merge_sort.py <space seperated numbers or letters>
"""

def merge_sort(list_to_sort):
    if len(list_to_sort) == 1:
        return

    pivot = len(list_to_sort) // 2

    first = list_to_sort[:pivot]
    second = list_to_sort[pivot:]

    merge_sort(first)
    merge_sort(second)

    left, right, index = 0, 0, 0

    while left < len(first) and right < len(second):
        if first[left] < second[right]:
            list_to_sort[index] = first[left]
            left += 1
        else:
            list_to_sort[index] = second[right]
            right += 1
        index += 1

    while left < len(first):
        list_to_sort[index] = first[left]
        index += 1
        left += 1

    while right < len(second):
        list_to_sort[index] = second[right]
        index += 1
        right += 1
    
    return list_to_sort

def main(args):
    import sys
    if not args:
        print('Need array to sort')
        sys.exit(1)
    else:
        try:
            int(args[0])
            a = [int(e) for e in args]
            print(merge_sort(a))
        except ValueError:
            print(merge_sort(args))

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
