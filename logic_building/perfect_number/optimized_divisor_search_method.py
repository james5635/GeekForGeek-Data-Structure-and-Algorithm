"""Optimized Divisor Search Method"""


def is_perfect(n: int) -> int:
    """
    >>> is_perfect(15)
    False
    """
    if n <= 1:
        return False
    sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum += i
            if i * i != n:
                sum += n // i
    """
    if n <= 1:
        return False
    return sum == n
    is logically equivalence to
    return sum == n and n <= 1
    """
    return sum == n


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
