"""
    Merge Sort
    Time Complexity: O(n log(n))
"""

def merge_sort(collection: list) -> list:
    
    if len(collection) <= 1:
        return collection

    mid = len(collection) // 2

    return _merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))

def _merge(leftCollection: list, rightCollection: list) -> list:
    """
        Merge  
        Time Complexity: O(n)
    """

    l_cursor = r_cursor = 0
    merged = []

    while l_cursor < len(leftCollection) and r_cursor < len(rightCollection):
        if leftCollection[l_cursor] <= rightCollection[r_cursor]:
            merged.append(leftCollection[l_cursor])
            l_cursor += 1
        else:
            merged.append(rightCollection[r_cursor])
            r_cursor += 1
    
    for l_cursor in range(l_cursor, len(leftCollection)):
        merged.append(leftCollection[l_cursor])

    for r_cursor in range(r_cursor, len(rightCollection)):
        merged.append(rightCollection[r_cursor])
    

    return merged

if __name__ == "main":

    a = [1, 4, 5, 8, 0, 1, 2, 100]

    for i in a:
        print(i)