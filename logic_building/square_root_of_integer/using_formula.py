"""Using Formula"""

import math


def floor_sqrt(n: int) -> int:
    """
    >>> floor_sqrt(11)
    3
    """
    res = int(math.exp(0.5 * math.log(n)))
    if (res + 1) ** 2 <= n:
        res += 1
    return res


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
