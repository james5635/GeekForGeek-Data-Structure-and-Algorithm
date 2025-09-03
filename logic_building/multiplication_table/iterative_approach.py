"""Iterative Approach"""


def printTable(n: int) -> None:
    """
    >>> printTable(5)
    5 * 1 = 5
    5 * 2 = 10
    5 * 3 = 15
    5 * 4 = 20
    5 * 5 = 25
    5 * 6 = 30
    5 * 7 = 35
    5 * 8 = 40
    5 * 9 = 45
    5 * 10 = 50
    """
    for i in range(1, 11):
        print("%d * %d = %d" % (n, i, n * i))


if __name__ == "__main__":
    from doctest import testmod

    testmod()
