"""Expected Approach - Modular Exponentiation Method - O(log(n)) Time and O(1) Space"""


def pow_mod(x: int, n: int, M: int) -> int:
    """
    Compute (x^n) % M using modular exponentiation (binary exponentiation).
    
    The idea of binary exponentiation is to reduce the exponent by half at each
    step, using squaring, which lowers the time complexity from O(n) to O(log n).
    -> x^n = (x^(n/2))^2 if n is even.
    -> x^n = x * x^(n-1) if n is odd.
    
    Step by step approach:
    - Start with the result as 1.
    - Use a loop that runs while the exponent n is greater than 0.
    - If the current exponent is odd, multiply the result by the current base
      and apply the modulo.
    - Square the base and take the modulo to keep the value within bounds.
    - Divide the exponent by 2 (ignore the remainder).
    - Repeat the process until the exponent becomes 0.
    
    >>> pow_mod(3, 2, 4)
    1
    >>> pow_mod(2, 6, 10)
    4
    >>> pow_mod(5, 3, 13)
    8
    >>> pow_mod(2, 0, 7)
    1
    """
    res = 1

    # Loop until exponent becomes 0
    while n >= 1:
        # n is odd, multiply result by current x and take modulo
        if n % 2 == 1:
            res = (res * x) % M

            # Make n even
            n -= 1
        else:
            # n is even, square the base and halve the exponent
            x = (x * x) % M
            n //= 2

    return res


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
