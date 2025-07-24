"""using LCM_GCD method"""

from math import gcd


def add_two_fractions(a: list[int], b: list[int]) -> list[int]:
    """
    >>> add_two_fractions([1, 2],[3, 2])
    [2, 1]
    """
    den = gcd(a[1], b[1])
    # LCM * GCD = a * b
    den = a[1] * b[1] // den
    num = a[0] * (den // a[1]) + b[0] * (den // b[1])

    _gcd = gcd(num, den)
    den //= _gcd
    num //= _gcd
    return [num, den]


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
