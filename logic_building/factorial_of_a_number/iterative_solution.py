""" iterative solution """
def factorial(n: int) -> int:
    """
    >>> factorial(5)
    120
    """
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)