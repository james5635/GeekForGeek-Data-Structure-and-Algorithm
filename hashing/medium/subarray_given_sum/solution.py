"""
Subarray with Given Sum

Problem Description:
Given an array arr[] of non-negative integers and an integer sum,
find a subarray that adds to the given sum. Return the left and right
indices (1-based indexing) of that subarray.

If multiple subarrays exist, return the one that comes first from left.
If no such subarray exists, return [-1].

Examples:
Input: arr[] = [15, 2, 4, 8, 9, 5, 10, 23], target = 23
Output: [2, 5]
Explanation: Sum of subarray arr[2..5] is 2 + 4 + 8 + 9 = 23

Input: arr[] = [1, 10, 4, 0, 3, 5], target = 7
Output: [3, 5]
Explanation: Sum of subarray arr[3..5] is 4 + 0 + 3 = 7

Approach:
Use sliding window technique for non-negative numbers:
- Maintain a window with two pointers
- Expand window by moving right pointer
- Shrink window from left when sum exceeds target

For arrays with negative numbers, use prefix sum + hash map.

Time Complexity: O(N)
Space Complexity: O(1) for sliding window, O(N) for prefix sum approach
"""


def find_subarray_with_given_sum(arr, target):
    """
    Find subarray with given sum using sliding window (for non-negative numbers).

    Args:
        arr: List of non-negative integers
        target: Target sum

    Returns:
        List [left, right] with 1-based indexing, or [-1]
    """
    n = len(arr)
    if n == 0:
        return [-1]

    left = 0
    current_sum = 0

    for right in range(n):
        current_sum += arr[right]

        # Shrink window from left while sum exceeds target
        while current_sum > target and left <= right:
            current_sum -= arr[left]
            left += 1

        # Check if current window has the target sum
        if current_sum == target:
            return [left + 1, right + 1]  # 1-based indexing

    return [-1]


def find_subarray_with_sum_hashing(arr, target):
    """
    Find subarray with given sum using prefix sum and hash map.
    Works with negative numbers as well.

    Args:
        arr: List of integers (can include negatives)
        target: Target sum

    Returns:
        List [left, right] with 1-based indexing, or [-1]
    """
    n = len(arr)
    if n == 0:
        return [-1]

    prefix_sum_map = {0: 0}  # sum -> index (0-based, position after element)
    prefix_sum = 0

    for i, num in enumerate(arr):
        prefix_sum += num

        # Check if there exists a prefix sum such that current - target = previous
        if (prefix_sum - target) in prefix_sum_map:
            start = prefix_sum_map[prefix_sum - target]
            return [start + 1, i + 1]  # 1-based indexing

        # Store first occurrence of prefix sum
        if prefix_sum not in prefix_sum_map:
            prefix_sum_map[prefix_sum] = i + 1

    return [-1]


def count_subarrays_with_sum(arr, target):
    """
    Count all subarrays with given sum.
    Works with negative numbers.

    Args:
        arr: List of integers
        target: Target sum

    Returns:
        Count of subarrays with sum equal to target
    """
    prefix_sum_count = {0: 1}
    prefix_sum = 0
    count = 0

    for num in arr:
        prefix_sum += num

        if (prefix_sum - target) in prefix_sum_count:
            count += prefix_sum_count[prefix_sum - target]

        prefix_sum_count[prefix_sum] = prefix_sum_count.get(prefix_sum, 0) + 1

    return count


def test_subarray_given_sum():
    """Test cases for subarray with given sum functions."""
    # Test Case 1: Example from problem
    arr1 = [15, 2, 4, 8, 9, 5, 10, 23]
    target1 = 23
    result1 = find_subarray_with_given_sum(arr1, target1)
    print(f"Test 1: arr={arr1}, target={target1}")
    print(f"Result: {result1}, Expected: [2, 5]")
    print(f"{'PASS' if result1 == [2, 5] else 'FAIL'}")
    print()

    # Test Case 2: Another example
    arr2 = [1, 10, 4, 0, 3, 5]
    target2 = 7
    result2 = find_subarray_with_given_sum(arr2, target2)
    print(f"Test 2: arr={arr2}, target={target2}")
    print(f"Result: {result2}, Expected: [3, 5]")
    print(f"{'PASS' if result2 == [3, 5] else 'FAIL'}")
    print()

    # Test Case 3: No subarray found
    arr3 = [1, 4]
    target3 = 0
    result3 = find_subarray_with_given_sum(arr3, target3)
    print(f"Test 3: arr={arr3}, target={target3}")
    print(f"Result: {result3}, Expected: [-1]")
    print(f"{'PASS' if result3 == [-1] else 'FAIL'}")
    print()

    # Test Case 4: Single element equals target
    arr4 = [5]
    target4 = 5
    result4 = find_subarray_with_given_sum(arr4, target4)
    print(f"Test 4: arr={arr4}, target={target4}")
    print(f"Result: {result4}, Expected: [1, 1]")
    print(f"{'PASS' if result4 == [1, 1] else 'FAIL'}")
    print()

    # Test Case 5: Empty array
    arr5 = []
    target5 = 5
    result5 = find_subarray_with_given_sum(arr5, target5)
    print(f"Test 5: arr={arr5}, target={target5}")
    print(f"Result: {result5}, Expected: [-1]")
    print(f"{'PASS' if result5 == [-1] else 'FAIL'}")
    print()

    # Test Case 6: With negative numbers using hashing approach
    arr6 = [10, 2, -2, -20, 10]
    target6 = -10
    result6 = find_subarray_with_sum_hashing(arr6, target6)
    print(f"Test 6 (with negatives): arr={arr6}, target={target6}")
    print(f"Result: {result6}")
    print()

    # Test Case 7: Count subarrays
    arr7 = [10, 2, -2, -20, 10]
    target7 = -10
    count7 = count_subarrays_with_sum(arr7, target7)
    print(f"Test 7: arr={arr7}, target={target7}")
    print(f"Count: {count7}, Expected: 3, {'PASS' if count7 == 3 else 'FAIL'}")
    print()


if __name__ == "__main__":
    test_subarray_given_sum()
