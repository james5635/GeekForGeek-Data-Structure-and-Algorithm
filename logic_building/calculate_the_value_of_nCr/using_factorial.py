"""Using Factorial"""


def nCr(n: int, r: int) -> int:
    """
    >>> nCr(5,2)
    10
    """
    if not (0 <= r and r <= n):
        raise ValueError("0 <= r <= n is not satisfied")

    return factorial(n) // (factorial(r) * factorial(n - r))


def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
