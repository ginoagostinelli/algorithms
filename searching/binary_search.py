"""
Binary Search

Time Complexity: O(log(n))

"""

def binary_search(sorted_array: list[int], target: int) -> int:

    left, right = 0, len(sorted_array) - 1

    while left <= right:
        mid = left + (right - left) // 2
        val = sorted_array[mid]

        if target < val:
            right = mid - 1
        elif target > val:
            left = mid + 1
        else:
            return mid

    return -1

def binary_search_by_recursion(sorted_array: list[int], target: int, left: int, right: int) -> int:

    if left > right:
        return -1

    mid = left + (right - left) // 2
    val = sorted_array[mid]
    
    if target < val:
         return binary_search_by_recursion(sorted_array, target, left, mid - 1)
    elif target > val:
         return binary_search_by_recursion(sorted_array, target, mid + 1, right)
    else:
        return mid

