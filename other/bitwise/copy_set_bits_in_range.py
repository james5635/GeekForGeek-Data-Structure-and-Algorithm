def copy_set_bits_in_range(x: int, y: int, l: int, r: int) -> int:
    """Copy set bits from y to x in the range l to r (1-indexed)."""
    for i in range(l - 1, r):
        if (y >> i) & 1:
            x |= 1 << i
    return x


if __name__ == "__main__":
    print(copy_set_bits_in_range(10, 13, 2, 4))
    print(copy_set_bits_in_range(8, 7, 1, 3))
