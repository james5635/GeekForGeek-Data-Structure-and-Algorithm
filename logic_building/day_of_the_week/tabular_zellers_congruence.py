"""tabular zeller's congruence"""


def day_of_week(d: int, m: int, y: int) -> int:
    """
    >>> day_of_week(15,6,1995)
    4
    """
    month_code = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if m < 3:
        y -= 1
    # Year code calculation
    year_part = y % 100
    century_part = y // 100
    year_code = (year_part + year_part // 4 + century_part // 4 + 5 * century_part) % 7

    return (d + month_code[m - 1] + year_code) % 7


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
