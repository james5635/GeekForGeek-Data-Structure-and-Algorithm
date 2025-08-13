"""sakamoto's method"""


def day_of_week(d: int, m: int, y: int) -> int:
    """
    >>> day_of_week(30,8,2010)
    1
    """
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y -= m < 3
    return (y + int(y / 4) - int(y / 100) + int(y / 400) + t[m - 1] + d) % 7


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
