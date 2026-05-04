"""
Program for nth Catalan Number

Catalan numbers are a sequence of natural numbers that occur in various
counting problems:
- Number of valid parenthesis expressions with n pairs
- Number of binary search trees with n keys
- Number of full binary trees with n+1 leaves
- Number of ways to draw n non-intersecting chords in a circle with 2n points

The nth Catalan number can be calculated using:
C_n = (1/(n+1)) * C(2n, n) where C is binomial coefficient

Time Complexity: O(n)
Space Complexity: O(1)
"""


def find_catalan(n):
    """
    Find the nth Catalan number using the formula:
    C_n = C_{n-1} * (4n - 2) / (n + 1)

    Args:
        n: Non-negative integer index

    Returns:
        The nth Catalan number
    """
    if n <= 1:
        return 1

    res = 1
    for i in range(2, n + 1):
        res = (res * (4 * i - 2)) // (i + 1)

    return res


def binomial_coeff(n, k):
    """
    Calculate binomial coefficient C(n, k).

    Args:
        n: Total number of items
        k: Number of items to choose

    Returns:
        Binomial coefficient C(n, k)
    """
    res = 1

    # Since C(n, k) = C(n, n-k)
    if k > n - k:
        k = n - k

    for i in range(k):
        res *= n - i
        res //= i + 1

    return res


def find_catalan_binomial(n):
    """
    Find the nth Catalan number using binomial coefficient:
    C_n = C(2n, n) / (n + 1)

    Args:
        n: Non-negative integer index

    Returns:
        The nth Catalan number
    """
    c = binomial_coeff(2 * n, n)
    return c // (n + 1)


if __name__ == "__main__":
    # Test cases
    test_cases = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]

    print("Catalan Numbers:")
    print("n\tResult\tExpected\tMatch")
    print("-" * 40)

    for n, exp in zip(test_cases, expected):
        result = find_catalan(n)
        match = "Yes" if result == exp else "No"
        print(f"{n}\t{result}\t{exp}\t\t{match}")

    # Additional test with binomial method
    print("\nVerifying with binomial coefficient method:")
    for n in range(10):
        result1 = find_catalan(n)
        result2 = find_catalan_binomial(n)
        print(f"C({n}) = {result1} (both methods match: {result1 == result2})")
