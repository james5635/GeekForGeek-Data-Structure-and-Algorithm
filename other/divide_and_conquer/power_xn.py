def power(x: float, n: int) -> float:
    """
    Calculate x raised to the power n using divide and conquer.

    Args:
        x: Base value
        n: Exponent (can be negative)

    Returns:
        x raised to the power n
    """
    if n == 0:
        return 1.0

    if n < 0:
        x = 1 / x
        n = -n

    half = power(x, n // 2)

    if n % 2 == 0:
        return half * half
    return half * half * x


if __name__ == "__main__":
    print(power(2, 10))
    print(power(3, -2))
    print(power(5, 0))
