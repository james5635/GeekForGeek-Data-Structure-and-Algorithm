"""Alternating Sum of 3-Digit Blocks"""


def check_division_by_13(num: str) -> bool:
    """
    >>> check_division_by_13("1234567589333862")
    False
    """
    num_len = len(num)
    if num_len == 1 and num[0] == "0":
        return True
    if num_len % 3 == 1:
        num += "00"
        num_len += 2

    elif num_len % 3 == 2:
        num += "0"
        num_len += 1

    sum = 0
    pos = +1

    i = num_len - 1
    while i >= 0:
        group_sum = 0
        group_sum += int(num[i])
        i -= 1
        group_sum += int(num[i]) * 10
        i -= 1
        group_sum += int(num[i]) * 100
        i -= 1

        sum += group_sum * pos
        pos *= -1
    return sum % 13 == 0


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
