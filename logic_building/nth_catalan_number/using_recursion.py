"""Naive Approach - By using Recursion"""


def find_catalan(n: int) -> int:
    """
    Find the nth Catalan number using recursion.
    
    Catalan numbers satisfy the following recursive formula:
    C_0 = C_1 = 1 and C_n = sum(C_i * C_{n-i-1}) for i = 0 to n-1, for n >= 2
    
    Step-by-step approach:
    - Base condition for the recursive approach, when n <= 1, return 1.
    - Iterate from i = 0 to i < n.
      - Make a recursive call catalan(i) and catalan(n - i - 1) and keep
        adding the product of both into res.
    - Return the res.
    
    >>> find_catalan(0)
    1
    >>> find_catalan(1)
    1
    >>> find_catalan(2)
    2
    >>> find_catalan(3)
    5
    >>> find_catalan(4)
    14
    >>> find_catalan(5)
    42
    >>> find_catalan(6)
    132
    """
    # Base case
    if n <= 1:
        return 1

    # catalan(n) is sum of catalan(i) * catalan(n-i-1)
    res = 0
    for i in range(n):
        res += find_catalan(i) * find_catalan(n - i - 1)

    return res


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
