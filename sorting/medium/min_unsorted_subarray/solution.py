"""
Minimum Length Unsorted Subarray

Given an unsorted array, find the minimum length subarray such that sorting
this subarray makes the complete array sorted.

Algorithm:
1. Find the leftmost index where order breaks (from left to right)
2. Find the rightmost index where order breaks (from right to left)
3. Find min and max in the subarray [left, right]
4. Extend left boundary if there are elements greater than min
5. Extend right boundary if there are elements smaller than max

Time Complexity: O(n) - Single pass to find boundaries, one pass for min/max,
                        and one pass each to extend boundaries
Space Complexity: O(1) - Only using a few variables
"""


def find_unsorted_subarray(arr):
    """
    Find the minimum length unsorted subarray.

    Args:
        arr: List of integers

    Returns:
        tuple: (start_index, end_index) of the unsorted subarray
               Returns (0, 0) if array is already sorted
    """
    n = len(arr)

    if n <= 1:
        return (0, 0)

    # Find the leftmost index where order breaks
    left = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            left = i
            break
    else:
        # Array is already sorted
        return (0, 0)

    # Find the rightmost index where order breaks
    right = n - 1
    for i in range(n - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            right = i
            break

    # Find min and max in the subarray [left, right]
    subarray_min = min(arr[left : right + 1])
    subarray_max = max(arr[left : right + 1])

    # Extend left boundary if there are elements greater than subarray_min
    start = left
    for i in range(left):
        if arr[i] > subarray_min:
            start = i
            break

    # Extend right boundary if there are elements smaller than subarray_max
    end = right
    for i in range(n - 1, right, -1):
        if arr[i] < subarray_max:
            end = i
            break

    return (start, end)


def find_unsorted_subarray_alternative(arr):
    """
    Alternative implementation using sorting for comparison.

    Args:
        arr: List of integers

    Returns:
        tuple: (start_index, end_index) of the unsorted subarray
    """
    n = len(arr)

    if n <= 1:
        return (0, 0)

    # Create sorted copy
    sorted_arr = sorted(arr)

    # Find first mismatch from left
    start = 0
    while start < n and arr[start] == sorted_arr[start]:
        start += 1

    # If no mismatch found, array is sorted
    if start == n:
        return (0, 0)

    # Find first mismatch from right
    end = n - 1
    while end >= 0 and arr[end] == sorted_arr[end]:
        end -= 1

    return (start, end)


def test_find_unsorted_subarray():
    """Test cases for minimum unsorted subarray algorithm."""
    # Test Case 1: Basic case
    arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
    result = find_unsorted_subarray(arr)
    expected = (3, 8)
    assert result == expected, f"Test 1 failed: Expected {expected}, got {result}"
    print("Test 1 passed: Basic case")

    # Test Case 2: Another example
    arr = [0, 1, 15, 25, 6, 7, 30, 40, 50]
    result = find_unsorted_subarray(arr)
    expected = (2, 5)
    assert result == expected, f"Test 2 failed: Expected {expected}, got {result}"
    print("Test 2 passed: Another example")

    # Test Case 3: Entire array unsorted
    arr = [30, 20, 10]
    result = find_unsorted_subarray(arr)
    expected = (0, 2)
    assert result == expected, f"Test 3 failed: Expected {expected}, got {result}"
    print("Test 3 passed: Entire array unsorted")

    # Test Case 4: Already sorted
    arr = [1, 2, 3, 4, 5]
    result = find_unsorted_subarray(arr)
    expected = (0, 0)
    assert result == expected, f"Test 4 failed: Expected {expected}, got {result}"
    print("Test 4 passed: Already sorted")

    # Test Case 5: Single element
    arr = [5]
    result = find_unsorted_subarray(arr)
    expected = (0, 0)
    assert result == expected, f"Test 5 failed: Expected {expected}, got {result}"
    print("Test 5 passed: Single element")

    # Test Case 6: Two elements unsorted
    arr = [2, 1]
    result = find_unsorted_subarray(arr)
    expected = (0, 1)
    assert result == expected, f"Test 6 failed: Expected {expected}, got {result}"
    print("Test 6 passed: Two elements unsorted")

    # Test Case 7: With duplicates
    arr = [1, 2, 4, 3, 3, 5, 6]
    result = find_unsorted_subarray(arr)
    expected_start, expected_end = 2, 4
    assert result[0] == expected_start and result[1] == expected_end, (
        f"Test 7 failed: Expected ({expected_start}, {expected_end}), got {result}"
    )
    print("Test 7 passed: With duplicates")

    # Test Case 8: Verify with alternative method
    test_arrays = [
        [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60],
        [0, 1, 15, 25, 6, 7, 30, 40, 50],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 3, 2, 4, 5],
    ]

    for i, arr in enumerate(test_arrays, 8):
        result1 = find_unsorted_subarray(arr)
        result2 = find_unsorted_subarray_alternative(arr)
        assert result1 == result2, (
            f"Test {i} failed: Methods disagree - O(n) gave {result1}, O(n log n) gave {result2}"
        )
        print(f"Test {i} passed: Verification with alternative method")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_find_unsorted_subarray()

    # Example usage
    print("\nExample:")
    arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
    start, end = find_unsorted_subarray(arr)
    print(f"Array: {arr}")
    print(f"Unsorted subarray indices: [{start}, {end}]")
    print(f"Unsorted subarray: {arr[start : end + 1]}")

    # Show that sorting this subarray sorts the entire array
    sorted_subarray = sorted(arr[start : end + 1])
    sorted_arr = arr[:start] + sorted_subarray + arr[end + 1 :]
    print(f"After sorting subarray: {sorted_arr}")
