"""Using Mathematical Formula"""


def sum_of_squares(n: int) -> int:
    """
    >>> sum_of_squares(5)
    55
    >>> sum_of_squares(10)
    385
    >>> sum_of_squares(100)
    338350
    """

    return (n * (n + 1) * (2 * n + 1)) // 6


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
