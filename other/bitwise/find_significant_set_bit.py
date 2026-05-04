def find_significant_set_bit(n: int) -> int:
    """Find position (1-indexed) of the most significant set bit."""
    if n <= 0:
        return -1
    position = 0
    while n > 0:
        position += 1
        n >>= 1
    return position


if __name__ == "__main__":
    print(find_significant_set_bit(10))
    print(find_significant_set_bit(16))
    print(find_significant_set_bit(0))
