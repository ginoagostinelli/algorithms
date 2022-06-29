"""
Binary Search

Time Complexity: O(log(n))

"""

def binary_search(array, target) -> int:

    left, right = 0, len(array) - 1

    while left <= right:
        mid = (right + left) // 2
        val = array[mid]

        if target < val:
            right = mid - 1
        elif target > val:
            left = mid + 1
        else:
            return mid

    return -1

