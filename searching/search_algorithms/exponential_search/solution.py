"""
Exponential Search

Problem:
Find the position of an element x in a sorted array using Exponential Search.

Exponential Search (also known as doubling search or galloping search)
involves two steps:
1. Find the range where the element could be present by repeatedly doubling
   the upper bound until we find an element greater than the key or reach end
2. Perform binary search in the found range

This is particularly useful when the key is near the beginning of the array.

Example:
    Input: arr = [2, 3, 4, 10, 40, 50, 60, 70], key = 10
    Output: 3 (index of 10)

    Input: arr = [2, 3, 4, 10, 40, 50, 60, 70], key = 100
    Output: -1 (not found)

Time Complexity: O(log n) - same as binary search
Space Complexity: O(1) - iterative approach
"""


def exponential_search(arr: list[int], key: int) -> int:
    """
    Search for a key using exponential search algorithm.

    First finds the range where key could be by exponentially
    increasing bounds, then performs binary search in that range.

    Args:
        arr: Sorted array to search in
        key: Element to search for

    Returns:
        Index of the key if found, -1 otherwise
    """
    if not arr:
        return -1

    n = len(arr)

    # If key is at first position
    if arr[0] == key:
        return 0

    # Find the range for binary search by repeated doubling
    bound = 1
    while bound < n and arr[bound] <= key:
        bound *= 2

    # Perform binary search in the found range
    # Range is from bound//2 to min(bound, n-1)
    return binary_search_range(arr, key, bound // 2, min(bound, n - 1))


def binary_search_range(arr: list[int], key: int, low: int, high: int) -> int:
    """Helper function for binary search in a given range."""
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Alternative: More explicit implementation
def exponential_search_v2(arr: list[int], key: int) -> int:
    """
    Alternative exponential search with explicit steps.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if not arr:
        return -1

    n = len(arr)

    # Check first element
    if arr[0] == key:
        return 0

    # Find range by exponential steps
    i = 1
    while i < n and arr[i] <= key:
        i = i * 2

    # Binary search between i/2 and min(i, n-1)
    left = i // 2
    right = min(i, n - 1)

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    # Test Case 1: Standard case
    arr1 = [2, 3, 4, 10, 40, 50, 60, 70]
    key1 = 10
    result = exponential_search(arr1, key1)
    print(f"Test 1: arr={arr1}, key={key1}")
    print(f"Result: Index {result}")  # Expected: 3
    assert result == 3, "Test 1 failed"

    # Test Case 2: Key not found
    arr2 = [2, 3, 4, 10, 40, 50, 60, 70]
    key2 = 100
    result = exponential_search(arr2, key2)
    print(f"\nTest 2: arr={arr2}, key={key2}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 2 failed"

    # Test Case 3: First element
    arr3 = [10, 20, 30, 40, 50]
    key3 = 10
    result = exponential_search(arr3, key3)
    print(f"\nTest 3: arr={arr3}, key={key3}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 3 failed"

    # Test Case 4: Last element
    arr4 = [2, 3, 4, 10, 40, 50, 60, 70]
    key4 = 70
    result = exponential_search(arr4, key4)
    print(f"\nTest 4: arr={arr4}, key={key4}")
    print(f"Result: Index {result}")  # Expected: 7
    assert result == 7, "Test 4 failed"

    # Test Case 5: Single element
    arr5 = [42]
    key5 = 42
    result = exponential_search(arr5, key5)
    print(f"\nTest 5: arr={arr5}, key={key5}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 5 failed"

    # Test Case 6: Two elements
    arr6 = [5, 10]
    key6 = 10
    result = exponential_search(arr6, key6)
    print(f"\nTest 6: arr={arr6}, key={key6}")
    print(f"Result: Index {result}")  # Expected: 1
    assert result == 1, "Test 6 failed"

    # Test Case 7: Large array
    arr7 = list(range(0, 1000, 5))  # [0, 5, 10, ..., 995]
    key7 = 555
    result = exponential_search(arr7, key7)
    print(f"\nTest 7: arr size={len(arr7)}, key={key7}")
    print(f"Result: Index {result}")  # Expected: 111
    assert result == 111, "Test 7 failed"

    # Test Case 8: Compare v2
    arr8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    key8 = 9
    result1 = exponential_search(arr8, key8)
    result2 = exponential_search_v2(arr8, key8)
    print(f"\nTest 8: arr={arr8}, key={key8}")
    print(f"V1 Result: Index {result1}")
    print(f"V2 Result: Index {result2}")
    assert result1 == result2 == 8, "Test 8 failed"

    # Test Case 9: Empty array
    arr9 = []
    key9 = 10
    result = exponential_search(arr9, key9)
    print(f"\nTest 9: arr={arr9}, key={key9}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 9 failed"

    # Test Case 10: Key near beginning (exponential search advantage)
    arr10 = list(range(1, 10001))
    key10 = 5  # Very close to start
    result = exponential_search(arr10, key10)
    print(f"\nTest 10: Large arr, key near beginning: {key10}")
    print(f"Result: Index {result}")  # Expected: 4
    assert result == 4, "Test 10 failed"

    print("\nAll tests passed!")
