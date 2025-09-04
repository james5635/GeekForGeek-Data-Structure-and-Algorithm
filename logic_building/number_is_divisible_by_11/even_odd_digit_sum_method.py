"""Even-Odd Digit Sum Method"""


def check_division_by_11(num: str) -> bool:
    """
    >>> check_division_by_4(1234567589333862)
    False
    """
    odd_digits_sum = 0
    even_digits_sum = 0
    for i in range(len(num)):
        digit = int(num[i])
        if i % 2 == 0:
            odd_digits_sum += digit
        else:
            even_digits_sum += digit

    return (odd_digits_sum - even_digits_sum) % 11 == 0


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
