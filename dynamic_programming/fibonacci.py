"""
Nth Fibonacci Number

The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n > 1

The sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

Approaches implemented:
1. Recursion - O(2^n) time, O(n) space
2. Memoization (Top-Down DP) - O(n) time, O(n) space
3. Tabulation (Bottom-Up DP) - O(n) time, O(n) space
4. Space Optimized - O(n) time, O(1) space
5. Matrix Exponentiation - O(log n) time, O(log n) space

Examples:
    Input: n = 2
    Output: 1

    Input: n = 5
    Output: 5
"""


def nth_fibonacci_recursive(n):
    """Find nth Fibonacci number using pure recursion."""
    if n <= 1:
        return n
    return nth_fibonacci_recursive(n - 1) + nth_fibonacci_recursive(n - 2)


def nth_fibonacci_memoization(n):
    """Find nth Fibonacci number using top-down DP with memoization."""

    def fib_util(n, dp):
        if n <= 1:
            return n

        if dp[n] != -1:
            return dp[n]

        dp[n] = fib_util(n - 1, dp) + fib_util(n - 2, dp)
        return dp[n]

    dp = [-1] * (n + 1)
    return fib_util(n, dp)


def nth_fibonacci_tabulation(n):
    """Find nth Fibonacci number using bottom-up DP (tabulation)."""
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def nth_fibonacci(n):
    """
    Find nth Fibonacci number using space-optimized iterative approach.

    Args:
        n: A non-negative integer

    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n

    prev2 = 0
    prev1 = 1

    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


def _multiply(mat1, mat2):
    """Multiply two 2x2 matrices in place."""
    x = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]
    y = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]
    z = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]
    w = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]

    mat1[0][0], mat1[0][1] = x, y
    mat1[1][0], mat1[1][1] = z, w


def _matrix_power(mat, n):
    """Raise a 2x2 matrix to power n using exponentiation by squaring."""
    if n == 0 or n == 1:
        return

    mat2 = [[1, 1], [1, 0]]

    _matrix_power(mat, n // 2)
    _multiply(mat, mat)

    if n % 2 != 0:
        _multiply(mat, mat2)


def nth_fibonacci_matrix(n):
    """Find nth Fibonacci number using matrix exponentiation."""
    if n <= 1:
        return n

    mat = [[1, 1], [1, 0]]
    _matrix_power(mat, n - 1)

    return mat[0][0]


if __name__ == "__main__":
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (10, 55),
    ]

    print("Nth Fibonacci Number - Space Optimized")
    print("=" * 40)
    for n, expected in test_cases:
        result = nth_fibonacci(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"F({n}) = {result} [Expected: {expected}] [{status}]")

    print()
    print("Nth Fibonacci Number - Matrix Exponentiation")
    print("=" * 40)
    for n, expected in test_cases:
        result = nth_fibonacci_matrix(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"F({n}) = {result} [Expected: {expected}] [{status}]")

    print()
    print("Nth Fibonacci Number - Tabulation")
    print("=" * 40)
    for n, expected in test_cases:
        result = nth_fibonacci_tabulation(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"F({n}) = {result} [Expected: {expected}] [{status}]")
