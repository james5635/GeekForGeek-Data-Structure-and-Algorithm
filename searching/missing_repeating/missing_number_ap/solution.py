"""
Find Missing Number in Arithmetic Progression

Problem Description:
Given an arithmetic progression (AP) with one missing number,
find the missing number. The AP has a common difference and
contains n-1 elements instead of n.

Example:
    Input: [2, 4, 8, 10, 12, 14]
    Output: 6

Time Complexity: O(log n)
Space Complexity: O(1)

Approach: Binary Search
    In a valid AP: arr[i] = first + i * diff
    If arr[mid] - first == mid * diff, missing is on right
    Otherwise, missing is on left
"""


def find_missing_in_ap(arr):
    """
    Find missing number in AP using binary search.

    Args:
        arr: Array forming AP with one missing element

    Returns:
        The missing number
    """
    n = len(arr)

    if n < 2:
        return -1

    # Calculate common difference by finding minimum consecutive difference
    diffs = [arr[i + 1] - arr[i] for i in range(n - 1)]
    diff = min(diffs)

    # Check if first element is missing
    # If arr[0] is first: expected last = arr[0] + n * diff (n intervals for n+1 elements)
    # If arr[0] is second (first missing): expected last = arr[0] + (n-1) * diff
    expected_last_if_first = arr[0] + n * diff
    expected_last_if_second = arr[0] + (n - 1) * diff

    if arr[-1] == expected_last_if_second:
        # First element is missing
        return arr[0] - diff
    elif arr[-1] == expected_last_if_first:
        # arr[0] is first element, missing element is somewhere in middle
        pass
    else:
        # Last element might be missing - handled by binary search
        pass

    left, right = 0, n - 1

    while left < right:
        mid = left + (right - left) // 2

        # Expected value at mid in a complete AP starting from arr[0]
        expected = arr[0] + mid * diff

        if arr[mid] == expected:
            # Missing element is on the right
            left = mid + 1
        else:
            # Missing element is at or before mid
            right = mid

    # Missing element is what should be at left position
    return arr[0] + left * diff


def find_missing_in_ap_linear(arr):
    """
    Find missing number using linear scan.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Args:
        arr: Array forming AP with one missing element

    Returns:
        The missing number
    """
    n = len(arr)

    if n < 2:
        return -1

    # Calculate common difference by finding minimum consecutive difference
    diffs = [arr[i + 1] - arr[i] for i in range(n - 1)]
    diff = min(diffs)

    # Check if first element is missing
    expected_last_if_first = arr[0] + n * diff
    expected_last_if_second = arr[0] + (n - 1) * diff

    if arr[-1] == expected_last_if_second:
        # First element is missing
        return arr[0] - diff

    # Find the gap in the middle
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] != diff:
            return arr[i - 1] + diff

    return -1  # Should not reach here if there's a missing element


def test_find_missing_in_ap():
    """Test cases for find_missing_in_ap."""
    # Test case 1: Basic example
    arr1 = [2, 4, 8, 10, 12, 14]
    assert find_missing_in_ap(arr1) == 6
    assert find_missing_in_ap_linear(arr1) == 6

    # Test case 2: Missing first element
    arr2 = [3, 5, 7, 9, 11, 13]
    # Full AP should be [1, 3, 5, 7, 9, 11, 13]
    # Missing element is 1, diff = 2
    assert find_missing_in_ap(arr2) == 1
    assert find_missing_in_ap_linear(arr2) == 1

    # Test case 3: Missing middle element
    arr3 = [1, 6, 11, 16, 21, 31]
    assert find_missing_in_ap(arr3) == 26
    assert find_missing_in_ap_linear(arr3) == 26

    # Test case 4: AP with negative numbers
    arr4 = [-10, -7, -4, 2, 5]
    assert find_missing_in_ap(arr4) == -1
    assert find_missing_in_ap_linear(arr4) == -1

    # Test case 5: Simple AP
    arr5 = [1, 3, 7, 9]
    assert find_missing_in_ap(arr5) == 5
    assert find_missing_in_ap_linear(arr5) == 5

    # Test case 6: Large AP
    arr6 = [10, 20, 30, 40, 60, 70, 80]
    assert find_missing_in_ap(arr6) == 50
    assert find_missing_in_ap_linear(arr6) == 50

    print("All test cases passed!")


if __name__ == "__main__":
    test_find_missing_in_ap()
