"""
Ternary Search

Problem:
Find the position of an element x in a sorted array using Ternary Search.

Ternary Search is a divide-and-conquer algorithm similar to binary search
but divides the array into three parts instead of two. It compares the
target with elements at two mid points (1/3 and 2/3 positions).

This is useful for unimodal functions (finding maximum/minimum) but can
also be used for searching in sorted arrays.

Example:
    Input: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key = 5
    Output: 4 (index of 5)

    Input: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key = 50
    Output: -1 (not found)

Time Complexity: O(log₃ n) ≈ O(log n) - divides array into 3 parts
Space Complexity: O(1) - iterative, O(log n) - recursive
"""


def ternary_search_recursive(arr: list[int], key: int, low: int, high: int) -> int:
    """
    Recursive ternary search implementation.

    Args:
        arr: Sorted array to search in
        key: Element to search for
        low: Lower bound index
        high: Upper bound index

    Returns:
        Index of the key if found, -1 otherwise
    """
    if low > high:
        return -1

    # Divide array into three parts
    mid1 = low + (high - low) // 3
    mid2 = high - (high - low) // 3

    if arr[mid1] == key:
        return mid1
    if arr[mid2] == key:
        return mid2

    # Search in appropriate third
    if key < arr[mid1]:
        return ternary_search_recursive(arr, key, low, mid1 - 1)
    elif key > arr[mid2]:
        return ternary_search_recursive(arr, key, mid2 + 1, high)
    else:
        return ternary_search_recursive(arr, key, mid1 + 1, mid2 - 1)


def ternary_search_iterative(arr: list[int], key: int) -> int:
    """
    Iterative ternary search implementation.

    Time Complexity: O(log₃ n)
    Space Complexity: O(1)
    """
    if not arr:
        return -1

    low, high = 0, len(arr) - 1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2

        if key < arr[mid1]:
            high = mid1 - 1
        elif key > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1

    return -1


# Ternary search for finding maximum in unimodal array
def ternary_search_maximum(arr: list[int]) -> int:
    """
    Find the maximum element in a unimodal array using ternary search.

    A unimodal array increases then decreases (or vice versa).

    Time Complexity: O(log₃ n)
    Space Complexity: O(1)
    """
    if not arr:
        return -1

    if len(arr) == 1:
        return arr[0]

    low, high = 0, len(arr) - 1

    while high - low > 3:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] < arr[mid2]:
            low = mid1
        else:
            high = mid2

    # Linear search in small range
    max_val = arr[low]
    for i in range(low + 1, high + 1):
        if arr[i] > max_val:
            max_val = arr[i]

    return max_val


if __name__ == "__main__":
    # Test Case 1: Standard case
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key1 = 5
    result = ternary_search_iterative(arr1, key1)
    print(f"Test 1: arr={arr1}, key={key1}")
    print(f"Iterative Result: Index {result}")  # Expected: 4
    assert result == 4, "Test 1 iterative failed"

    result_rec = ternary_search_recursive(arr1, key1, 0, len(arr1) - 1)
    print(f"Recursive Result: Index {result_rec}")
    assert result_rec == 4, "Test 1 recursive failed"

    # Test Case 2: Key not found
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key2 = 50
    result = ternary_search_iterative(arr2, key2)
    print(f"\nTest 2: arr={arr2}, key={key2}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 2 failed"

    # Test Case 3: Single element
    arr3 = [42]
    key3 = 42
    result = ternary_search_iterative(arr3, key3)
    print(f"\nTest 3: arr={arr3}, key={key3}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 3 failed"

    # Test Case 4: Two elements
    arr4 = [10, 20]
    key4 = 20
    result = ternary_search_iterative(arr4, key4)
    print(f"\nTest 4: arr={arr4}, key={key4}")
    print(f"Result: Index {result}")  # Expected: 1
    assert result == 1, "Test 4 failed"

    # Test Case 5: First element
    arr5 = [5, 10, 15, 20, 25]
    key5 = 5
    result = ternary_search_iterative(arr5, key5)
    print(f"\nTest 5: arr={arr5}, key={key5}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 5 failed"

    # Test Case 6: Last element
    arr6 = [5, 10, 15, 20, 25]
    key6 = 25
    result = ternary_search_iterative(arr6, key6)
    print(f"\nTest 6: arr={arr6}, key={key6}")
    print(f"Result: Index {result}")  # Expected: 4
    assert result == 4, "Test 6 failed"

    # Test Case 7: Maximum in unimodal array
    arr7 = [1, 3, 5, 7, 9, 11, 10, 8, 6, 4, 2]
    result_max = ternary_search_maximum(arr7)
    print(f"\nTest 7 (Unimodal max): arr={arr7}")
    print(f"Maximum: {result_max}")  # Expected: 11
    assert result_max == 11, "Test 7 failed"

    # Test Case 8: Empty array
    arr8 = []
    key8 = 10
    result = ternary_search_iterative(arr8, key8)
    print(f"\nTest 8: arr={arr8}, key={key8}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 8 failed"

    print("\nAll tests passed!")
