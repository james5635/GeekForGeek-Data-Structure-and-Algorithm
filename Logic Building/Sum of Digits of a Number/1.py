"""Iterative Approach"""


def sum_of_digits(n: int) -> int:
    """
    >>> sum_of_digits(12345)
    15
    >>> sum_of_digits(0)
    0
    >>> sum_of_digits(9999)
    36
    """
    sum = 0
    while n != 0:
        last = n % 10
        sum += last
        n //= 10
    return sum


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
