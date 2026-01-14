"""Using Sieve of Eratosthenes (Smallest Prime Factor)"""


def _build_spf(limit: int) -> list[int]:
    """Build smallest prime factor (SPF) array up to limit."""
    spf = list(range(limit + 1))

    # 0 and 1 are not primes
    if limit >= 0:
        spf[0] = 0
    if limit >= 1:
        spf[1] = 1

    p = 2
    while p * p <= limit:
        if spf[p] == p:  # p is prime
            for multiple in range(p * p, limit + 1, p):
                if spf[multiple] == multiple:
                    spf[multiple] = p
        p += 1

    return spf


def prime_factors_spf(n: int) -> list[int]:
    """
    Return the **distinct** prime factors of n using SPF (sieve).

    This mirrors the smallest-prime-factor based approach from
    GeeksforGeeks DSA prime factor article.

    >>> prime_factors_spf(1)
    []
    >>> prime_factors_spf(2)
    [2]
    >>> prime_factors_spf(60)
    [2, 3, 5]
    >>> prime_factors_spf(100)
    [2, 5]
    """
    if n <= 1:
        return []

    spf = _build_spf(n)
    factors: list[int] = []
    last = -1

    while n > 1:
        p = spf[n]
        if p != last:
            factors.append(p)
            last = p
        n //= p

    return factors


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)

