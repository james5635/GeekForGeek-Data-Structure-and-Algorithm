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

if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
