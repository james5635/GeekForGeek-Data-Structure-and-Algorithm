def square_root(n: int) -> int:
    """
    Find the integer square root of a non-negative integer using binary search.

    Args:
        n: A non-negative integer

    Returns:
        The floor of the square root of n
    """
    if n < 0:
        raise ValueError("Square root is not defined for negative numbers")
    if n <= 1:
        return n

    return _binary_search(1, n, n)


def _binary_search(low: int, high: int, target: int) -> int:
    if low > high:
        return high

    mid = (low + high) // 2
    sq = mid * mid

    if sq == target:
        return mid
    if sq < target:
        result = _binary_search(mid + 1, high, target)
        return max(mid, result)
    return _binary_search(low, mid - 1, target)


if __name__ == "__main__":
    print(square_root(11))
    print(square_root(16))
    print(square_root(25))
    print(square_root(0))
    print(square_root(1))
