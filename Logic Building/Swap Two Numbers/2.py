"""Without using Third Variable"""


def swap_by_arithmetic() -> None:
    """
    >>> swap_by_arithmetic()
    a = 2 b = 3
    a = 3 b = 2
    """
    a: int = 2
    b: int = 3
    print("a =", a, "b =", b)

    a = a + b
    b = a - b
    a = a - b
    print("a =", a, "b =", b)


def swap_by_bitwise() -> None:
    """
    >>> swap_by_bitwise()
    a = 2 b = 3
    a = 3 b = 2
    """
    a: int = 2
    b: int = 3
    print("a =", a, "b =", b)

    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("a =", a, "b =", b)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
