""" By Reversing The Number """
def is_palindrome(n: int) -> bool:
    """
    >>> is_palindrome(12321)
    True
    """
    if n < 0:
        raise ValueError("n muse be non-negative")
    reverse = 0
    temp = n
    while temp:
        reverse = (reverse * 10 ) + (temp % 10)
        temp //= 10
    return reverse == n
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)
