"""Factorization using Trial Division"""

from math import isqrt


def prime_factors(n: int) -> list[int]:
    """
    Return the **distinct** prime factors of n using trial division.

    >>> prime_factors(1)
    []
    >>> prime_factors(2)
    [2]
    >>> prime_factors(60)
    [2, 3, 5]
    >>> prime_factors(100)
    [2, 5]
    """
    factors: list[int] = []

    if n <= 1:
        return factors

    # Factor out all 2s
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2

    # Factor out odd primes up to sqrt(n)
    i = 3
    while i <= isqrt(n):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
        i += 2

    # If remaining n is > 2, it is a prime factor
    if n > 2:
        factors.append(n)

    return factors


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)

