"""Memoization Approach"""


def nth_fibonacci(n: int) -> int:
    """
    >>> nth_fibonacci(5)
    5
    >>> nth_fibonacci(2)
    1
    """

    def nth_fibonacci_util(n: int, memo: list[int]) -> int:
        if n < 0:
            raise ValueError("n must be non-negative")
        if n <= 1:
            return n
        memo[n] = nth_fibonacci_util(n - 1, memo) + nth_fibonacci_util(n - 2, memo)
        return memo[n]

    memo = [-1] * (n + 1)
    return nth_fibonacci_util(n, memo)


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
