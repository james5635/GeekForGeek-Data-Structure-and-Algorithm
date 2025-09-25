"""Using Iterative Factorial Method"""


def factorial(n: int) -> int:
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def calculate_nPr(n: int, r: int) -> int:
    """
    >>> calculate_nPr(5,2)
    20
    """
    return factorial(n) // factorial(n - r)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
