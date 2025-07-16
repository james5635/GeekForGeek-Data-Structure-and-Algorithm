""" Recursive Solution """
def factorial(n: int) -> int:
    """
    >>> factorial(5)
    120
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
