"""Expected Approach - Euler's Product Formula"""


def etf(n: int) -> int:
    """
    Evaluate Euler Totient Function using Euler's Product Formula.
    
    Euler's Totient function Φ(n) for an input n is the count of numbers in
    {1, 2, 3, ..., n-1} that are relatively prime to n, i.e., the numbers
    whose GCD (Greatest Common Divisor) with n is 1.
    
    If n is a positive integer and its prime factorization is:
    n = p₁^e₁ · p₂^e₂ · ... · pₖ^eₖ
    
    Where p₁, p₂, ..., pₖ are distinct prime factors of n, then:
    φ(n) = n · (1 - 1/p₁) · (1 - 1/p₂) · ... · (1 - 1/pₖ)
    
    The idea is based on Euler's product formula which states that the value
    of totient functions is below the product overall prime factors p of n.
    
    Algorithm:
    1) Initialize result as n
    2) Consider every number 'p' (where 'p' varies from 2 to √n).
       If p divides n, then do following:
       a) Subtract all multiples of p from 1 to n [all multiples of p will
          have gcd more than 1 (at least p) with n]
       b) Update n by repeatedly dividing it by p.
    3) If the reduced n is more than 1, then remove all multiples of n
       from result.
    
    Time Complexity: O(√n)
    Auxiliary Space: O(1)
    
    >>> etf(11)
    10
    >>> etf(16)
    8
    >>> etf(1)
    1
    >>> etf(2)
    1
    >>> etf(5)
    4
    """
    result = n

    # Consider all prime factors of n and subtract their multiples from result
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p

            result -= result // p
        p += 1

    # If n has a prime factor greater than sqrt(n)
    # (There can be at-most one such prime factor)
    if n > 1:
        result -= result // n

    return result


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
