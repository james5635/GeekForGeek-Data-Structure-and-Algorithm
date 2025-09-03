"""Using if-else statement"""


def opposite_face(n: int) -> int | None:
    """
    >>> opposite_face(1)
    6
    >>> opposite_face(2)
    5
    >>> opposite_face(3)
    4
    """
    if n == 1:
        return 6
    elif n == 2:
        return 5
    elif n == 3:
        return 4
    elif n == 4:
        return 3
    elif n == 5:
        return 2
    elif n == 6:
        return 1
    return None


if __name__ == "__main__":
    from doctest import testmod

    testmod()
