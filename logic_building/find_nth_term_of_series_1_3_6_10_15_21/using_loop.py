"""using loop"""


def term(n: int) -> int:
    """
    >>> term(4)
    10
    """
    ans = 0
    for i in range(1, n + 1):
        ans = ans + i
    return ans


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
