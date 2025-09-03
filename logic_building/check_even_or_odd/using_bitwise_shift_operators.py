"""Using Bitwise Shift Operators"""


def is_even(n: int) -> bool:
    """
    >>> is_even(10)
    True
    >>> is_even(11)
    False
    """
    if n == (n >> 1) << 1:
        return True
    else:
        return False


if __name__ == "__main__":
    from doctest import testmod

    testmod()
