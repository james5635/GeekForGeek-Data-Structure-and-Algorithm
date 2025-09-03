"""Using Built In functions"""

import math


def floor_sqrt(n: int) -> int:
    """
    >>> floor_sqrt(11)
    3
    """
    res = int(math.sqrt(n))
    return res


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
