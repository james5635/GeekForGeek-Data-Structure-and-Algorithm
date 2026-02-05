"""
Maximum Array from Two Arrays

Problem Description:
    Given two arrays A[] and B[] of size n, create an array C[] of size 2n such that:
    - C contains all elements from A and B
    - For every i from 0 to 2n-1, C[i] >= C[i+1] (non-increasing)
    - The relative order of elements from the same array is preserved
    - C maximizes the lexicographical order

Approach:
    Use monotonic stack and greedy approach with hash map to track positions.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
from collections import deque


def max_array_from_two_arrays(A: List[int], B: List[int]) -> List[int]:
    """
    Create maximum lexicographical array preserving relative order.

    Args:
        A: First array
        B: Second array

    Returns:
        Maximum lexicographical merged array
    """
    n = len(A)
    m = len(B)

    # Create monotonic decreasing sequences
    def monotonic_decreasing(arr: List[int]) -> List[int]:
        """Find next greater or equal element indices."""
        n = len(arr)
        result = [-1] * n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                idx = stack.pop()
                result[idx] = i
            stack.append(i)

        return result

    # Get next greater element positions
    next_greater_A = monotonic_decreasing(A)
    next_greater_B = monotonic_decreasing(B)

    result = []
    i, j = 0, 0

    while i < n and j < m:
        if A[i] > B[j]:
            result.append(A[i])
            i += 1
        elif A[i] < B[j]:
            result.append(B[j])
            j += 1
        else:
            # Equal elements - need to look ahead
            # Choose the one that leads to better sequence
            temp_i, temp_j = i, j

            while temp_i < n and temp_j < m and A[temp_i] == B[temp_j]:
                temp_i += 1
                temp_j += 1

            # Determine which sequence is better
            if temp_j >= m or (temp_i < n and A[temp_i] > B[temp_j]):
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1

    # Add remaining elements
    while i < n:
        result.append(A[i])
        i += 1

    while j < m:
        result.append(B[j])
        j += 1

    return result


def max_array_greedy(A: List[int], B: List[int]) -> List[int]:
    """
    Greedy approach for maximum array.

    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """

    def merge_max_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
        """Merge two arrays to get maximum lexicographical order."""
        result = []
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i:] > arr2[j:]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        result.extend(arr1[i:])
        result.extend(arr2[j:])
        return result

    return merge_max_arrays(A, B)


def max_subsequence_of_length_k(nums: List[int], k: int) -> List[int]:
    """
    Find maximum subsequence of length k preserving relative order.

    Uses monotonic stack approach.
    """
    n = len(nums)
    if k == 0:
        return []
    if k == n:
        return nums[:]

    stack = []
    to_remove = n - k

    for num in nums:
        while stack and to_remove > 0 and stack[-1] < num:
            stack.pop()
            to_remove -= 1
        stack.append(num)

    # Remove remaining elements if any
    while to_remove > 0:
        stack.pop()
        to_remove -= 1

    return stack


def max_array_from_two_arrays_with_k(A: List[int], B: List[int], k: int) -> List[int]:
    """
    Create maximum array of length k using elements from both arrays.

    Args:
        A: First array
        B: Second array
        k: Desired length of result

    Returns:
        Maximum lexicographical array of length k
    """
    max_result = []

    # Try all possible ways to take elements from A and B
    for take_from_A in range(max(0, k - len(B)), min(k, len(A)) + 1):
        take_from_B = k - take_from_A

        # Get maximum subsequences
        sub_A = max_subsequence_of_length_k(A, take_from_A)
        sub_B = max_subsequence_of_length_k(B, take_from_B)

        # Merge to get maximum
        merged = max_array_greedy(sub_A, sub_B)

        if merged > max_result:
            max_result = merged

    return max_result


def test_max_array():
    """Test cases for maximum array from two arrays."""
    test_cases = [
        # (A, B, expected_result)
        ([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], [9, 8, 6, 5, 3]),
        ([6, 7], [6, 0, 4], [6, 7, 6, 0, 4]),
        ([3, 9], [8, 9], [9, 9, 8, 3]),
        ([1], [2], [2, 1]),
        ([5, 5, 5], [5, 5], [5, 5, 5, 5, 5]),
    ]

    print("Running test cases for Maximum Array from Two Arrays:")
    print("=" * 60)

    for i, (A, B, expected) in enumerate(test_cases, 1):
        result = max_array_greedy(A, B)
        status = "✓ PASS" if result == expected else "✗ FAIL"

        print(f"Test {i}:")
        print(f"  A = {A}")
        print(f"  B = {B}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print(f"  Status:   {status}\n")

    # Test with length constraint
    print("\nTest with length constraint (k=5):")
    test_k_cases = [
        ([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5),
        ([6, 7, 8], [6, 0, 4], 5),
    ]

    for A, B, k in test_k_cases:
        result = max_array_from_two_arrays_with_k(A, B, k)
        print(f"A={A}, B={B}, k={k}")
        print(f"Result: {result}\n")


if __name__ == "__main__":
    # Example usage
    A = [3, 4, 6, 5]
    B = [9, 1, 2, 5, 8, 3]

    print("Maximum Array from Two Arrays Example:")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"Result: {max_array_greedy(A, B)}")
    print()

    # Run tests
    test_max_array()
