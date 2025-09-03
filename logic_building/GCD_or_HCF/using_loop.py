"""Using Loop"""


def gcd(a: int, b: int) -> int:
    """
    >>> gcd(20,28)
    4
    """
    result = min(a, b)
    while result > 0:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
    return result


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
