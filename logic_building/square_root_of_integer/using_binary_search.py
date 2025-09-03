"""Using Binary Search"""


def floor_sqrt(n: int) -> int:
    """
    >>> floor_sqrt(11)
    3
    """
    low = 1

    high = n
    res = 1
    while low <= high:
        mid = low + (high - low) // 2
        if mid * mid <= n:
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
