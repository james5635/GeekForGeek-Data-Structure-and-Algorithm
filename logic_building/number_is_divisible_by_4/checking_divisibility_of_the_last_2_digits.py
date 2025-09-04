"""Checking Divisibility of the Last 2 Digits"""


def check_division_by_4(num: str) -> bool:
    """
    >>> check_division_by_4("1234567589333862")
    False
    """
    num_len = len(num)
    if num_len == 0:
        return False
    if num_len == 1:
        return int(num[0]) % 4 == 0
    last = int(num[num_len - 1])
    prev_last = int(num[num_len - 2])
    return (prev_last * 10 + last) % 4 == 0


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
