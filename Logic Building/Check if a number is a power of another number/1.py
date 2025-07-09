"""Repeated Multiplication Method"""


def is_power(x: int, y: int) -> bool:
    """
    >>> is_power(10,1)
    True
    >>> is_power(1,20)
    False
    >>> is_power(2,128)
    True
    >>> is_power(2,30)
    False
    """
    if x == 1:
        return y == 1
    pow = 1
    while pow < y:
        pow *= x

    return pow == y


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
