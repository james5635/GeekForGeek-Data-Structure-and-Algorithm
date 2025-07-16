"""Using Mathematical Formula (Not Overflow)"""


def sum_of_squares_not_overflow(n: int) -> int:
    """
    >>> sum_of_squares_not_overflow(5)
    55
    >>> sum_of_squares_not_overflow(10)
    385
    >>> sum_of_squares_not_overflow(100)
    338350
    """
    return (n * (n + 1) // 2) * (2 * n + 1) // 3


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
