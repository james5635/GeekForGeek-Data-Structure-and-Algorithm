"""Formula Based Method (Not Overflow)"""


def find_sum_not_overflow(n: int) -> int:
    """
    >>> find_sum_not_overflow(10)
    55
    >>> find_sum_not_overflow(100)
    5050
    >>> find_sum_not_overflow(1000)
    500500
    """
    if n % 2 == 0:
        return (n // 2) * (n + 1)
    else:
        return n * ((n + 1) // 2)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
