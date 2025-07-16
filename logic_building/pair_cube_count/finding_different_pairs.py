"""Finding different pairs"""

import math


def count_pair_cube(n: int) -> int:
    """
    >>> count_pair_cube(9)
    2
    """
    count = 0
    for i in range(1, int(math.pow(n, 1 / 3)) + 1):
        cb = i * i * i
        diff = n - cb
        cbrt_diff = round(diff ** (1 / 3))
        if cbrt_diff * cbrt_diff * cbrt_diff == diff:
            count += 1
    return count


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
