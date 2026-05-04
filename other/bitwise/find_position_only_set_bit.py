def find_position_only_set_bit(n: int) -> int:
    """Find position (1-indexed) of the only set bit in a number. Returns -1 if not power of 2 or zero."""
    if n <= 0 or (n & (n - 1)) != 0:
        return -1
    position = 0
    while n > 0:
        position += 1
        n >>= 1
    return position


if __name__ == "__main__":
    print(find_position_only_set_bit(8))
    print(find_position_only_set_bit(4))
    print(find_position_only_set_bit(6))
