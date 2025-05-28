"""Using Third Variable"""


def main() -> None:
    """
    >>> main()
    a = 2 b = 3
    a = 3 b = 2
    """
    a = 2
    b = 3
    print("a =", a, "b =", b)

    temp = a
    a = b
    b = temp
    print("a =", a, "b =", b)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
