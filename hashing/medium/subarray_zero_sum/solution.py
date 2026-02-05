"""
Subarray with 0 Sum

Problem Description:
Given an array of positive and negative numbers, find if there is a subarray
(of size at least one) with 0 sum.

Examples:
Input: {4, 2, -3, 1, 6}
Output: True
Explanation: There is a subarray with zero sum from index 1 to 3: [2, -3, 1]

Input: {4, 2, 0, 1, 6}
Output: True
Explanation: The third element is zero. A single element is also a subarray.

Input: {-3, 2, 3, 1, 6}
Output: False

Approach:
Use prefix sum with hash set:
- If prefix sum repeats, there is a subarray with 0 sum between those indices
- Store prefix sums in a set
- If current prefix sum is 0 or seen before, return True

Time Complexity: O(N)
Space Complexity: O(N)
"""


def has_subarray_with_zero_sum(arr):
    """
    Check if there exists a subarray with sum equal to 0.

    Args:
        arr: List of integers

    Returns:
        True if subarray with 0 sum exists, False otherwise
    """
    prefix_sum_set = set()
    prefix_sum = 0

    for num in arr:
        prefix_sum += num

        # If prefix sum is 0 or seen before, subarray with 0 sum exists
        if prefix_sum == 0 or prefix_sum in prefix_sum_set:
            return True

        prefix_sum_set.add(prefix_sum)

    return False


def find_subarray_with_zero_sum(arr):
    """
    Find and return the subarray with sum equal to 0.

    Args:
        arr: List of integers

    Returns:
        Tuple (start_index, end_index) of subarray with 0 sum, or None
    """
    prefix_sum_map = {}  # sum -> index
    prefix_sum = 0

    for i, num in enumerate(arr):
        prefix_sum += num

        # If prefix sum is 0, subarray from 0 to i has sum 0
        if prefix_sum == 0:
            return (0, i)

        # If prefix sum seen before, subarray between indices has sum 0
        if prefix_sum in prefix_sum_map:
            start = prefix_sum_map[prefix_sum] + 1
            return (start, i)

        prefix_sum_map[prefix_sum] = i

    return None


def count_zero_sum_subarrays(arr):
    """
    Count all subarrays with sum equal to 0.

    Args:
        arr: List of integers

    Returns:
        Count of subarrays with sum 0
    """
    prefix_sum_count = {0: 1}  # sum -> count
    prefix_sum = 0
    count = 0

    for num in arr:
        prefix_sum += num

        if prefix_sum in prefix_sum_count:
            count += prefix_sum_count[prefix_sum]
            prefix_sum_count[prefix_sum] += 1
        else:
            prefix_sum_count[prefix_sum] = 1

    return count


def test_subarray_zero_sum():
    """Test cases for subarray with zero sum functions."""
    # Test Case 1: Example from problem
    arr1 = [4, 2, -3, 1, 6]
    result1 = has_subarray_with_zero_sum(arr1)
    subarray1 = find_subarray_with_zero_sum(arr1)
    print(f"Test 1: arr={arr1}")
    print(f"Has zero sum subarray: {result1}, Expected: True")
    print(f"Subarray indices: {subarray1}")
    print(f"{'PASS' if result1 else 'FAIL'}")
    print()

    # Test Case 2: Array with zero element
    arr2 = [4, 2, 0, 1, 6]
    result2 = has_subarray_with_zero_sum(arr2)
    print(f"Test 2: arr={arr2}")
    print(f"Has zero sum subarray: {result2}, Expected: True")
    print(f"{'PASS' if result2 else 'FAIL'}")
    print()

    # Test Case 3: No zero sum subarray
    arr3 = [-3, 2, 3, 1, 6]
    result3 = has_subarray_with_zero_sum(arr3)
    print(f"Test 3: arr={arr3}")
    print(f"Has zero sum subarray: {result3}, Expected: False")
    print(f"{'PASS' if not result3 else 'FAIL'}")
    print()

    # Test Case 4: Empty array
    arr4 = []
    result4 = has_subarray_with_zero_sum(arr4)
    print(f"Test 4: arr={arr4}")
    print(f"Has zero sum subarray: {result4}, Expected: False")
    print(f"{'PASS' if not result4 else 'FAIL'}")
    print()

    # Test Case 5: Single element zero
    arr5 = [0]
    result5 = has_subarray_with_zero_sum(arr5)
    print(f"Test 5: arr={arr5}")
    print(f"Has zero sum subarray: {result5}, Expected: True")
    print(f"{'PASS' if result5 else 'FAIL'}")
    print()

    # Test Case 6: Count zero sum subarrays
    arr6 = [6, -4, 4, 2, -2]
    count6 = count_zero_sum_subarrays(arr6)
    print(f"Test 6: arr={arr6}")
    print(f"Count of zero sum subarrays: {count6}")
    print(f"Subarrays: [-4, 4], [2, -2], [-4, 4, 2, -2]")
    print(f"Expected: 3, {'PASS' if count6 == 3 else 'FAIL'}")
    print()


if __name__ == "__main__":
    test_subarray_zero_sum()
