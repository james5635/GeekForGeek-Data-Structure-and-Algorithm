"""
Find Partition Point in Array

Problem Description:
Given an array, find a partition point such that all elements
before it are smaller and all elements after it are greater.
Return -1 if no such partition point exists.

Example:
    Input: [5, 1, 4, 3, 6, 8, 10, 7, 9]
    Output: 4 (index 4, element 6)
    Explanation: All elements before 6 are smaller [5, 1, 4, 3]
                 All elements after 6 are greater [8, 10, 7, 9]

Time Complexity: O(n)
Space Complexity: O(n)

Approach: Precompute max from left and min from right arrays
    For each index i, check if max_left[i-1] < arr[i] < min_right[i+1]
"""


def find_partition_point(arr):
    """
    Find partition point using prefix max and suffix min arrays.

    Args:
        arr: Array of integers

    Returns:
        Index of partition point, or -1 if not found
    """
    n = len(arr)

    if n < 3:
        return -1

    # max_left[i] = maximum element from arr[0] to arr[i]
    max_left = [0] * n
    max_left[0] = arr[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], arr[i])

    # min_right[i] = minimum element from arr[i] to arr[n-1]
    min_right = [0] * n
    min_right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], arr[i])

    # Find partition point (excluding first and last elements)
    for i in range(1, n - 1):
        if max_left[i - 1] < arr[i] < min_right[i + 1]:
            return i

    return -1


def find_partition_point_optimized(arr):
    """
    Find partition point with O(n) space (similar to main function).

    Time Complexity: O(n)
    Space Complexity: O(n) - using arrays for clarity

    Args:
        arr: Array of integers

    Returns:
        Index of partition point, or -1 if not found
    """
    n = len(arr)

    if n < 3:
        return -1

    # max_left[i] = maximum element from arr[0] to arr[i]
    max_left = [0] * n
    max_left[0] = arr[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], arr[i])

    # min_right[i] = minimum element from arr[i] to arr[n-1]
    min_right = [0] * n
    min_right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], arr[i])

    # Find partition point (excluding first and last elements)
    for i in range(1, n - 1):
        if max_left[i - 1] < arr[i] < min_right[i + 1]:
            return i

    return -1

    # Compute min from right in O(n) time, O(1) space
    # We traverse from right and check each position
    # For O(1) space, we need to precompute right min differently

    # First, find overall min from right for each position
    # We do two passes: one to find min from right, one to find partition
    # But for true O(1) space, we'd need to recalculate, so let's use
    # a simpler approach with single pass from right

    # Actually, let's use a different O(1) space approach:
    # Find the leftmost position where all left elements are smaller
    # and all right elements are greater

    # First pass: track max so far
    max_so_far = [arr[0]] * n
    for i in range(1, n):
        max_so_far[i] = max(max_so_far[i - 1], arr[i])

    # Second pass: from right, check if current is partition
    min_from_right = float("inf")
    for i in range(n - 1, 0, -1):
        if max_so_far[i - 1] < arr[i] < min_from_right:
            return i
        min_from_right = min(min_from_right, arr[i])

    return -1


def test_find_partition_point():
    """Test cases for find_partition_point."""
    # Test case 1: Basic example
    arr1 = [5, 1, 4, 3, 6, 8, 10, 7, 9]
    assert find_partition_point(arr1) == 4
    assert find_partition_point_optimized(arr1) == 4

    # Test case 2: No partition point
    arr2 = [5, 5, 5, 5]
    assert find_partition_point(arr2) == -1
    assert find_partition_point_optimized(arr2) == -1

    # Test case 3: Single valid partition
    arr3 = [1, 2, 3, 4, 5]
    # 2 at index 1: left max is 1, right min is 3
    # 1 < 2 < 3, so partition at index 1
    assert find_partition_point(arr3) == 1
    assert find_partition_point_optimized(arr3) == 1

    # Test case 4: Multiple partition points (returns first)
    arr4 = [1, 2, 5, 3, 6, 8, 7, 9]
    result = find_partition_point(arr4)
    assert result != -1

    # Test case 5: Simple valid case
    arr5 = [1, 3, 2, 4, 5]
    # 4 at index 3: left elements [1, 3, 2] all < 4, right [5] all > 4
    assert find_partition_point(arr5) == 3
    assert find_partition_point_optimized(arr5) == 3

    # Test case 6: Minimum valid array
    arr6 = [1, 2, 3]
    assert find_partition_point(arr6) == 1
    assert find_partition_point_optimized(arr6) == 1

    # Test case 7: All decreasing
    arr7 = [5, 4, 3, 2, 1]
    assert find_partition_point(arr7) == -1
    assert find_partition_point_optimized(arr7) == -1

    print("All test cases passed!")


if __name__ == "__main__":
    test_find_partition_point()
