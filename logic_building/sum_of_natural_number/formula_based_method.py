"""Formula Based Method"""


def find_sum(n: int) -> int:
    """
    >>> find_sum(10)
    55
    >>> find_sum(100)
    5050
    >>> find_sum(1000)
    500500
    """
    return n * (n + 1) // 2  # // ensure it return integer


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
