"""
Search in an Almost Sorted Array

Problem:
Given an array that is sorted but some adjacent elements are swapped,
search for an element x in the array.

An almost sorted array means each element is at most one position away
from its correct position in the sorted array.

Example:
    Input: arr = [10, 3, 40, 20, 50, 80, 70], key = 40
    Output: 2 (index of 40)

    Input: arr = [10, 3, 40, 20, 50, 80, 70], key = 90
    Output: -1 (not found)

Time Complexity: O(log n) - modified binary search
Space Complexity: O(1) - iterative approach
"""


def search_almost_sorted(arr: list[int], key: int) -> int:
    """
    Search for a key in an almost sorted array.

    In an almost sorted array, an element that should be at index i
    in a sorted array can be at index i, i-1, or i+1.

    Args:
        arr: Almost sorted array
        key: Element to search for

    Returns:
        Index of the key if found, -1 otherwise
    """
    if not arr:
        return -1

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check mid and its neighbors
        if arr[mid] == key:
            return mid

        if mid > low and arr[mid - 1] == key:
            return mid - 1

        if mid < high and arr[mid + 1] == key:
            return mid + 1

        # Decide which half to search
        if key < arr[mid]:
            high = mid - 2  # Skip checked elements
        else:
            low = mid + 2  # Skip checked elements

    return -1


if __name__ == "__main__":
    # Test Case 1: Standard almost sorted array
    arr1 = [10, 3, 40, 20, 50, 80, 70]
    key1 = 40
    result = search_almost_sorted(arr1, key1)
    print(f"Test 1: arr={arr1}, key={key1}")
    print(f"Result: Index {result}")  # Expected: 2
    assert result == 2, "Test 1 failed"

    # Test Case 2: Key not in array
    arr2 = [10, 3, 40, 20, 50, 80, 70]
    key2 = 90
    result = search_almost_sorted(arr2, key2)
    print(f"\nTest 2: arr={arr2}, key={key2}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 2 failed"

    # Test Case 3: Key at beginning (swapped)
    arr3 = [3, 10, 20, 40, 50]
    key3 = 3
    result = search_almost_sorted(arr3, key3)
    print(f"\nTest 3: arr={arr3}, key={key3}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 3 failed"

    # Test Case 4: Key at end (swapped with previous)
    arr4 = [10, 20, 30, 50, 40]
    key4 = 40
    result = search_almost_sorted(arr4, key4)
    print(f"\nTest 4: arr={arr4}, key={key4}")
    print(f"Result: Index {result}")  # Expected: 4
    assert result == 4, "Test 4 failed"

    # Test Case 5: Single element
    arr5 = [5]
    key5 = 5
    result = search_almost_sorted(arr5, key5)
    print(f"\nTest 5: arr={arr5}, key={key5}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 5 failed"

    # Test Case 6: Empty array
    arr6 = []
    key6 = 5
    result = search_almost_sorted(arr6, key6)
    print(f"\nTest 6: arr={arr6}, key={key6}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 6 failed"

    # Test Case 7: All adjacent swapped
    arr7 = [2, 1, 4, 3, 6, 5, 8, 7]
    key7 = 6
    result = search_almost_sorted(arr7, key7)
    print(f"\nTest 7: arr={arr7}, key={key7}")
    print(f"Result: Index {result}")  # Expected: 4
    assert result == 4, "Test 7 failed"

    print("\nAll tests passed!")
