def smallest_power_of_2_ge(n: int) -> int:
    """Find smallest power of 2 greater than or equal to n."""
    if n <= 0:
        return 1
    if (n & (n - 1)) == 0:
        return n
    while n & (n - 1):
        n &= n - 1
    return n << 1


if __name__ == "__main__":
    print(smallest_power_of_2_ge(5))
    print(smallest_power_of_2_ge(16))
    print(smallest_power_of_2_ge(0))
