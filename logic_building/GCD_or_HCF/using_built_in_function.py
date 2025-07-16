"""Using Built-in Function"""

import math


def gcd(a: int, b: int) -> int:
    """
    >>> gcd(20,28)
    4
    """
    return math.gcd(a, b)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
