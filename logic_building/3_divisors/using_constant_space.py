"""Using Constant Space"""


def is_prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_divisors(n: int) -> int:
    """
    >>> count_divisors(100)
    4
    """
    total = 0
    for i in range(2, int(n**0.5) + 1):
        if is_prime(i):
            total += 1
    return total


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
