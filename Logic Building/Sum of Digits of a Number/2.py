"""Recursive Approach"""


def sum_of_digits(n: int) -> int:
    """
    >>> sum_of_digits(12345)
    15
    >>> sum_of_digits(0)
    0
    >>> sum_of_digits(9999)
    36
    """
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
