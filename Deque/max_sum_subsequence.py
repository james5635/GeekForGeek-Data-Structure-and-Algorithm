"""
Maximum Sum Subsequence with K distance constraint
Find maximum sum where consecutive selected elements must have index difference >= k
Uses DP with deque for optimization
"""

from collections import deque


def max_sum_subsequence(arr, k):
    """
    Find maximum sum subsequence where consecutive elements must be at least k indices apart.
    Constraint: if we select arr[i] and arr[j] consecutively, then |i - j| >= k
    """
    if not arr:
        return 0

    n = len(arr)
    dp = [float("-inf")] * n

    for i in range(n):
        dp[i] = arr[i]
        for j in range(max(0, i - k), i):
            if dp[j] != float("-inf"):
                dp[i] = max(dp[i], dp[j] + arr[i])

    return max(dp) if dp else 0


def max_sum_subsequence_optimized(arr, k):
    """
    Optimized using deque for sliding window maximum
    """
    if not arr:
        return 0

    n = len(arr)
    if k == 0:
        return sum(max(0, x) for x in arr)

    dp = [float("-inf")] * n
    dq = deque()

    for i in range(n):
        while dq and dq[0] < i - k:
            dq.popleft()

        if dq:
            dp[i] = max(dp[i], dq[0] + arr[i])

        dp[i] = max(dp[i], arr[i])

        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        dq.append(i)

    return max(dp) if any(x != float("-inf") for x in dp) else 0


def reconstruct_subsequence(arr, k):
    """
    Reconstruct the subsequence that gives maximum sum
    """
    if not arr:
        return []

    n = len(arr)
    dp = [float("-inf")] * n
    parent = [-1] * n

    for i in range(n):
        dp[i] = arr[i]
        for j in range(max(0, i - k), i):
            if dp[j] != float("-inf") and dp[j] + arr[i] > dp[i]:
                dp[i] = dp[j] + arr[i]
                parent[i] = j

    max_idx = max(range(n), key=lambda x: dp[x])

    result = []
    idx = max_idx
    while idx != -1:
        result.append(arr[idx])
        idx = parent[idx]

    return result[::-1]


def main():
    print("=" * 60)
    print("Maximum Sum Subsequence with K Distance Constraint")
    print("=" * 60)

    print("\n--- Test Case 1 ---")
    arr = [10, -5, -2, 4, 0, 3]
    k = 3
    result = max_sum_subsequence(arr, k)
    subsequence = reconstruct_subsequence(arr, k)
    print(f"Input: arr = {arr}, k = {k}")
    print(f"Output: {result} (subsequence: {subsequence})")
    print(f"Expected: 17 (10->4->3)")
    print(f"Pass: {result == 17}")

    print("\n--- Test Case 2 ---")
    arr = [1, -5, -20, 4, -1, 3, -6, -3]
    k = 2
    result = max_sum_subsequence(arr, k)
    subsequence = reconstruct_subsequence(arr, k)
    print(f"Input: arr = {arr}, k = {k}")
    print(f"Output: {result} (subsequence: {subsequence})")
    print(f"Expected: 7 (4->3)")

    print("\n--- Test Case 3 ---")
    arr = [5, 5, 5, 5, 5]
    k = 1
    result = max_sum_subsequence(arr, k)
    subsequence = reconstruct_subsequence(arr, k)
    print(f"Input: arr = {arr}, k = {k}")
    print(f"Output: {result} (subsequence: {subsequence})")
    print(f"Expected: 15")
    print(f"Pass: {result == 15}")

    print("\n--- Test Case 4 ---")
    arr = [1, 2, 3, 4, 5]
    k = 5
    result = max_sum_subsequence(arr, k)
    subsequence = reconstruct_subsequence(arr, k)
    print(f"Input: arr = {arr}, k = {k}")
    print(f"Output: {result} (subsequence: {subsequence})")
    print(f"Expected: 5")
    print(f"Pass: {result == 5}")

    print("\n--- Test Case 5 ---")
    arr = [1, 2, 3, 4, 5]
    k = 1
    result = max_sum_subsequence(arr, k)
    subsequence = reconstruct_subsequence(arr, k)
    print(f"Input: arr = {arr}, k = {k}")
    print(f"Output: {result} (subsequence: {subsequence})")
    print(f"Expected: 9 (1,3,5 or 2,4)")

    print("\n--- Test Case 6 ---")
    arr = []
    k = 2
    result = max_sum_subsequence(arr, k)
    print(f"Input: arr = {arr}, k = {k}")
    print(f"Output: {result}")
    print(f"Expected: 0")
    print(f"Pass: {result == 0}")


if __name__ == "__main__":
    main()
