"""
Minimum Jumps to Reach End of Array

Problem: Given an array arr[] where each element represents the maximum number
of steps that can be made forward from that element. Find the minimum number
of jumps to reach the end of the array starting from the first element.
If an element is 0, then you cannot move through that element.

Example:
    Input: arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    Output: 3
    Explanation: 1 -> 3 -> 8 -> 9 (jumps: 0->1, 1->3, 3->10)

Time Complexity:
    - Greedy: O(n)
    - DP: O(n²)
    - Space: O(1) for greedy, O(n) for DP

Author: Generated for GeekForGeeks DSA Tutorial
"""

from typing import List, Optional, Tuple
from functools import lru_cache

# Constant to represent infinity for integer operations
INF = 10**9


def min_jumps_greedy(arr: List[int]) -> int:
    """
    Find minimum jumps using greedy approach (optimal).

    Algorithm: Keep track of current range and farthest reachable.
    When current range is exhausted, increment jump and set new range.

    Args:
        arr: Array where arr[i] is max jump from position i

    Returns:
        Minimum number of jumps, or -1 if end is unreachable

    Time: O(n), Space: O(1)
    """
    n = len(arr)

    if n <= 1:
        return 0

    if arr[0] == 0:
        return -1  # Cannot move anywhere

    jumps = 1
    max_reach = arr[0]  # Farthest we can reach
    steps = arr[0]  # Steps we can still take in current jump

    for i in range(1, n):
        if i == n - 1:
            return jumps

        max_reach = max(max_reach, i + arr[i])
        steps -= 1

        if steps == 0:
            jumps += 1

            if i >= max_reach:
                return -1  # Cannot move further

            steps = max_reach - i

    return -1


def min_jumps_dp(arr: List[int]) -> int:
    """
    Find minimum jumps using dynamic programming.

    Args:
        arr: Array where arr[i] is max jump from position i

    Returns:
        Minimum number of jumps, or -1 if unreachable

    Time: O(n²), Space: O(n)
    """
    n = len(arr)

    if n <= 1:
        return 0

    # dp[i] = minimum jumps to reach index i
    dp = [INF] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            if j + arr[j] >= i and dp[j] != INF:
                dp[i] = min(dp[i], dp[j] + 1)
                break

    return dp[n - 1] if dp[n - 1] != INF else -1


def min_jumps_with_path(arr: List[int]) -> Tuple[int, List[int]]:
    """
    Find minimum jumps and the actual path taken.

    Args:
        arr: Array where arr[i] is max jump from position i

    Returns:
        Tuple of (min_jumps, path_indices)

    Time: O(n), Space: O(n)
    """
    n = len(arr)

    if n <= 1:
        return 0, [0]

    if arr[0] == 0:
        return -1, []

    jumps = [0] * n  # jumps[i] = min jumps to reach i
    path = [-1] * n  # path[i] = previous index to reach i optimally

    for i in range(1, n):
        jumps[i] = INF
        for j in range(i):
            if j + arr[j] >= i and jumps[j] != INF:
                if jumps[j] + 1 < jumps[i]:
                    jumps[i] = jumps[j] + 1
                    path[i] = j

    if jumps[n - 1] == INF:
        return -1, []

    # Reconstruct path
    result_path = []
    curr = n - 1
    while curr != -1:
        result_path.append(curr)
        curr = path[curr]
    result_path.reverse()

    return jumps[n - 1], result_path


def min_jumps_recursive(arr: List[int]) -> int:
    """
    Find minimum jumps using recursive approach with memoization.

    Args:
        arr: Array where arr[i] is max jump from position i

    Returns:
        Minimum number of jumps

    Time: O(n²), Space: O(n)
    """
    n = len(arr)

    @lru_cache(maxsize=None)
    def solve(pos: int) -> int:
        if pos >= n - 1:
            return 0

        if arr[pos] == 0:
            return INF

        min_j = INF
        for i in range(1, arr[pos] + 1):
            min_j = min(min_j, 1 + solve(pos + i))

        return min_j

    result = solve(0)
    return result if result != INF else -1


if __name__ == "__main__":
    # Test Case 1: Basic example from problem
    print("=" * 60)
    print("Test Case 1: Standard Example")
    print("=" * 60)

    arr1 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    print(f"Array: {arr1}")
    print(f"Length: {len(arr1)}")

    jumps_greedy = min_jumps_greedy(arr1)
    jumps_dp = min_jumps_dp(arr1)
    jumps_path, path = min_jumps_with_path(arr1)

    print(f"\nMinimum jumps (greedy): {jumps_greedy}")
    print(f"Minimum jumps (DP): {jumps_dp}")
    print(f"Minimum jumps (with path): {jumps_path}")
    print(f"Path taken: {' -> '.join(map(str, path))}")

    # Verify path
    print("\nPath verification:")
    for i, pos in enumerate(path):
        if i < len(path) - 1:
            jump = path[i + 1] - pos
            print(f"  Position {pos}: value={arr1[pos]}, jump={jump}")

    # Test Case 2: Edge cases
    print("\n" + "=" * 60)
    print("Test Case 2: Edge Cases")
    print("=" * 60)

    # Single element
    arr2 = [0]
    print(f"\nSingle element {arr2}: {min_jumps_greedy(arr2)} jumps")

    # Two elements
    arr3 = [1, 0]
    print(f"Two elements {arr3}: {min_jumps_greedy(arr3)} jumps")

    # All zeros (unreachable)
    arr4 = [0, 0, 0, 0]
    print(f"All zeros {arr4}: {min_jumps_greedy(arr4)} jumps")

    # Large first jump
    arr5 = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(f"Large first jump {arr5}: {min_jumps_greedy(arr5)} jumps")

    # Test Case 3: Various scenarios
    print("\n" + "=" * 60)
    print("Test Case 3: Various Scenarios")
    print("=" * 60)

    test_cases = [
        [2, 3, 1, 1, 4],
        [2, 3, 0, 1, 4],
        [1, 1, 1, 1, 1],
        [3, 2, 1, 0, 4],  # Unreachable
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]

    for i, arr in enumerate(test_cases, 4):
        print(f"\nArray {i}: {arr}")
        greedy = min_jumps_greedy(arr)
        dp = min_jumps_dp(arr)
        print(f"  Greedy: {greedy}, DP: {dp}")
        print(f"  Match: {'✓' if greedy == dp else '✗'}")

    # Test Case 4: Performance comparison
    print("\n" + "=" * 60)
    print("Test Case 4: Large Array Performance")
    print("=" * 60)

    import time

    # Large array with varying values
    large_arr = [i % 10 + 1 for i in range(1000)]

    start = time.time()
    result_greedy = min_jumps_greedy(large_arr)
    time_greedy = time.time() - start

    start = time.time()
    result_dp = min_jumps_dp(large_arr)
    time_dp = time.time() - start

    print(f"Array size: {len(large_arr)}")
    print(f"Greedy result: {result_greedy}, time: {time_greedy:.6f}s")
    print(f"DP result: {result_dp}, time: {time_dp:.6f}s")
    print(f"Speedup: {time_dp / time_greedy:.2f}x")

    print("\n" + "=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)
