"""Using Built-in Method"""

import math


def dec_to_binary(n: int) -> str:
    """
    >>> dec_to_binary(12)
    '1100'
    """
    return bin(n)[2::]


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
