"""Using Head Recursion"""


def dec_to_bin(n: int) -> str:
    """
    >>> dec_to_bin(12)
    '1100'
    """

    def dec_to_bin_util(n: int, bin_arr: list[str]):
        if n == 0:
            return
        dec_to_bin_util(n // 2, bin_arr)
        bin_arr.append(str(n % 2))

    if n == 0:
        return "0"
    bin_arr = []
    dec_to_bin_util(n, bin_arr)
    return "".join(bin_arr)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
