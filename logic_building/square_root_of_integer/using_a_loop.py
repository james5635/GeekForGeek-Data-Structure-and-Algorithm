"""Using a loop"""

import math


def floor_sqrt(n: int) -> int:
    """
    >>> floor_sqrt(11)
    3
    """
    res = 1
    while res * res <= n:
        res += 1
    return res - 1


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
    print()
