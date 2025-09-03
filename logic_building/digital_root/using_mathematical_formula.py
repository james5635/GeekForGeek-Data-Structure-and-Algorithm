""" Using Mathematical Formula """
def single_digit(n: int) -> int:
    """
    >>> single_digit(1234)
    1
    """
    if n == 0:
        return 0
    if n % 9 == 0:
        return 9
    return n % 9
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)
