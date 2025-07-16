"""Logarithmic Method"""

import math


def is_power(x: int, y: int) -> bool:
    """
    >>> is_power(2,128)
    True
    """
    res = math.log(y) / math.log(x)
    return res == math.floor(res)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
