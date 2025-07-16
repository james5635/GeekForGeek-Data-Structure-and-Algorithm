"""Pythagorean theorem"""

import math


def distance(x1, y1, x2, y2):
    """
    >>> print("%.5f" % distance(3,4,4,3))
    1.41421
    """
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
