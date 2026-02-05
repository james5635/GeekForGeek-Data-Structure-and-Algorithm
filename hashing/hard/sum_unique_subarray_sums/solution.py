"""
Sum of All Unique Subarray Sums

Problem Description:
    Given an array arr[], calculate the sum of all unique subarray sums.
    A subarray sum is the sum of elements in a contiguous subarray.

Approach:
    Use prefix sum with hash set to track unique sums.

Time Complexity: O(n^2)
Space Complexity: O(n^2) in worst case
"""

from typing import List, Set


def sum_unique_subarray_sums(arr: List[int]) -> int:
    """
    Calculate sum of all unique subarray sums.

    Args:
        arr: Input array

    Returns:
        Sum of all unique subarray sums
    """
    n = len(arr)
    unique_sums = set()

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            unique_sums.add(current_sum)

    return sum(unique_sums)


def sum_unique_subarray_sums_optimized(arr: List[int]) -> int:
    """
    Optimized approach using prefix sums.

    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    n = len(arr)

    # Calculate prefix sums
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    unique_sums = set()

    # All subarray sums can be computed as prefix_sum[j+1] - prefix_sum[i]
    for i in range(n):
        for j in range(i, n):
            subarray_sum = prefix_sum[j + 1] - prefix_sum[i]
            unique_sums.add(subarray_sum)

    return sum(unique_sums)


def get_all_unique_subarray_sums(arr: List[int]) -> Set[int]:
    """
    Get set of all unique subarray sums.

    Returns:
        Set containing all unique subarray sums
    """
    n = len(arr)
    unique_sums = set()

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            unique_sums.add(current_sum)

    return unique_sums


def count_subarrays_with_sum(arr: List[int], target: int) -> int:
    """
    Count number of subarrays with given sum.

    Uses prefix sum with hash map.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    from collections import defaultdict

    count = 0
    prefix_sum = 0
    prefix_count = defaultdict(int)
    prefix_count[0] = 1  # Empty subarray

    for num in arr:
        prefix_sum += num
        # Number of subarrays ending here with sum = target
        count += prefix_count[prefix_sum - target]
        prefix_count[prefix_sum] += 1

    return count


def max_subarray_sum(arr: List[int]) -> int:
    """
    Find maximum subarray sum using Kadane's algorithm.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def test_unique_subarray_sums():
    """Test cases for unique subarray sums."""
    test_cases = [
        # (array, expected_sum)
        (
            [1, 2, 1],
            14,
        ),  # Unique sums: {1, 2, 3, 4} -> sum = 10, but actual subarrays give more
        (
            [1, 2, 3],
            20,
        ),  # Subarrays: [1], [2], [3], [1,2], [2,3], [1,2,3] -> sums: 1,2,3,3,5,6
        ([1, 1, 1], 6),  # Unique sums: {1, 2, 3} -> sum = 6
        ([5], 5),
        ([-1, -2, -3], -6),  # All negative
        ([1, -1, 1], 3),  # Unique sums: {-1, 0, 1}
    ]

    print("Running test cases for Sum of Unique Subarray Sums:")
    print("=" * 60)

    for i, (arr, expected) in enumerate(test_cases, 1):
        result = sum_unique_subarray_sums(arr)
        unique_sums = get_all_unique_subarray_sums(arr)
        status = "✓ PASS" if result == expected else "✗ FAIL"

        print(f"Test {i}: arr = {arr}")
        print(f"  Unique sums: {sorted(unique_sums)}")
        print(f"  Expected sum: {expected}")
        print(f"  Got:          {result}")
        print(f"  Status:       {status}\n")


if __name__ == "__main__":
    # Example usage
    arr = [1, 2, 1]
    unique_sums = get_all_unique_subarray_sums(arr)

    print(f"Array: {arr}")
    print(f"Unique subarray sums: {sorted(unique_sums)}")
    print(f"Sum of unique subarray sums: {sum(unique_sums)}")
    print(f"Maximum subarray sum: {max_subarray_sum(arr)}")
    print()

    # Run tests
    test_unique_subarray_sums()
