"""
Longest Strictly Bitonic Subsequence

Problem Description:
    Given an array arr[], find the length of the longest strictly bitonic subsequence.
    A bitonic subsequence first increases then decreases (with at least one element on each side).

Approach:
    Calculate LIS from left and LDS from right for each position, then combine.

Time Complexity: O(n^2) or O(n log n) with optimization
Space Complexity: O(n)
"""

from typing import List


def longest_bitonic_subsequence(arr: List[int]) -> int:
    """
    Find length of longest bitonic subsequence.

    Args:
        arr: Input array

    Returns:
        Length of longest bitonic subsequence
    """
    n = len(arr)
    if n < 2:
        return 0

    # LIS ending at each position
    lis = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                lis[i] = max(lis[i], lis[j] + 1)

    # LDS starting at each position (longest decreasing)
    lds = [1] * n

    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[i]:
                lds[i] = max(lds[i], lds[j] + 1)

    # Find maximum bitonic length
    # Need at least one element in increasing and one in decreasing part
    max_len = 0
    for i in range(n):
        if lis[i] > 1 and lds[i] > 1:
            max_len = max(max_len, lis[i] + lds[i] - 1)

    return max_len


def longest_bitonic_subsequence_dp(arr: List[int]) -> int:
    """
    Dynamic programming approach with path reconstruction.

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    n = len(arr)
    if n < 2:
        return 0

    # LIS from left
    lis = [1] * n
    lis_parent = [-1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1
                lis_parent[i] = j

    # LDS from right
    lds = [1] * n
    lds_parent = [-1] * n

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[i] and lds[j] + 1 > lds[i]:
                lds[i] = lds[j] + 1
                lds_parent[i] = j

    # Find peak
    max_len = 0
    peak_idx = -1

    for i in range(n):
        if lis[i] > 1 and lds[i] > 1:
            if lis[i] + lds[i] - 1 > max_len:
                max_len = lis[i] + lds[i] - 1
                peak_idx = i

    return max_len


def get_bitonic_subsequence(arr: List[int]) -> List[int]:
    """
    Get the actual bitonic subsequence.

    Returns:
        The longest bitonic subsequence
    """
    n = len(arr)
    if n < 2:
        return []

    lis = [1] * n
    lis_parent = [-1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1
                lis_parent[i] = j

    lds = [1] * n
    lds_parent = [-1] * n

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[i] and lds[j] + 1 > lds[i]:
                lds[i] = lds[j] + 1
                lds_parent[i] = j

    # Find peak
    max_len = 0
    peak_idx = -1

    for i in range(n):
        if lis[i] > 1 and lds[i] > 1:
            if lis[i] + lds[i] - 1 > max_len:
                max_len = lis[i] + lds[i] - 1
                peak_idx = i

    if peak_idx == -1:
        return []

    # Reconstruct increasing part
    inc_part = []
    cur = peak_idx
    while cur != -1:
        inc_part.append(arr[cur])
        cur = lis_parent[cur]
    inc_part.reverse()

    # Reconstruct decreasing part (excluding peak)
    dec_part = []
    cur = lds_parent[peak_idx]
    while cur != -1:
        dec_part.append(arr[cur])
        cur = lds_parent[cur]

    return inc_part + dec_part


def count_bitonic_subsequences(arr: List[int]) -> int:
    """
    Count total number of bitonic subsequences.

    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    n = len(arr)
    if n < 2:
        return 0

    MOD = 10**9 + 7

    # Count LIS ending at each position
    lis_count = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                lis_count[i] = (lis_count[i] + lis_count[j]) % MOD

    # Count LDS starting at each position
    lds_count = [1] * n

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[i]:
                lds_count[i] = (lds_count[i] + lds_count[j]) % MOD

    # Total bitonic = sum over all peaks
    total = 0
    for i in range(n):
        if lis_count[i] > 1 and lds_count[i] > 1:
            total = (total + (lis_count[i] - 1) * (lds_count[i] - 1)) % MOD

    return total


def test_bitonic():
    """Test cases for longest bitonic subsequence."""
    test_cases = [
        # (array, expected_length)
        ([1, 2, 5, 3, 2], 5),  # 1, 2, 5, 3, 2
        ([1, 11, 2, 10, 4, 5, 2, 1], 6),  # 1, 2, 10, 5, 2, 1 or similar
        ([80, 60, 30, 40, 20, 10], 0),  # Only decreasing, no bitonic
        ([10, 20, 30, 40], 0),  # Only increasing, no bitonic
        ([1, 2, 3, 4, 5, 3, 2], 7),  # 1, 2, 3, 4, 5, 3, 2
        ([1], 0),  # Single element
        ([1, 1, 1], 0),  # No strict increase/decrease possible
        ([1, 2, 1], 3),  # 1, 2, 1
    ]

    print("Running test cases for Longest Bitonic Subsequence:")
    print("=" * 60)

    for i, (arr, expected) in enumerate(test_cases, 1):
        result = longest_bitonic_subsequence(arr)
        subseq = get_bitonic_subsequence(arr)
        status = "✓ PASS" if result == expected else "✗ FAIL"

        print(f"Test {i}: arr = {arr}")
        print(f"  Expected length: {expected}")
        print(f"  Got length:      {result}")
        print(f"  Subsequence:     {subseq}")
        print(f"  Status:          {status}\n")


if __name__ == "__main__":
    # Example usage
    arr = [1, 11, 2, 10, 4, 5, 2, 1]
    print(f"Array: {arr}")
    print(f"Longest bitonic subsequence length: {longest_bitonic_subsequence(arr)}")
    print(f"Longest bitonic subsequence: {get_bitonic_subsequence(arr)}")
    print()

    # Run tests
    test_bitonic()
