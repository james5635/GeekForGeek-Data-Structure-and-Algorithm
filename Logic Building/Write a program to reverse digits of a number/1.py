""" Reversing Digit by Digit """
def reverse_digits(n: int) -> int:
    """
    >>> reverse_digits(1234)
    4321
    >>> reverse_digits(0)
    0
    >>> reverse_digits(1000)
    1
    >>> reverse_digits(987654321)
    123456789
    """
    reversed_number = 0
    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n //= 10
    return reversed_number
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)