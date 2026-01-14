"""Naive Approach - Iterating till n"""


def print_divisors(n: int) -> list[int]:
    """
    >>> print_divisors(10)
    [1, 2, 5, 10]
    >>> print_divisors(100)
    [1, 2, 4, 5, 10, 20, 25, 50, 100]
    """
    divisors: list[int] = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)

