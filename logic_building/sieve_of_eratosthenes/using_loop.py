"""Naive Approach - Using Loop O(n*sqrt(n)) Time and O(1) Space"""


def is_prime(num: int) -> bool:
    """
    Check if a number is prime.
    
    >>> is_prime(2)
    True
    >>> is_prime(4)
    False
    >>> is_prime(17)
    True
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def sieve(n: int) -> list[int]:
    """
    Find all prime numbers less than or equal to n using naive approach.
    
    The Naive Approach for finding all prime numbers from 1 to n involves
    checking each number individually to determine whether it is prime.
    
    Step By Step Implementations:
    - Loop through all numbers i from 2 to n.
    - For each i, check if it is divisible by any number from 2 to i - 1.
    - If it is divisible, then i is not prime.
    - If it is not divisible by any number in that range, then i is prime.
    
    >>> sieve(10)
    [2, 3, 5, 7]
    >>> sieve(35)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    >>> sieve(2)
    [2]
    >>> sieve(1)
    []
    """
    res = []
    for i in range(2, n + 1):
        if is_prime(i):
            res.append(i)
    return res


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
