"""By using multiplicative Binomial Coefficient formula"""


def nCr(n: int, r: int) -> int:
    """
    >>> nCr(5,2)
    10
    """
    product = 1
    for i in range(1, r + 1):
        product = product * (n - r + i) // i
    return product


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
