# Binary Search in python


def binary_search(array, x, low, high):

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binary_search(array, x, low, mid-1)

        # Search the right half
        else:
            return binary_search(array, x, mid + 1, high)

    else:
        return -1



test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1, 0, len(test_list)))
print(binary_search(test_list, test_val2, 0, len(test_list)))