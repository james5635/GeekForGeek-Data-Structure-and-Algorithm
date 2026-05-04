"""
Matrix Chain Multiplication

Given an array arr[] where the dimension of the ith matrix is (arr[i-1] x arr[i]),
find the minimum number of scalar multiplications needed to multiply the chain of matrices.

When two matrices of size m*n and n*p are multiplied, the resulting matrix is of size m*p
and the number of scalar multiplications performed is m*n*p.

Approaches implemented:
1. Recursion - O(2^n) time, O(n) space
2. Memoization (Top-Down DP) - O(n^3) time, O(n^2) space
3. Tabulation (Bottom-Up DP) - O(n^3) time, O(n^2) space

Examples:
    Input: arr = [2, 1, 3, 4]
    Output: 20
    Explanation: ((M1 x M2) x M3) requires 30 multiplications
                 (M1 x (M2 x M3)) requires 20 multiplications (minimum)
"""


def matrix_chain_multiplication_recursive(arr):
    """Find minimum multiplications using pure recursion."""

    def min_mult_rec(i, j):
        if i + 1 == j:
            return 0

        res = float("inf")
        for k in range(i + 1, j):
            curr = min_mult_rec(i, k) + min_mult_rec(k, j) + arr[i] * arr[k] * arr[j]
            res = min(curr, res)

        return res

    return min_mult_rec(0, len(arr) - 1)


def matrix_chain_multiplication_memoization(arr):
    """Find minimum multiplications using top-down DP with memoization."""

    def min_mult_rec(i, j, memo):
        if i + 1 == j:
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        res = float("inf")
        for k in range(i + 1, j):
            curr = (
                min_mult_rec(i, k, memo)
                + min_mult_rec(k, j, memo)
                + arr[i] * arr[k] * arr[j]
            )
            res = min(res, curr)

        memo[i][j] = res
        return res

    n = len(arr)
    memo = [[-1] * n for _ in range(n)]
    return min_mult_rec(0, n - 1, memo)


def matrix_chain_multiplication(arr):
    """
    Find minimum multiplications using bottom-up DP (tabulation).

    Args:
        arr: List of dimensions where matrix i has dimensions arr[i-1] x arr[i]

    Returns:
        Minimum number of scalar multiplications needed
    """
    n = len(arr)

    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = float("inf")

            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


if __name__ == "__main__":
    test_cases = [
        ([2, 1, 3, 4], 20),
        ([1, 2, 3, 4, 3], 30),
        ([3, 4], 0),
        ([10, 20, 30], 6000),
        ([40, 20, 30, 10, 30], 26000),
    ]

    print("Matrix Chain Multiplication - Tabulation (Bottom-Up DP)")
    print("=" * 55)
    for arr, expected in test_cases:
        result = matrix_chain_multiplication(arr)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: {arr}")
        print(f"  Expected: {expected}, Got: {result} [{status}]")
        print()

    print("Matrix Chain Multiplication - Memoization (Top-Down DP)")
    print("=" * 55)
    for arr, expected in test_cases:
        result = matrix_chain_multiplication_memoization(arr)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: {arr}")
        print(f"  Expected: {expected}, Got: {result} [{status}]")
        print()
