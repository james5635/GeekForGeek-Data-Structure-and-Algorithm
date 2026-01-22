"""Naive Approach - Iterative GCD Method"""


def gcd(a: int, b: int) -> int:
    """
    Function to return gcd of a and b.
    
    >>> gcd(20, 28)
    4
    >>> gcd(11, 5)
    1
    >>> gcd(0, 5)
    5
    """
    if a == 0:
        return b
    return gcd(b % a, a)


def etf(n: int) -> int:
    """
    A simple method to evaluate Euler Totient Function.
    
    Euler's Totient function Φ(n) for an input n is the count of numbers in
    {1, 2, 3, ..., n-1} that are relatively prime to n, i.e., the numbers
    whose GCD (Greatest Common Divisor) with n is 1.
    
    A simple solution is to iterate through all numbers from 1 to n-1 and
    count numbers with gcd with n as 1.
    
    Time Complexity: O(n log n)
    Auxiliary Space: O(log min(a,b)) where a,b are the parameters of gcd function.
    
    >>> etf(11)
    10
    >>> etf(16)
    8
    >>> etf(1)
    1
    >>> etf(2)
    1
    """
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
