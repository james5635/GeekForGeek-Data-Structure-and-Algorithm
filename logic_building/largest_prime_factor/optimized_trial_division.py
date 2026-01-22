"""Expected Approach - Optimized Trial Division"""


def largest_prime_factor(n: int) -> int:
    """
    Find the largest prime factor of a number using optimized trial division.
    
    The method first removes all factors of 2 and 3 to simplify the number.
    After eliminating these smallest primes, further factorization follows a
    structured approach.
    Instead of checking all odd numbers, only numbers of the form 6k ± 1 are tested.
    This works because all prime numbers greater than 3 follow this pattern.
    By skipping unnecessary checks, the approach reduces iterations while
    efficiently finding the largest prime factor.
    
    >>> largest_prime_factor(6)
    3
    >>> largest_prime_factor(15)
    5
    >>> largest_prime_factor(28)
    7
    >>> largest_prime_factor(1)
    -1
    """
    # Initialize the maximum prime factor variable
    max_prime = -1

    # Check for factors of 2
    while n % 2 == 0:
        max_prime = 2
        n //= 2

    # Check for factors of 3
    while n % 3 == 0:
        max_prime = 3
        n //= 3

    # Check for odd factors starting from 5 and
    # incrementing by 6 (i and i+2)
    i = 5
    while i * i <= n:
        while n % i == 0:
            max_prime = i
            n //= i
        while n % (i + 2) == 0:
            max_prime = i + 2
            n //= (i + 2)
        i += 6

    # If n is still greater than 4, it is a prime number
    if n > 4:
        max_prime = n

    return max_prime


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
