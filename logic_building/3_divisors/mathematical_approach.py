"""Mathematical Approach"""


def exactly_3_divisors(n: int) -> list[bool]:
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
    return prime


def count_divisors(n: int) -> int:
    """
    >>> count_divisors(100)
    4
    """
    total = 0
    prime = exactly_3_divisors(n)
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            total += 1
    return total


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
