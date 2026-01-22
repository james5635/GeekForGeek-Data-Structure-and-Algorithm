"""Using Space Optimized DP - O(n * k) Time and O(k) Space"""


def binomial_coeff(n: int, k: int) -> int:
    """
    Returns value of Binomial Coefficient C(n, k) using space optimized DP.
    
    In the previous approach using dynamic programming, we derived a relation
    between states as follows: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    
    We do not need to maintain whole matrix for this. We can just maintain one
    array of length k and add dp[j-1] every time to dp[j].
    
    Approach:
    - Use a 1D array dp[] of size k+1 to store binomial coefficients, reducing
      space complexity to O(k).
    - Set dp[0] = 1, representing nC0 = 1.
    - Update dp[j] in reverse order, using the previous values from the same array.
    - Each entry dp[j] is updated as dp[j] + dp[j-1] for each row.
    - The final value of C(n,k) is stored in dp[k], and returned.
    
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
    dp = [0] * (k + 1)

    # nC0 is 1
    dp[0] = 1

    for i in range(1, n + 1):
        # Compute next row of pascal triangle using the previous row
        for j in range(min(i, k), 0, -1):
            dp[j] = dp[j] + dp[j - 1]

    return dp[k]


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
