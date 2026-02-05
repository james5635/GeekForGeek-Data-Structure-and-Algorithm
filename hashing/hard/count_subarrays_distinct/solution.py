"""
Count Subarrays Having Distinct Elements

Problem Description:
    Given an array arr[], count the total number of subarrays having
    all distinct elements (no duplicates).

Approach:
    Use sliding window with hash set to track distinct elements.
    For each position, count subarrays ending at that position.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


def count_subarrays_distinct(arr: List[int]) -> int:
    """
    Count all subarrays with distinct elements.

    Uses sliding window technique.

    Args:
        arr: Input array

    Returns:
        Total count of subarrays with all distinct elements
    """
    n = len(arr)
    count = 0
    left = 0
    seen = set()

    for right in range(n):
        # Remove elements from left until current element can be added
        while arr[right] in seen:
            seen.remove(arr[left])
            left += 1

        # Add current element
        seen.add(arr[right])

        # All subarrays ending at 'right' with start from 'left' to 'right'
        # are valid and have distinct elements
        count += right - left + 1

    return count


def count_subarrays_distinct_brute_force(arr: List[int]) -> int:
    """
    Brute force approach for comparison.

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    n = len(arr)
    count = 0

    for i in range(n):
        seen = set()
        for j in range(i, n):
            if arr[j] in seen:
                break
            seen.add(arr[j])
            count += 1

    return count


def count_subarrays_at_most_k_distinct(arr: List[int], k: int) -> int:
    """
    Count subarrays with at most k distinct elements.

    Args:
        arr: Input array
        k: Maximum number of distinct elements allowed

    Returns:
        Count of subarrays with at most k distinct elements
    """
    from collections import defaultdict

    n = len(arr)
    count = 0
    left = 0
    freq = defaultdict(int)
    distinct_count = 0

    for right in range(n):
        if freq[arr[right]] == 0:
            distinct_count += 1
        freq[arr[right]] += 1

        while distinct_count > k:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                distinct_count -= 1
            left += 1

        count += right - left + 1

    return count


def count_subarrays_exactly_k_distinct(arr: List[int], k: int) -> int:
    """
    Count subarrays with exactly k distinct elements.

    Uses the formula: exactly(k) = at_most(k) - at_most(k-1)
    """
    return count_subarrays_at_most_k_distinct(
        arr, k
    ) - count_subarrays_at_most_k_distinct(arr, k - 1)


def longest_subarray_distinct(arr: List[int]) -> int:
    """
    Find length of longest subarray with all distinct elements.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(arr)
    max_len = 0
    left = 0
    seen = set()

    for right in range(n):
        while arr[right] in seen:
            seen.remove(arr[left])
            left += 1

        seen.add(arr[right])
        max_len = max(max_len, right - left + 1)

    return max_len


def test_count_subarrays_distinct():
    """Test cases for counting subarrays with distinct elements."""
    test_cases = [
        # (array, expected_count)
        ([1, 2, 3], 6),  # All subarrays are valid: 3+2+1 = 6
        ([1, 2, 1], 5),  # [1], [2], [1], [1,2], [2,1] = 5
        ([1, 1, 1], 3),  # Only single elements: [1], [1], [1] = 3
        ([1, 2, 3, 4], 10),  # 4+3+2+1 = 10
        ([1, 2, 1, 3], 8),  # Various combinations
        ([], 0),
        ([1], 1),
        ([1, 2, 3, 1, 2, 3], 15),
    ]

    print("Running test cases for Count Subarrays with Distinct Elements:")
    print("=" * 60)

    for i, (arr, expected) in enumerate(test_cases, 1):
        result = count_subarrays_distinct(arr)
        status = "✓ PASS" if result == expected else "✗ FAIL"

        print(f"Test {i}: arr = {arr}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print(f"  Status:   {status}\n")

    # Test exactly k distinct
    print("\nTest with exactly k distinct elements:")
    test_k_cases = [
        ([1, 2, 1, 2, 3], 2, 8),  # 8 subarrays with exactly 2 distinct
        ([1, 2, 1, 3, 4], 3, 3),
    ]

    for arr, k, expected in test_k_cases:
        result = count_subarrays_exactly_k_distinct(arr, k)
        status = "✓" if result == expected else "✗"
        print(f"arr={arr}, k={k}: Expected={expected}, Got={result} {status}")


if __name__ == "__main__":
    # Example usage
    arr = [1, 2, 1, 3]
    print(f"Array: {arr}")
    print(f"Total subarrays with distinct elements: {count_subarrays_distinct(arr)}")
    print(f"Longest subarray with distinct elements: {longest_subarray_distinct(arr)}")
    print(
        f"Subarrays with exactly 2 distinct: {count_subarrays_exactly_k_distinct(arr, 2)}"
    )
    print()

    # Run tests
    test_count_subarrays_distinct()
