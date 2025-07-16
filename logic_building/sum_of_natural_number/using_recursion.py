"""Using Recursion"""


def find_sum(n: int) -> int:
    """
    >>> find_sum(10)
    55
    >>> find_sum(100)
    5050
    >>> find_sum(1000)
    500500
    """
    if n == 1:
        return 1
    return n + find_sum(n - 1)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
