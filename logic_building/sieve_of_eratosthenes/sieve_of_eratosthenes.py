"""Efficient Approach - Sieve of Eratosthenes"""


def sieve(n: int) -> list[int]:
    """
    Find all prime numbers less than or equal to n using Sieve of Eratosthenes.
    
    The Sieve of Eratosthenes efficiently finds all primes up to n by repeatedly
    marking multiples of each prime as non-prime, starting from 2. This avoids
    redundant checks and quickly filters out all composite numbers.
    
    Step By Step Implementations:
    - Initialize a Boolean array prime[0..n] and set all entries to true, except
      for 0 and 1 (which are not primes).
    - Start from 2, the smallest prime number.
    - For each number p from 2 up to √n:
      - If p is marked as prime(true):
        - Mark all multiples of p as not prime(false), starting from p * p
          (since smaller multiples have already been marked by smaller primes).
    - After the loop ends, all the remaining true entries in prime represent
      prime numbers.
    
    Time Complexity: O(n*log(log(n))). For each prime number, we mark its
    multiples, which takes around n/p steps. The total time is proportional
    to n*(1/2 + 1/3 + 1/5 + ....). This sum over primes grows slowly and is
    approximately O(n*log(log(n))) making the algorithm very efficient.
    
    Auxiliary Space: O(n)
    
    >>> sieve(10)
    [2, 3, 5, 7]
    >>> sieve(35)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    >>> sieve(2)
    [2]
    >>> sieve(1)
    []
    """
    # Create a boolean list to track prime status of numbers
    prime = [True] * (n + 1)
    p = 2

    # Sieve of Eratosthenes algorithm
    while p * p <= n:
        if prime[p]:
            # Mark all multiples of p as non-prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Collect all prime numbers
    res = []
    for p in range(2, n + 1):
        if prime[p]:
            res.append(p)

    return res


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
