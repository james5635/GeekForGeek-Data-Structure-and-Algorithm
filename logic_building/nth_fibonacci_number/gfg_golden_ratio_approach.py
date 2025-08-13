"""GFG Golden ratio Approach"""

PHI = 1.6180339
prefib = [0, 1, 1, 2, 3, 5]


def nth_fibonacci(n: int) -> int:
    """
    >>> nth_fibonacci(5)
    5
    >>> nth_fibonacci(2)
    1
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 6:
        return prefib[n]
    fib = prefib[5]
    for _ in range(5, n):
        fib = round(fib * PHI)
    return fib


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
