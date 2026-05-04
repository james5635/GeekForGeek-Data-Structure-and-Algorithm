def position_rightmost_set_bit(n: int) -> int:
    """Find position (1-indexed) of the rightmost set bit."""
    if n == 0:
        return -1
    position = 1
    while (n & 1) == 0:
        n >>= 1
        position += 1
    return position


if __name__ == "__main__":
    print(position_rightmost_set_bit(12))
    print(position_rightmost_set_bit(18))
    print(position_rightmost_set_bit(0))
