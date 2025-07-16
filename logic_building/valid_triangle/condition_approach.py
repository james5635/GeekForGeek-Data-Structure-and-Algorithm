"""Condition Approach"""


def check_valid_triangle(a: int, b: int, c: int):
    """
    >>> a = 7
    >>> b = 10
    >>> c = 5
    >>> if check_valid_triangle(a,b,c):
    ...     print("valid")
    ... else:
    ...     print("invalid")
    valid
    """
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
