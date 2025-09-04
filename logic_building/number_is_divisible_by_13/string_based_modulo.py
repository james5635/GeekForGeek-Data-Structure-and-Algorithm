"""String-Based Modulo"""


def check_division_by_13(num: str) -> bool:
    """
    >>> check_division_by_13("1234567589333862")
    False
    """
    remainder = 0
    for char in num:
        remainder = (remainder * 10 + int(char)) % 13
    return remainder == 0


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
