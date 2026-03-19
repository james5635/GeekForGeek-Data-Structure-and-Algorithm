from collections import deque


def max_sum_subsequence(arr, k):
    n = len(arr)
    if n == 0:
        return 0
    dp = [0] * n
    dq = deque()
    dp[0] = arr[0]
    dq.append(0)
    for i in range(1, n):
        while dq and dq[0] < i - k:
            dq.popleft()
        dp[i] = (dp[dq[0]] if dq else 0) + arr[i]
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        dq.append(i)
    return max(dp)


if __name__ == "__main__":
    arr = [10, -5, -2, 4, 0, 3]
    k = 3
    assert max_sum_subsequence(arr, k) == 17
    assert max_sum_subsequence([1, 15, 7, 9, 2, 5, 10], 3) == 39
    assert max_sum_subsequence([-1, -2, -3], 1) == -1
    assert max_sum_subsequence([], 3) == 0
    assert max_sum_subsequence([5], 1) == 5
    print("All tests passed!")
