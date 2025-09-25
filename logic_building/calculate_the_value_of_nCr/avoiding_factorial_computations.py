"""Avoiding Factorial Computations"""


def multiplier(start: int, end: int) -> int:
    if start == end:
        return start
    result = 1
    while start <= end:
        result *= start
        start += 1
    return result


def nCr(n: int, r: int) -> int:
    """
    >>> nCr(5,2)
    10
    """
    if n < r:
        return 0
    if n == r or r == 0:
        return 1
    max_val = max(r, n - r)
    min_val = min(r, n - r)

    numerator = multiplier(max_val + 1, n)
    denominator = multiplier(1, min_val)
    return numerator // denominator


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
