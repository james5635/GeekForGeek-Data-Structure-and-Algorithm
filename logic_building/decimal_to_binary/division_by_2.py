"""Division by 2"""


def dec_to_bin(n: int) -> str:
    """
    >>> dec_to_bin(12)
    '1100'
    """
    bin_arr: list[str] = []
    # loop count := floor(log2(n)) + 1
    # [n, n1, n2, n3, ..., 1]
    while n > 0:
        bit = n % 2
        bin_arr.append(str(bit))
        n //= 2
    bin_arr.reverse()
    return "".join(bin_arr)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
