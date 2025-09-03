"""By Repetitively Adding Digits"""


def single_digit(n: int) -> int:
    """
    >>> single_digit(1234)
    1
    """
    if n < 0:
        raise ValueError("n muse be non-negative")
    sum = 0
    while n > 0 or sum > 9:
        if n == 0:
            n = sum
            sum = 0
        sum += n % 10
        n //= 10
    return sum


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
