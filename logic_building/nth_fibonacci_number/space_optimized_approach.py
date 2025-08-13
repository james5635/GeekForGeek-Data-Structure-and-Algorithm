def nth_fibonacci(n: int) -> int:
    """
    >>> nth_fibonacci(5)
    5
    >>> nth_fibonacci(2)
    1
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    prev1 = 1
    prev2 = 0
    for _ in range(2, n + 1):
        # curr is recommended
        # cur is not recommended
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
