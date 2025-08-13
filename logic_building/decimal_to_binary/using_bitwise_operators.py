"""Using Bitwise Operators"""


def dec_to_binary(n: int) -> str:
    """
    >>> dec_to_binary(12)
    '1100'
    """
    bin = ""
    while n > 0:
        bit = n & 1
        bin += str(bit)
        n = n >> 1
    return bin[::-1]


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
