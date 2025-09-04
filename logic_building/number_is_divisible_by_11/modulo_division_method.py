"""Modulo Division Method"""


def check_division_by_11(num: str) -> bool:
    """
    >>> check_division_by_11("1234567589333862")
    False
    """
    num_int = int(num)
    return num_int % 11 == 0


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
