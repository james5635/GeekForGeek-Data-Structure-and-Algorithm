"""Simple Approach"""


def kth_digits(a: int, b: int, k: int):
    """
    >>> kth_digits(5,2,1)
    5
    """

    # res = (a**b) % (10**k)
    mod = 10**k
    res = 1
    base = a
    while b > 0:
        if b & 1:
            res = (res * base) % mod
        base = (base * base) % mod
        b >>= 1

    for i in range(1, k):
        res //= 10
    return res


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
