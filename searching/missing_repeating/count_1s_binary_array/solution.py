"""
Count 1s in a Sorted Binary Array

Problem Description:
Given a sorted binary array (containing only 0s and 1s),
count the number of 1s in the array.

Example:
    Input: [0, 0, 0, 1, 1, 1, 1]
    Output: 4

Time Complexity: O(log n)
Space Complexity: O(1)

Approach: Binary search to find the first occurrence of 1
    All 1s appear after 0s in sorted binary array
    Count = n - index_of_first_1
"""


def count_ones(arr):
    """
    Count the number of 1s in a sorted binary array.

    Args:
        arr: Sorted binary array containing 0s followed by 1s

    Returns:
        Count of 1s in the array
    """
    n = len(arr)

    if n == 0 or arr[-1] == 0:
        return 0

    if arr[0] == 1:
        return n

    # Binary search for first occurrence of 1
    left, right = 0, n - 1
    first_one_index = n

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == 1:
            first_one_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return n - first_one_index


def count_ones_linear(arr):
    """
    Count ones using linear search (for comparison).

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: Sorted binary array

    Returns:
        Count of 1s
    """
    count = 0
    for num in reversed(arr):
        if num == 1:
            count += 1
        else:
            break
    return count


def test_count_ones():
    """Test cases for count_ones."""
    # Test case 1: Basic example
    arr1 = [0, 0, 0, 1, 1, 1, 1]
    assert count_ones(arr1) == 4
    assert count_ones_linear(arr1) == 4

    # Test case 2: All 0s
    arr2 = [0, 0, 0, 0]
    assert count_ones(arr2) == 0
    assert count_ones_linear(arr2) == 0

    # Test case 3: All 1s
    arr3 = [1, 1, 1, 1, 1]
    assert count_ones(arr3) == 5
    assert count_ones_linear(arr3) == 5

    # Test case 4: Single 1
    arr4 = [0, 0, 1]
    assert count_ones(arr4) == 1
    assert count_ones_linear(arr4) == 1

    # Test case 5: Single 0
    arr5 = [0, 1, 1, 1]
    assert count_ones(arr5) == 3
    assert count_ones_linear(arr5) == 3

    # Test case 6: Empty array
    arr6 = []
    assert count_ones(arr6) == 0
    assert count_ones_linear(arr6) == 0

    # Test case 7: Single element 0
    arr7 = [0]
    assert count_ones(arr7) == 0
    assert count_ones_linear(arr7) == 0

    # Test case 8: Single element 1
    arr8 = [1]
    assert count_ones(arr8) == 1
    assert count_ones_linear(arr8) == 1

    print("All test cases passed!")


if __name__ == "__main__":
    test_count_ones()
