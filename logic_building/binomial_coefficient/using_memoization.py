"""Top-Down DP (Memoization) - O(n * k) Time and O(n * k) Space"""


def getnCk(n: int, k: int, memo: list[list[int]]) -> int:
    """
    Helper function to compute binomial coefficient with memoization.
    
    >>> memo = [[-1 for _ in range(3)] for _ in range(6)]
    >>> getnCk(5, 2, memo)
    10
    """
    # k cannot be greater than n so we return 0 here
    if k > n:
        return 0

    # base condition when k and n are equal or k = 0
    if k == 0 or k == n:
        return 1

    # Check if pair n and k is already calculated then return it from here
    if memo[n][k] != -1:
        return memo[n][k]

    # Recursive add the value and store to memo table
    memo[n][k] = getnCk(n - 1, k - 1, memo) + getnCk(n - 1, k, memo)
    return memo[n][k]


def binomial_coeff(n: int, k: int) -> int:
    """
    Returns value of Binomial Coefficient C(n, k) using memoization.
    
    It should be noted that the recursive function computes the same subproblems
    again and again. This approach has two properties of Dynamic Programming:
    
    1. Optimal Substructure: The value of C(n, k) depends on the optimal solutions
       of the subproblems C(n-1, k-1) and C(n-1, k). By adding these optimal
       substructures, we can efficiently calculate the total value of C(n, k).
    
    2. Overlapping Subproblems: While applying a recursive approach in this
       problem, we notice that certain subproblems are computed multiple times.
       For large values of n, there will be many common subproblems.
    
    The Binomial Coefficient C(n, k) is computed recursively, but to avoid
    redundant calculations, dynamic programming with memoization is used. A 2D
    table stores previously computed values, allowing efficient lookups instead
    of recalculating.
    
    >>> binomial_coeff(4, 2)
    6
    >>> binomial_coeff(5, 2)
    10
    >>> binomial_coeff(6, 3)
    20
    >>> binomial_coeff(5, 0)
    1
    >>> binomial_coeff(5, 5)
    1
    >>> binomial_coeff(3, 5)
    0
    """
    # Create table for memoization
    memo = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]

    return getnCk(n, k, memo)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
