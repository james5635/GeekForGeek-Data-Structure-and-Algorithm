"""Using String"""


def reverse_digits(n: int) -> int:
    """
    >>> reverse_digits(1234)
    4321
    >>> reverse_digits(0)
    0
    >>> reverse_digits(1000)
    1
    >>> reverse_digits(987654321)
    123456789
    """
    s: str = str(n)
    digits: list[str] = list(s)
    digits.reverse()
    reversed_number = int("".join(digits))

    return reversed_number


def reverse_digits_2(n: int) -> int:
    """
    >>> reverse_digits_2(1234)
    4321
    >>> reverse_digits_2(0)
    0
    >>> reverse_digits_2(1000)
    1
    >>> reverse_digits_2(987654321)
    123456789
    """
    s: str = str(n)
    s_reversed: str = s[::-1]
    reversed_number = int(s_reversed)
    return reversed_number


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
