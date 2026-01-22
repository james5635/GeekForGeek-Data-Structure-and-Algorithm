"""Expected Approach - By using Binomial Coefficient"""


def binomial_coeff(n: int, k: int) -> int:
    """
    Returns value of Binomial Coefficient C(n, k).
    
    >>> binomial_coeff(5, 2)
    10
    >>> binomial_coeff(6, 3)
    20
    """
    res = 1

    # Since C(n, k) = C(n, n-k)
    if k > n - k:
        k = n - k

    # Calculate value of [n*(n-1)*...*(n-k+1)] / [k*(k-1)*...*1]
    for i in range(k):
        res *= n - i
        res //= i + 1

    return res


def find_catalan(n: int) -> int:
    """
    Find the nth Catalan number using binomial coefficient.
    
    We can also use the below formula to find nth Catalan number in O(n) time.
    C_n = (1/(n+1)) * C(2n, n)
    
    Below are steps to calculate Catalan numbers using the formula: 2nCn/(n+1)
    - Calculate 2nCn using the similar steps that we use to calculate nCr
    - Return the value 2nCn / (n + 1)
    
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
    # Calculate value of 2nCn
    c = binomial_coeff(2 * n, n)

    # return 2nCn / (n+1)
    return c // (n + 1)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
