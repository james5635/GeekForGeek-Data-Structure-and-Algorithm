"""Exponentiation and Binary Search Method"""

import math


def is_power(x: int, y: int) -> bool:
    """
    >>> is_power(10,1)
    True
    >>> is_power(1,20)
    False
    >>> is_power(2,128)
    True
    >>> is_power(2,30)
    False
    """
    if x == 1:
        return y == 1
    if y == 1:
        return True

    pow = x
    while pow < y:
        pow *= x
    if pow == y:
        return True

    # Double check
    low, high = x, pow
    while low <= high:
        mid = low + (high - low) // 2
        result = int(x ** int(math.log(mid) / math.log(x)))
        if result == y:
            return True
        if result < y:
            low = mid + 1
        else:
            high = mid - 1
    return False


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
