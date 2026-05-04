def is_power_of_2(n: int) -> bool:
    """Check whether a given number is a power of 2."""
    return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    print(is_power_of_2(8))
    print(is_power_of_2(6))
    print(is_power_of_2(1))
