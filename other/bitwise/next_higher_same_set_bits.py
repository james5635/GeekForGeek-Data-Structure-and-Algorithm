def next_higher_same_set_bits(n: int) -> int:
    """Find next higher number with same number of set bits."""
    if n == 0:
        return 0
    smallest = n & -n
    ripple = n + smallest
    ones = n ^ ripple
    ones = (ones >> 2) // smallest
    return ripple | ones


if __name__ == "__main__":
    print(next_higher_same_set_bits(6))
    print(next_higher_same_set_bits(12))
