"""Optimized Euclidean Algorithm by Checking Remainder"""


def gcd(a: int, b: int) -> int:
    """
    >>> gcd(20,28)
    4
    """
    return a if b == 0 else gcd(b, a % b)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
