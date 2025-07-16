""" Using rescursion """


def reverse_digits(n: int, reversed_number: list[int], base_position: list[int]) -> int:
    """
    >>> reverse_number = [0] # must be [0]
    >>> base_position = [1] # must be [1]
    >>> reverse_digits(1234, reverse_number, base_position)
    4321
    >>> reverse_number = [0] # must be [0]
    >>> base_position = [1] # must be [1]
    >>> reverse_digits(0, reverse_number, base_position)
    0
    >>> reverse_number = [0] # must be [0]
    >>> base_position = [1] # must be [1]
    >>> reverse_digits(1000, reverse_number, base_position)
    1
    >>> reverse_number = [0] # must be [0]
    >>> base_position = [1] # must be [1]
    >>> reverse_digits(987654321, reverse_number, base_position)
    123456789
    """
    if n > 0:
        reverse_digits(n // 10, reversed_number, base_position)
        reversed_number[0] += (n % 10) * base_position[0]
        base_position[0] *= 10
    return reversed_number[0]


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
