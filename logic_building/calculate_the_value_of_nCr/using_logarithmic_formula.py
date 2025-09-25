"""Using Logarithmic Formula"""

import math


def nCr(n: int, r: int) -> int:
    """
    >>> nCr(5,2)
    10
    """
    if r > n:
        return 0
    if r == 0 or n == r:
        return 1
    res = 0
    for i in range(r):
        res += math.log(n - i) - math.log(i + 1)
    return round(math.exp(res))


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
