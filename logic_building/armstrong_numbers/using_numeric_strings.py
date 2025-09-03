""" Using Numberic Strings """
def armstrong(n: int) -> bool:
    """
    >>> armstrong(153)
    True
    """
    num = str(n)
    digits = len(num)
    out = 0
    for i in num:
        out += int(i) ** digits
    return out == n
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)
