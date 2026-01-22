"""Naive Approach - Repeated Multiplication Method - O(n) Time and O(1) Space"""


def pow_mod(x: int, n: int, M: int) -> int:
    """
    Compute (x^n) % M using repeated multiplication method.
    
    We initialize the result as 1 and iterate from 1 to n, updating the result
    by multiplying it with x and taking the modulo by M in each step to keep
    the number within integer bounds.
    
    >>> pow_mod(3, 2, 4)
    1
    >>> pow_mod(2, 6, 10)
    4
    >>> pow_mod(5, 3, 13)
    8
    >>> pow_mod(2, 0, 7)
    1
    """
    # Initialize result as 1 (since anything power 0 is 1)
    res = 1

    # n times to multiply x with itself
    for _ in range(n):
        # Multiplying res with x
        # and taking modulo to avoid overflow
        res = (res * x) % M

    return res


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
