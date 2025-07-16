""" Using Bitwise AND Operator """

def is_even(n: int) -> bool:
    """
    >>> is_even(10)
    True
    >>> is_even(11)
    False
    """
    if n & 1 == 0:
        return True
    else:
        return False
if __name__ == "__main__":
    from doctest import testmod
    testmod()