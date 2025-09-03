""" using formula """
def term(n: int) -> int:
    """
    >>> term(4)
    10
    """
    return n * (n + 1) // 2
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)
