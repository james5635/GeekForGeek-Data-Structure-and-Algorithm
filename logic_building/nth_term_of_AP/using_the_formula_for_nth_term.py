"""Using the Formula for nth Term"""


def nth_term_of_AP(a1: int, a2: int, n: int) -> int:
    """
    >>> nth_term_of_AP(2, 4, 5)
    10
    >>> nth_term_of_AP(1, 3, 10)
    19
    >>> nth_term_of_AP(5, 10, 1)
    5
    """

    return a1 + (n - 1) * (a2 - a1)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
