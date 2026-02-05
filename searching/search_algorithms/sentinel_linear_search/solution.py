"""
Sentinel Linear Search

Problem:
Search for an element x in an array using Sentinel Linear Search.

The sentinel linear search is a variation of standard linear search that
reduces the number of comparisons by placing the target element at the end
of the array as a sentinel. This eliminates the need to check for the end
of array condition in each iteration.

Example:
    Input: arr = [10, 20, 180, 30, 50, 60], key = 180
    Output: 2 (index of 180)

    Input: arr = [10, 20, 180, 30, 50, 60], key = 90
    Output: -1 (not found)

Time Complexity: O(n) - may need to scan entire array
Space Complexity: O(1) - no extra space needed
"""


def sentinel_linear_search(arr: list[int], key: int) -> int:
    """
    Search for a key using sentinel linear search algorithm.

    This algorithm places the key at the end of the array temporarily
    and searches from the beginning. This eliminates one comparison
    per iteration (no need to check if we've reached the end).

    Args:
        arr: Array to search in
        key: Element to search for

    Returns:
        Index of the key if found, -1 otherwise
    """
    if not arr:
        return -1

    n = len(arr)
    last = arr[n - 1]  # Store the last element
    arr[n - 1] = key  # Place sentinel

    i = 0
    while arr[i] != key:
        i += 1

    arr[n - 1] = last  # Restore the last element

    # Check if we found it in the original array
    if i < n - 1 or last == key:
        return i

    return -1


# Alternative without modifying array
def sentinel_linear_search_no_modify(arr: list[int], key: int) -> int:
    """
    Sentinel search without modifying the original array.
    Creates a copy with sentinel appended.

    Time Complexity: O(n)
    Space Complexity: O(n) - creates a copy
    """
    if not arr:
        return -1

    # Create array with sentinel
    temp = arr + [key]

    i = 0
    while temp[i] != key:
        i += 1

    # If found within original bounds
    if i < len(arr):
        return i

    return -1


if __name__ == "__main__":
    # Test Case 1: Standard case
    arr1 = [10, 20, 180, 30, 50, 60]
    key1 = 180
    result = sentinel_linear_search(arr1.copy(), key1)
    print(f"Test 1: arr={arr1}, key={key1}")
    print(f"Result: Index {result}")  # Expected: 2
    assert result == 2, "Test 1 failed"

    # Test Case 2: Key not found
    arr2 = [10, 20, 180, 30, 50, 60]
    key2 = 90
    result = sentinel_linear_search(arr2.copy(), key2)
    print(f"\nTest 2: arr={arr2}, key={key2}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 2 failed"

    # Test Case 3: Key at beginning
    arr3 = [10, 20, 30, 40, 50]
    key3 = 10
    result = sentinel_linear_search(arr3.copy(), key3)
    print(f"\nTest 3: arr={arr3}, key={key3}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 3 failed"

    # Test Case 4: Key at end
    arr4 = [10, 20, 30, 40, 50]
    key4 = 50
    result = sentinel_linear_search(arr4.copy(), key4)
    print(f"\nTest 4: arr={arr4}, key={key4}")
    print(f"Result: Index {result}")  # Expected: 4
    assert result == 4, "Test 4 failed"

    # Test Case 5: Single element found
    arr5 = [42]
    key5 = 42
    result = sentinel_linear_search(arr5.copy(), key5)
    print(f"\nTest 5: arr={arr5}, key={key5}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 5 failed"

    # Test Case 6: Single element not found
    arr6 = [42]
    key6 = 100
    result = sentinel_linear_search(arr6.copy(), key6)
    print(f"\nTest 6: arr={arr6}, key={key6}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 6 failed"

    # Test Case 7: Empty array
    arr7 = []
    key7 = 10
    result = sentinel_linear_search(arr7.copy(), key7)
    print(f"\nTest 7: arr={arr7}, key={key7}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 7 failed"

    # Test Case 8: Duplicate elements
    arr8 = [1, 2, 3, 2, 4, 2, 5]
    key8 = 2
    result = sentinel_linear_search(arr8.copy(), key8)
    print(f"\nTest 8: arr={arr8}, key={key8}")
    print(f"Result: Index {result}")  # Expected: 1 (first occurrence)
    assert result == 1, "Test 8 failed"

    # Test non-modifying version
    arr9 = [10, 20, 30, 40]
    key9 = 30
    result = sentinel_linear_search_no_modify(arr9, key9)
    print(f"\nTest 9 (no-modify): arr={arr9}, key={key9}")
    print(f"Result: Index {result}")  # Expected: 2
    assert result == 2, "Test 9 failed"

    print("\nAll tests passed!")
