"""Substring to Integer Conversion"""


def check_division_by_4(num: str) -> bool:
    """
    >>> check_division_by_4("1234567589333862")
    False
    """
    if len(num) == 0:
        return False
    if len(num) == 1:
        return int(len(num[0])) % 4 == 0
    return int(num[-2:]) % 4 == 0


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
