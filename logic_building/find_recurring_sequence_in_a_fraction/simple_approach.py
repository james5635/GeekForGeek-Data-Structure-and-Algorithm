"""simple approach"""

from tabnanny import verbose


def find_recurring_sequence(numerator: int, denominator: int) -> str | None:
    """
    >>> find_recurring_sequence(50,22)
    '27'
    >>> find_recurring_sequence(10,2) == None
    True
    """
    res = ""
    map = {}
    remainder = numerator % denominator
    while remainder != 0 and remainder not in map:
        map[remainder] = len(res)
        remainder = remainder * 10
        res += str(remainder // denominator)
        remainder = remainder % denominator
    if remainder == 0:
        return None
    else:
        return res[map[remainder] :]


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
