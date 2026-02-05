"""
Interpolation Search

Problem:
Find the position of an element x in a sorted array using Interpolation Search.

Interpolation Search is an improvement over Binary Search for uniformly
distributed sorted arrays. Instead of always going to the middle element,
it goes to different locations according to the value of the key being
searched. The probe position is calculated using a formula similar to
linear interpolation.

Position = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])

Example:
    Input: arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23], key = 18
    Output: 4 (index of 18)

    Input: arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23], key = 25
    Output: -1 (not found)

Time Complexity:
    - Best/Average: O(log log n) - for uniformly distributed data
    - Worst: O(n) - when elements are exponentially distributed
Space Complexity: O(1) - iterative approach
"""


def interpolation_search(arr: list[int], key: int) -> int:
    """
    Search for a key using interpolation search algorithm.

    Uses linear interpolation formula to estimate the position of key,
    making it efficient for uniformly distributed data.

    Args:
        arr: Sorted array with uniformly distributed elements
        key: Element to search for

    Returns:
        Index of the key if found, -1 otherwise
    """
    if not arr:
        return -1

    low, high = 0, len(arr) - 1

    while low <= high and key >= arr[low] and key <= arr[high]:
        # If the array has same values
        if arr[low] == arr[high]:
            if arr[low] == key:
                return low
            return -1

        # Calculate probe position using interpolation formula
        # pos = low + ((key - arr[low]) * (high - low)) / (arr[high] - arr[low])
        pos = low + int(((key - arr[low]) * (high - low)) / (arr[high] - arr[low]))

        # Check if we found the key
        if arr[pos] == key:
            return pos

        # If key is larger, search right subarray
        if arr[pos] < key:
            low = pos + 1
        # If key is smaller, search left subarray
        else:
            high = pos - 1

    return -1


# Recursive implementation
def interpolation_search_recursive(
    arr: list[int], key: int, low: int, high: int
) -> int:
    """
    Recursive interpolation search implementation.

    Time Complexity: O(log log n) average, O(n) worst
    Space Complexity: O(log log n) - recursive stack
    """
    if low > high or key < arr[low] or key > arr[high]:
        return -1

    if arr[low] == arr[high]:
        if arr[low] == key:
            return low
        return -1

    # Calculate probe position
    pos = low + int(((key - arr[low]) * (high - low)) / (arr[high] - arr[low]))

    if arr[pos] == key:
        return pos

    if arr[pos] < key:
        return interpolation_search_recursive(arr, key, pos + 1, high)
    else:
        return interpolation_search_recursive(arr, key, low, pos - 1)


if __name__ == "__main__":
    # Test Case 1: Standard case (uniformly distributed)
    arr1 = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23]
    key1 = 18
    result = interpolation_search(arr1, key1)
    print(f"Test 1: arr={arr1}, key={key1}")
    print(f"Iterative Result: Index {result}")  # Expected: 4
    assert result == 4, "Test 1 iterative failed"

    result_rec = interpolation_search_recursive(arr1, key1, 0, len(arr1) - 1)
    print(f"Recursive Result: Index {result_rec}")
    assert result_rec == 4, "Test 1 recursive failed"

    # Test Case 2: Key not found
    arr2 = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23]
    key2 = 25
    result = interpolation_search(arr2, key2)
    print(f"\nTest 2: arr={arr2}, key={key2}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 2 failed"

    # Test Case 3: First element
    arr3 = [5, 10, 15, 20, 25, 30, 35, 40]
    key3 = 5
    result = interpolation_search(arr3, key3)
    print(f"\nTest 3: arr={arr3}, key={key3}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 3 failed"

    # Test Case 4: Last element
    arr4 = [5, 10, 15, 20, 25, 30, 35, 40]
    key4 = 40
    result = interpolation_search(arr4, key4)
    print(f"\nTest 4: arr={arr4}, key={key4}")
    print(f"Result: Index {result}")  # Expected: 7
    assert result == 7, "Test 4 failed"

    # Test Case 5: Single element
    arr5 = [42]
    key5 = 42
    result = interpolation_search(arr5, key5)
    print(f"\nTest 5: arr={arr5}, key={key5}")
    print(f"Result: Index {result}")  # Expected: 0
    assert result == 0, "Test 5 failed"

    # Test Case 6: Key smaller than all elements
    arr6 = [10, 20, 30, 40, 50]
    key6 = 5
    result = interpolation_search(arr6, key6)
    print(f"\nTest 6: arr={arr6}, key={key6}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 6 failed"

    # Test Case 7: Key larger than all elements
    arr7 = [10, 20, 30, 40, 50]
    key7 = 100
    result = interpolation_search(arr7, key7)
    print(f"\nTest 7: arr={arr7}, key={key7}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 7 failed"

    # Test Case 8: Duplicate elements
    arr8 = [1, 2, 2, 2, 3, 4, 4, 4, 5]
    key8 = 2
    result = interpolation_search(arr8, key8)
    print(f"\nTest 8: arr={arr8}, key={key8}")
    print(f"Result: Index {result}")  # Expected: any index with value 2
    assert result in [1, 2, 3], "Test 8 failed"

    # Test Case 9: Large uniformly distributed array
    arr9 = list(range(0, 1000, 2))  # [0, 2, 4, ..., 998]
    key9 = 500
    result = interpolation_search(arr9, key9)
    print(f"\nTest 9: arr size={len(arr9)}, key={key9}")
    print(f"Result: Index {result}")  # Expected: 250
    assert result == 250, "Test 9 failed"

    # Test Case 10: Empty array
    arr10 = []
    key10 = 10
    result = interpolation_search(arr10, key10)
    print(f"\nTest 10: arr={arr10}, key={key10}")
    print(f"Result: Index {result}")  # Expected: -1
    assert result == -1, "Test 10 failed"

    print("\nAll tests passed!")
