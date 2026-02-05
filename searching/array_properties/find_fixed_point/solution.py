"""
Find a Fixed Point in a Given Array

Problem Description:
Given a sorted array of distinct elements, find a Fixed Point where
arr[i] == i. Return -1 if no such element exists.

Example:
    Input: [-10, -1, 0, 3, 10, 11, 30, 50, 100]
    Output: 3 (since arr[3] == 3)

Time Complexity: O(log n)
Space Complexity: O(1)

Approach: Modified Binary Search
    Since array is sorted, if arr[mid] < mid, fixed point must be on right
    If arr[mid] > mid, fixed point must be on left
"""


def find_fixed_point(arr):
    """
    Find fixed point using binary search.

    Args:
        arr: Sorted array of distinct integers

    Returns:
        Index where arr[i] == i, or -1 if not found
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def find_fixed_point_linear(arr):
    """
    Find fixed point using linear search.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: Array of integers

    Returns:
        Index where arr[i] == i, or -1 if not found
    """
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return -1


def test_find_fixed_point():
    """Test cases for find_fixed_point."""
    # Test case 1: Basic example
    arr1 = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
    assert find_fixed_point(arr1) == 3
    assert find_fixed_point_linear(arr1) == 3

    # Test case 2: No fixed point
    arr2 = [-10, -5, 0, 5, 10]
    assert find_fixed_point(arr2) == -1
    assert find_fixed_point_linear(arr2) == -1

    # Test case 3: Fixed point at start
    arr3 = [0, 2, 3, 4, 5]
    assert find_fixed_point(arr3) == 0
    assert find_fixed_point_linear(arr3) == 0

    # Test case 4: Fixed point at end
    arr4 = [-5, -4, -3, -2, 4]
    assert find_fixed_point(arr4) == 4
    assert find_fixed_point_linear(arr4) == 4

    # Test case 5: Single element with fixed point
    arr5 = [0]
    assert find_fixed_point(arr5) == 0
    assert find_fixed_point_linear(arr5) == 0

    # Test case 6: Single element without fixed point
    arr6 = [5]
    assert find_fixed_point(arr6) == -1
    assert find_fixed_point_linear(arr6) == -1

    # Test case 7: Multiple fixed points (only returns first found)
    arr7 = [-5, 1, 2, 3, 4]
    result = find_fixed_point(arr7)
    assert arr7[result] == result if result != -1 else True

    print("All test cases passed!")


if __name__ == "__main__":
    test_find_fixed_point()
