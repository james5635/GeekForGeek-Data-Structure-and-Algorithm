"""Expected Approach - Finding all factors in pairs"""


def print_divisors(n: int) -> list[int]:
    """
    >>> sorted(print_divisors(10))
    [1, 2, 5, 10]
    >>> sorted(print_divisors(100))
    [1, 2, 4, 5, 10, 20, 25, 50, 100]
    """
    divisors: list[int] = []

    i = 1
    while i * i <= n:
        if n % i == 0:
            if n // i == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(n // i)
        i += 1

    return divisors


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)

