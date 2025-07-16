"""Adding One By One"""


def sum_of_squares(n: int) -> int:
    """
    >>> sum_of_squares(5)
    55
    >>> sum_of_squares(10)
    385
    >>> sum_of_squares(100)
    338350
    """
    return sum([i**2 for i in range(1, n + 1)])


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
