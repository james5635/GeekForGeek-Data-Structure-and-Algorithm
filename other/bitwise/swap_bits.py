def swap_bits(n: int, i: int, j: int) -> int:
    """Swap bits at positions i and j in a given number (0-indexed)."""
    if (n >> i) & 1 != (n >> j) & 1:
        n ^= (1 << i) | (1 << j)
    return n


if __name__ == "__main__":
    print(swap_bits(10, 0, 3))
    print(swap_bits(28, 1, 4))
