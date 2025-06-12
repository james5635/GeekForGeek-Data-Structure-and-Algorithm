"""Another Appoach"""

import math


def is_prime(n: int) -> bool:
    """
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    """
    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        return False
    return True


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
