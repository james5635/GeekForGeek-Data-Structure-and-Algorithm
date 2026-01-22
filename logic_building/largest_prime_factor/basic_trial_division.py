"""Naive Approach - Basic Trial Division"""


def largest_prime_factor(n: int) -> int:
    """
    Find the largest prime factor of a number using basic trial division.
    
    The method starts by removing all factors of 2, as it is the only even prime.
    Once 2 is completely removed, odd numbers are checked starting from 3.
    Each odd number is tested for divisibility, and the number is divided
    repeatedly until the factor is fully removed.
    This process continues for all odd numbers up to √n.
    If a number greater than 2 remains after all divisions, it is a prime
    number and the largest prime factor.
    
    >>> largest_prime_factor(6)
    3
    >>> largest_prime_factor(15)
    5
    >>> largest_prime_factor(28)
    7
    >>> largest_prime_factor(1)
    -1
    """
    largest_prime = -1

    # Check for factors of 2
    while n % 2 == 0:
        largest_prime = 2
        n //= 2

    # Check for odd factors starting from 3
    i = 3
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n //= i
        i += 2

    # If n is still greater than 2, it is a prime number
    if n > 2:
        largest_prime = n

    return largest_prime


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
