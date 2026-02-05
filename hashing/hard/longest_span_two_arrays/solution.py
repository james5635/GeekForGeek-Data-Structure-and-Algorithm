"""
Longest Span with Same Sum in Two Binary Arrays

Problem Description:
    Given two binary arrays arr1[] and arr2[] of same size n, find the longest
    span (i, j) where j >= i such that sum(arr1[i..j]) == sum(arr2[i..j]).

Approach:
    Use difference array and hash map to track first occurrence of each difference.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List, Tuple


def longest_span_same_sum(arr1: List[int], arr2: List[int]) -> int:
    """
    Find length of longest span with same sum in two binary arrays.

    Args:
        arr1: First binary array
        arr2: Second binary array

    Returns:
        Length of longest span with equal sums
    """
    n = len(arr1)
    max_len = 0
    prefix_sum1 = 0
    prefix_sum2 = 0

    # Hash map to store first occurrence of difference
    diff_map = {}

    for i in range(n):
        prefix_sum1 += arr1[i]
        prefix_sum2 += arr2[i]

        # Calculate difference between prefix sums
        diff = prefix_sum1 - prefix_sum2

        # If difference is 0, span from 0 to i has equal sums
        if diff == 0:
            max_len = max(max_len, i + 1)

        # If this difference seen before, span between indices has equal sums
        if diff in diff_map:
            max_len = max(max_len, i - diff_map[diff])
        else:
            diff_map[diff] = i

    return max_len


def longest_span_with_indices(arr1: List[int], arr2: List[int]) -> Tuple[int, int, int]:
    """
    Find longest span and return length, start and end indices.

    Returns:
        Tuple of (length, start_index, end_index)
    """
    n = len(arr1)
    max_len = 0
    start_idx = -1
    end_idx = -1
    prefix_sum1 = 0
    prefix_sum2 = 0

    diff_map = {}

    for i in range(n):
        prefix_sum1 += arr1[i]
        prefix_sum2 += arr2[i]

        diff = prefix_sum1 - prefix_sum2

        if diff == 0:
            if i + 1 > max_len:
                max_len = i + 1
                start_idx = 0
                end_idx = i

        if diff in diff_map:
            current_len = i - diff_map[diff]
            if current_len > max_len:
                max_len = current_len
                start_idx = diff_map[diff] + 1
                end_idx = i
        else:
            diff_map[diff] = i

    return max_len, start_idx, end_idx


def longest_span_brute_force(arr1: List[int], arr2: List[int]) -> int:
    """
    Brute force approach for comparison.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr1)
    max_len = 0

    for i in range(n):
        sum1 = 0
        sum2 = 0
        for j in range(i, n):
            sum1 += arr1[j]
            sum2 += arr2[j]
            if sum1 == sum2:
                max_len = max(max_len, j - i + 1)

    return max_len


def test_longest_span():
    """Test cases for longest span with same sum."""
    test_cases = [
        # (arr1, arr2, expected_length)
        ([0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1], 4),
        ([0, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1], 6),
        ([0, 0, 0], [1, 1, 1], 0),
        ([1, 1, 1], [1, 1, 1], 3),
        ([0], [0], 1),
        ([1], [0], 0),
        ([0, 1], [1, 0], 2),
        ([1, 0, 1, 0, 1], [0, 1, 0, 1, 0], 4),
    ]

    print("Running test cases for Longest Span with Same Sum:")
    print("=" * 60)

    for i, (arr1, arr2, expected) in enumerate(test_cases, 1):
        result = longest_span_same_sum(arr1, arr2)
        status = "✓ PASS" if result == expected else "✗ FAIL"

        print(f"Test {i}:")
        print(f"  arr1 = {arr1}")
        print(f"  arr2 = {arr2}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print(f"  Status:   {status}\n")


if __name__ == "__main__":
    # Example usage
    arr1 = [0, 1, 0, 0, 0, 0]
    arr2 = [1, 0, 1, 0, 0, 1]

    print("Longest Span with Same Sum Example:")
    print(f"arr1 = {arr1}")
    print(f"arr2 = {arr2}")

    length, start, end = longest_span_with_indices(arr1, arr2)
    print(f"\nLongest span: {length}")
    print(f"Start index: {start}, End index: {end}")

    if start >= 0:
        print(
            f"\nSpan in arr1: {arr1[start : end + 1]} (sum = {sum(arr1[start : end + 1])})"
        )
        print(
            f"Span in arr2: {arr2[start : end + 1]} (sum = {sum(arr2[start : end + 1])})"
        )

    print()

    # Run tests
    test_longest_span()
