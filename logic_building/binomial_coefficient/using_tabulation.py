"""Using Bottom-Up DP (Tabulation) - O(n * k) Time and O(n * k) Space"""


def binomial_coeff(n: int, k: int) -> int:
    """
    Returns value of Binomial Coefficient C(n, k) using tabulation.
    
    The approach is similar to the previous one. Just instead of breaking down
    the problem recursively, we iteratively build up the solution by calculating
    in bottom-up manner. Maintain a dp[][] table such that dp[i][j] stores the
    count all unique possible paths to reach the cell (i, j).
    
    Base Case:
    - For i = j and 0 <= i <= n, dp[i][j] = 1
    - for j = 0 and 0 <= j <= min(i, k), dp[i][j] = 1
    
    Recursive Case:
    - For i > 1 and j > 1, dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    
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
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # Calculate value of Binomial Coefficient in bottom up manner
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base Cases
            if j == 0 or j == i:
                dp[i][j] = 1

            # Calculate value using previously stored values
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][k]


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
