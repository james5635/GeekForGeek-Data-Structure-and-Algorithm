"""
Longest Increasing Subsequence (LIS) - Dynamic Programming
Source: https://www.geeksforgeeks.org/dsa/longest-increasing-subsequence-dp-3/

Given an array arr[] of size n, find the length of the Longest Increasing Subsequence.
The LIS is the longest possible subsequence in which elements are sorted in
strictly increasing order.

Time Complexity (DP): O(n^2)
Time Complexity (Binary Search): O(n log n)
Space Complexity: O(n)
"""


def lis_dp(arr: list[int]) -> int:
    """
    Find the length of the Longest Increasing Subsequence using
    bottom-up dynamic programming (tabulation).

    Args:
        arr: Input array of integers

    Returns:
        Length of the longest strictly increasing subsequence
    """
    n = len(arr)
    if n == 0:
        return 0

    # lis[i] stores the length of LIS ending at index i
    lis = [1] * n

    # Compute optimized LIS values in bottom-up manner
    for i in range(1, n):
        for prev in range(i):
            if arr[i] > arr[prev]:
                lis[i] = max(lis[i], lis[prev] + 1)

    return max(lis)


def lis_binary_search(arr: list[int]) -> int:
    """
    Find the length of the Longest Increasing Subsequence using
    binary search (patience sorting approach).

    This is the optimal O(n log n) solution.

    Args:
        arr: Input array of integers

    Returns:
        Length of the longest strictly increasing subsequence
    """
    n = len(arr)
    if n == 0:
        return 0

    # tails[i] stores the smallest tail of all increasing subsequences of length i+1
    tails = [arr[0]]

    for i in range(1, n):
        if arr[i] > tails[-1]:
            # Extend the longest subsequence
            tails.append(arr[i])
        else:
            # Find the position to replace using binary search
            low, high = 0, len(tails) - 1
            while low < high:
                mid = low + (high - low) // 2
                if tails[mid] < arr[i]:
                    low = mid + 1
                else:
                    high = mid
            tails[low] = arr[i]

    return len(tails)


def get_lis_sequence(arr: list[int]) -> list[int]:
    """
    Reconstruct and return the actual Longest Increasing Subsequence.

    Args:
        arr: Input array of integers

    Returns:
        The longest strictly increasing subsequence as a list
    """
    n = len(arr)
    if n == 0:
        return []

    lis = [1] * n
    parent = [-1] * n

    for i in range(1, n):
        for prev in range(i):
            if arr[i] > arr[prev] and lis[prev] + 1 > lis[i]:
                lis[i] = lis[prev] + 1
                parent[i] = prev

    # Find the index of maximum LIS value
    max_len = max(lis)
    max_idx = lis.index(max_len)

    # Reconstruct the sequence by backtracking
    sequence = []
    while max_idx != -1:
        sequence.append(arr[max_idx])
        max_idx = parent[max_idx]

    return list(reversed(sequence))


if __name__ == "__main__":
    # Test case 1
    arr = [3, 10, 2, 1, 20]
    print(f"arr = {arr}")
    print(f"LIS length (DP): {lis_dp(arr)}")  # Expected: 3
    print(f"LIS length (Binary Search): {lis_binary_search(arr)}")  # Expected: 3
    print(f"LIS sequence: {get_lis_sequence(arr)}")  # Expected: [3, 10, 20]
    print()

    # Test case 2
    arr = [30, 20, 10]
    print(f"arr = {arr}")
    print(f"LIS length (DP): {lis_dp(arr)}")  # Expected: 1
    print(f"LIS length (Binary Search): {lis_binary_search(arr)}")  # Expected: 1
    print()

    # Test case 3
    arr = [2, 2, 2]
    print(f"arr = {arr}")
    print(f"LIS length (DP): {lis_dp(arr)}")  # Expected: 1
    print(f"LIS length (Binary Search): {lis_binary_search(arr)}")  # Expected: 1
    print()

    # Test case 4
    arr = [3, 4, 5, 1, 2, 3, 4]
    print(f"arr = {arr}")
    print(f"LIS length (DP): {lis_dp(arr)}")  # Expected: 4
    print(f"LIS length (Binary Search): {lis_binary_search(arr)}")  # Expected: 4
    print(f"LIS sequence: {get_lis_sequence(arr)}")  # Expected: [1, 2, 3, 4]
    print()

    # Test case 5
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print(f"arr = {arr}")
    print(f"LIS length (DP): {lis_dp(arr)}")  # Expected: 6
    print(f"LIS length (Binary Search): {lis_binary_search(arr)}")  # Expected: 6
    print(f"LIS sequence: {get_lis_sequence(arr)}")
    print()

    # Test case 6 - empty array
    arr = []
    print(f"arr = {arr}")
    print(f"LIS length (DP): {lis_dp(arr)}")  # Expected: 0
    print(f"LIS length (Binary Search): {lis_binary_search(arr)}")  # Expected: 0
    print()

    # Test case 7 - single element
    arr = [5]
    print(f"arr = {arr}")
    print(f"LIS length (DP): {lis_dp(arr)}")  # Expected: 1
    print(f"LIS length (Binary Search): {lis_binary_search(arr)}")  # Expected: 1
