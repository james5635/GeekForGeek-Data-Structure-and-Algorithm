"""Using GCD LCM Formula"""


def gcd(a: int, b: int) -> int:
    return a if b == 0 else gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    """
    >>> lcm(10,5)
    10
    """
    return (a // gcd(a, b)) * b
    # return (a * b) // gcd(a, b)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
