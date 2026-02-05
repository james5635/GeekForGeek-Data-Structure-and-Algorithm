"""
Ceiling in a Sorted Array

Problem:
Given a sorted array and a value x, find the ceiling of x.
The ceiling is the smallest element >= x. Return the index
of first occurrence if multiple.

Examples:
Input: arr = [1, 2, 8, 10, 10, 12, 19], x = 5
Output: 2 (element 8)

Input: arr = [1, 2, 8, 10, 10, 12, 19], x = 20
Output: -1 (not found)

Input: arr = [1, 2, 8, 10, 10, 12, 19], x = 0
Output: 0 (element 1)

Approach:
Binary Search - Since array is sorted, use binary search to
find the smallest element >= x.

Time Complexity: O(log n)
Space Complexity: O(1)

Reference:
https://www.geeksforgeeks.org/dsa/ceiling-in-a-sorted-array/
"""

import bisect


def find_ceiling(arr, x):
    """
    Find index of ceiling of x in sorted array.

    Args:
        arr: Sorted list of integers
        x: Target value

    Returns:
        Index of ceiling element, or -1 if not exists
    """
    n = len(arr)

    if n == 0:
        return -1

    # If x <= first element, first is ceiling
    if x <= arr[0]:
        return 0

    # If x > last element, no ceiling
    if x > arr[-1]:
        return -1

    # Binary search
    left, right = 0, n - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] < x:
            left = mid + 1
        else:
            # Potential ceiling found
            result = mid
            right = mid - 1

    return result


def find_ceiling_builtin(arr, x):
    """
    Using Python's bisect module.
    """
    idx = bisect.bisect_left(arr, x)
    return idx if idx < len(arr) else -1


def find_floor(arr, x):
    """
    Bonus: Find floor (largest element <= x).
    """
    n = len(arr)

    if n == 0:
        return -1

    if x < arr[0]:
        return -1

    if x >= arr[-1]:
        return n - 1

    left, right = 0, n - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] > x:
            right = mid - 1
        else:
            result = mid
            left = mid + 1

    return result


def test_find_ceiling():
    """Test cases for find_ceiling function."""
    arr = [1, 2, 8, 10, 10, 12, 19]

    # Test case 1: x = 5
    assert find_ceiling(arr, 5) == 2

    # Test case 2: x = 20 (not exists)
    assert find_ceiling(arr, 20) == -1

    # Test case 3: x = 0
    assert find_ceiling(arr, 0) == 0

    # Test case 4: x = 1 (first element)
    assert find_ceiling(arr, 1) == 0

    # Test case 5: x = 19 (last element)
    assert find_ceiling(arr, 19) == 6

    # Test case 6: x = 10 (duplicate - first occurrence)
    assert find_ceiling(arr, 10) == 3

    # Test case 7: Single element
    assert find_ceiling([5], 3) == 0
    assert find_ceiling([5], 7) == -1

    # Test built-in version
    assert find_ceiling_builtin(arr, 5) == 2

    print("All test cases passed!")


if __name__ == "__main__":
    # Example usage
    arr = [1, 2, 8, 10, 10, 12, 19]
    x = 5
    print(f"Array: {arr}")
    print(f"x = {x}")
    idx = find_ceiling(arr, x)
    if idx != -1:
        print(f"Ceiling of {x} is {arr[idx]} at index {idx}")
    else:
        print(f"Ceiling of {x} doesn't exist")

    # Run tests
    test_find_ceiling()
