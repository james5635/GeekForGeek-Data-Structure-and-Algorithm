"""Modified Euclidean Algorithm using Subtraction by Checking Divisibility"""


def gcd(a: int, b: int) -> int:
    """
    >>> gcd(20,28)
    4
    """
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        if a % b == 0:
            return b
        return gcd(a - b, b)
    if b % a == 0:
        return a
    return gcd(a, b - a)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
