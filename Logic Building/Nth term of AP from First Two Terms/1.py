"""Using for Loop"""


def nth_term_of_AP(a1: int, a2: int, n: int) -> int:
    """
    >>> nth_term_of_AP(2, 4, 5)
    10
    >>> nth_term_of_AP(1, 3, 10)
    19
    >>> nth_term_of_AP(5, 10, 1)
    5
    """
    nth_term: int = a1
    d: int = a2 - a1
    for i in range(1, n):
        nth_term += d
    return nth_term


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
