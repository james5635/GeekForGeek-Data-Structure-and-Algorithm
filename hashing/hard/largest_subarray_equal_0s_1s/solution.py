"""
Largest Subarray with Equal 0s and 1s

Problem Description:
    Given a binary array containing only 0s and 1s, find the length of
    the largest subarray with equal number of 0s and 1s.

Approach:
    Replace 0s with -1s and use prefix sum with hash map.
    When prefix sum repeats, elements between indices have equal 0s and 1s.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


def largest_subarray_equal_zeros_ones(arr: List[int]) -> int:
    """
    Find length of largest subarray with equal 0s and 1s.

    Args:
        arr: Binary array containing only 0s and 1s

    Returns:
        Length of largest subarray with equal 0s and 1s
    """
    n = len(arr)
    max_len = 0
    prefix_sum = 0

    # Hash map to store first occurrence of each prefix sum
    prefix_map = {}

    for i in range(n):
        # Treat 0 as -1
        prefix_sum += 1 if arr[i] == 1 else -1

        # If prefix sum is 0, subarray from 0 to i has equal 0s and 1s
        if prefix_sum == 0:
            max_len = max(max_len, i + 1)

        # If prefix sum seen before, subarray between indices has equal 0s and 1s
        if prefix_sum in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum])
        else:
            # Store first occurrence
            prefix_map[prefix_sum] = i

    return max_len


def largest_subarray_with_indices(arr: List[int]) -> tuple:
    """
    Find the largest subarray and return length, start and end indices.

    Returns:
        Tuple of (length, start_index, end_index)
    """
    n = len(arr)
    max_len = 0
    start_idx = -1
    end_idx = -1
    prefix_sum = 0

    prefix_map = {}

    for i in range(n):
        prefix_sum += 1 if arr[i] == 1 else -1

        if prefix_sum == 0:
            if i + 1 > max_len:
                max_len = i + 1
                start_idx = 0
                end_idx = i

        if prefix_sum in prefix_map:
            current_len = i - prefix_map[prefix_sum]
            if current_len > max_len:
                max_len = current_len
                start_idx = prefix_map[prefix_sum] + 1
                end_idx = i
        else:
            prefix_map[prefix_sum] = i

    return max_len, start_idx, end_idx


def count_subarrays_equal_zeros_ones(arr: List[int]) -> int:
    """
    Count all subarrays with equal number of 0s and 1s.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(arr)
    count = 0
    prefix_sum = 0

    # Count occurrences of each prefix sum
    from collections import defaultdict

    prefix_count = defaultdict(int)
    prefix_count[0] = 1  # Empty subarray has sum 0

    for i in range(n):
        prefix_sum += 1 if arr[i] == 1 else -1

        # Each previous occurrence of this sum forms a valid subarray
        count += prefix_count[prefix_sum]
        prefix_count[prefix_sum] += 1

    return count


def test_largest_subarray():
    """Test cases for largest subarray with equal 0s and 1s."""
    test_cases = [
        # (array, expected_length)
        ([1, 0, 1, 1, 1, 0, 0], 6),
        ([0, 0, 1, 1, 0], 4),
        ([0], 0),
        ([1], 0),
        ([0, 1], 2),
        ([1, 0], 2),
        ([0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0], 10),
        ([1, 1, 1, 1], 0),
        ([0, 0, 0, 0], 0),
        ([0, 1, 0, 1, 0, 1, 0], 6),
    ]

    print("Running test cases for Largest Subarray with Equal 0s and 1s:")
    print("=" * 60)

    for i, (arr, expected) in enumerate(test_cases, 1):
        result = largest_subarray_equal_zeros_ones(arr)
        status = "✓ PASS" if result == expected else "✗ FAIL"

        print(f"Test {i}: arr = {arr}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print(f"  Status:   {status}\n")

    # Test with indices
    print("\nTest with subarray indices:")
    test_arr = [1, 0, 1, 1, 1, 0, 0]
    length, start, end = largest_subarray_with_indices(test_arr)
    print(f"Array: {test_arr}")
    print(f"Largest subarray: length={length}, start={start}, end={end}")
    if start >= 0 and end >= 0:
        print(f"Subarray: {test_arr[start : end + 1]}")


if __name__ == "__main__":
    # Example usage
    arr = [1, 0, 1, 1, 1, 0, 0]
    print(f"Array: {arr}")
    print(
        f"Length of largest subarray with equal 0s and 1s: {largest_subarray_equal_zeros_ones(arr)}"
    )
    print(f"Count of all such subarrays: {count_subarrays_equal_zeros_ones(arr)}")
    print()

    # Run tests
    test_largest_subarray()
