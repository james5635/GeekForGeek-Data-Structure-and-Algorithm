"""Simple Approach"""


def calculate_fraction(a: int, b: int) -> str:
    """
    >>> calculate_fraction(50,22)
    '2.(27)'
    """
    if a == 0:
        return "0"
    res = "-" if a < 0 ^ b < 0 else ""

    a = abs(a)
    b = abs(b)

    res += str(a // b)
    rem = a % b
    if rem == 0:
        return res
    res += "."
    map = {}

    while rem > 0:
        if rem in map:
            res = res[: map[rem]] + "(" + res[map[rem] :] + ")"
            break
        map[rem] = len(res)
        rem = rem * 10
        res += str(rem // b)
        rem = rem % b
    return res


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
