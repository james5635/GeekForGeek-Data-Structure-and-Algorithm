"""Alternate Approach - By using the (n-1)th Catalan Number"""


def find_catalan(n: int) -> int:
    """
    Find the nth Catalan number using iterative formula.
    
    We already know how to calculate the nth Catalan Number using the formula:
    C_n = (2n)! / ((n+1)! * n!)
    
    This formula can be further simplified to express the nth Catalan Number
    in terms of (n-1)th Catalan Number:
    C_n = (2(2n-1) / (n+1)) * C_{n-1} for n > 0
    
    Below are steps to calculate Catalan numbers using the above formula:
    - Initialize a variable res = 1
    - Use the iterative approach to calculate the nth Catalan number
    - Iterate from i = 2 to i <= n
      - Update res with res = (res * (4 * i - 2)) / (i + 1)
    - Return res
    
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
    if n <= 1:
        return 1
    
    res = 1

    # Use the iterative approach to calculate the nth Catalan number
    for i in range(2, n + 1):
        res = (res * (4 * i - 2)) // (i + 1)

    return res


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
