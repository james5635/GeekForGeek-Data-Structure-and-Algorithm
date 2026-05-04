def closest_numbers_same_set_bits(n: int) -> tuple[int, int]:
    """Find next smaller and greater numbers with same number of set bits."""
    c = n
    c0 = 0
    c1 = 0
    while (c & 1) == 0 and c > 0:
        c0 += 1
        c >>= 1
    while (c & 1) == 1:
        c1 += 1
        c >>= 1
    p = c0 + c1
    next_num = n + (1 << p) + (1 << (c1 - 1)) - 1
    prev_num = n - (1 << p) + (1 << (c1 + c0 - 1)) - (1 << (c0 - 1))
    return prev_num, next_num


if __name__ == "__main__":
    print(closest_numbers_same_set_bits(6))
    print(closest_numbers_same_set_bits(12))
