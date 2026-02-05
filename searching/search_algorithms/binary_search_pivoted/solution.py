"""
Binary Search on Pivoted (Rotated) Array

Problem:
Given a sorted and rotated array arr[] of n distinct elements,
find if there is an element x in the array.

A sorted array is rotated at some pivot point. For example,
[0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].

Example:
    Input: arr = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 3
    Output: 8 (index of 3)

    Input: arr = [5, 6, 7, 8, 9, 10, 1, 2, 3], key = 30
    Output: -1 (not found)

Time Complexity: O(log n) - binary search approach
Space Complexity: O(1) - iterative approach
"""


def find_pivot(arr: list[int]) -> int:
    """Find the pivot index where array is rotated."""
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    return low


def binary_search(arr: list[int], low: int, high: int, key: int) -> int:
    """Standard binary search on a sorted subarray."""
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def search_pivoted_array(arr: list[int], key: int) -> int:
    """
    Search for a key in a sorted and pivoted array.

    Args:
        arr: Sorted and rotated array of distinct elements
        key: Element to search for

    Returns:
        Index of the key if found, -1 otherwise
    """
    if not arr:
        return -1

    n = len(arr)
    pivot = find_pivot(arr)

    # If array is not rotated, do normal binary search
    if pivot == 0:
        return binary_search(arr, 0, n - 1, key)

    # Check if key is in first half or second half
    if key >= arr[0]:
        return binary_search(arr, 0, pivot - 1, key)
    else:
        return binary_search(arr, pivot, n - 1, key)


# Alternative approach - single pass
def search_pivoted_single_pass(arr: list[int], key: int) -> int:
    """
    Search in rotated sorted array using single binary search.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if not arr:
        return -1

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        # Check if left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


if __name__ == "__main__":
    # Test Case 1: Standard rotated array
    arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key1 = 3
    result = search_pivoted_single_pass(arr1, key1)
    print(f"Test 1: arr={arr1}, key={key1}")
    print(f"Result: Index {result}")  # Expected: 8
    assert result == 8, "Test 1 failed"

    # Test Case 2: Key not in array
    arr2 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key2 = 30
    result = search_pivoted_single_pass(arr2, key2)
    print(f"\nTest 2: arr={arr2}, key={key2}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 2 failed"

    # Test Case 3: Single element
    arr3 = [1]
    key3 = 1
    result = search_pivoted_single_pass(arr3, key3)
    print(f"\nTest 3: arr={arr3}, key={key3}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 3 failed"

    # Test Case 4: Not rotated
    arr4 = [1, 2, 3, 4, 5]
    key4 = 3
    result = search_pivoted_single_pass(arr4, key4)
    print(f"\nTest 4: arr={arr4}, key={key4}")
    print(f"Result: Index {result}")  # Expected: 2
    assert result == 2, "Test 4 failed"

    # Test Case 5: Key at pivot
    arr5 = [4, 5, 6, 7, 0, 1, 2]
    key5 = 0
    result = search_pivoted_single_pass(arr5, key5)
    print(f"\nTest 5: arr={arr5}, key={key5}")
    print(f"Result: Index {result}")  # Expected: 4
    assert result == 4, "Test 5 failed"

    print("\nAll tests passed!")
