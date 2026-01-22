"""Using Sieve of Eratosthenes"""


def sieve_of_eratosthenes(n: int) -> list[bool]:
    """
    Generate all prime numbers less than or equal to n using Sieve of Eratosthenes.
    
    Returns a boolean array where isPrime[i] is True if i is prime, False otherwise.
    
    >>> is_prime = sieve_of_eratosthenes(10)
    >>> [i for i in range(len(is_prime)) if is_prime[i]]
    [2, 3, 5, 7]
    """
    # Initialize all entries of boolean array as true
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                is_prime[i] = False

    return is_prime


def super_primes(n: int) -> list[int]:
    """
    Find all super primes less than or equal to n.
    
    Super-prime numbers (also known as higher order primes) are the subsequence
    of prime number sequence that occupy prime-numbered positions within the
    sequence of all prime numbers. The first few super primes are 3, 5, 11, and 17.
    
    The idea is to generate all the primes less than or equal to the given number
    n using the Sieve of Eratosthenes. Once we have generated all such primes,
    we iterate through the array and print all prime number that occupy prime
    number positions.
    
    Step-by-step approach:
    1. Generate all primes up to n using Sieve of Eratosthenes
    2. Store all primes in an array
    3. For each prime at position k (1-indexed), check if k is also prime
    4. If yes, add that prime to the result
    
    Time complexity: O(n*log(log(n))) - Due to the use of Sieve of Eratosthenes
    Auxiliary Space: O(n) - Due to the array used to store primes up to n
    
    >>> super_primes(7)
    [3, 5]
    >>> super_primes(17)
    [3, 5, 11, 17]
    >>> super_primes(2)
    []
    >>> super_primes(1)
    []
    """
    # Generating primes using Sieve
    is_prime = sieve_of_eratosthenes(n)

    # Storing all the primes generated in an array
    primes = [i for i in range(2, n + 1) if is_prime[i]]

    # Collecting all those prime numbers that occupy prime-numbered
    # position in sequence of prime numbers (1-indexed positions)
    ans = []
    for k in range(len(primes)):
        # Position is k+1 (1-indexed), check if position is prime
        if k + 1 < len(is_prime) and is_prime[k + 1]:
            ans.append(primes[k])

    return ans


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
