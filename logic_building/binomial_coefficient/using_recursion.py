"""Using recursion - O(2^n) Time and O(n) Space"""


def binomial_coeff(n: int, k: int) -> int:
    """
    Returns value of Binomial Coefficient C(n, k) using recursion.
    
    The idea is to use recursion to find C(n, k). The value of C(n, k) can be
    recursively calculated using the following standard formula for Binomial
    Coefficients: C(n, k) = C(n-1, k-1) + C(n-1, k). C(n, 0) = C(n, n) = 1.
    So we just need to make recursive calls of C(n-1, k-1) and C(n-1, k).
    The base conditions will be when k = 0 or value of k and n be equal.
    
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
    # k cannot be greater than n so we return 0 here
    if k > n:
        return 0

    # base condition when k and n are equal or k = 0
    if k == 0 or k == n:
        return 1

    # Recursive add the value
    return binomial_coeff(n - 1, k - 1) + binomial_coeff(n - 1, k)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
