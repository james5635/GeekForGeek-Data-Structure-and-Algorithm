"""
Lucas Numbers

Lucas numbers are similar to Fibonacci numbers but start with different initial values.
Each Lucas number is the sum of its two immediately preceding terms.

Definition:
    L(0) = 2
    L(1) = 1
    L(n) = L(n-1) + L(n-2) for n > 1

The Lucas sequence: 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, ...

Approaches implemented:
1. Recursion - O(2^n) time, O(n) space
2. Iterative (Space Optimized) - O(n) time, O(1) space

Examples:
    Input: n = 3
    Output: 4

    Input: n = 7
    Output: 29

    Input: n = 9
    Output: 76
"""


def lucas_recursive(n):
    """Find nth Lucas number using pure recursion."""
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas_recursive(n - 1) + lucas_recursive(n - 2)


def lucas(n):
    """
    Find nth Lucas number using iterative approach.

    Args:
        n: A non-negative integer

    Returns:
        The nth Lucas number
    """
    if n == 0:
        return 2

    a = 2
    b = 1

    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


if __name__ == "__main__":
    test_cases = [
        (0, 2),
        (1, 1),
        (2, 3),
        (3, 4),
        (4, 7),
        (5, 11),
        (6, 18),
        (7, 29),
        (8, 47),
        (9, 76),
        (10, 123),
    ]

    print("Lucas Numbers - Iterative (Space Optimized)")
    print("=" * 45)
    for n, expected in test_cases:
        result = lucas(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"L({n}) = {result} [Expected: {expected}] [{status}]")

    print()
    print("Lucas Numbers - Recursive")
    print("=" * 45)
    for n, expected in test_cases[:8]:
        result = lucas_recursive(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"L({n}) = {result} [Expected: {expected}] [{status}]")
