def turn_off_rightmost_set_bit(n: int) -> int:
    """Turn off the rightmost set bit in a given integer."""
    return n & (n - 1)


if __name__ == "__main__":
    print(turn_off_rightmost_set_bit(12))
    print(turn_off_rightmost_set_bit(7))
    print(turn_off_rightmost_set_bit(8))
