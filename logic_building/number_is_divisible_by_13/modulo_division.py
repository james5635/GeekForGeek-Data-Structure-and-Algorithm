"""Modulo Division"""


def check_division_by_13(num: str) -> bool:
    """
    >>> check_division_by_13("1234567589333862")
    False
    """
    num_int = int(num)
    return num_int % 13 == 0


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
