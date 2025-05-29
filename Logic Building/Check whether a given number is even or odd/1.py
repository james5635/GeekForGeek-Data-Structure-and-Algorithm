""" By Finding the Remainder """

def isEven(n: int) -> bool:
    """
    >>> isEven(10)
    true
    >>> isEven(11)
    false
    """
    return n % 2 == 0

if __name__ == "__main__":
    from doctest import testmod
    testmod()