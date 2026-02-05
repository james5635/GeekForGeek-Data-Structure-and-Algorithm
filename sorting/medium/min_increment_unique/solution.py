"""
Minimum Increment to Make Array Unique

Problem Description:
    Given an array of integers, find the minimum number of increment operations
    required to make all elements in the array unique.

Time Complexity: O(n log n)
- Sorting the array: O(n log n)
- Single pass through array: O(n)

Space Complexity: O(1) auxiliary
- Sorting may use O(log n) or O(n) depending on implementation
- Only using a few variables for tracking

Example:
    Input: arr = [1, 2, 2]
    Output: 1
    Explanation: We need to increment one of the 2s by 1 to make it 3.
                 Total increments = 1

    Input: arr = [3, 2, 1, 2, 1, 7]
    Output: 6
    Explanation: After increment operations:
                 [3, 2, 1, 2, 1, 7] -> [3, 4, 1, 2, 5, 7]
                 Increments: 2->4 (2), 1->5 (4), Total = 6

Approach:
    1. Sort the array
    2. Traverse through array, ensuring each element is at least 1 greater than previous
    3. Keep track of total increments needed
"""

from typing import List


def min_increment_for_unique(arr: List[int]) -> int:
    """
    Find minimum increments needed to make all array elements unique.

    Args:
        arr: List of integers

    Returns:
        Minimum number of increments required
    """
    if not arr or len(arr) <= 1:
        return 0

    # Sort the array
    arr.sort()

    increments = 0

    # Traverse through array starting from second element
    for i in range(1, len(arr)):
        # If current element is not greater than previous
        if arr[i] <= arr[i - 1]:
            # We need to increment current element to be arr[i-1] + 1
            needed = arr[i - 1] + 1
            increments += needed - arr[i]
            arr[i] = needed

    return increments


def min_increment_for_unique_optimized(arr: List[int]) -> int:
    """
    Optimized version using only O(1) extra space (modifies input).

    Args:
        arr: List of integers

    Returns:
        Minimum number of increments required
    """
    if not arr or len(arr) <= 1:
        return 0

    arr.sort()
    increments = 0

    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            increments += arr[i - 1] - arr[i] + 1
            arr[i] = arr[i - 1] + 1

    return increments


# Test cases
def test_min_increment_for_unique():
    """Test cases for min_increment_for_unique function."""
    # Test case 1: Basic example from problem
    arr1 = [1, 2, 2]
    assert min_increment_for_unique(arr1.copy()) == 1, "Test 1 failed"

    # Test case 2: Another example from problem
    arr2 = [3, 2, 1, 2, 1, 7]
    assert min_increment_for_unique(arr2.copy()) == 6, "Test 2 failed"

    # Test case 3: All unique elements
    arr3 = [1, 2, 3, 4, 5]
    assert min_increment_for_unique(arr3.copy()) == 0, "Test 3 failed"

    # Test case 4: All same elements
    arr4 = [1, 1, 1, 1]
    # [1,1,1,1] -> [1,2,3,4], increments = 0+1+2+3 = 6
    assert min_increment_for_unique(arr4.copy()) == 6, "Test 4 failed"

    # Test case 5: Empty array
    arr5 = []
    assert min_increment_for_unique(arr5) == 0, "Test 5 failed"

    # Test case 6: Single element
    arr6 = [5]
    assert min_increment_for_unique(arr6.copy()) == 0, "Test 6 failed"

    # Test case 7: Two same elements
    arr7 = [5, 5]
    assert min_increment_for_unique(arr7.copy()) == 1, "Test 7 failed"

    # Test case 8: Negative numbers
    arr8 = [-1, -1, 0]
    # Sorted: [-1, -1, 0] -> [-1, 0, 0] -> [-1, 0, 1], increments = 0 + 1 + 1 = 2
    assert min_increment_for_unique(arr8.copy()) == 2, "Test 8 failed"

    # Test case 9: Compare with optimized version
    arr9 = [3, 2, 1, 2, 1, 7, 8, 8, 8]
    result1 = min_increment_for_unique(arr9.copy())
    result2 = min_increment_for_unique_optimized(arr9.copy())
    assert result1 == result2, f"Test 9 failed: {result1} != {result2}"

    print("All test cases passed!")


if __name__ == "__main__":
    # Run test cases
    test_min_increment_for_unique()

    # Example usage
    arr = [3, 2, 1, 2, 1, 7]
    print(f"Original: {arr}")
    print(f"Minimum increments: {min_increment_for_unique(arr.copy())}")
