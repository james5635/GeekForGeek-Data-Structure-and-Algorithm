"""Taking Input Number as String"""


def sum_of_digits(s: str) -> int:
    """
    >>> sum_of_digits("12345")
    15
    >>> sum_of_digits("0")
    0
    >>> sum_of_digits("9999")
    36
    >>> sum_of_digits("1234567890")
    45
    >>> sum_of_digits("123456789123456789123422")
    104
    """
    sum: int = 0
    for i in range(len(s)):
        digit: int = ord(s[i]) - ord("0")
        sum += digit
    return sum


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
