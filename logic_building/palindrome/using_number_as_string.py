""" Using Number as String """
def is_palindrome(n: int) -> bool:
    """
    >>> is_palindrome(12321)
    True
    """
    if n < 0:
        raise ValueError("n muse be non-negative")
    str_ = str(n)
    len_ = len(str_)
    for i in range(len_ // 2):
        if str_[i] != str_[len_ - i - 1]:
            return False
    return True
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)
