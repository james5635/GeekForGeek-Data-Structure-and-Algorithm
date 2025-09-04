"""Using the modulo division operator"""


def check_division_by_4(n: str) -> bool:
    """
    >>> check_division_by_4(1234567589333862)
    False
    """
    return int(n) % 4 == 0


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
