"""Nested Loop Method"""


def exacly_3_divisors(n: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


def count_divisors(n: int) -> int:
    """
    >>> count_divisors(100)
    4
    """
    total = 0
    for i in range(1, n + 1):
        if exacly_3_divisors(i) == 3:
            total += 1
    return total


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
