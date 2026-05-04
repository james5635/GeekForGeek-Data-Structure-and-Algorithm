"""
Tribonacci Numbers

The Tribonacci sequence is a generalization of the Fibonacci sequence where
each term is the sum of the three preceding terms.

Definition:
    T(0) = 0
    T(1) = 0
    T(2) = 1
    T(n) = T(n-1) + T(n-2) + T(n-3) for n > 2

The Tribonacci sequence: 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, ...

Approaches implemented:
1. Recursion - O(3^n) time, O(n) space
2. Memoization (Top-Down DP) - O(n) time, O(n) space
3. Tabulation (Bottom-Up DP) - O(n) time, O(n) space
4. Space Optimized - O(n) time, O(1) space
5. Matrix Exponentiation - O(log n) time, O(log n) space

Examples:
    Input: n = 5
    Output: 0, 0, 1, 1, 2

    Input: n = 10
    Output: 0, 0, 1, 1, 2, 4, 7, 13, 24, 44
"""


def tribonacci_recursive(n):
    """Find nth Tribonacci number using pure recursion."""
    if n == 0 or n == 1 or n == 2:
        return 0
    if n == 3:
        return 1
    return (
        tribonacci_recursive(n - 1)
        + tribonacci_recursive(n - 2)
        + tribonacci_recursive(n - 3)
    )


def tribonacci_memoization(n):
    """Find nth Tribonacci number using top-down DP with memoization."""
    memo = {}

    def tribo(n):
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            return 0
        if n == 2:
            return 1

        res = tribo(n - 3) + tribo(n - 2) + tribo(n - 1)
        memo[n] = res
        return res

    return tribo(n)


def tribonacci_tabulation(n):
    """
    Generate first n Tribonacci numbers using bottom-up DP (tabulation).

    Args:
        n: Number of Tribonacci numbers to generate

    Returns:
        List of first n Tribonacci numbers
    """
    if n < 1:
        return []

    dp = [0] * n
    if n >= 1:
        dp[0] = 0
    if n >= 2:
        dp[1] = 0
    if n >= 3:
        dp[2] = 1

    for i in range(3, n):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp


def print_tribonacci(n):
    """
    Print first n Tribonacci numbers using space-optimized approach.

    Args:
        n: Number of Tribonacci numbers to print
    """
    if n < 1:
        return

    first = 0
    second = 0
    third = 1

    result = [first]
    if n > 1:
        result.append(second)
    if n > 2:
        result.append(third)

    for _ in range(3, n):
        curr = first + second + third
        first = second
        second = third
        third = curr
        result.append(curr)

    return result


def tribonacci(n):
    """
    Find nth Tribonacci number using matrix exponentiation.

    Uses the transformation matrix:
        | 1  1  1 |
        | 1  0  0 |
        | 0  1  0 |

    Args:
        n: Index of the Tribonacci number to find

    Returns:
        The nth Tribonacci number
    """
    if n == 0 or n == 1:
        return 0

    def multiply(T, M):
        a = T[0][0] * M[0][0] + T[0][1] * M[1][0] + T[0][2] * M[2][0]
        b = T[0][0] * M[0][1] + T[0][1] * M[1][1] + T[0][2] * M[2][1]
        c = T[0][0] * M[0][2] + T[0][1] * M[1][2] + T[0][2] * M[2][2]
        d = T[1][0] * M[0][0] + T[1][1] * M[1][0] + T[1][2] * M[2][0]
        e = T[1][0] * M[0][1] + T[1][1] * M[1][1] + T[1][2] * M[2][1]
        f = T[1][0] * M[0][2] + T[1][1] * M[1][2] + T[1][2] * M[2][2]
        g = T[2][0] * M[0][0] + T[2][1] * M[1][0] + T[2][2] * M[2][0]
        h = T[2][0] * M[0][1] + T[2][1] * M[1][1] + T[2][2] * M[2][1]
        i = T[2][0] * M[0][2] + T[2][1] * M[1][2] + T[2][2] * M[2][2]

        T[0][0], T[0][1], T[0][2] = a, b, c
        T[1][0], T[1][1], T[1][2] = d, e, f
        T[2][0], T[2][1], T[2][2] = g, h, i

    def power(T, n):
        if n == 0 or n == 1:
            return

        M = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]

        power(T, n // 2)
        multiply(T, T)

        if n % 2:
            multiply(T, M)

    T = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
    power(T, n - 2)

    return T[0][0]


if __name__ == "__main__":
    expected_sequence = [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927]

    print("Tribonacci Numbers - Space Optimized (First 15)")
    print("=" * 50)
    result = print_tribonacci(15)
    print("Generated:", result)
    print("Expected: ", expected_sequence)
    print("Status:   ", "PASS" if result == expected_sequence else "FAIL")

    print()
    print("Tribonacci Numbers - Tabulation (First 15)")
    print("=" * 50)
    result = tribonacci_tabulation(15)
    print("Generated:", result)
    print("Expected: ", expected_sequence)
    print("Status:   ", "PASS" if result == expected_sequence else "FAIL")

    print()
    print("Tribonacci Numbers - Matrix Exponentiation")
    print("=" * 50)
    for i, expected in enumerate(expected_sequence):
        result = tribonacci(i)
        status = "PASS" if result == expected else "FAIL"
        print(f"T({i}) = {result} [Expected: {expected}] [{status}]")

    print()
    print("Tribonacci Numbers - Memoization")
    print("=" * 50)
    for i, expected in enumerate(expected_sequence):
        result = tribonacci_memoization(i)
        status = "PASS" if result == expected else "FAIL"
        print(f"T({i}) = {result} [Expected: {expected}] [{status}]")
