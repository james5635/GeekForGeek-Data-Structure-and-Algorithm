"""Using Recursion"""


def find_nCr(n: int, r: int) -> int:
    """
    >>> find_nCr(5,2)
    10
    """
    if not (0 <= r and r <= n):
        raise ValueError("0 <= r <= n is not satisfied")
    if r == 0 or r == n:
        return 1
    return find_nCr(n - 1, r - 1) + find_nCr(n - 1, r)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
