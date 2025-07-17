"""Divisor Sum Method"""


def is_perfect(n: int) -> int:
    """
    >>> is_perfect(15)
    False
    """
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
